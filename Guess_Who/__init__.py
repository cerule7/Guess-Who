from gym.envs.registration import register

register(
    id='guess-who-v0',
    entry_point='gym_guess_who.envs:GuesswhoEnv',
)