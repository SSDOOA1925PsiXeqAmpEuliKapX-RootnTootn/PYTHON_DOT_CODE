def f(x):
    return x**2+3*x+3

a=0
b=3

n=5 #Antall Rectangles

dx = (b-a)/n # BRedde på hvert rectangle
x=a
sumAreal=0 #Startverdi for total area

for i in range(0,n,1):
    arealRektangel=((f(x)*f(x+dx))/2)*dx # This is based on maths related to trapezoids. ØØÅ doesn't understand it, he only understands that it works.
    sumAreal=sumAreal+arealRektangel
    x = x + dx
print(sumAreal)

#Caution, turns out the above program is wrong.