#Arithmetic:'

a = 2
d = 3

s = a
o_formula = 0

for i in range(1, 20):
    print(a)
    s = s + a
    a = a + d
    o_formula=o_formula+1

print ("And also the sum is", s)


text = "We're doing another 300 steps"
i = 1
count = 1
while a <= 10_000:
    count = count + 1

    s = s + a
    a = a + d
    o_formula=o_formula+1

    if count % 300 == 0:
        i += 1
        dots = "." * (i % 4)
        print(f"{text} {dots}")

output = o_formula

print ("The number of links for the line to reach over value 10 000 is,", output, "and the total value has become,", a)

print  ()
print  ()
print  ()
print  ()

a=2
k=3

s = a
o_formula = 0

for i in range(1, 20):
    print(a)
    s = s + a
    a = a*k
    o_formula=o_formula+1
print()
print ("And also the sum is", s)


text = "We're doing another step"
i = 1
count = 1
while a <= 10_000:
    count = count + 1
    i += 1
    dots = "." * (i % 4)
    print(f"{text} {dots}")

    s = s + a
    a = a *k
    o_formula=o_formula+1

output = o_formula

print ("The number of links for the line to reach over value 10 000 is,", output, "and the total value has become,", a)

print("Obviously, the output is already over 10 000, let's fix this")

print()
print()
print()

print()


a=2
k=3

s = a
o_formula = 0

while a <= 10_000:
    count = count + 1
    i += 1
    dots = "." * (i % 4)
    print(f"{text} {dots}")

    s = s + a
    a = a *k
    o_formula=o_formula+1

output = o_formula

print ("The number of links for the line to reach over value 10 000 is,", output, "and the total value has become,", a)