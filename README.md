# Hands on RL: SOC

> **Note:**
>
> To solve the questions in the Weeks (If you are interested ☺️), checkout the Questions folder in the Weeks.
> Check out the [Course Info](CourseInfo.md) file for more details!

## [Prerequisites]

<!-- To Complete -->

## [Week 1](Week1)

So for the first week we'll start with a bit of light work. Your task will be to read the first two chapters from
[**Grokking**](Books/Grokking_RL.pdf) and explore more about the new terms that you come across.

Also in this week, we will learn about Python, in particular Python Libraries such as NumPy, TensorFlow, PyTorch,
MatPlotLib and Scikit-Learn.

We will implement some of the common ML algorithms from scratch, I will provide some reading material for the same and
an assignment by eod or by tomorrow. Till then, you can get some basic ideas about Machine Learning through any online
source or YouTube video.

<!--
Also, I feel the best way to enhance collaboration in this project is to make teams among the mentees.
Please find a group of co-mentees and team up with (no strict limit on team size).
Let me know the people you are teaming up with.
Also note that, in the end, we wish for all the mentees to work together on this project.
Hence, team membership is not fixed for the duration of the project, and there is no cap on team size.
Collaboration and Discussions across teams is also encouraged.
-->

### [Reading Material](Books)

- The first two chapters from [**Grokking**](Books/Grokking_RL.pdf).
- You can also read the first chapter of [**Sutton and Barto**](Books/Sutton_and_Barto.pdf) and further if you
  finish the first two chapters of [**Grookings**](Books/Grokking_RL.pdf).

### [Week 1 Assignment](Week1/Questions)

- [**Q1:**](Week1/Questions/q1) **Inverse Transform Sampling** - https://en.wikipedia.org/wiki/Inverse_transform_sampling
- [**Q2:**](Week1/Questions/q2)
    - **PCA** -
      https://medium.com/analytics-vidhya/understanding-principle-component-analysis-pca-step-by-step-e7a4bb4031d9q2
    - **`pandas.read_csv`** - https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    - **Scatter Plot** - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
- [**Q3:**](Week1/Questions/q3) **`scipy.optimize.curve_fit`** -
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

<!--
For this week DM the solution files to me, we will make a proper repository from the next week.
Note that using any generative AI is not encouraged.
Happy Learning!
-->

## [Week 2](Week2)

Hope everyone had fun learning the basics of ML in the first week (and finished the assignment in time). Now it's time
to start with Reinforcement Learning, a paradigm in Machine Learning. We will be learning the basics of RL this week.

Our learning objectives for this week are:

1. **N-armed bandits**:

   Perhaps the simplest RL challenge. You are provided with n arms, and you can pull one of them at a time. Each arm
   gives a reward from a probability distribution, independent of which arms you pulled beforehand (However, it may
   depend on the time step you pull). Your task is to maximize the sum of these rewards; that is essentially finding the
   arm which gives the maximum expected reward. We will be studying a few algorithms to solve this problem.

2. **Formalism of Reinforcement Learning in terms of Markov Decision Process**:

   Way to generalize and represent a given problem as a Reinforcement Learning problem.

3. **Dynamic Programming**:

   The most basic set of algorithms to deal with prediction and control problems, that is, finding an optimal policy
   given the complete Markov Decision Process.

### [Reading Material](Books)

- [**Grokking**](Books/Grokking_RL.pdf):

  Skim through chapter 1. Read and try to implement from chapters 2, 3 and 4.

- If you are more interested in theory, you may also read these topics from
  [**Sutton and Barto**](Books/Sutton_and_Barto.pdf).

### [Week 2 Assignment](Week2/Questions)

This ([snake.py](Week2/Questions/snake.py)) contains some starter code for creating a window and moving a square
around in it.
Modify this code to implement a game of Snake.
(This project is intended to be highly collaborative: so get to know your co-mentees and work with them on this! Also,
this is a widespread game and can be found anywhere, but try implementing it yourself, adding some valid customisations
is encouraged.)

<!--
- **Submission deadline:** 15th June EOD, DM me your submissions and tell the customizations if you did any.
-->

## [Week 3](Week3)

It's time to start proper Reinforcement Learning.
For Week 3, we will be looking at two classes of algorithms to deal with prediction and control problems, when we don't
know the model of the environment:

1. Monte Carlo Methods
2. Temporal Difference Learning

### [Reading Material](Books)

- The primary reading material for this week will be Chapters 5 and 6 of [**Grokking RL**](Books/Grokking_RL.pdf).

- Also, if you are interested in a more theoretical approach, you may also refer to chapters 5 and 6 from
  [**Sutton and Barto**](Books/Sutton_and_Barto.pdf) and additionally chapter 7 for Eligibility Traces, which
  acts as a bridge between these two classes of algorithms.
  The topics may seem more difficult than what you have been reading upon, but the basic ideas remain the same, and by
  the end, you will definitely get a sense of how these algorithms are constructed.

<!--
Assignments for this week will be released shortly (we will probably start with our first game 🥳, albeit a simple one).
PS: Do submit the assignment for the previous week as soon as possible 🥲.
-->