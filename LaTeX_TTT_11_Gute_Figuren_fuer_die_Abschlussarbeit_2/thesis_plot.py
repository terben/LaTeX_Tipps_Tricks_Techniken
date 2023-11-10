import matplotlib
import numpy as np

# store original plot parameters so that we can revert:
ORIG_MATPLOTLIB_CONF = dict(matplotlib.rcParams)

def thesis_plot(fig_width=None, fig_height=None,
                fontsize=12, draft=False):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this function before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches; default is 0.9 * 6.2 inch
    fig_height : float,  optional, inches
    fontsize : 12 pt default
    draft : False by default (False: LaTeX rendering is used; maybe slow)
    """

    if fig_width is None:
        # we take a DINA4 scrartcl LaTeX class
        # with a fontsize of 12 pt and a textwidth of 6.2 inch as default.
        # Our default figure size is the 0.9 * 6.2 inch.
        # Just change according to your own thesis textwidth dimensions.
        fig_width = 0.9 * 6.2

    # If we do not provide a figure_height, we take the golden ratio
    # as the ratio between figure width and figure height. It gives a
    # visually appealing impression.
    if fig_height is None:
        golden_mean = (np.sqrt(5.0) - 1.0) / 2.0    # Aesthetic ratio
        # height in inches
        fig_height = fig_width * golden_mean

    # modify matplotlib parameters to enable LaTeX rendering of your plots.
    # Only change if you know what you are doing!

    # If we use LaTeX to render our figures, we can provide packages
    # to the LaTeX interpreter. This is important if you change fonts
    # in your preamble. Then you need to include corresponding packages
    # here as well to obatin the same fonts within your plots:
    latex_preamble = "\n".join([
        r'\usepackage[utf8]{inputenc}',
        r'\usepackage[T1]{fontenc}',
        r'\usepackage[locale = DE]{siunitx}',
    ])

    params_latex = {}
    # If we enable the draft option, LaTeX is *not* used to render
    # our figures. This is useful to build up the figure as the
    # processing is faster.
    if draft == False:
        params_latex = {'text.usetex' : True,
                        'text.latex.preamble' : latex_preamble
                        }

    params_default = {
        'font.family' : 'serif',
        'axes.labelsize' : fontsize,
        'axes.titlesize' : fontsize,
        'font.size': fontsize,
        'legend.fontsize' : fontsize - 2,
        'xtick.labelsize' : fontsize - 2,
        'ytick.labelsize' : fontsize - 2,
        'axes.linewidth' : 1,
        'lines.linewidth' : 1,
        'figure.figsize' : [fig_width, fig_height],
        'figure.constrained_layout.use' : True,
        'savefig.dpi' : 300  # set to 600 for poster printing or PR
                             # figures
    }

    params = {**params_latex, **params_default}

    matplotlib.rcParams.update(params)

def revert_params():
    """
    reverts any changes done to matplotlib parameters and restores
    the state before thesis_plot was called
    """

    matplotlib.rcParams.update(ORIG_MATPLOTLIB_CONF)
