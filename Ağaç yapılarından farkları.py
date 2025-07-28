# Ağaç yapısı (döngüsüz)
tree = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# Graf yapısı (döngü içeren)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': ['A']  # döngü: A → B → D → A
}
