# -----------------------------------------------------------
# Graphs DFS & BFS Script
#
# (C) 2024 Ivan Gustavo Ortiz García
# GH Repository https://github.com/0zymandias-Courses/interview_challenges
# -----------------------------------------------------------

#Constants 
name = "Graphs DFS & BFS"
graph = {
    "A" : ["B", "C"],
    "B" : ["A", "D"],
    "C" : ["A", "E"],
    "D" : ["B"],
    "E" : ["C"],
};
visited_dfs = [];
visited_bfs = [];

def dfs(node = ""):  
    """
      function dfs Depth First Search.
      Args:
          node :String:
      Returns:
        None
    """
    try:
        visited_dfs.append(node);
        print(f"Nodes Visited: {visited_dfs}");
        vertices = graph[node];
        for vertex in vertices:
            if vertex not in visited_dfs:
                dfs(vertex);
    except Exception as e: 
        print(f"Error at dfs: {e}");

def bfs(node = ""):  
    """
      function bfs Breadth First Search.
      Args:
          node :Array:
      Returns:
        None
    """
    try:
        visited_bfs.append(node);
        print(f"Nodes Visited: {visited_bfs}");
        vertices = graph[node];
        if(len(vertices)>0):
            goDepthly(vertices);
    except Exception as e: 
        print(f"Error at bfs: {e}");
        
def goDepthly(vertices = []):
    """
      function goDepthly works recursively to perform the search
      Args:
          node :Array:
      Returns:
        None
    """
    try:
        next_vertices = [];
        for vertex in vertices:
                if vertex not in visited_bfs:
                    visited_bfs.append(vertex);
                    next_vertices.extend([nxt_node for nxt_node in graph[vertex] if nxt_node not in visited_bfs])
        print(f"Nodes Visited: {visited_bfs}");
        if(len(next_vertices)>0):
            goDepthly(next_vertices);
    except Exception as e: 
        print(f"Error at goDepthly: {e}");
        
def main():
    try:
        print(f"Running the script: {name}");
        print("DFS:");
        dfs("A");
        print("BFS:");
        bfs("A");
      
    except Exception as e: 
        print(f"Error at Main: {e}");

if __name__ == "__main__":
    main();
