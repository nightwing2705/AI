import random


def objective_function(x):
    return -(x - 3) ** 2 + 9

def steepest_ascent_hill_climb(objective_function, x_start, step_size, max_iterations):
    current_x = x_start
    current_value = objective_function(current_x)

    for _ in range(max_iterations):
        
        neighbors = [current_x + step_size, current_x - step_size]

        
        neighbor_values = [objective_function(x) for x in neighbors]

        
        best_neighbor_value = max(neighbor_values)
        best_neighbor = neighbors[neighbor_values.index(best_neighbor_value)]

        
        if best_neighbor_value > current_value:
            current_x, current_value = best_neighbor, best_neighbor_value
        else:
            
            break

    return current_x, current_value



best_x, best_value = steepest_ascent_hill_climb(
    objective_function, 
    x_start=random.uniform(-10, 10), 
    step_size=0.1, 
    max_iterations=100
)

print("Best solution found: x =", best_x, "f(x) =", best_value)
