import numpy as np

class Qlearn:
    
    def __init__(self):
        self.Q = np.zeros((pow(2,11),3))
    
    def convert_state(self,state):
        idx = 0
        for i in range(11):
            idx += state[i]*pow(2,i)
        return idx
    
    def convert_action(self,action):
        return np.argmax(action)
    
    def predict(self,state):
        idx = self.convert_state(state)
        best_action_index = np.argmax(self.Q[idx])
        
        best_action = [0,0,0]
        best_action[best_action_index] = 1
        
        return best_action
    
    def train(self, state, action, next_state, reward , learning_rate , discount_factor):
        state_idx = self.convert_state(state)
        action_idx = self.convert_action(action)
        
        next_state_idx = self.convert_state(next_state)
        best_next_action_idx = self.convert_action(self.Q[next_state_idx])
        
        self.Q[state_idx, action_idx] += learning_rate * \
        ( reward + discount_factor * self.Q[next_state_idx,best_next_action_idx] - self.Q[state_idx,action_idx])
        
    def save(self):
        with open('Qlearn_cfg.npy', 'wb') as file:
            print("----Config saved----")
            np.save(file,self.Q)
        
    def load(self):
        with open('Qlearn_cfg.npy', 'rb') as file:
            print("----Config loaded----")
            self.Q = np.load(file)
    