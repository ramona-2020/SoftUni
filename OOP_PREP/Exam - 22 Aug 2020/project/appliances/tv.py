from project.appliances.appliance import Appliance


class TV(Appliance):

    def __init__(self, cost=1.5):
        super().__init__(cost)
