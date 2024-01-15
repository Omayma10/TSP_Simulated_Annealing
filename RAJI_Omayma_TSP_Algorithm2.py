import random
import math
import time
import matplotlib.pyplot as plt

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

def generate_neighbor(tour):
    m, n = sorted(random.sample(range(len(tour)), 2))
    new_tour = tour[:]
    # Swap all positions between m and n
    new_tour[m:n+1] = reversed(tour[m:n+1])
    return new_tour

def calculate_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        total_distance += ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return total_distance

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)

def cool_down(temperature, cooling_rate):
    return temperature * cooling_rate

def simulated_annealing(coordinates, initial_temp, cooling_rate, min_temperature):
    initial_tour = list(range(len(coordinates)))
    random.shuffle(initial_tour)

    current_tour = initial_tour
    current_cost = calculate_distance(current_tour, coordinates)
    temperature = initial_temp
    best_cost = float('inf')
    best_tour = initial_tour

    while temperature > min_temperature:
        neighbor_tour = generate_neighbor(current_tour)
        neighbor_cost = calculate_distance(neighbor_tour, coordinates)

        if acceptance_probability(current_cost, neighbor_cost, temperature) > random.random():
            current_tour = neighbor_tour
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour

        temperature = cool_down(temperature, cooling_rate)

    return best_tour, best_cost

def run_iterations(coordinates, initial_temp, cooling_rate, min_temperature, iterations):
    best_10_cost = float('inf')
    best_10_tour = None
    for i in range(iterations):
        start_time = time.time()
        tour, cost = simulated_annealing(coordinates, initial_temp, cooling_rate, min_temperature)
        duration = time.time() - start_time
        print(f"Iteration {i+1}: Cost = {cost}, Duration = {duration} seconds")

        if cost < best_10_cost:
            best_10_cost = cost
            best_10_tour = tour

    print("\nBest tour found:")
    print(best_10_tour)
    print(f"Best cost: {best_10_cost}")
    return best_10_tour

# Parameters for the experiment
initial_temp = 1000
cooling_rate = 0.9999
min_temperature = 1
iterations = 10

# Running the code
file_path = 'berlin52.tsp'
coordinates = read_tsp_data(file_path)
best_tour = run_iterations(coordinates, initial_temp, cooling_rate, min_temperature, iterations)

# Plotting the best tour
plot_tour(best_tour, coordinates)


