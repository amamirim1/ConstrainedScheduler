class Problem:
    Supply = []
    Demand = []
    Distances = []
    Speeds = []

    def __init__(self, data):
        self.Demand = data[0]
        self.Supply = data[1]
        self.Distances = data[2]
        self.Speeds = data[3]

    def getTravelTime(self, source, destination, vehicleType):
        return 0

    def getAvailableTrucksByTime(self, time):


class Solution:
    Actions = [] #(Time, Action)
