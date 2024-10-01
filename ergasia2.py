class villages():
    def __init__(self,graph):
        self.road = {}
        self.graph = graph

    def shortest_paths(self,village):
        shortest_paths = {village: []}
        queue = [village]
        visited = {village}
        level = {village: 0}
        while queue:
            village = queue.pop(0)
            for neighbor in self.graph[village]:
                if neighbor not in visited:
                    shortest_paths[neighbor] = shortest_paths[village] + [(neighbor)]
                    queue.append(neighbor)
                    visited.add(neighbor)
                    level[neighbor] = level[village] + 1
                elif level[neighbor] == level[village] + 1:
                    shortest_paths[neighbor].append(village)
                    shortest_paths[neighbor].append(neighbor)
        return shortest_paths

    
    def closeness_centrality(self, village):
        total_distance = 0
        shortest = self.shortest_paths(village)
        for key in shortest:
            total_distance += len(shortest[key])
        closeness = 1 / total_distance
        return closeness
    
    def allClosenessCentrality(self):
        closeness_centrality_values = {}
        for village in self.graph:
            closeness_centrality_values[village] = self.closeness_centrality(village)
        return closeness_centrality_values


    def accumulate_shortest_paths(self,shortest_paths):
        accumulation = {village: 0 for village in shortest_paths.keys()}
        for village in shortest_paths:
            for path in shortest_paths[village]:
                if path != village:
                    accumulation[path] += 1
        return accumulation
    
    def betweenness_centrality(self):
        betweenness_centrality_values = {village: 0 for village in self.graph}
        for village in self.graph:
            shortest = self.shortest_paths(village)
            accumulation = self.accumulate_shortest_paths(shortest)
            for neighbor in self.graph:
                if neighbor != village:
                    betweenness_centrality_values[neighbor] += accumulation[neighbor]
        return betweenness_centrality_values

class main():
    def __init__(self,graph):
        self.myvillages = villages(graph)
        self.placeHealthCenter()
        self.placePharmacy()

    
    def placeHealthCenter(self):
        closeness_centrality_values =self.myvillages.allClosenessCentrality()
        self.hCvillage = max(closeness_centrality_values, key = closeness_centrality_values.get)
        print("Closeness_centrality_values:",closeness_centrality_values)
        print("The Village that the Health Center should be put in:",self.hCvillage)
        

    def placePharmacy(self):
        betweenness_centrality_values = self.myvillages.betweenness_centrality()
        pharmVillage = max(betweenness_centrality_values, key = betweenness_centrality_values.get)
        print("Betweenness centrality values:", betweenness_centrality_values)
        if self.hCvillage == pharmVillage:
            betweenness_centrality_values.pop(pharmVillage)
            pharmVillage2 = max(betweenness_centrality_values, key = betweenness_centrality_values.get)
            print("The Village that the Pharmacy should be put in:",pharmVillage2) 
        else:
            print("The Village that the Pharmacy should be put in:",pharmVillage)
         

graph = {'A': ['D'],
             'B': ['H'],
             'C': ['D'],
             'D': ['A','C','E','F','G'],
             'E': ['D'],
             'F': ['D'],
             'G': ['D','H'],
             'H':['B','G']}


start = main(graph)