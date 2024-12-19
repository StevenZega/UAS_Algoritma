import argparse
from utils import load_algorithm, get_available_algorithms

def display_help():
    """Display available categories and algorithms."""
    available_algorithms = get_available_algorithms()
    print("\nAvailable Categories and Algorithms:\n")
    for category, algorithms in available_algorithms.items():
        print(f"{category.capitalize()}:")
        for algo, (module, class_name) in algorithms.items():
            print(f"  - {algo} (module: {module}, class: {class_name})")
    print("\nExample usage:")
    print('python main.py --category basic --algorithm euclidian --params "56" "98"')
    print('python main.py --category searching --algorithm binary --params "[1, 2, 3, 4, 5]" "3"')
    print('python main.py --category sorting --algorithm insertion_sort --params "[5, 2, 9, 1]"')
    print('python main.py --category arrays --algorithm kadane --params "[1, -2, 3, 4, -1, 2, 1, -5, 4]"')
    print('python main.py --category graph --algorithm kruskal --params "4" "[(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]"')

def main():
    parser = argparse.ArgumentParser(description="Algorithm Runner")
    parser.add_argument("--category", help="Category of the algorithm (e.g., basic, searching).")
    parser.add_argument("--algorithm", help="Algorithm name (e.g., depth_first, binary).")
    parser.add_argument("--params", nargs="*", help="Parameters required by the algorithm.")
    
    args = parser.parse_args()

    if not args.category or not args.algorithm:
        print("\nNo category or algorithm provided. Showing help:\n")
        display_help()
        return
    
    try:
        algo_instance = load_algorithm(args.category, args.algorithm)
        if args.params:
            # Convert parameters to appropriate types
            params = [eval(param) if param.startswith("{") or param.startswith("[") else param for param in args.params]
            result = algo_instance.run(*params)
            print(f"\nAlgorithm Result:\n{result}")
        else:
            print("\nNo parameters provided. This algorithm may require additional inputs.\n")
    except ValueError as e:
        print(f"\nError: {e}\n")
        display_help()

if __name__ == "__main__":
    main()
