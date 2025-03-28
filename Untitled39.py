#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.tree import DecisionTreeClassifier
import random
X = np.array([[133, 7], [111, 7], [222, 8], [333, 8], [444, 15], [555, 16], [666, 15], [777, 16]])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0]) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
supervised_model = KNeighborsClassifier(n_neighbors=3)
supervised_model.fit(X_train, y_train)
supervised_accuracy = supervised_model.score(X_test, y_test)
unsupervised_model = KMeans(n_clusters=2, random_state=42)
unsupervised_model.fit(X)
unsupervised_labels = unsupervised_model.labels_
random_unlabeled = random.sample(range(len(y_train)), 2)
y_train_semi = y_train.copy()
for idx in random_unlabeled:
    y_train_semi[idx] = -1 
    
semi_supervised_model = SelfTrainingClassifier(base_estimator=DecisionTreeClassifier())
semi_supervised_model.fit(X_train, y_train_semi)
semi_supervised_accuracy = semi_supervised_model.score(X_test, y_test)

class QLearningAgent:
    def __init__(self, n_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.q_table = np.zeros((2, n_actions))
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.n_actions = n_actions
    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.n_actions)
        return np.argmax(self.q_table[state])
    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        self.q_table[state, action] += self.lr * (reward + self.gamma * self.q_table[next_state, best_next_action] - self.q_table[state, action])
rewards = [1, -1]  
agent = QLearningAgent(n_actions=2)
for episode in range(50):
    state = np.random.choice(2)
    action = agent.choose_action(state)
    reward = rewards[state]
    next_state = (state + 1) % 2
    agent.update(state, action, reward, next_state)
print("Supervised Learning Accuracy (KNN):", supervised_accuracy)
print("Semi-Supervised Learning Accuracy (SelfTraining):", semi_supervised_accuracy)
print("Unsupervised Learning Clusters (KMeans):", np.bincount(unsupervised_labels))
print("Reinforcement Learning Q-Table:\n", agent.q_table)



# In[ ]:




