# Add your name
# Final Project
import matplotlib
import matplotlib.pyplot as plt
matplotlib.get_backend 


#  Line Graph 
# Sampled gas prices from actual data stream
print("Line Graph of Gas Prices:") 
prices = [
          1.98, 1.8, 1.8, 1.7, 3.1, 2.0, 1.8, 0.6, 2.8, 0.5,
          2.51, 3.51, 1.4, 2.6, 2.5, 2.4, 2.9, 2.6, 2.8, 2.5,
          1.5, 0.9, 0.9, 1.3, 1.0, 1.7, 0.62, 1.9, 1.2, 0.6,
          0.13, 0.5, 1.1, 0.7, 1.4, 3.1, 3.9, 1.3, 1.06, 3.4]

# Perform all processing tasks HERE first, then plot data 
displayData = []   
print(displayData)   
for p in prices:
  if p >= 0.0:
      displayData.append(p)
print(displayData) 
     
# Compute average gas price  
#avPrice = sum(prices)/len(prices)
avPrice = sum(displayData)/len(displayData)
   
# Plot line graph of gas prices
#plt.plot(prices)
plt.plot(displayData)

# Add line for average price: a line from (0,avPrice)
#                                       to (len(price), avPrice)
plt.plot([0, len(displayData)] , [avPrice, avPrice])

# Label Axes and figure
plt.xlabel('Time')
plt.ylabel('Gas Prices')
plt.title('History of Gas Prices')

# Display line graph
plt.show()

# Clear before the next graph
plt.clf()


######## Bar Chart Example ##########
# Sampled temperatures from real data stream

print("Bar Chart of City Temperatures:")
cities = [ "New York", "El Paso", "Tucson", "San Diego","Las Cruces"] 
temperatures = [ 77, 91, 98, 62, 90]


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
plt.xlabel('Cities')
plt.ylabel('Temperatures')
plt.title('Comparison of Temperatures in Different Cities')

# Display bar chart
plt.show()

# Clear before the next set of graphs
plt.clf()

######## Histogram Example ##########
# Sampled earthquake magnitudes from real data stream
magnitudes = [
       1.98, 1.8, 1.8, 1.7, 3.1, 2.0, 1.8, 0.6, 2.8, 0.5,
       2.51, 3.51, 1.4, 2.6, 2.5, 2.4, 2.9, 2.6, 2.8, 2.5]

# Plot histogram of magnitudes
plt.hist(magnitudes, bins=[0,1,2,3,4,5,6,7])

# Label Axis
plt.xlabel('Magnitudes')
plt.ylabel('Occurrences')
plt.title('Histogram of Magnitudes')

# Display histogram
plt.show()

# Clear before the next set of graphs
plt.clf()