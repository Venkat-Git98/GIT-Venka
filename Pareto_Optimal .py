import random
import time
import matplotlib.pyplot as plt


def compute_staircase_divide_and_conquer(points):
    n = len(points)

    if n <= 2:
        return sorted(points, key=lambda p: (p[0], p[1]))

    points.sort(key=lambda p: (-p[1], p[0]))

    # Initialize with the point having the highest Y-value
    pareto_optimal = [points[0]]
    current_max_x = points[0][0]

    for i in range(1, n):
        if points[i][0] > current_max_x:
            pareto_optimal.append(points[i])
            current_max_x = points[i][0]

    return pareto_optimal


def generate_random_points(n, max_coordinate):
    return [(random.randint(0, max_coordinate), random.randint(0, max_coordinate)) for _ in range(n)]


def main():
    n = 100
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

    print(f"\nExecution Time: {execution_time: .6f} seconds")

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    pareto_x = [point[0] for point in pareto_optimal]
    pareto_y = [point[1] for point in pareto_optimal]

    plt.scatter(x, y, label='Input Points')
    plt.scatter(pareto_x, pareto_y, color='red', label='Pareto-Optimal Points')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('Visualization of Pareto-Optimal Points')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
