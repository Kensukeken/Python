""" Class Vehicle and Bicycle
--- Class Vehicle has two methods: description and make_noise"""
class Vehicle:
          def __init__(self, current_speed=0):
                    self.current_speed = current_speed
                    
          def description(self):
                    print(f'Traveling at {self.current_speed} km/h')
                    
          def make_noise(self):
                    print('Vroom Vroom')

""" Class Bicycle inherits from Vehicle"""
class Bicycle(Vehicle):
          def __init__(self, has_basket=False):
                    Vehicle.__init__(self)
                    self.has_basket = has_basket
                    
          def description(self):
                    Vehicle.description(self)
                    print('But in the bike lane!')
                              
          def make_noise(self):
                  print('Ring Ring')

""" Class DirtBike inherits from Bicycle and has two mixins: StuntMixin and CarefulMinix"""  
class StuntMixin:
          def jump(self, distance):
                    print(f'Jumped {distance} meters!')
          
          def skid(self, distance):
                    print(f'Slid {distance} meters!')
          
class CarefulMinix:
          def sigma(self, direction):
                    print(f'Sigma {direction} meters!')
          

class DirtBike(Bicycle, CarefulMinix):
          def __init__(self, has_basket=False):
                    super().__init__(has_basket)
          
          def make_noise(self):
                  print('Braaaap')

car =  Vehicle()
car.description()
car.make_noise()

bike = Bicycle()
bike.description()
bike.make_noise()

duke = DirtBike()
duke.jump(10)
duke.skid(5)
duke.sigma('right')
duke.current_speed = 100
duke.description()
