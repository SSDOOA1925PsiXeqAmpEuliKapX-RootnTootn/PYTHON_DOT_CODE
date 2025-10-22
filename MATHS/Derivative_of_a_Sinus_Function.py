import math            #(math library imported)

def f(x):              # Defining the function as a sinusfunction of X
    return math.sin(x)

DTAX = 0.001           # Setting Delta X to be approximately 0, or in this case, just a small number

x = math.pi/2                  # Setting x to an arbitrary number. NOTE: It turns out setting 2 here makes it so that it counts as 2 radians in the above sinus function. Not intentional... NOTE2: We changed it to pi/2 for fun, since we already know it's supposed to output something close to "1" NOTE3: It turned out to be something close to 0, but that makes sense... The derivative of Sinus(x) is Cosine(x)...

print ('The derivative of the sine function is this: ', (f(x+DTAX)-f(x))/DTAX) #Prints final output as the derivate of the sinus function using the definition of the derivative. NOTE: x is in radians appearently. Does that make a difference? I'm trying to imagine a normal sinusfunction without undefined x values, other than their scalar property... I don't think it makes a difference.

print(f'The derivative of the sine function is this: {(f(x+DTAX)-f(x))/DTAX}') # Grok helped make the print more modern and cool looking. Thank you!