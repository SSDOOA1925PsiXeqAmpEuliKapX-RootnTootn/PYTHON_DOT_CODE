from pylab import *

# Constants
m = 100           # Satellite mass, kg
M = 5.972e24      # Earth mass, kg
gamma = 6.67e-11  # Gravitational constant, Nm²/kg²

# Initial values
r = array([4e7, 0])   # Initial position (x, y), m
v = array([0, 2.4e3]) # Initial velocity (vx, vy), m/s
t = 0                 # Initial time, s
r_liste = [r]         # List to store positions

def akselerasjon(r):
    G_abs = gamma*m*M/norm(r)**2
    e_r = -r/norm(r)
    G = G_abs*e_r
    aks = G/m
    return aks

def FTR_r(r_current, v_current):
    r_temp = r_current.copy()
    v_temp = v_current.copy()
    a_temp = akselerasjon(r_temp)
    v_temp += a_temp * dt
    r_temp += v_temp * dt
    return r_temp

dt = 1  # Smoother time step, as you noted
prev_mag = norm(r)
flip_count = 0
flip_times = []

# Single loop to detect periapsis and apoapsis
while t < 1e5 and norm(r) > 6.371e6 and flip_count < 2:
    curr_mag = norm(r)
    next_r_val = FTR_r(r, v)
    next_mag = norm(next_r_val)
    if prev_mag > curr_mag and curr_mag < next_mag:  # Periapsis
        flip_times.append(t)
        flip_count += 1
        print(f"Periapsis at t = {t} s, |r| = {curr_mag:.2e} m")
    elif prev_mag < curr_mag and curr_mag > next_mag and flip_count == 1:  # Apoapsis
        flip_times.append(t)
        flip_count += 1
        print(f"Apoapsis at t = {t} s, |r| = {curr_mag:.2e} m")
    prev_mag = curr_mag
    a = akselerasjon(r)
    v = v + a*dt
    r = r + v*dt
    t = t + dt
    r_liste = concatenate([r_liste, [r]])

# Estimate T
if flip_count == 2:
    T = flip_times[1] - flip_times[0]
    print(f"Estimated orbital period T: {T} s")
else:
    print("Not enough flips detected")

# Plot orbit
axis("equal")
title("Satellittbane")
xlabel("$x$ / m")
ylabel("$y$ / m")
gca().add_artist(Circle((0,0), 6.37e6))
r_array = array(r_liste)  # Fix for TypeError
plot(r_array[:,0], r_array[:,1])
show()

print(f"Final time: {t} s")