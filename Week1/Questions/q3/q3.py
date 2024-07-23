from typing import Callable

import pandas as pd


def func(t, func_v, func_k):
    """ computes the function S(t) with constants v and k """

    # TODO: return the given function S(t)

    # END TODO


def find_constants(df_to_fit: pd.DataFrame, func_to_fit: Callable):
    """ returns the constants v and k """

    fit_v = None
    fit_k = None

    # TODO: fit a curve using SciPy to estimate v and k

    # END TODO
    # v and k should be of the appropriate dtype
    return fit_v, fit_k


if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    v, k = find_constants(df, func)
    v = v.round(4)
    k = k.round(4)
    print(v, k)

    # TODO: plot a histogram and save to fit_curve.png

    # END TODO
