from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing("Niye jao ")

rahim = Rider("Rahim", "rahim@gmail.com", 1234, "Mohakahli", 1200)
niye_jao.add_rider(rahim)

kalim = Driver("kalim", "kalim@gmail.com", 1256, "Gulshan")
niye_jao.add_driver(kalim)

rahim.request_ride(niye_jao, "Uttara", "car")
# rahim.show_current_ride()
kalim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
print(niye_jao)
