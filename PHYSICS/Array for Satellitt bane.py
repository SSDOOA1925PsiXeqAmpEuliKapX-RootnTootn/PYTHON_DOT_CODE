from pylab import *

# Konstanter
m = 100           # masse av satellitt, kg
M = 5.972e24      # masse av jorda, kg
gamma = 6.67e-11  # gravitasjonskonstanten, Nm²/kg²

# Startverdier
r = array([4e7, 0])   # posisjonen til satellitten, m
v = array([0, 2.4e3]) # farten satellitten, m/s
t = 0                 # tid, s

# Liste for lagring av verdier
r_liste = [r]  # liste med posisjoner

# Variable krefter, beregning av kraftsum akselerasjon oh akselerasjon
def akselerasjon(r):
    G_abs = gamma*m*M/norm(r)**2
    e_r = -r/norm(r)
    G = G_abs*e_r
    aks = G/m
    return aks

# Simulerer bevegelsen så lenge det ikke har gitt 1*10⁵ s
# og banen er over jordoverflaten
dt = 10  # tidssteg, s

while t < 1e5 and norm(r) > 6.371e6:
    a = akselerasjon(r)  # beregner akselerasjon
    v = v + a*dt         # beregner ny fart
    r = r + v*dt         # beregner ny posisjon
    t = t + dt           # ny tid
    
    # Lagring av 2D-verdier
    r_liste = concatenate([r_liste, [r]])

# Tegner graf
axis("equal")
title("Satellittbane")
xlabel("$x$ / m")
ylabel("$y$ / m")
gca().add_artist(Circle((0,0), 6.37e6))
plot(r_liste[:,0], r_liste[:,1])
show()