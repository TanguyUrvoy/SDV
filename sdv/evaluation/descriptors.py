import numpy as np
import scipy as sp


def categorical_distribution(column):
    """Compute the empirical distribution for a categorical column.

    Args:
        column(pandas.Series): Column to compute the empirical distribution.

    Returns:
        pandas.Series: Serie whose index are the catogories, and their relative frequency is
                       their value.

    """
    return column.value_counts(normalize=True)


DESCRIPTORS = {
    'mean': np.mean,
    'std': np.std,
    'skew': sp.stats.skew,
    'kurtosis': sp.stats.kurtosis,
    'categorical_distribution': categorical_distribution
}
