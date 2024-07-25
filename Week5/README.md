# Week 5

We will start this week's topic (Temporal Difference Learning and Q Learning) today.
The next topic is on Eligibility Traces, in Chapter 6 of S&B. Please try to read it within a few days.
Please start reading the relevant chapter from S&B. The assignment will be released soon.

## Gymnasium

Provides environments to represent RL problems with a simple interface to interact with.

Documentation: https://gymnasium.farama.org/

A basic usage of gymnasium is provided in the code, but if you are interested in pursuing RL further, familiarizing
yourself with it would be highly useful.

## Mountain Car

The environment we will be solving in the assignment. The task and documentation can be found here:

https://gymnasium.farama.org/environments/classic_control/mountain_car/

### Basic Strategy:

Since the observation space is continuous, but classic RL algorithms require discrete observation spaces, we will first
discretize the observation space by grouping nearby values.
This technique, discussed by Sutton and Barto in the chapter on function approximations, will allow us to treat these
groups as single states.

Then, the method goes as usual, act $\epsilon$ greedily, and keep updating the state-action pair values based on
Q-Learning update rule:

$Q(s,a) \leftarrow Q(s,a) + \alpha (r_t + \gamma \text{max}_{a'} Q(s', a') - Q(s,a))$

You are free to play along with the hyperparameters, but one set of them have been provided to you.
It is highly suggested to try different values though, as the ones provided may not be the optimal ones and later,
you will have to decide these hyperparameters yourselves.

Once done with the basic requirements of assignment, you may try to plot various quantities to check the learning
performance of agent.
Creativity is encouraged.
You may also save the q-table every few training episodes.
