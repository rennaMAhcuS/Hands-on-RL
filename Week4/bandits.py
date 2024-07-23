import numpy as np


class Bandit:
    """This class describes a Bandit with n possible actions"""

    BANDIT_TYPES = ("Bernoulli", "Gaussian")

    def __init__(self, n: int, distro_type: str) -> None:
        assert distro_type in Bandit.BANDIT_TYPES
        self.N = n
        self.type = distro_type
        if distro_type == "Bernoulli":
            # bandits will give reward/no reward
            self.probs = np.random.uniform(size=(n,))
            self.optimal = np.max(self.probs)

        elif distro_type == "Gaussian":
            self.means = np.random.normal(15, 10, (n,))
            self.optimal = np.max(self.means)

        self.regret = 0.0

    # Gets the cumulative regret
    def get_regret(self) -> float:
        return self.regret

    def getN(self) -> int:
        return self.N

    def reset_regret(self) -> None:
        self.regret = 0.0

    # pull the kth lever 0 to n-1
    def choose(self, k: int) -> int:
        assert 0 <= k < self.N
        # returns 1 with probability = self.probs[k]
        if self.type == "Bernoulli":
            reward = np.random.binomial(1, self.probs[k])
            self.regret += self.optimal - reward
            return int(reward)

        # Returns reward based on gaussian distribution
        elif self.type == "Gaussian":
            reward = np.random.normal(self.means[k], 1)
            self.regret += self.optimal - reward
            return int(reward)
