# Hands on RL: SOC

> **Note:**
> 
> To solve the questions in the Weeks (If you are interested ☺️), check out the Questions folder in the Weeks.
> Check out the [Course Info](CourseInfo.md) file for more details!

<!--
 ##[Prerequisites]
 -->

<!-- To Complete -->

## [Week 1](Week1)

So for the first week, we'll start with some light work.
The task is to read the first two chapters from [**Grokking**](Resources/Books/Grokking_RL.pdf)
and explore the new terms you come across.

Also, this week, we will learn about Python, in particular Python Libraries such as NumPy, TensorFlow, PyTorch,
MatPlotLib and Scikit-Learn.

We will implement some of the common ML algorithms from scratch.
Some basic ideas on Machine Learning (if you are interested) can be achieved from [**here**]().

<!--
I will provide some reading material for the same and an assignment by EOD or tomorrow.
Till then, you can get some basic ideas about Machine Learning through any online source
or YouTube video.
-->

<!--
Also, I feel the best way to enhance collaboration in this project is to make teams among the mentees.
Please find a group of co-mentees and team up with (no strict limit on team size).
Let me know the people you are teaming up with.
Also note that, in the end, we wish for all the mentees to work together on this project.
Hence, team membership is not fixed for the duration of the project, and there is no cap on team size.
Collaboration and Discussions across teams are also encouraged.
-->

### [Reading Material](Resources/Books)

- The first two chapters from [**Grokking**](Resources/Books/Grokking_RL.pdf).
- You can also read the first chapter of [**Sutton and Barto**](Resources/Books/Sutton_and_Barto.pdf)
  if you finish the first two chapters of [**Grookings**](Resources/Books/Grokking_RL.pdf).

### [Week 1 Assignment](Week1/Questions)

- [**Q1:**](Week1/Questions/q1) **Inverse Transform Sampling** - https://en.wikipedia.org/wiki/Inverse_transform_sampling
- [**Q2:**](Week1/Questions/q2)
  - **PCA** - https://youtu.be/FgakZw6K1QQ
  - **`pandas.read_csv`** - https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
  - **Scatter Plot** - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
- [**Q3:**](Week1/Questions/q3) **`scipy.optimize.curve_fit`** - https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

<!--
For this week DM the solution files to me, and we will make a proper repository the next week.
Note that using any generative AI is not encouraged.
Happy Learning!
-->

## [Week 2](Week2)

Hopefully, everyone had fun learning the basics of ML in the first week (and finished the assignment in time).
Now it's time to start with Reinforcement Learning, a paradigm in Machine Learning.
We will be learning the basics of RL this week.

Our learning objectives for this week are:

1. **N-armed bandits**:
   
   Perhaps the simplest RL challenge. You are provided with n arms, and you can pull one of them at a time. Each arm
   gives a reward from a probability distribution, independent of which arms you pulled beforehand (However, it may
   depend on the time step you pull). Your task is to maximize the sum of these rewards, i.e., finding the
   arm that gives the maximum expected reward. We will be studying a few algorithms to solve this problem.

2. **Formalism of Reinforcement Learning in terms of Markov Decision Process**:
   
   This is to generalize and represent a given problem as a Reinforcement Learning problem.

3. **Dynamic Programming**:
   
   The most basic set of algorithms to deal with prediction and control problems, that is, finding an optimal policy
   given the complete Markov Decision Process.

### [Reading Material](Resources/Books)

- [**Grokking**](Resources/Books/Grokking_RL.pdf): Skim through Chapter 1. Read and try to implement from chapters 2, 3, and 4.

- If you are more interested in theory, you may also read these topics from [**Sutton and Barto**](Resources/Books/Sutton_and_Barto.pdf).

### [Week 2 Assignment](Week2/Questions)

This ([snake.py](Week2/Questions/snake.py)) contains some starter code for creating a window and moving a square around
in it.
Modify this code to implement a game of Snake.

<!--
This project is intended to be highly collaborative: so get to know your co-mentees and work with them on this! Also,
this is a widespread game and can be found anywhere, but try implementing it yourself, adding some valid customizations
is encouraged.
-->

<!--
- **Submission deadline:** 15th June EOD, DM me your submissions and tell me the customizations if you did any.
-->

## [Week 3](Week3)

It's time to start proper Reinforcement Learning.
For Week 3, we will be looking at two classes of algorithms to deal with prediction and control problems, when we don't
know the model of the environment:

1. Monte Carlo Methods
2. Temporal Difference Learning

### [Reading Material](Resources/Books)

- The primary reading material for this week will be Chapters 5 and 6 of [**Grokking RL**](Resources/Books/Grokking_RL.pdf).

- Also, if you are interested in a more theoretical approach,
  you may refer to Chapters 5 and 6 from [**Sutton and Barto**](Resources/Books/Sutton_and_Barto.pdf) and additionally,
  Chapter 7 for Eligibility Traces, which acts as a bridge between these two classes of algorithms.
  The topics may seem more difficult than what you have been reading up on, but the basic ideas remain the same,
  and by the end, you will get a sense of how these algorithms are constructed.

- Refer to [**this book**](Resources/Books/TS_Tutorial.pdf) if anyone is interested in learning more about the theory of [**Thompson Sampling**](Resources/Books/TS_Tutorial.pdf).

<!--
Assignments for this week will be released shortly (we will probably start with our first game 🥳, albeit a simple one).
PS: Do submit the assignment for the previous week as soon as possible 🥲.
-->