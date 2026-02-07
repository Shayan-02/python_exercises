# airplane.py

from ground_vehicle import GroundVehicle
from flying_vehicle import FlyingVehicle


class Airplane(GroundVehicle, FlyingVehicle):
    def __init__(
        self,
        name,
        price,
        number_of_seats,
        max_speed,
        number_of_wheels,
        steering_wheel,
        fuel,
        number_of_fins,
        airline,
        number_of_crew,
        captain,
    ):
        GroundVehicle.__init__(
            self,
            name,
            price,
            number_of_seats,
            max_speed,
            number_of_wheels,
            steering_wheel,
        )
        FlyingVehicle.__init__(
            self, name, price, number_of_seats, max_speed, fuel, number_of_fins
        )
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain


class B707(Airplane):
    def __init__(
        self,
        name,
        price,
        number_of_seats,
        max_speed,
        number_of_wheels,
        steering_wheel,
        fuel,
        number_of_fins,
        airline,
        number_of_crew,
        captain,
    ):
        super().__init__(
            name,
            price,
            number_of_seats,
            max_speed,
            number_of_wheels,
            steering_wheel,
            fuel,
            number_of_fins,
            airline,
            number_of_crew,
            captain,
        )
