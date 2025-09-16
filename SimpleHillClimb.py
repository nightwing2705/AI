import random

def objective_function(x):

    return -(x - 3) ** 2 + 9

def generate_neighbor(current_solution, step_size=0.1):
    
    direction = random.choice([-1, 1])
    return current_solution + (direction * step_size)

def simple_hill_climbing(objective_func, initial_solution, max_iterations=1000, step_size=0.1):
    
    current_solution = initial_solution
    current_evaluation = objective_func(current_solution)

    for _ in range(max_iterations):
        neighbor_solution = generate_neighbor(current_solution, step_size)
        neighbor_evaluation = objective_func(neighbor_solution)

        
        if neighbor_evaluation > current_evaluation:
            current_solution = neighbor_solution
            current_evaluation = neighbor_evaluation
        
        
    return current_solution, current_evaluation


if __name__ == "__main__":
    initial_x = random.uniform(-10, 10) 
    print(f"Initial solution: {initial_x}")

    best_x, best_eval = simple_hill_climbing(objective_function, initial_x)

    print(f"Final solution: {best_x}")
    print(f"Final evaluation: {best_eval}")