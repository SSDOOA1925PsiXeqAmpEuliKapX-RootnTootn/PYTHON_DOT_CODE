import math

# Task: If the earth shrunk in half, what gravity would a person feel on the surface?

# The gravitational formula by Isaac: F = (G*m_1*m_2)/r^2

Grav_Constant = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
Mass_EARTH = 5.972e24     # Earth's mass (kg)
Mass_PERSON = 70 #kg
Radius_EARTH_ARBITRARY = 10000 * 10**3 # meters Note, using an arbitrary radius since I don't remmeber the proper radius of the earth off the top of my head. This is not a problem

# "Real" equation results
Force_Real_Equation = (Grav_Constant*Mass_EARTH*Mass_PERSON)/(Radius_EARTH_ARBITRARY**2)

# Simulate what a person feels on the surface:
print("Equation for the 'real' results:", Force_Real_Equation)
print("\n"*3)

Radius_EARTH_ARBITRARY_with_HALF_DIAMETER = Radius_EARTH_ARBITRARY /2

Force_Real_Equation_with_Half_Earth_Diameter = (Grav_Constant*Mass_EARTH*Mass_PERSON)/(Radius_EARTH_ARBITRARY_with_HALF_DIAMETER**2)

print("Equation for the 'half' results:", Force_Real_Equation_with_Half_Earth_Diameter)

print("\n" *2)
print("The relationship between the results:", Force_Real_Equation_with_Half_Earth_Diameter / Force_Real_Equation)

print("\n"*2)
from fractions import Fraction
print("The relationship:", Fraction(Force_Real_Equation_with_Half_Earth_Diameter / Force_Real_Equation), ", with respect to the Half Diameter earth first")


