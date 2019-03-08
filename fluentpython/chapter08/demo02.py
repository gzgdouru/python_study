'''
防御可变参数
'''


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # self.passengers = passengers
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

if __name__ == "__main__":
    basketball_team = ["Sue", "Tina", "Maya", "Diana", "Pat"]
    bus = TwilightBus(basketball_team)
    bus.drop("Tina")
    bus.drop("Pat")
    print(bus.passengers)
    print(basketball_team)
