import json
import numpy as np
import matplotlib.pyplot as plt

def inv_transform(distribution: str, num_samples: int, **kwargs) -> list:
    """ populate the 'samples' list from the desired distribution """

    samples = []

    # TODO: first generate random numbers from the uniform distribution
    random_U = np.random.random(num_samples)
    if distribution == "cauchy":
        samples.extend(np.around(kwargs["gamma"] * np.tan(np.pi * (random_U - 0.5)) + kwargs["peak_x"], decimals=4))
    elif distribution == "exponential":
        samples.extend(np.around(np.log(1 / random_U) / kwargs["lambda"], decimals=4))
    # END TODO
            
    return samples


if __name__ == "__main__":
    np.random.seed(42)

    for distribution in ["cauchy", "exponential"]:
        file_name = "q1_" + distribution + ".json"
        args = json.load(open(file_name, "r"))
        samples = inv_transform(**args)
        
        with open("q1_output_" + distribution + ".json", "w") as file:
            json.dump(samples, file)

        # TODO: plot and save the histogram to "q1_" + distribution + ".png"
        plt.hist(samples, bins='auto')
        plt.savefig("q1_" + distribution + ".png")
        plt.clf()
        # END TODO
