# Pathfinding Project
## Introduction
In this project, I aimed to visualize pathfinding algorithms I learned in the university course "Data Structures". In this course, we learned proof of correctness and the theory of the algorithms: bfs,dfs, and Dijkstra's algorithm. After completing the course I wondered what those algorithms' real use cases are. Inspired by the Micromouse competition I decided to make an app in pygame that shows those algorithms' process of finding and searching for the endpoint.
## Installation and using the app
1. Use this command to download the project `git clone https://github.com/Dan7nm/Pathfinding-Project.git`. if you do not have git installed download the repo folder and unzip in your preferred directory.
2. Run the main.py file.
3. Choose the starting point by clicking on the grid. When clicked, a green square will indicate the chosen starting point.
4. Similarly choose an ending point, indicated by a red square
5. Now click or click and drag to draw obstacles for the algorithm.
6. When done press 'b' to run BFS algorithm, 'd' for DFS and 'j' for Dijkstra.
7. When done or at any point press 'space' to reset the board and start again
## Explanation
Originally all the algorithms use a Graph object, this means we have a node and it's children. In my case we have a two dimensional grid and I decided to make a function that checks the valid neighbours of every square given to the function. Valid neighbours means all neighbours that are within the limits of the grid, not visited and are an obstacle the user has chosen. Everytime the algorithm mentions adjacent edges we use the the 'get_neighbours' function. 
Additionally to visualize the steps of the algorithm I draw an orange square everytime the algorithm visits that square on the grid. This way the user can understand which squares are visited first and why algorithms such as BFS and Dijkstra are more usefull in the general case and why DFS can be faster then BFS in specific cases.

**Note that BFS and DFS only search for the ending square. They do not return the shortest path like Dijkstra's algorithm. A common misconception and one that I fell for in the beginning of the project.**
## Resources used for the project:
### Understanding basic Pygame:
1. Pygame in 90 Minutes For Beginners - https://www.youtube.com/watch?v=jO6qQDNa2UY
2. Pygame Doc - https://www.pygame.org/docs/
### Algorithms Pseudocode:
1. BFS - https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
2. DFS - https://en.wikipedia.org/wiki/Depth-first_search#Pseudocode
3. Dijkstra - https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue

