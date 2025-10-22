# Orbital radius calculator
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24     # Earth's mass (kg)
v = 7.5e3        # Orbital speed (m/s)
m = 1000         # Satellite mass (kg, arbitrary)

# F_g = ((G*M*m)/r) #Note, this is the correct formula for calculating gravitational force, in the Newtonian way at least, but how does this help figuring out if the orbital radius remains the same?
        # Gods, this almost feels frustrating, because I know the answer, it's "r", the radius remains the same regrardless of mass, btu I can't imagine how I will prove it... I decide I will try to start by reforming the formula to give me R instead:
        # I got: r = ((G*M*m)/F_g)

# Step 1: Write the formula for radius based on force balance
# radius = ?  # Try deriving from F_g = F_c
print(f"Radius for mass m: {radius / 1000:.2f} km")