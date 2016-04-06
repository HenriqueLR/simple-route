#encoding: utf-8

from collections import namedtuple


inf = float('inf')
List = namedtuple('List', 'start, end, km')

class RoutePrice():
    def __init__(self, lists):
        self.list_new = []
        for obj in lists:
            self.list_new.append((obj.origin_route,obj.destination_route,obj.distance_route))

        self.lists = tuples = [List(*l) for l in self.list_new]
        self.unique = set(sum(([e.start, e.end] for e in tuples), []))

    def calc(self, origin, destination):

        if origin not in self.unique:
            return None
        
        if destination not in self.unique:
            return None
        
        dist = {head: inf for head in self.unique}
        previous = {head: None for head in self.unique}
        dist[origin] = 0
        q = self.unique.copy()
        neighbours = {head: set() for head in self.unique}
        
        for start, end, km in self.lists:
            neighbours[start].add((end, km))
        
        while q:
            u = min(q, key=lambda head: dist[head])
            q.remove(u)
            distance = dist[u]
            if dist[u] == inf or u == destination:
                break
            for v, km in neighbours[u]:
                alt = dist[u] + float(km)
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
        s, u = [], destination
        
        while previous[u]:
            s.insert(0, u)
            u = previous[u]
        s.insert(0, u)
        
        return {'routes': s, 'distance': distance}