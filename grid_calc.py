import matplotlib.pyplot as plt

def visualize_wind_turbines(area_width, area_length, turbine_diameter, row_spacing, column_spacing):
    total_turbines = 0

    plt.figure(figsize=(area_width/150, area_length/150))  # Adjust figure size based on the area size
    plt.xlim(-10, area_width+120)
    plt.ylim(-10, area_length+120)
#row calcuations for the turbines
    row_count = 0
    while row_count * (row_spacing) < area_length:
        col_count = 0
        while col_count * (column_spacing) < area_width:
            plt.scatter(col_count * (column_spacing),
                        row_count * (row_spacing),
                        color='blue', marker='o')
            total_turbines += 1
            col_count += 1
        row_count += 1
#vertical direction calculation
    col_count = 0
    while col_count * (column_spacing) < area_width:
        row_count = 0
        while row_count * (row_spacing) < area_length:
            plt.scatter(col_count * (column_spacing),
                        row_count * (row_spacing),
                        color='red', marker='o')
            total_turbines += 1
            row_count += 1
        col_count += 1
    
    plt.title(f'Number of Turbines: {int(total_turbines/2)}')
    plt.xlabel('Width (meters)')
    plt.ylabel('Length (meters)')
    plt.grid(True)
    plt.show()
    return (int(total_turbines/2))

