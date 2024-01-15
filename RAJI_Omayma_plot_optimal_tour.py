# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:33:37 2024

@author: Omimiya
"""

import matplotlib.pyplot as plt

def calculate_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        total_distance += ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return total_distance

def read_tsp_data(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                try:
                    x, y = float(parts[1]), float(parts[2])
                    coordinates.append((x, y))
                except ValueError:
                    continue
    return coordinates

# optimal tour from "berlin52.opt.tour"
optimal_tour = [1,
                49,
                32,
                45,
                19,
                41,
                8,
                9,
                10,
                43,
                33,
                51,
                11,
                52,
                14,
                13,
                47,
                26,
                27,
                28,
                12,
                25,
                4,
                6,
                15,
                5,
                24,
                48,
                38,
                37,
                40,
                39,
                36,
                35,
                34,
                44,
                46,
                16,
                29,
                50,
                20,
                23,
                30,
                2,
                7,
                42,
                21,
                17,
                3,
                18,
                31,
                22]
adjusted_tour = [city - 1 for city in optimal_tour]

# Compute the distance
file_path = 'berlin52.tsp'
coordinates = read_tsp_data(file_path)
optimal_distance = calculate_distance(adjusted_tour, coordinates)

print("Total distance of the optimal tour:", optimal_distance)

# Plotting the optimal tour
def plot_tour(tour, coordinates):
    plt.figure(figsize=(10, 8))

    # Plotting each city
    for i in range(len(tour)):
        x, y = coordinates[tour[i]]
        plt.scatter(x, y, color='blue')
        plt.text(x, y, str(tour[i] + 1), color='red', fontsize=8)

    # Plotting the path
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        plt.plot([x1, x2], [y1, y2], color='green')

    # Connecting the last city to the first
    x1, y1 = coordinates[tour[-1]]
    x2, y2 = coordinates[tour[0]]
    plt.plot([x1, x2], [y1, y2], color='green')

    plt.title('TSP Solution Tour')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()


plot_tour(adjusted_tour, coordinates)
