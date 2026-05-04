import math

cities = [
    (0, 0),
    (1, 5),
    (5, 2),
    (6, 6),
    (8, 3)
]

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def greedy_tsp(start=0):
    n = len(cities)
    visited = [False] * n
    tour = [start]
    visited[start] = True

    current = start
    print("current:" + str(current))

    for _ in range(n - 1):
        next_city = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i]:
                print("cities[current]:"+ str(cities[current]) + "citites[i]:"+str(cities[i]))
                d = distance(cities[current], cities[i])
                print("distance(d):"+ str(d))
                print("min_dist:"+ str(min_dist) )
                if d < min_dist:
                    min_dist = d
                    next_city = i

        tour.append(next_city)
        visited[next_city] = True
        current = next_city
        print("Tour:"+ str(tour) + "visted:" + str(visited) + "current:"+str(current))

    return tour

# Run
tour = greedy_tsp()
print("Tour:", tour)