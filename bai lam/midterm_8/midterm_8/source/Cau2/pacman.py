import sys
from problems import *
import searchAgents

if __name__ == "__main__":
    
    def check_syntax(value, valid_values, message):
        if value not in valid_values:
            print(f"{message} syntax is wrong")
            print(f"<{message}>: {', '.join(valid_values)}")
            exit()

    if len(sys.argv) < 4:
        print("Missing arguments")
        print("Syntax: pacman.py <maze_path> <search_agent> <heuristic_type>")
        print("search_agent: ucs, astar")
        print("Heuristic_type: manhattaDistance, euclideanDistance, None")
    else:
        _, maze_path, search_agent, Heuristic = sys.argv

        # check_syntax(maze_path, ['bigMaze.lay', 'mediumMaze.lay', 'smallMaze.lay'], "maze_path")
        # check_syntax(search_agent, ['ucs', 'astar'], "search_agent")
        # check_syntax(Heuristic, ['manhattaDistance', 'euclideanDistance', 'None'], "Heuristic_type")
            
        problem = MultiFoodSearchProblem()

        problem.readMaze(maze_path)
        if Heuristic == 'None':
            sAgentFunc = getattr(searchAgents, search_agent)
            actions = sAgentFunc(problem)
        elif search_agent == 'ucs':
            print("The program does not support the heuristic function for the ucs algorithm.")
            exit()
        else:
            sAgentFunc = getattr(searchAgents, search_agent)
            sAgentFunc1 = getattr(searchAgents, Heuristic)
            actions = sAgentFunc(problem,sAgentFunc1)
        problem.animate(actions)

