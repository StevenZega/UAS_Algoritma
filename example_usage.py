python main.py --category basic --algorithm euclidian --params "56" "98"
python main.py --category basic --algorithm huffman --params "'A': 5, 'B': 2, 'R': 2, 'C': 1, 'D': 1"
python main.py --category basic --algorithm union_find --params "[1, 2, 3, 4]" "[[1, 2], [2, 3], [3, 4]]"

python main.py --category searching --algorithm binary --params "[1, 2, 3, 4, 5]" "3"
python main.py --category searching --algorithm depth_first --params "{1: [2, 3], 2: [4], 3: [4], 4: []}" "1"
python main.py --category searching --algorithm breadth_first --params "{1: [2, 3], 2: [4], 3: [4], 4: []}" "1"
python main.py --category searching --algorithm linear --params "[1, 2, 3, 4, 5]" "3"

python main.py --category sorting --algorithm insertion_sort --params "[5, 2, 9, 1]"
python main.py --category sorting --algorithm selection_sort --params "[5, 2, 9, 1]"
python main.py --category sorting --algorithm heap_sort --params "[5, 2, 9, 1]"
python main.py --category sorting --algorithm merge_sort --params "[5, 2, 9, 1]"
python main.py --category sorting --algorithm quick_sort --params "[5, 2, 9, 1]"
python main.py --category sorting --algorithm counting_sort --params "[5, 2, 9, 1]"

python main.py --category arrays --algorithm kadane --params "[1, -2, 3, 4, -1, 2, 1, -5, 4]"
python main.py --category arrays --algorithm floyd --params "[[0, 1, float('inf'), float('inf')], [1, 0, 1, float('inf')], [float('inf'), 1, 0, 1], [float('inf'), float('inf'), 1, 0]]"
python main.py --category arrays --algorithm kmp --params "'ABABABCABABABAC'" "'ABABABAC'"
python main.py --category arrays --algorithm quick_select --params "[7, 10, 4, 3, 20, 15]" "3"
python main.py --category arrays --algorithm boyer_moore --params "'ABABABCABABABAC'" "'ABABABAC'"

python main.py --category graph --algorithm kruskal --params "4" "[(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]"
python main.py --category graph --algorithm dijkstra --params "[(1, 2, 1), (1, 3, 2), (2, 3, 2), (3, 4, 1)]" "1"
python main.py --category graph --algorithm flood_fill --params "[[1, 1, 1], [1, 0, 1], [1, 1, 1]]" "0" "0" "2"
python main.py --category graph --algorithm lee --params "[[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]" "0" "0" "2" "3"
python main.py --category graph --algorithm topological --params "{0: [1, 2], 1: [2], 2: [3], 3: []}"
python main.py --category graph --algorithm floyd_warshall --params "[[0, 3, float('inf'), 7], [8, 0, 2, float('inf')], [5, float('inf'), 0, 1], [2, float('inf'), 3, 0]]"
python main.py --category graph --algorithm bellman_ford --params "{0: [(1, 5), (2, 3)], 1: [(3, 2)], 2: [(3, 7)], 3: []}" 4
