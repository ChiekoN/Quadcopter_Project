# Project: Teach a Quadcopter How to Fly
## Category: Reinforcement Learning

### Overview

The **Quadcopter** or **Quadrotor Helicopter** is becoming an increasingly popular aircraft for both personal and professional use. Its maneuverability lends itself to many applications, from last-mile delivery to cinematography, from acrobatics to search-and-rescue.

Most quadcopters have 4 motors to provide thrust, although some other models with 6 or 8 motors are also sometimes referred to as quadcopters. Multiple points of thrust with the center of gravity in the middle improves stability and enables a variety of flying behaviors.

But it also comes at a price – the high complexity of controlling such an aircraft makes it almost impossible to manually control each individual motor's thrust. So, most commercial quadcopters try to simplify the flying controls by accepting a single thrust magnitude and yaw/pitch/roll controls, making it much more intuitive and fun.

The next step in this evolution is to enable quadcopters to autonomously achieve desired control behaviors such as takeoff and landing. One way to do it is using reinforcement learning to build agents that can learn these behaviors on their own. In this project, I aim to teach the agent to take off and fly up to a certain height applying Reinforcement Learning techniques.

### Goal

In this project, I design my own reinforcement learning task and an agent to complete it. My goal is to teach the agent to take off and fly up to a certain height. I define my reward function which provides the feedback to the agent when it takes an action. I need to design my reward function so that the agent can obtain more reward when it is approaching a desired behavior. Also I implement the agent's learning algorithm that makes the agent learn its behavior from the interaction with the task (environment).

After implementation and training, I examine whether the quadcopter is actually learned to take off and go up towards the height I specified. To judge it, I visualize the rewards plot, and observe how the amount of the reward the agent gains changes as it experiences more episodes. As a summary, I give a discussion about my experience through this project and suggest ideas for further improvements.

### Techniques

- The agent's learning algorithm:

 - DDPG algorithm

   [Lillicrap, Timothy P., et al., 2015. Continuous Control with Deep Reinforcement Learning](https://arxiv.org/pdf/1509.02971.pdf)

 - Replay Buffer

 - Ornstein–Uhlenbeck Process (to enhance exploratory behavior)

- Implementation to train the agent
- Visualization of rewards per episode to illustrate how the agent learns over time


### Libraries

This project requires **Python 3** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

This project runs on a [Jupyter Notebook](http://ipython.org/notebook.html)

### Files

- ```Quadcopter_Project.ipynb```: Project main file (jupyter notebook)
- ```Quadcopter_Project.html```: HTML version of above notebook (Can see this file on your browser)

- ```task.py```: My task (environment) and reward function defined.

- ```agents/```: Folder containing reinforcement learning agents.
  - ```policy_search.py```: A sample agent being provided.
  - ```agent.py```: My agent algorithm implemented.

- ```physics_sim.py```: The simulator for the quadcopter. DO NOT MODIFY THIS FILE.

- ```log_DDPG_Agent.csv```: Log file from training

- ```data.txt ```: Sample log file (not my implementation)

### Note

This project has been done as a part of Machine Learning Engineer Nanodegree program, at [Udacity](https://www.udacity.com/).
