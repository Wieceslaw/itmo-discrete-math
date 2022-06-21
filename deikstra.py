def nearby_tops(G, C, p: int):
    tops = [nearby_top for nearby_top, weight in enumerate(G[p]) if weight > 0]
    print(f"Гp = {{{', '.join(['e_{' + str(i + 1) + '}' for i in tops])}}}")
    tops = [nearby_top for nearby_top, weight in enumerate(G[p]) if weight > 0 and not C[nearby_top]]
    if tops: print(f"Временные пометки имеют вершины: {', '.join(['e_{' + str(top + 1) + '}' for top in tops])}, уточняем их:")
    else: print("Все вершины имею постоянные пометки.")
    return tops


def mark_tops(G, L, C, p):
    for top in nearby_tops(G, C, p):
        print(f"l(e_{{{top + 1}}}) = min({'∞' if L[top] == INFINITY else L[top]}, {L[p]}^+ + {G[p][top]}) = {min(L[top], L[p] + G[p][top])}")
        L[top] = min(L[top], L[p] + G[p][top])
    mn_value = INFINITY
    mn_index = -1
    for top in [i for i in range(n) if not C[i]]:
        if L[top] < mn_value:
            mn_value = L[top]
            mn_index = top
    C[mn_index] = True
    print(f'l(e_i^*) = min[l(e_i)] = l(e_{{{mn_index + 1}}}) = {mn_value}')
    print(f"e_{mn_index + 1} получает постоянную пометку l(e_{mn_index + 1}) = {mn_value}+, p = e_{mn_index + 1}")
    return mn_index


def showL(L, C, k):
    for i, el in enumerate(L):
        print('e_' + '{' + str(i + 1) + '} : ' + ('∞' if el == INFINITY else ((str(el) + '+' if i == k else ' ') if C[i] else str(el))))


def showL_without_e(L, C, k):
    print('===')
    for i, el in enumerate(L):
        print(('∞' if el == INFINITY else ((str(el) + '+' if i == k else ' ') if C[i] else str(el))))
    print('===')

# G = [
#     [0,2,0,0,0,10,17], 
#     [2,0,3,0,0,0,10],
#     [0,3,0,15,0,3,0],
#     [0,0,15,0,5,0,5],
#     [0,0,0,5,0,15,0],
#     [10,0,3,0,15,0,3],
#     [17,10,0,5,0,3,0]
# ]

G = [
    [0, 4, 4, 0, 2, 0, 0, 2, 0, 0, 3, 0],
    [4, 0, 0, 0, 4, 0, 2, 0, 5, 0, 2, 2],
    [4, 0, 0, 0, 0, 4, 4, 4, 0, 5, 2, 2],
    [0, 0, 0, 0, 0, 5, 0, 0, 4, 0, 4, 0],
    [2, 4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4],
    [0, 0, 4, 5, 3, 0, 0, 4, 0, 3, 2, 0],
    [0, 2, 4, 0, 0, 0, 0, 0, 0, 1, 3, 0],
    [2, 0, 4, 0, 0, 4, 0, 0, 0, 1, 3, 0],
    [0, 5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 3, 1, 1, 0, 0, 0, 0],
    [3, 2, 2, 4, 0, 2, 3, 3, 0, 0, 0, 0],
    [0, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0]
]

FROM = 0
INFINITY = 10e10
n = len(G)
L = [INFINITY for _ in range(n)]
C = [False for _ in range(n)]

L[FROM] = 0
C[FROM] = True

print(f"l(e_{{{FROM}}})=0^+; l(e_i)=∞, для всех i \\neq 1, p = e_1")
showL(L, C, FROM)
print()

p = FROM

while not all(C):
    print("Не все вершины имеют постоянные пометки, поэтому")
    p = mark_tops(G, L, C, p)
    if p < 0:
        break
    showL_without_e(L, C, p)
    print()