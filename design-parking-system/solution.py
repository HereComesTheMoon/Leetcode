class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small
        

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                self.b -= 1
                return 0 <= self.b
            case 2:
                self.m -= 1
                return 0 <= self.m
            case 3:
                self.s -= 1
                return 0 <= self.s
            case _:
                assert False
                
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)