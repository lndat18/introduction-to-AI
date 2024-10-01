import numpy as np
import random
import math

class LocalSearchStrategy:
    @staticmethod
    def random_restart_hill_climbing(problem, num_trial):
        best_path = []
        cur_best_state = 0
        for _ in range(num_trial):
            cur_path = []
            current_state = problem.get_random_state()  # Lấy trạng thái bắt đầu ngẫu nhiên
            cur_path.append(current_state)
            while True:
                the_best_neighbor = problem.get_the_best_neighbor(current_state)  # Lấy các trạng thái láng giềng

                if the_best_neighbor == None :
                    if problem.evaluate_state(current_state) > cur_best_state:
                        cur_best_state = problem.evaluate_state(current_state)
                        best_path = cur_path
                    break

                # Cập nhật trạng thái hiện tại và giá trị evaluation
                current_state = the_best_neighbor
                cur_path.append(current_state)

        return best_path
    
    def simulated_annealing_search(problem, schedule):
        path = []
        current, current_value = problem.initial_state()
        path.append(current)
        t = 0.000001
        while True:
            T = schedule(t)
            if T < 0.000001:
                # run out of energy
                break
            next, next_value = problem.random_neighbor(current)
            next_value = float(next_value)
            current_value = float(current_value)
            delta_E = next_value - current_value
            if delta_E > 0 or random.random() < math.exp(delta_E / T):
                current = next 
                current_value = next_value
                path.append(current)  
            t *= 1.1
        return path             

    def local_beam_search(problem, k):
        path = []
        node_max = None
        # begin with k randomly generated states
        current_states = []
        k_state = problem.get_k_randomly_state(k)
        for state in k_state:
            current_states.append(Node(state))
        while True:
            next_states = []
            # generate all successors of k state
            for state in current_states:
                next_states.extend(state.next_state(problem))
            # sort current state and next_state
            sorted_current = sorted(current_states, key=lambda node: problem.evaluate_state(node.state), reverse=True)
            sorted_next_state = sorted(next_states, key=lambda node: problem.evaluate_state(node.state), reverse=True)

            # get max current and next
            current_max = sorted_current[0]
            next_max = sorted_next_state[0]

            # check if reach the goals state or not
            if problem.evaluate_state(next_max.state) <= problem.evaluate_state(current_max.state):
                node_max = current_max
                break

            # if goal is not found, select k best successor
            current_states = sorted_next_state[:k]
        
        path.append(node_max.state)
        parent_node = node_max.parent
        while parent_node:
            path.append(parent_node.state)
            parent_node = parent_node.parent
        return path

class Node:
    def __init__(self, state, parent=None):
        self.state = state      
        self.parent = parent  
    def next_state(self, problem):
        next_state = []
        for neighbor in problem.neighbors(self.state):
            next_state.append(Node(neighbor,parent=self))
        return next_state
    def __repr__(self):
        return f"Node({self.state})"