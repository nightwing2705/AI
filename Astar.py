import heapq

def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [])]  # (f, g, node, path)
    seen = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node in seen: continue
        path = path + [node]
        if node == goal: return path
        seen.add(node)
        for nbr, w in graph.get(node, []):
            heapq.heappush(pq, (g+w+h[nbr], g+w, nbr, path))
    return None
graph = {
    'A':[('B',2),('E',3)],
    'B':[('C',1),('G',9)],
    'C':[],
    'E':[('D',6)],
    'D':[('G',1)]
}
h = {'A':11,'B':6,'C':99,'D':1,'E':7,'G':0}

print(astar(graph,h,'A','G'))  # → ['A','E','D','G']
