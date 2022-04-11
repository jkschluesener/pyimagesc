#!/usr/bin/env python

"""
@license: MIT
@author: Jan K. Schluesener
https://github.com/jkschluesener/pyimagesc
pyimagesc
"""

import numpy as np
import matplotlib.pylab as plt


def imagesc(d, ax=None, **kwargs):
    """Quick display of matrices that are not (even close to) square

    Display images similar to Matlab's `imagesc` function.
    This change in display parameters is very useful for
    fast review of arrays, for e.g. debugging or denoising.

    The difference to the default plt.imshow() parameters are the following:
        - 'aspect': 'auto':
            Aspect is adjusted so that the data fits the axes, resulting in non-square pixels.
        - 'interpolation': None:
            No interpolation is performed (if possible depending on the backend).

    The [0, 0] coordinate of the matrix is the upper left, as is default for most applications.

    Parameters
    ----------
    d : np.ndarray
        Data array to display, with at most 2 dimensions
    ax : matplotlib axis handle, optional
        Axis handle to plot on, otherwise one will be created, by default None
    **kwargs
        Arbitrary keyword arguments that will be passed on to matplotlib.pylab.imshow.
        See the matplotlib documentation for more information on possible keywords.

    Returns
    -------
    Figure handle or None
        Figure handle of the created plot. If `ax` was supplied, `None` is returned.
    """

    # ensure the input is a 2d numpy array
    if not isinstance(d, np.ndarray):
        d = np.array(d)
    assert len(d.shape) <= 2, 'Array must be at most 2-dimensional'
    d = np.atleast_2d(d)

    # update the user-supplied kwargs with our default parameters
    kwargs.update({'aspect': 'auto',
                   'interpolation': 'none'})

    # create a new figure if no axis was supplied
    if ax is None:
        fig, ax = plt.subplots(1, 1)
    else:
        fig = None

    # display array, pass kwargs on
    ax.imshow(d, **kwargs)

    return fig
