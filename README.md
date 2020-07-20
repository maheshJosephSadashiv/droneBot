## Project Name: Swarm Copter

### Description:

The code in the linked repository explains the implementation of the Swarm Copter. It includes the React web application code along with the flask framework.


### Hardware Requirements: 

DJI Tello Drone: 2 Nos.

Overhead Camera: 1 No.

#### Software and tools required:

* React
* Material UI
* Flask
* APScheduler
* MySQL
* sqlAlchemy
* Marshmellow
* TelloSDK
* OpenCV


### Instructions/Steps to run the project:
Please make sure you are working on the virtual environment while working on the project. That way we don't need to keep on downloading any dependencies.
The virtual environment is in the tello folder and is named venv.

* To run the virtual environment make sure you have virtualenv installed If not run "pip install virtualenv"
* To run the virtual environment: run the command: ./telloenv/Scripts/Activate (make sure you are in the tello dir) Follow this link for more info: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
* To run the server side of the application using Flask
* First, install virtualenv pip install virtualenv
* Run virtualenv venv in the project root.
* Run .\venv\Scripts\Activate
* Run pip install -r requirements.txt
* Run python db_init.py
* Run python app.py
* Go to http://127.0.0.1:5000/ you should see success on the screen

### For the front-end side(REACT):

* Run npm install (inside the project root directory)
* Run npm start (inside the project root directory)

### For the Hardware connection :

* Make sure that the Tello drone is switched ON.
* Connect the laptop’s wifi to the Tello Wifi hotspot.
* Make sure the drone is not ideal for too long. 
 
