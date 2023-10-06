import random
import time

def compute_staircase_divide_and_conquer(points):
    """
    Computes the Pareto-optimal points (top-right staircase) using a divide-and-conquer approach.
    
    Args:
        points (list): List of points represented as tuples (x, y).
    
    Returns:
        list: List of Pareto-optimal points.
    """
    n = len(points)

    if n <= 2:
        return sorted(points, key=lambda p: (p[0], p[1]))

    points.sort(key=lambda p: (-p[1], p[0]))

    pareto_optimal = [points[0]]  # Initialize with the point having the highest Y-value
    current_max_x = points[0][0]

    for i in range(1, n):
        if points[i][0] > current_max_x:
            pareto_optimal.append(points[i])
            current_max_x = points[i][0]

    return pareto_optimal

def generate_random_points(n, max_coordinate):
    """
    Generates a list of random points with coordinates in the range [0, max_coordinate].
    
    Args:
        n (int): Number of points to generate.
        max_coordinate (int): Maximum X or Y coordinate value.
    
    Returns:
        list: List of random points represented as tuples (x, y).
    """
    return [(random.randint(0, max_coordinate), random.randint(0, max_coordinate)) for _ in range(n)]

def main():
    n = 1000000
    max_coordinate = 100
    random.seed(42)

    points = generate_random_points(n, max_coordinate)

    print("Input Points:")
    for point in points:
        print(point)

    start_time = time.time()
    pareto_optimal = compute_staircase_divide_and_conquer(points)
    end_time = time.time()

    execution_time = end_time - start_time

    print("\nPareto-Optimal Points (Top-Right Staircase):")
    for point in pareto_optimal:
        print(point)

    print(f"\nExecution Time: {execution_time:.6f} seconds")

if __name__ == "__main__":
    main()
