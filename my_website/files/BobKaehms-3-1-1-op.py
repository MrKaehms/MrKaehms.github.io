''' Bob Kaehms and Roger Dohm '''
''' Assignment 3.1.1 '''
''' Modified to ask for user input for names and state of interest '''

#name1 = 'Juan'
#name2 = 'Juanita'

# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__)) 

#initialize the aggregators
years1=[]
number_of_people1=[]
years2=[]
number_of_people2=[]

yst=raw_input('Enter Your State ')
name1=raw_input('Enter Your Boy Name ( use a cap) ')

name2=raw_input('Enter Your Girl Name ( use a cap) ')
# Scan one year's file at a time
#for year in range(1880, 2012):
for bunk in range(1):
    # Open the file
    filename = os.path.join(directory, yst + '.TXT')
    datafile = open(filename, 'r')
    # Go through all the names that year
    for line in datafile:
        state, gender, year, name, number = line.split(',')
        # Aggregate based on name1
        if name == name1 and gender == 'M':
            years1.append(year)
            number_of_people1.append(number) 
            #Aggregate based on name2
        if name == name2 and gender == 'F':
            years2.append(year)
            number_of_people2.append(number) 
                # Close that year's file
datafile.close()

# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot(years1, number_of_people1, '#0000FF')
ax.plot(years2, number_of_people2, '#FF00FF')

ax.set_title('U.S. Babies Named '+name1+' (blue) or '+name2+' (pink) in '+yst)
fig.show()