# Week 5

This week, we will focus on **Temporal Difference Learning and Q Learning**.
We will also explore **Eligibility Traces**, covered in **Chapter 6 of Sutton and Barto**.

## Gymnasium

Gymnasium provides environments for reinforcement learning problems with a simple interface with which to interact.
Refer to the [**Gymnasium Documentation**](https://gymnasium.farama.org/).
The code provides primary gymnasium usage, but familiarizing yourself with it would be highly useful if you are
interested in pursuing RL further.

## Assignment — Mountain Car

The environment we'll tackle in the assignment is the Mountain Car.
Details and documentation can be found here:
[Mountain Car Environment](https://gymnasium.farama.org/environments/classic_control/mountain_car/)

### Basic Strategy:

Since the observation space is continuous and classic RL algorithms require discrete observation spaces, we'll first
discretize the observation space by grouping nearby values.
This technique, as discussed by Sutton and Barto in the chapter on function approximations, will help us treat these
groups as single states.
Then, proceed with the usual method: act $ \epsilon $ greedily and update the state-action pair values using the
Q-Learning update rule:

$ Q(s,a) \leftarrow Q(s,a) + \alpha (r_t + \gamma \text{max}_{a'} Q(s', a') - Q(s,a)) $

Experiment with different hyperparameters.
One set is given.
It is highly suggested to try different values, though, as the ones provided may not be the optimal ones, and later,
You will have to decide on these hyperparameters yourselves.
Creativity is encouraged — plot various quantities to check the agent's learning performance and consider saving the
q-table periodically during training.