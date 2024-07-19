class graph:
    Graph = { #Directly define the problem as a tree with its children and their separation
        'Arad': [('Zerind',75),('Timisoara',118),('Sibiu',140)],
        'Zerind': [('Oradea',71),('Arad',75)],
        'Timisoara': [('Lugoj',111),('Arad',118)],
        'Oradea': [('Sibiu',151),('Zerind',71)],
        'Sibiu': [('Fagaras',99),('Rimnicu Vilcea',80),('Oradea',151),('Arad',140)],
        'Lugoj': [('Mehadia',70),('Timisoara',111)],
        'Mehadia': [('Drobeta',75),('Lugoj',70)],
        'Fagaras': [('Bucharest',211),('Sibiu',99)],
        'Drobeta': [('Craiova',120),('Mehadia',75)],
        'Rimnicu Vilcea': [('Craiova',146),('Pitesti',97),('Sibiu',80)],
        'Pitesti': [('Bucharest',101),('Craiova',138)],
        'Craiova': [('Pitesti',138),('Drobeta',120),('Rimnicu Vilcea',146)],
        'Bucharest': [('Fagaras',211),('Pitesti',101),('Giurgiu',90),('Urziceni',85)],
        'Giurgiu': [('Bucharest',90)],
        'Urziceni': [('Valsui',142),('Hirsova',98),('Bucharest',85)],
        'Valsui': [('Iasi',92),('Urziceni',142)],
        'Hirsova': [('Urziceni',98),('Eforie',86)],
        'Eforie': [('Hirsova',86)],
        'Iasi': [('Valsui',92)],
        'Neamt': [('Iasi',87)]
        }