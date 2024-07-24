# Week 2

Hope everyone had fun learning the basics of ML in the first week.
Now it's time to start with Reinforcement Learning, a paradigm in Machine Learning.
We will be learning the basics of RL this week.

Our learning objectives for this week are:

1. **N-armed bandits**:
   Perhaps the simplest RL challenge.
   You are provided with n arms, and you can pull one of them at a time.
   Each arm gives a reward from a probability distribution, independent of which arms you pulled beforehand
   (However, it may depend on the time step you pull).
   Your task is to maximize the sum of these rewards, i.e., finding the arm that gives the maximum expected reward.
   We will be studying a few algorithms to solve this problem.

2. **Formalism of Reinforcement Learning in terms of Markov Decision Process**:
   Way to generalize and represent a given problem as a Reinforcement Learning problem.

3. **Dynamic Programming**:
   The most basic set of algorithms to deal with prediction and control problems, that is, finding an optimal policy
   given the complete Markov Decision Process.


## Reading Material

- Skim through chapter 1 of **Grokking**. Read and try to implement from chapters 2, 3 and 4.
- If you are more interested in theory, you may also read these topics from **Sutton and Barto**.


## [Assignment](Assignment)

This [snake.py](Assignment/snake.py) contains some starter code for creating a window and moving a square around in it.
Modify this code to implement a game of **Snake**.