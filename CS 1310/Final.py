# Add your name
# Final Project
import matplotlib
import matplotlib.pyplot as plt
matplotlib.get_backend 


#  Line Graph 
# Sampled probabilities for readings of state 0 qubits.
print("Line state-0-probabilities of multiple readings in a quantum measurement:") 
print("Probabilities:")
probabilities = [0.97,0.85,0.34,0.76,0.65,0.31,0.56,0.48,0.17,0.23,0.35
                 ,0.33,0.62]

# Perform all processing tasks HERE first, then plot data 
displayData = []   
#print(displayData)   
for p in probabilities:
  #if p >= 1.0: this line is erased because all probabilities have to be at least 0 and a maximum of 1
      displayData.append(p)
      
print(probabilities)
#print(displayData) 
     
# Compute average gas price  
#avPrice = sum(prices)/len(prices)
avPrice = sum(displayData)/len(displayData)
print("Average probability:", avPrice)
   
# Plot line graph of gas prices
#plt.plot(prices)
plt.axis([0,12,0,1])
plt.plot(displayData)

# Add line for average price: a line from (0,avPrice)
#                                       to (len(price), avPrice)
plt.plot([0, len(displayData)] , [avPrice, avPrice])

# Label Axes and figure
plt.xlabel('Iteration')
plt.ylabel('Probability of State 0')
plt.title('Probability of state 0 as first bit')

# Display line graph
plt.show()

# Clear before the next graph
plt.clf()


######## Bar Chart Example ##########
# Sampled temperatures from real data stream

print("Probabilities among different computations")
cities = [ "Addition", "Substraction", "Division", "Multiplication","Modulus"] 
temperatures = [ 0.53, 0.41, 0.52, 0.63, 0.42]


#for i in (len(cities):
#    print("The city ",cities[i]," has a temperature of: ",
#           temperatures[i])

# You'll need to calculate the x-positions of the bars
#   a) range is used to create a list of a given length
#   b) then, len is used to calculate the length of a given list

x_positions = range(len(cities))

# Plot bar chart of temperatures
#   there is also a plt.barh function for horizontal bar charts
plt.bar(x_positions, temperatures)

# Label the bar chart's x axis
#   this function can be used to label the y-axis too.
plt.xticks(x_positions, cities)

# Label Axis
plt.xlabel('Activities')
plt.ylabel('Probabilities')
plt.title('Comparison of state-0 probabilities among different operations')

# Display bar chart
plt.show()

# Clear before the next set of graphs
plt.clf()

######## Histogram Example ##########
# Sampled earthquake magnitudes from real data stream


# Plot histogram of magnitudes
plt.hist(probabilities, bins=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])

# Label Axis
plt.xlabel('Magnitudes')
plt.ylabel('Occurrences')
plt.title('Histogram of Magnitudes of Probabilities')

# Display histogram
plt.show()

# Clear before the next set of graphs
plt.clf()