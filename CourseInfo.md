# Hands-on Reinforcement Learning [Project ID: 153]

## (IIT Bombay) ITSA-2024: SoC

## General Information

- **General Category:** Machine Learning
- **Specific Category:** RL
- **Mentee Capacity:** 10-15
- **Mentor:** Soham Dahane (22b0941)
- **Co-Mentor:** Shreyas Katdare (22b0636)
- [**Source GitHub Repo Fork**](https://github.com/rennaMAhcuS/Hands-on-RL-Source)
- [**Source GitHub Repo**](https://github.com/SohamD1234/HandsOnRL-SOC)
- **Description:**
  Hands-on Reinforcement Learning.
  Reading material: Sutton & Barto, "Grokking Deep Reinforcement Learning."
  We will be following Grokking as a reference for the theory and reading chapters from it while implementing the
  strategies described in it in Python.
  Some resources we may use are the
  [Slides on RL by David Silver](https://www.deepmind.com/learning-resources/introduction-to-reinforcement-learning-with-david-silver)
  and the [Slides from the course CS 747: Foundations of Intelligent and Learning Agents](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2022/index.html).
  I have done both WiDS and SoC myself under the same topic
  ([Project Repo](https://github.com/theashwinabraham/WiDS-Training-AI-to-play-games-using-Reinforcement-Learning)).

## Timeline

- **Week 1: Implementations of Common Machine Learning Algorithms**
  - Using the standard implementations of some famous algorithms using Scikit-Learn.
- **Week 2: MAB, MDPs, Implement a Game of Snake**
  - Learning objectives for this week are:
    1. **N-armed bandits:** Perhaps the simplest RL challenge.
       You are provided with n arms, and you can pull one of them at a time.
       Each arm gives a reward from a probability distribution, independent of which arms you pulled beforehand
       (However, it may depend on the time step you pull).
       Your task is to maximize the sum of these rewards, essentially finding the arm that gives the maximum expected reward.
       We will be studying a few
       algorithms to solve this problem.
    2. **Formalism of Reinforcement Learning in terms of Markov Decision Process:** A way to generalize and
       represent a given problem as a Reinforcement Learning problem.
    3. **Dynamic Programming:** The most basic set of algorithms to deal with prediction and control problems, that
       is, finding an optimal policy given the complete Markov Decision Process.
- **Week 3: Monte Carlo Methods, Temporal Difference Learning**
  - **Part I:** Implementing the Monte Carlo ES algorithm for a given MDP.
    I've provided the MDP as a Linux executable.
    If it doesn't run on your device, please let me know, and I will share another executable.
  - **Part II:** Solving the game of Tic Tac Toe.
    Tic Tac Toe can be solved exactly via the minimax algorithm, and in Part I you will have to implement this algorithm.
    However, you will see that this algorithm is extremely computationally expensive.
    Therefore, we will use an on-policy RL algorithm (we will use an algorithm based on ε-soft policies).
- **Week 4: DDQN**
  - Reading chapters from Grokking and implementing.
- **Weeks 5 & 6: Implementing a Paper to Create a Chess Engine Based on Deep RL**
  - Implement the paper.

## Checkpoints

- **Checkpoint 1:** Implementations of Common Machine Learning Algorithms
- **Checkpoint 2:** MAB, MDPs, Implement a Game of Snake
- **Checkpoint 3:** Monte Carlo Methods, Temporal Difference Learning
- **Checkpoint 4:** DDQN
- **Checkpoints 5 & 6:** Implementing a Paper to Create a Chess Engine Based on Deep RL

## Prerequisites

1. Basic knowledge of Python libraries like NumPy, and SkLearn.
2. Basic knowledge of RL (can read the first 2–3 chapters from Sutton & Barto).

<!--
## Statement of Purpose (SOP)

I am very much interested in learning about Reinforcement Learning and Machine Learning (as AI-ML is a field with very
high demand 🙂). I believe working on your project would be a fantastic way for me to advance in this area. I am excited
to learn about the theoretical foundations of reinforcement learning and machine learning and their real-world
applications. I also have a basic knowledge of Python. I have a strong commitment to learning and meeting deadlines. I
am confident that my participation will enhance my Machine Learning and Reinforcement Learning expertise.
-->