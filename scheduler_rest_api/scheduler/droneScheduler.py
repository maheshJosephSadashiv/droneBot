from collections import deque
from extensions import db
from model.drone_table import Drone, drones_schema, drone_schema
import math


class droneScheduler():
    drones = []
    items = deque()
    destinations = deque()
    maplist = []
    droneToItem = []
    itemToDestination = []

    def distance(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    def getdronelist(self, drone_0, drone_1):
        self.drones = [drone_0, drone_1]
        # ENTER DRONES COORDINATES HERE
        # dq.append((4, 9))
        # dq.append((7, 2))



    def getitemlist(self, item_coordinates, item_id):
        iq = self.items

        # ENTER ITEM COODRINATES HERE
        # iq.append((2, 5))
        # iq.append((10, 5))
        # iq.append((10, 3))
        # iq.append((6, 3))
        iq.append((item_coordinates, item_id))


    def getdestinationlist(self, destination_coordinates):
        desq = self.destinations

        # ENTER ITEM DESTINATION COODRINATES HERE
        # desq.append((10, 10))
        # desq.append((1, 1))
        # desq.append((3, 8))
        # desq.append((8, 3))
        desq.append(destination_coordinates)


    def createList(self, no):

        if no == 1 and len(self.items) != 0:
            for i in range(len(self.drones)):
                self.droneToItem.append(
                    self.distance(self.drones[i][0], self.drones[i][1], self.items[0][0][0], self.items[0][0][1]))

        elif no == 2 and len(self.items) != 0:
            for i in range(len(self.items)):
                self.itemToDestination.append(
                    self.distance(self.items[i][0][0], self.items[i][0][1], self.destinations[i][0],
                                  self.destinations[i][1]))

    def schedule(self):

        try:
            schedule_result = {}
            d1, d2 = get_drone_coordinates()
            self.getdronelist(d1, d2)
            self.createList(1)
            self.createList(2)
            li = []
            if len(self.items) == 0:
                return
            for i in range(len(self.droneToItem)):
                li.append(self.droneToItem[i] + self.itemToDestination[0])

            while len(self.items) != 0:
                droneNo = li.index(min(li))
                schedule_result[self.items[0][1]] = droneNo

                li.clear()
                self.droneToItem.clear()
                self.itemToDestination.clear()
                self.maplist.append(droneNo)
                del self.items[0]
                pos = self.destinations.popleft()
                self.drones[droneNo] = pos
                if len(self.items) != 0:
                    self.createList(1)
                    self.createList(2)
                    for i in range(len(self.droneToItem)):
                        li.append(self.droneToItem[i] + self.itemToDestination[0])

        except Exception as ex:
            print(ex)

        return schedule_result


obj = droneScheduler()


def get_drone_coordinates():
    return (4, 9), (7, 2)


def schedule(context):
    with context:
        objs = db.session.query(Drone).filter(Drone.assigned_drone.is_(None))
        try:
            rows = drones_schema.dump(objs)
            for row in rows:
                item_id = row["item_id"]
                item_coordinates = (row["item_x"], row["item_y"])
                destination_coordinates = (row["destination_x"], row["destination_y"])
                obj.getitemlist(item_coordinates, item_id)
                obj.getdestinationlist(destination_coordinates)
        except TypeError:
            pass
        results = obj.schedule()
        if results is None:
            return
        for i in results.keys():
            db.session.query(Drone).filter(Drone.item_id == i). \
                update({Drone.assigned_drone: "Assigned to drone {}".format(results[i]), Drone.status: "Pending"},
                       synchronize_session=False)
            db.session.commit()
    obj.drones = []
    obj.items = deque()
    obj.destinations = deque()