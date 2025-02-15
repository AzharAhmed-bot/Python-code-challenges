# RL model for traffic lights
# RL models basically derive a function that will be rewarded or punished considering how it performed
# They follow the Markov decision process
# 1. No. of states
# 2. Set of actions
# 3. Transition model
# 4. The reward

# Most famous example is the Q-learning that'll always come up with Q(s,a) in form of reward
# How?
# Q(s,a) <--- Q(s,a) + α((r+ γ * max(Q(s',a'))))- Q(s,a))
# learning rate
# discount factor
# Epsilon e- Measure Exploitation vs exploration
import math
import random


class TrafficLightAI:
    def __init__(self,alpha=0.5,gamma=0.9,epsilon=0.1):
        self.q=dict()
        self.alpha=alpha
        self.gamma=gamma
        self.epsilon=epsilon
        self.possible_actions=["NS-Green","EW-green"]
        self.max_car_depart=4

    def initial_state(self):
        return tuple([0,0,0,0])


    def update(self,old_state,action,new_state,reward):
        old_q=self.get_q_value(old_state,action)
        best_future=self.best_future_reward(new_state)
        self.update_q_value(old_state,action,old_q,reward,best_future)


    def get_q_value(self,state,action):
        if (tuple(state),action) in self.q:
            return self.q[(tuple(state),action)]
        else:
            return 0

    def update_q_value(self,state,action,old_q,reward,future_rewards):
        new_q=old_q+self.alpha*(reward+self.gamma*future_rewards-old_q)
        self.q[(tuple(state),action)]=new_q
    
    def best_future_reward(self,state):
        best_reward=0
        for action in self.possible_actions:
            if (tuple(state),action) in self.q:
                best_reward=max(best_reward,self.q[(tuple(state),action)])
        return best_reward
    
    def calculate_reward(self,cars):
        return -sum(cars)
        
    def choose_action(self,state,epsilon=True):
        if random.random() < self.epsilon:
            return random.choice(self.possible_actions)
        
        best_reward=-math.inf
        best_action=None
        for action in self.possible_actions:
            if self.get_q_value(state,action) > best_reward:
                best_reward=self.get_q_value(state,action)
                best_action=action
        
        return best_action
    
    def simulate_traffic(self,cars,action):
        new_cars=cars.copy()
        arrival_prob=0.8
        if action== "NS-Green":
            new_cars[0]=max(0,new_cars[0]-self.max_car_depart)
            new_cars[1]=max(0,new_cars[1]-self.max_car_depart)
        else:
            new_cars[2]=max(0,new_cars[2]-self.max_car_depart)
            new_cars[3]=max(0,new_cars[3]-self.max_car_depart)

        for i in range(4):
            if random.random() < arrival_prob:
                new_cars[i]+=1

        return tuple(new_cars)
    

def test(model, steps=60):
    current_state = (0, 0, 0, 0)  
    print("\nTesting trained agent:")
    print("Step | Cars (N, S, E, W) | Action     | Total Cars")
    print("-" * 50)

    for step in range(steps):
        total_cars = sum(current_state)
        action = model.choose_action(current_state, epsilon=False) 
        new_state = model.simulate_traffic(list(current_state), action)

        print(f"{step+1:4} | {current_state} | {action:10} | {total_cars}")

        current_state = new_state 

def train(n):
    ai = TrafficLightAI()
    current_state = (1, 2, 3, 4) 

    for i in range(n):
        action = ai.choose_action(current_state)
        new_state = ai.simulate_traffic(list(current_state), action)
        reward = ai.calculate_reward(new_state)
        ai.update(current_state, action, new_state, reward)
        current_state = new_state

    print("\nTraining complete!")
    test(ai)




print(train(1000))






