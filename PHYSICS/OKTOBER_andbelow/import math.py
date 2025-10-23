import math
g = 9.8
v0 = 10
angle = 45
# Hi, I'm slightly annoyed by how little you comment your own code. It's jsut that when you use things I've never seen before, I'm like "how the f am I supposed to effectively manipulate the code to do what i want when I don't understand what is written there?"
# t0 = (2 * v0 * math.sin(math.radians(angle))) / g

# For 2*v0
# t2 = ?  # Fill in the formula
# print("time(first): ", t_f, "   and time(second):", t_s, " ", "to see the difference between time(first) and time(second):", t_s - t_f )

#I've decided that I would use the mechanics equations to simulate an environment where everyhting remains the same except for speed.

# I found out that I don't know how to simulate that environment, BUT I managed to find out that if I pretend I know v0 and a, I might be able to use two of the formulas to figure out a simulated environment. I mean, if I have two equations with two different unknowns, that should be good, right?
# I decided to go with V = Vo + a*t since it doesn't have s (distance) and V² - Vo² = 2*a*s since it doesn't have t(time)
# Decided: a=0 (unless it hits the gorun), Vo=10m/s


# time_FIRST = 
# After scribbling a fair bit on my paper I realized it's not fucking working
# Can you tell me what's wrong with my logic and give me a C[]Rating on my method?

#ATTPMT2:
# Hold on, identify which variables are unique to the axis
# t is just t
# a has to be divided into a_x and a_Y
# v must also be divided, and v_0 too
# distance must also divide
# Hold on, does that mean I have two different V = Vo + a*t equations? It feels like a dead end so I won't explore it yet...

def YValue(angle):
    return math.sin(math.radians(angle))
def XValue(angle):
    return math.cos(math.radians(angle))


initial_velocity_FIRST_X = 10 * XValue(45)
initial_velocity_SECOND_X = initial_velocity_FIRST_X * 2

initial_velocity_FIRST_Y = 10 * YValue(45)  #Decided to flip from sin to cos, I think that should give "the other half" of 10 and therefore give the initial Vo but Y axis
initial_velocity_SECOND_Y = initial_velocity_FIRST_Y * 2

acceleration_Y = -9.81 # Zero resistance, so the constant is the only thing affecting it.
acceleration_X = 0 # I actually have no idea about this one. I mean, I'm imagining zero air resistance, so it should be 0 right? Until it meets the ground and instantly stops the projectile.

final_velocity_FIRST_X = 10 * XValue(45)  #without decelleration, it should be like Vo
final_velocity_FIRST_Y = 10 * YValue(45)

final_velocity_SECOND_X = 2 * final_velocity_FIRST_X
final_velocity_SECOND_Y = 2 * final_velocity_FIRST_Y

#Hold on, what if only try to calculate the Y version of the formula?

BIGTIME = (final_velocity_FIRST_Y - initial_velocity_FIRST_Y) / acceleration_Y

# print(BIGTIME) (this failed)

#Hold on, final velocity... maybe it's zero because it stops on the ground?

final_velocity_FIRST_X = 0
final_velocity_FIRST_Y = 0
final_velocity_SECOND_X = 0
final_velocity_SECOND_Y = 0

BIGTIME_FIRST =2* ((final_velocity_FIRST_Y - initial_velocity_FIRST_Y) / acceleration_Y)

print(BIGTIME_FIRST, "s")
#Output: 0.7208020195581524. Did it work? Is that 0.7 seconds?

BIGTIME_SECOND_EQUATION = 2* ((final_velocity_SECOND_Y - initial_velocity_SECOND_Y) / acceleration_Y)

print("Time with double speed:", BIGTIME_SECOND_EQUATION)

print("Difference between the two times :  Double speed minus normal speed :", BIGTIME_SECOND_EQUATION - BIGTIME_FIRST, ". ", "for contrast, this is what the first equation's speed is on its own :", BIGTIME_FIRST)

# I was not able to create a program which shows the actual relationship between the values, something that shows "value two is double the first one", but I can see it with my own eyes. Still, I am curious how I could write something that does show the relationship if I am in a situation where it's difficult to tell

number1 = 721
number2 = 613

ratio = number1/number2

print("\n" *3)
print (ratio, "and that's the ratio of the two numbers")

#Success!

print("\n"*2)                   #Holy shit, it's almost 2am and I'ms till coding... Fuck my ass. After this, good night Grok
print("Ratio between the two Times: ", BIGTIME_SECOND_EQUATION/BIGTIME_FIRST) 
# Output Ratio between the two Times:  2.0 | Check that out! Is that a C[10]?? If there's anything missing, it is way way too late to work on it now, and we will tackle a different issue for tomorrow, but still, mention it. Good night