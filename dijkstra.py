# -----------------------------------------------------------
# Graphs Dijkstra search Script
#
# (C) 2024 Ivan Gustavo Ortiz García
# GH Repository https://github.com/0zymandias-Courses/interview_challenges
# -----------------------------------------------------------

#Constants 
name = "Graphs Dijkstra search"
graph = {
    "A" : {"B": 1, "C": 4},
    "B" : {"A": 1, "C": 2, "D": 5},
    "C" : {"A": 4, "B": 2, "D": 1},
    "D" : {"B": 5, "C": 1}
};
routes = {};
best_routes = {};

def get_best_routes():
    try:
        for route in routes:
            if (route[len(route)-1] not in best_routes):
                best_routes[route[len(route)-1]] = { "weight":routes[route], "route":route}
            else:
                if(best_routes[route[len(route)-1]]["weight"]>routes[route]):
                    best_routes[route[len(route)-1]] = { "weight":routes[route], "route":route}
        print(best_routes);
    except Exception as e:
        print(f"Error at get_best_routes: {e}");
        
def dijkstra_search(next_node = "", previous_node = "", route_counting = 0, route = ""):
    try:
        # print(f"Route: {route} Counting: {route_counting}")
        routes[route]=route_counting;
        vertices = filter(lambda vertex : vertex != previous_node ,graph[next_node]);
        for vertex in list(vertices):
            if(vertex not in route):
                dijkstra_search(vertex, next_node,graph[next_node][vertex]+route_counting,route + vertex)
    except Exception as e:
        print(f"Error at dijkstra_search: {e}");

def dijkstra(intial_node = ""):
    try:
        routes[intial_node]=0
        dijkstra_search(intial_node,"",0,intial_node);
    except Exception as e:
        print(f"Error at dijkstra: {e}");
        
def main ():
    try:
        print(f"Running the script: {name}");
        dijkstra("D");
        get_best_routes();
    except Exception as e:
        print(f"Error at Main: {e}");
    
if __name__ == "__main__":
    main()
