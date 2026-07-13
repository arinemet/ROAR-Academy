import gymnasium as gym
from gymnasium.utils.play import play
import pygame

env = gym.make("Pendulum-v1", render_mode="rgb_array")

keys_to_action = {
    (pygame.K_LEFT,): 0,
    (pygame.K_RIGHT,): 1
}

# Fix: noop must be a valid integer action (0), NOT None.
# wait_on_player=True stops it from running automatically.
play(env, keys_to_action=keys_to_action, noop=0, wait_on_player=False)
