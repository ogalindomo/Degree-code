tempF = (float)(input("Enter the tempeature in Fahrenheit:",)) 
#Error: unsupported operand type(s) for -: 'str' and 'int'
#The conversion of the input to float is made with 'float' and this is necessary to convert between strings and doubles.
#Whatever has quotes is a string, else it is a variable.
tempC = (tempF - 32)*5/9.0
print(tempF,"degrees in Fahrenheit degrees is",tempC,"degrees Celsius.")