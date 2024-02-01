
import math
import pandas as pd
from grid_calc import visualize_wind_turbines
import tkinter as tk
import tkinter.messagebox as tkmb
#enter avalaible area
df = pd.read_csv(r"C:\Users\punee\Documents\4TH YEAR\ELEC 491\Wind_energy Calculations\Wind_Rm.csv")
#Values
wind_speed = df['Wind Speed'].mean()
area_width = 1000 #entered by the user
area_length = 1000 
turbine_diameter = 120
row_spacing = turbine_diameter * 7 
column_spacing = turbine_diameter * 5 

def calc_wind_power(Wind_speed, turbine_diameter, f):
    rho = 1.225 #air density(kg/m^3)
    #Cf = 0.35 #capacity factor
    Cp = 0.4 #power coefficent
    Ar = math.pi * (turbine_diameter/2)**2 #area of blades(meter)
    v = Wind_speed #wind speed() units unknown m/s
    wind_energy = 0.5 * rho * Cp * Ar * (v**3) * 8760 * (f)
    f_energy = f'The Energy in watthour per year is: {wind_energy:.2f} Wh/year'
    tkmb.showinfo("Output Energy in Wh/year", f_energy)
f = visualize_wind_turbines(area_width, area_length, turbine_diameter, row_spacing, column_spacing)
calc_wind_power(wind_speed, turbine_diameter, f)


