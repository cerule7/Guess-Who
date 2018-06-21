from gym.envs.registration import register

register(
    id='guesswho-v0',
    entry_point='gym_guesswho.envs:GuesswhoEnv',
)
register(
    id='guesswho-extrahard-v0',
    entry_point='gym_guesswho.envs:GuesswhoExtraHardEnv',
)