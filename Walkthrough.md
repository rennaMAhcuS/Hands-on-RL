# Hands on RL: SOC

> **Note:**
> To solve the questions in the Weeks (If you are interested ☺️), checkout the Questions folder in the Weeks.

## [Prerequisites](Books)

<!-- To Complete -->

## [Week 1](Week1)

So for the first week we'll start with a bit of light work. Your task will be to read the first two chapters from
grookings and explore more about the new terms that you come across.

Also in this week, we will learn about Python, in particular Python Libraries such as NumPy, TensorFlow, PyTorch,
MatPlotLib and Scikit-Learn.

We will implement some of the common ML algorithms from scratch, I will provide some reading material for the same and
an assignment by eod or by tomorrow. Till then, you can get some basic ideas about Machine Learning through any online
source or YouTube video.

### [Week 1 Assignment](Week1/week1.pdf)

- **Q1:** _Inverse Transform Sampling_ - https://en.wikipedia.org/wiki/Inverse_transform_sampling
- **Q2:**
    - _PCA_ - https://medium.com/analytics-vidhya/understanding-principle-component-analysis-pca-step-by-step-e7a4bb4031d9q2.
    - _pandas.read_csv_ - https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    - _scatter plot_ - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
- **Q3:** _scipy.optimize.curve fit._ - https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

## [Week 2](Week2)

Hope everyone had fun learning the basics of ML in the first week (and finished the assignment in time). Now it's time
to start with Reinforcement Learning, a paradigm in Machine Learning. We will be learning the basics of RL this week.

Our learning objectives for this week are:

1. **N-armed bandits:**

   Perhaps the simplest RL challenge. You are provided with n arms, and you can pull one of them at a time. Each arm
   gives a reward from a probability distribution, independent of which arms you pulled beforehand (However it may
   depend on the time step you pull). Your task is to maximize the sum of these rewards, that is essentially find the
   arm which gives the maximum expected reward. We will be studying few algorithms to solve this problem.

2. **Formalism of Reinforcement Learning in terms of Markov Decision Process:**

   Way to generalise and represent a given problem as a Reinforcement Learning problem.

3. **Dynamic Programming:**

   The most basic set of algorithms to deal with prediction and control problems, that is, finding an optimal policy
   given the complete Markov Decision Process.

### [Week 2 Assignment](Week2)

This ([snake.py](Week2/snake.py)) contains some starter code for creating a window and moving a square around in
it. Modify this code to implement a game of Snake. (This project is intended to be highly collaborative, so get to know
your co-mentees and work with them on this! Also, this is a very common game and can be found anywhere but try
implementing it yourself, adding some valid customisations is encouraged.)
- **Submission deadline:** 15th June EOD, dm me your submissions and tell the customisations if you did any.