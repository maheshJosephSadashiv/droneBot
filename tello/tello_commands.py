from tello.TelloSDK.djitellopy import Tello


class TelloClass:

    def create_tello_object(self):
        self.tello = Tello()

    def tello_connect(self):
        self.tello.connect()

    def tello_takeoff(self):
        self.tello.takeoff()

    def tello_left_cm(self, distance):
        self.tello.move_left(distance)

    def tello_right_cm(self, distance):
        self.tello.move_right(distance)

    def tello_up_cm(self, distance):
        self.tello.move_up(distance)

    def tello_down_cm(self, distance):
        self.tello.move_down(distance)

    def tello_back_cm(self, distance):
        self.tello.move_back(distance)

    def tello_forward_cm(self, distance):
        self.tello.move_forward(distance)

    def tello_rotate_counter_clockwise(self, angle):
        self.tello.rotate_counter_clockwise(angle)

    def tello_rotate_clockwise(self, angle):
        self.tello.rotate_clockwise(angle)

    def tello_land(self):
        self.tello.land()

    def tello_end(self):
        self.tello.end()
