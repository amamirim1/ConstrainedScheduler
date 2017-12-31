import Problem as problemModule

class ProblemState:
    Time = 0
    Idle_trucks = [] #(TruckID, City)
    Busy_trucks = [] #(TruckID, ShipmentID)
    Remaining_demand = [] #ShipmentIDs
    Distance_delivered = 0 #Total distance travelled by all trucks where they were loaded
    Distance_travelled = 0 #Total distance travelled by all trucks regardless of being loaded or not

    def __init__(self, time):
        self.Time = time

    def __init__(self, problem):
        self.Time = 0


class Action:
    Assignments = [] #(truckID, ShipmentID)

