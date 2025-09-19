
import math

# This code calculates the total amount of areal inside the tank.
# which can further calculate into volume based on the viscosity

class TankParameters:
   
    # Default starting values for the simulator
    tank_cylinder_height: float = 5.0
    tank_radius: float = 1.5

    # Function to calculate the inner areal of the cylindrical part of the tank
    def tank_cylinder_volume(self) -> float:
        return (self.tank_radius ** 2) * math.pi * self.tank_cylinder_height

    # Function to calculate the inner areal of the hemisphere at the bottom of the tank
    def tank_hemisphere_volume(self) -> float:
        return ((2.0 / 3.0) * math.pi * (self.tank_radius ** 3))

    # Function to calculate the total volume capabilities of the tank
    def tank_total_volume(self) -> float:
        return self.tank_cylinder_volume() + self.tank_hemisphere_volume()

    if __name__ == "__main__":
        tank = TankParameters()
        print(f"Cylinder volume:    {tank.tank_cylinder_volume()}")
        print(f"Hemisphere volume : {tank.tank_hemisphere_volume()}")
        print(f"Total volume:       {tank.tank_total_volume()}")






