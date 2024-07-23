import numpy as np
import pandas as pd


def pca(pca_init_array: pd.DataFrame):
    pca_sorted_eigenvalues = None
    pca_final_data = None
    dimensions = 2  # Use this while writing the function

    # TODO: transform init_array to final_data using PCA

    # END TODO

    # pca_sorted_eigenvalues and pca_final_data should be of the appropriate dtype
    return pca_sorted_eigenvalues, pca_final_data


if __name__ == '__main__':
    init_array = pd.read_csv("pca_data.csv", header=None)
    sorted_eigenvalues, final_data = pca(init_array)
    np.savetxt("transform.csv", final_data, delimiter=',')
    for eig in sorted_eigenvalues:
        print(eig)

    # TODO: plot and save a scatter plot of final_data to out.png

    # END TODO
