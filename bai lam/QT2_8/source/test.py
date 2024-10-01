from problem import Problem
from search import LocalSearchStrategy

problem = Problem('monalisa.jpg')

# # random restart hill climbing
# path = LocalSearchStrategy.random_restart_hill_climbing(problem, num_trial=20)
# problem.draw_path(path)

# # simulated annealing
# def schedule(t):
#     # schedule(t) = 1/(t^2) with t is the iteration step
#     return 1/(t**2)
# path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
# problem.draw_path(path)

# #local beam search
# k = 10
# path = LocalSearchStrategy.local_beam_search(problem, k)
# problem.draw_path(path)