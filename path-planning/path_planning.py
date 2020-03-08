import threading 
import numpy as np
import cv2
import cv2.aruco as aruco
import glob



def callibrate_camera():

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    objp = np.zeros((6*7,3), np.float32)
    objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    images = glob.glob('calib_images/*.jpg')

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners2)
            img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    return ret, mtx, dist, rvecs, tvecs



def find_aruco_marker_by_id(ret, mtx, dist, rvecs, tvecs, id, cap):
    while (True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters = aruco.DetectorParameters_create()

        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        font = cv2.FONT_HERSHEY_SIMPLEX #font for displaying text (below)
        if np.all(ids != None):
            rvec, tvec,_ = aruco.estimatePoseSingleMarkers(corners[0], 0.05, mtx, dist) 
            #(rvec-tvec).any() # get rid of that nasty numpy value array error
            if id in ids:
                aruco.drawAxis(frame, mtx, dist, rvec[0], tvec[0], 0.1)
                aruco.drawDetectedMarkers(frame, corners) 
                cv2.putText(frame, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

        cv2.imshow('frame '+str(id),frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    

if __name__ == "__main__":
    ret, mtx, dist, rvecs, tvecs = callibrate_camera()
    cap = cv2.VideoCapture(0)
    t1 = threading.Thread(target=find_aruco_marker_by_id, args=(ret, mtx, dist, rvecs, tvecs, 1, cap, )) 
    t2 = threading.Thread(target=find_aruco_marker_by_id, args=(ret, mtx, dist, rvecs, tvecs, 2, cap, ))
    t1.start() 
    t2.start()
    t1.join() 
    t2.join()
    cv2.destroyAllWindows()
    print("Done!") 




