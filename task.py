import numpy as np
from physics_sim import PhysicsSim

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 
        
        self.prev_pose = self.sim.pose # initialize the previous position as the initial position
        self.init_pose = self.sim.pose 

    def get_reward(self):
        """Uses current pose of sim to return reward."""       
        
        ##### Give a positive reward when it is going up, a negative reward when it is going down.
        # relative_height = self.sim.pose[2] - self.prev_pose[2]
        # reward = relative_height
        
        ##### Give a larger reward as it gets closer to the target.
        dist_tar_sim = self.target_pos[2] - self.sim.pose[2]
        dist_tar_init  = self.target_pos[2] - self.init_pose[2]
        reward_sqr = -(dist_tar_sim**2) + (dist_tar_init**2)
        #reward = reward_sqr*0.001
        reward = np.sqrt(reward_sqr)*0.1 if reward_sqr >= 0 else -np.sqrt(abs(reward_sqr))*0.1
                                
        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        self.prev_pose = self.sim.pose # store the current position
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        self.prev_pose = self.sim.pose # store the initial position as the previous position
        self.init_pose = self.sim.pose
        return state