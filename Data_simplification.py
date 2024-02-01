import pandas as pd
import statistics
import matplotlib.pyplot as plt
from grid_calc import visualize_wind_turbines
import tkinter as tk
import tkinter.messagebox as tkmb
import math
import numpy as np
file_path = r"C:\Users\punee\OneDrive - UBC\Documents\4th YEAR\ELEC 491\MileStone2\Wind_energy Calculations\WIndData2020-2022_open-meteo.xlsx"
df = pd.read_excel(file_path)

extracted_data = df.iloc[4:26309, [0,2,3]]  # 2 corresponds to column C (0-indexed)

filtered_data = extracted_data[extracted_data.iloc[:, 1] >= 5.5]
#filtering the data here
#checking for git push
print(filtered_data)
filtered_data.iloc[:, 0] = pd.to_datetime(filtered_data.iloc[:, 0])

averaged_data = filtered_data.groupby(filtered_data.iloc[:, 0].dt.to_period("M")).mean()

averaged_data_list = averaged_data.values.tolist()

all_data_points = []

for i in range(len(averaged_data)):
    values = averaged_data.iloc[i, 1:].tolist()
    all_data_points.append(values)

for data_point in all_data_points:
    print(data_point)
middle_column_values = filtered_data.iloc[:, 1]
average_wind_speed = np.mean(middle_column_values)
variance_ws = np.var(middle_column_values)
std_ws = np.std(middle_column_values)
print("Average of Wind Speeds:", average_wind_speed)
print("Variance of Wind Speeds:", variance_ws)
print("Standard Deviation of Wind Speeds:", std_ws)

# Reset index to make 'Month' a regular column

'''CALCULATION FOR THE ACTUAL ENERGY PRODUCED'''
area_width = 1000 #entered by the user in m
area_length = 1000 
turbine_diameter = 120 # in meters
row_spacing = turbine_diameter * 7 
column_spacing = turbine_diameter * 5 
def calc_wind_power(Wind_speed, turbine_diameter, f):
    rho = 1.225 #air density(kg/m^3) taken from the data sets
    #Cf = 0.35 #capacity factor
    Cp = 0.4 #power coefficent
    Ar = math.pi * (turbine_diameter/2)**2 #area of blades(meter)
    v = Wind_speed #wind speed() units unknown m/s
    wind_energy = 0.5 * rho * Cp * Ar * (v**3) * 8760 * (f)
    f_energy = f'The Energy in watthour per year is: {wind_energy/1000000} MWh/year'
    tkmb.showinfo("Output Energy in MWh/year", f_energy)
f = visualize_wind_turbines(area_width, area_length, turbine_diameter, row_spacing, column_spacing)
calc_wind_power(average_wind_speed, turbine_diameter, f)
'''END OF CALCULATION FOR ENERGY'''
# Manually specify the months for three years (2020 to 2022)
months = ['Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020', 'Dec 2020',
          'Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021', 'Nov 2021', 'Dec 2021',
          'Jan 2022', 'Feb 2022', 'Mar 2022', 'Apr 2022', 'May 2022', 'Jun 2022', 'Jul 2022', 'Aug 2022', 'Sep 2022', 'Oct 2022', 'Nov 2022', 'Dec 2022']

# Create a plot
second_column_values = [point[0] for point in all_data_points]

# Create the first plot
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)  # Create a subplot with 2 rows and 1 column, and set it as the first plot
plt.plot(months, second_column_values, marker='o', linestyle='-')
plt.xlabel('Months (Year 2020 to 2022)')
plt.ylabel('Second Column Values')
plt.title('Wind Speed')
plt.xticks(rotation=45, ha='right')

# Extract values from the third column (index 1) for all 36 points
third_column_values = [point[1] for point in all_data_points]

# Create the second plot
plt.subplot(2, 1, 2)  # Set the second plot in the same subplot
plt.plot(months, third_column_values, marker='o', linestyle='-')
plt.xlabel('Months (Year 2020 to 2022)')
plt.ylabel('Third Column Values')
plt.title('Wind Direction')
plt.xticks(rotation=45, ha='right')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()