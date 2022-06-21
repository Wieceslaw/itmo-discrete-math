def get_nearest_top_to_top(top, core):
    mn = None
    for el in enumerate(sp[top]):
        if el[0] in core or el[1] == 0:
            pass
        else:
            if mn == None:
                mn = el
            else:
                if el[1] < mn[1]:
                    mn = el
    if mn != None:
        print(f"Вершина в ядре: {top + 1}, блиайшая к ней {mn[0] + 1}")
    return mn
        

def get_nearest_top_to_core(core, sp):
    mn = None
    for top in core:
        nearest_top = get_nearest_top_to_top(top, core)
        if nearest_top is not None:
            if mn is None:
                mn = (top, ) + nearest_top
            else:
                mn = min((top, ) + nearest_top, mn, key=lambda x: x[-1])
    return mn


def calculate_weight(matrix):
    return sum([sum(row) for row in matrix]) / 2


def build_tree(sp, top):
    print("Начинаем с вершины: ", top + 1)
    n = len(sp)
    tops = list(range(n))
    core = [tops[top]]
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(n - 1):
        top, nearest_top, weight = get_nearest_top_to_core(core, sp)
        core.append(nearest_top)
        print(f"Пара с минимальным расстоянием: Вершина в ядре: {top + 1}, вершина ближайшая к ядру: {nearest_top + 1}")
        print(f"Добавляем в ядро новую вершину: {nearest_top + 1}")
        new_matrix[top][nearest_top] = weight
        new_matrix[nearest_top][top] = weight
        print("Текущее ядро: ", [el + 1 for el in core])
        print()
    print("Конечная матрица смежности:")
    for row in new_matrix:
        print(row)
    print("Суммарный вес связей: ", calculate_weight(new_matrix))
    print()


# ======================================
# вписать матрицу смежности
# sp = [
#     [0, 4, 4, 2, 2, 4, 3, 2, 2],
#     [4, 0, 4, 2, 2, 2, 5, 4, 4],
#     [4, 4, 0, 4, 2, 2, 3, 2, 4],
#     [2, 2, 4, 0, 2, 2, 5, 4, 4],
#     [2, 2, 2, 2, 0, 2, 3, 2, 2],
#     [4, 2, 2, 2, 2, 0, 3, 2, 4],
#     [3, 5, 3, 5, 3, 3, 0, 1, 1],
#     [2, 4, 2, 4, 2, 2, 1, 0, 2],
#     [2, 4, 4, 4, 2, 4, 1, 2, 0]
# ]

# sp = [
#     [0, 4, 4, 2, 2, 4, 3, 2, 2],
#     [4, 0, 4, 2, 2, 2, 5, 4, 4],
#     [4, 4, 0, 4, 2, 2, 3, 2, 4],
#     [2, 2, 4, 0, 2, 2, 5, 4, 4],
#     [2, 2, 2, 2, 0, 2, 3, 2, 2],
#     [4, 2, 2, 2, 2, 0, 3, 2, 4],
#     [3, 5, 3, 5, 3, 3, 0, 1, 1],
#     [2, 4, 2, 4, 2, 2, 1, 0, 2],
#     [2, 4, 4, 4, 2, 4, 1, 2, 0]
# ]

# sp = [[0,6,3,2,2,2,4,5,7],[6,0,5,4,4,4,2,3,1],[3,5,0,1,3,5,5,2,4],[2,4,1,0,2,4,4,3,5],[2,4,3,2,0,2,2,3,5],[2,4,5,4,2,0,2,3,5],[4,2,5,4,2,2,0,3,3],[5,3,2,3,3,3,3,0,2],[7,1,4,5,5,5,3,2,0]]
sp = [
    [0, 2, 3, 2, 3, 4, 5, 2, 2],
    [2, 0, 3, 2, 3, 6, 5, 2, 4],
    [3, 3, 0, 5, 2, 3, 2, 3, 3],
    [2, 2, 5, 0, 5, 4, 7, 4, 2],
    [3, 3, 2, 5, 0, 5, 2, 1, 3],
    [4, 6, 3, 4, 5, 0, 3, 6, 2],
    [5, 5, 2, 7, 2, 3, 0, 3, 5],
    [2, 2, 3, 4, 1, 6, 3, 0, 4],
    [2, 4, 3, 2, 3, 2, 5, 4, 0]
]
# ======================================
# for i in range(6):
build_tree(sp, 0)
