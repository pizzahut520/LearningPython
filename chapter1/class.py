class Bike:
    compose = ['frame', 'wheel', 'pedal']
    other = "Basket"
    def __init__(self):
        self.other = "basket"
    def use(self):
        print("riding")
    def use_time(self, distance, mark):
        print("you rode {} with a {} bike".format(distance, mark))

class Share_Bike(Bike):
    def cost(self, hour):
            print("you sent {} ".format(hour*2))

one_bike = Share_Bike()
one_bike.cost(2)
print(one_bike.other)
"""
my_bike = Bike()
print(my_bike.other)


my_bike.compose.append('bascket')
print(my_bike.compose)
my_bike.use_time("1OOOm", "giant")

"""