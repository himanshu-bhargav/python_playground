''' This file is for learning purposes only. It is not intended to be used in production. '''
# DFS (Depth First Search) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It uses a stack data structure to keep track of the nodes to be explored.
graph={
    "folder1":["file1","file2","folder2"],
    "folder2":["file3", "folder4"],
    "folder4":["file4", "file5"],
    "folder5":["file6"]    
}

stack=["folder1"]

while stack:

    current_node=stack.pop()

    print("Current node :",current_node)

    if current_node=="file5":
         print("Found file5 at",current_node)
         break

    # SAFE CHECK
    if current_node in graph:
        stack.extend(graph[current_node])