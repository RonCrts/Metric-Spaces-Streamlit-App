import streamlit as st
import numpy as np
import dask.array as da
import seaborn as sns
import matplotlib.pyplot as plt
from db import MetricSpaces



def define_metric_space(X):
    """
    Calculates the distance matrix of a set of points X.

    Parameters:
    X (numpy.ndarray): Set of points.

    Returns:
    numpy.ndarray: Distance matrix of the metric space.
    """
    def metric(x, y):
        """
        Defines a metric function.

        Parameters:
        x (float): First point.
        y (float): Second point.

        Returns:
        float: Distance between the two points.
        """
        return abs(x - y)

    chunk_size = len(X) // 2
    if len(X) % 2 != 0:
        chunk_size += 1

    X_dask = da.from_array(X, chunks=(chunk_size,))
    D_dask = da.zeros((len(X), len(X)), chunks=(chunk_size, chunk_size))

    for i in range(len(X)):
        for j in range(len(X)):
            D_dask[i, j] = metric(X_dask[i], X_dask[j])

    D = D_dask.compute()

    return D


def is_metric_space(D):
    """
    Verifies if a distance matrix is a metric space.

    Parameters:
    D (numpy.ndarray): Distance matrix of the metric space.

    Returns:
    bool: True if the distance matrix is a metric space, False otherwise.
    """
    # Verifies if the distance matrix is square.
    if D.shape[0] != D.shape[1]:
        return False

    # Verifies if the distance matrix is symmetric.
    if not np.allclose(D, D.T):
        return False

    # Verifies if the distance matrix satisfies the triangle inequality.
    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            for k in range(D.shape[0]):
                if D[i, j] > D[i, k] + D[k, j]:
                    return False

    return True


def plot_metric_space(D):
    """
    Plots the distance matrix of a metric space.

    Parameters:
    D (numpy.ndarray): Distance matrix of the metric space.

    Returns:
    None
    """
    sns.heatmap(D, annot=True, cmap='Blues')
    plt.title('Distance Matrix')
    plt.xlabel('Points')
    plt.ylabel('Points')
    st.pyplot()

