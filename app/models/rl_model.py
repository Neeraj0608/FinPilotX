import gymnasium as gym
from gymnasium import spaces
import numpy as np
from stable_baselines3 import PPO

class TradingEnv(gym.Env):
    """A simple trading environment for RL demo."""
    def __init__(self, df):
        super(TradingEnv, self).__init__()
        self.df = df.reset_index()
        self.current_step = 0
        
        # Action space: 0 (Hold), 1 (Buy), 2 (Sell)
        self.action_space = spaces.Discrete(3)
        
        # Observation space: Close price + Technical Indicators
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(5,), dtype=np.float32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_step = 0
        return self._get_observation(), {}

    def step(self, action):
        self.current_step += 1
        done = self.current_step >= len(self.df) - 1
        
        # Simplified reward: price change if Buy, negative if Sell, 0 if Hold
        price_change = self.df.loc[self.current_step, 'Close'] - self.df.loc[self.current_step - 1, 'Close']
        reward = 0
        if action == 1: # Buy
            reward = price_change
        elif action == 2: # Sell
            reward = -price_change
            
        obs = self._get_observation()
        return obs, reward, done, False, {}

    def _get_observation(self):
        # Mocking 5 indicators for the observation
        return np.random.rand(5).astype(np.float32)

class RLTrader:
    def __init__(self):
        self.model = None

    def train(self, df):
        """Train PPO agent on provided data."""
        env = TradingEnv(df)
        self.model = PPO("MlpPolicy", env, verbose=0)
        self.model.learn(total_timesteps=1000)
        return self.model

    def predict(self, df):
        """Run the trader on data."""
        if self.model is None:
            self.train(df)
            
        env = TradingEnv(df)
        obs, _ = env.reset()
        actions = []
        done = False
        while not done:
            action, _states = self.model.predict(obs)
            actions.append(action)
            obs, reward, done, truncated, info = env.step(action)
        return actions
