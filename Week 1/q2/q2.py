import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def PCA(init_array: pd.DataFrame):

    sorted_eigenvalues = None
    final_data = None
    dimensions = 2

    # TODO: transform init_array to final_data using PCA
    # Standardization
    # std_matrix = (init_array.values - np.mean(init_array.values)) / np.std(init_array.values)
    std_matrix = (init_array.to_numpy() - np.mean(init_array.to_numpy(), axis=0))

    # Covariance Matrix
    cov_matrix = np.cov(std_matrix.T)

    # Eigenvalues and Eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Sorting and taking the first K dimensions
    sorted_indices = np.argsort(np.abs(eigenvalues))[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # top_k_eigenvalues = sorted_eigenvalues[:dimensions]
    top_k_eigenvectors = sorted_eigenvectors[:, :dimensions]

    # Collecting the dimensions of the N samples on the top K (calculated from the
    # spread factors) eigenvectors and rounding them to 4 decimal places
    # np.dot does the projection to find the Coordinate Vector
    final_data = np.around(np.dot(std_matrix, top_k_eigenvectors), decimals=4)
    # END TODO

    return sorted_eigenvalues, final_data


if __name__ == '__main__':
    init_array = pd.read_csv("pca_data.csv", header = None)
    sorted_eigenvalues, final_data = PCA(init_array)
    np.savetxt("transform.csv", final_data, delimiter = ',')
    for eig in sorted_eigenvalues:
        print(eig)

    # TODO: plot and save a scatter plot of final_data to out.png
    plt.scatter(final_data[:, 0], final_data[:, 1])
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)

    plt.savefig("out.png")
    # END TODO
