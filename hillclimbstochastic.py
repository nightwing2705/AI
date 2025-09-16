import random


def objective_function(x):
    return -(x - 3) ** 2 + 9

def hill_climb_stochastic(objective_function, x_start, step_size, max_iterations):
    current_x = x_start
    current_value = objective_function(current_x)

    for i in range(max_iterations):
        
        next_x = current_x + random.choice([-step_size, step_size])
        next_value = objective_function(next_x)

        
        if next_value > current_value:
            current_x, current_value = next_x, next_value
            print(f"Iteration {i+1}: Moved to x={current_x}, f(x)={current_value}")
        else:
            print(f"Iteration {i+1}: No improvement at x={current_x}, f(x)={current_value}")

    return current_x, current_value



best_x, best_value = hill_climb_stochastic(
    objective_function,
    x_start=random.randint(-10, 10),  
    step_size=1,
    max_iterations=18
)

print("\nBest solution found:")
print(f"x = {best_x}, f(x) = {best_value}")
