'''
Introduction to Backtracking

Backtracking is an algorithmic paradigm that tries different solutions until finds a solution that “works”.
Problems which are typically solved using backtracking technique have following property in common.
These problems can only be solved by trying every possible configuration and each configuration is tried only once.
'''

'''
Algorithm:

If all colors are assigned,
    print vertex assigned colors
Else
    a. Trying all possible colors, assign a color to the vertex
    b. If color assignment is possible, recursively assign colors to next vertices
    c. If color assignment is not possible, de-assign color, return False
'''

'''
Problem Statement
We wish to color the 4 states in southern India, them being Andhra Pradesh, Karnataka, Tamil Nadu and Kerala
The following lists out the neighbors for a particular state.
We wish to figure out how many colors would be needed to color each state such that no 2 neighboring states are represented using the same color
neighbors['Andhra'] = ['Karnataka', 'TamilNadu']
neighbors['Karnataka'] = ['Andhra', 'TamilNadu', 'Kerala']
neighbors['TamilNadu'] = ['Andhra', 'Karnataka', 'Kerala']
neighbors['Kerala'] = ['Karnataka', 'TamilNadu']

We would represent the given information using an undirected 2D graph where the adjacency matrix graph[i][j] = 1 represents that i and j are neighbors and 0 represents otherwise.
graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]
where graph[i][j] = 1 represents that i and j are neighbors and 0 represents otherwise.
'''

'''
Output: An array color[V] that should have numbers from 1 to m. color[i] should represent the color assigned to the ith state.
The code should also return false if the graph cannot be colored with m colors.
'''


def is_safe(n, graph, colors, c):
    # Iterate trough adjacent vertices
    # and check if the vertex color is different from c
    for i in range(n):
        if graph[n][i] and c == colors[i]: return False
    return True

# n = vertex nb
def graphColoringUtil(graph, color_nb, colors, n):
    # Check if all vertices are assigned a color
    if color_nb+1 == n :
        return True

    # Trying differents color for the vertex n
    for c in range(1, color_nb+1):
        # Check if assignment of color c to n is possible
        if is_safe(n, graph, colors, c):
            # Assign color c to n
            colors[n] = c
            # Recursively assign colors to the rest of the vertices
            if graphColoringUtil(graph, color_nb, colors, n+1): return True
            # If there is no solution, remove color (BACKTRACK)
            colors[n] = 0

#nb of vertex
vertex_nb = 4
# nb of colors
color_nb = 2
# Initiate vertex colors
colors = [0] * vertex_nb

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

#beginning with vertex 0
if graphColoringUtil(graph, color_nb, colors, 0):
    print(colors)
else:
    print("No solutions")