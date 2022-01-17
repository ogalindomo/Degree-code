#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:37:05 2020

@author: oscargalindo
"""
import random, math
'''
State Assignment:
    S0 = RU 8p
    S1 = TU 10p
    S2 = RU 10p
    S3 = RD 10p
    S4 = RU 8a
    S5 = RD 8a
    S6 = TU 10a
    S7 = RU 10a
    S8 = RD 10a
    S9 = TD 10a
    S10 = 11am class begins 
    

'''
def monte_carlo(state_names, actions_states, transition_rewards, n_episodes, learning_rate):

    state_values = [0] * len(states_names)
    total_reward = 0
    terminal_state = 10

    for i in range(n_episodes):

        print(f"Ep{i+1: 02}: ", end="")

        states_visited = set()
        curr_state = 0
        episode_reward = 0

        while curr_state != terminal_state:

            curr_state_name = states_names[curr_state]

            states_visited.add(curr_state)

            # Decide what action to take.
            n_actions = len(actions_states[curr_state])
            action = random.randint(0, n_actions-1)
            action_name = actions_states[curr_state][action][0]

            # If the action leads to a split path, choose path randomly.
            n_paths = len(actions_states[curr_state][action]) - 1
            path = 0 if n_paths == 1 else random.randint(0, n_paths-1)

            # Collect your reward.
            reward = transition_rewards[curr_state][action][path]

            episode_reward += reward
            total_reward += reward

            print(f"[{curr_state_name: <6}] → {action_name} → {reward:+} → ", end="")

            # Move to new state.
            curr_state = actions_states[curr_state][action][path+1]

        # Reached terminal state, wrap up episode.
        states_visited.add(curr_state)
        curr_state_name = states_names[curr_state]
        print(f"[{curr_state_name}] r={episode_reward}")

        # Episode done. Perform Monte-Carlo updates for all states visited.
        for s in states_visited:
            state_values[s] = state_values[s] + learning_rate * (episode_reward - state_values[s])
        
    # All episodes done. Print state values.
    print("StateVals:")
    for state, value in enumerate(state_values):
        state_name = states_names[state]
        print(f"\t[{state_name: <6}] {value:+.3f}")
    
    # Print average reward.
    average_reward = total_reward / n_episodes
    print(f"AvgReward:{average_reward:+.3f}")

def valueIteration(actions,rewards,lambda_value=0.99,difference=0.001):
    state_values = [0.]*len(rewards)
    update_times = [0.]*len(rewards)
    policies = ['']*(len(rewards)-1)
    difference_met = True
    count = 1
    while difference_met:
        difference_met = False
        print("------------Iteration ",count,"-------------")
        for state in range(len(actions)):
            max_value = -math.inf
            max_action = 0
            all_actions = []
            for action in range(len(actions[state])):
                added_value = 0
                probability = 1/(len(actions[state][action][1:])) if len(actions[state]) >0 else 1
                for next_states in range(len(actions[state][action][1:])):
                    transition_reward = transition_rewards[state][action][next_states]
                    next_state = actions_states[state][action][next_states+1]
                    added_value += probability*(transition_reward+(lambda_value*state_values[next_state]))
                if max_value < added_value:
                    max_value = added_value
                    max_action = actions[state][action][0]
                all_actions.append([actions_states[state][action][0],added_value])
            if not len(actions[state]) == 0: 
                if abs(state_values[state]-max_value) >= difference:
                    difference_met = True
                print("Updated value of state S"+str(state),"from:",str(state_values[state]),"to:",max_value)
                print("Action Selected:",max_action,"with value:",max_value,end=' ')
                print("All actions values:",all_actions)
                state_values[state] = max_value
                policies[state] = max_action 
                # print("")
            # print("At iteration ",count,"state","S"+str(state),"equals",state_values[state])
        count+=1
        print("--------------------------------------------")
    print("Finalized iterations. Ran for",count-1,"iteration, optimal policy by state",policies)
    print("Values:",state_values)


def q_learning(actions,rewards,alpha=0.1,lambda_value=0.99):
    difference_met = True
    q_values = [[random.randint(0,10)]*len(actions[state]) for state in range(len(actions))]
    q_values[-1].append(0)
    c_q_values = [[e for e in q_values[i]] for i in range(len(q_values))]
    terminal_state = 10
    difference_met = True
    counter = 1
    while difference_met:
        difference_met = False
        state_actions_pairs = list()
        curr_state = 0
        episode_reward = 0
        print("------------Episode ",counter,"-------------")
        while curr_state != terminal_state:
            # Decide what action to take.
            n_actions = len(actions_states[curr_state])
            action = random.randint(0, n_actions-1)
            state_actions_pairs.append((curr_state,action))
            # If the action leads to a split path, choose path randomly.
            n_paths = len(actions_states[curr_state][action]) - 1
            path = 0 if n_paths == 1 else random.randint(0, n_paths-1)
            # Move to new state.
            curr_state = actions_states[curr_state][action][path+1]
        # Reached terminal state, wrap up episode.
        state_actions_pairs.append((curr_state,None))

        # Episode done. Perform Monte-Carlo updates for all states visited.
        #(1,2) what is the next state (4,2)
        for i,(state, action) in enumerate(state_actions_pairs):
            if i == len(state_actions_pairs)-1: break
            print(state_actions_pairs[i+1])
            print(type(state_actions_pairs[i+1]))
            next_state = state_actions_pairs[i+1][0]
            q = q_values[state][action]
            q_next_state = max(q_values[next_state])
            reward = rewards[state][action][path]
            new_q = q + alpha*(reward+lambda_value*q_next_state-q)
            diff = abs(q - new_q)
            if diff >= 0.001:
                difference_met = True
            print("For state S"+str(state),"the previous Q is:",str(q),"the new Q is:",str(new_q),".")
            print("Immediate Reward:",str(reward),".","Q value of the next state is:",str(q_next_state)+".")
            q_values[state][action] = new_q
        print("--------------------------------------------")
        counter+=1  
        alpha = alpha *0.99
    print("Number of episodes is:",counter)
    print("Q values:",q_values)
    return c_q_values,q_values
    

if __name__=="__main__":
    states_names = ["RU 8p","TU 10p","RU 10p","RD 10p","RU 8a","RD 8a","TU 10a",
                    "RU 10a","RD 10a","TD 10a","11am class begins"]
    actions_states = [
        [["P",1],["R",2],["S",3]],#State 0  
        [["R",4],["P",7]],
        [["R",4],["P",4,7],["S",5]],
        [["R",5],["P",5,8]],
        [["P",6],["R",7],["S",8]],
        [["R",8],["P",9]],
        [["R",10],["P",10],["S",10]],
        [["R",10],["P",10],["S",10]],
        [["R",10],["P",10],["S",10]],
        [["R",10],["P",10],["S",10]],
        [],#State S10
        ]
    transition_rewards = [
        [[2],[0],[-1]],#State 0  
        [[0],[2]],
        [[0],[2,2],[-1]],
        [[0],[2,2]],
        [[2],[0],[-1]],
        [[0],[2]],
        [[-1],[-1],[-1]],
        [[0],[0],[0]],
        [[4],[4],[4]],
        [[3],[3],[3]],
        [],#State S10
        ]
    
    # monte_carlo(state_names=states_names, actions_states=actions_states,transition_rewards=transition_rewards, n_episodes=50, learning_rate=0.1)
    # valueIteration(actions_states,transition_rewards,lambda_value=0.99,difference=0.001)
    old,new = q_learning(actions_states,transition_rewards)
    
    
    