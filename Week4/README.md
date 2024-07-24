# Week 4

We shall properly learn about **Multi-armed bandits** and **Finite Markov decision processes**.

## Reading Material
It is implementation time! Learn along with the assignment!

## [Assignment](Questions)

You have to implement some policies for the Multi-armed bandit problem.

The file structure:
```text
Questions
├── bandits.py
│   ├── (↓ Distributions ↓)
│   ├── Bernoulli
│   └── Gaussian
├── agents.py
└── results.py
```

### `bandits.py`
This file contains the class for the bandit.
No need to edit this unless you want to add new input formats, e.g., batch wise processing.

Currently, it implements two types of distribution for bandit arms:

- **Bernoulli**: Returns a reward of 1 with fixed probabilities.
- **Gaussian**: Returns reward from a Gaussian Distribution with a fixed mean (dependent on the arm) and `variance = 1`.

The `Bandit` class also tracks the regret: 
$ \text{regret}(T) = {T \cdot \text{optimal}} - \text{reward} - {\sum\limits_{t=1}^T} {R_t} $
You can access the regret at any timestamp using the `get_regret()` function.

> [!NOTE]
> 
> For Thompson Sampling, the Beta Distribution (`np.random.beta`) is the conjugate prior for a Bernoulli Distribution.

### `agents.py`
This file contains the class for agents and subclasses for each policy type.
You only need to implement the subclasses unless you want to add something new or fix bugs.

### `results.py`
This file is for showing your results. Train the algorithms and plot the graphs. Be creative.
