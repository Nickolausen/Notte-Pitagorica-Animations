from manim import *
import numpy as np

# Original Function
func_period_from, func_period_to = -PI, PI
func_discontinuities = []


def func(x):
    return abs(x)


# Fourier series for the func above
def series(x, n_terms):
    sum_terms = PI / 2

    # reverse order
    # adding up from small numbers
    for n in range(n_terms, 0, -1):
        if (n % 2) == 0:
            continue
        sum_terms += -(4 / (n * n * PI)) * np.cos(n * x)

    return sum_terms


# Tex
# Web Tool : Hand writing math expression to Tex
#   https://webdemo.myscript.com/views/math/index.html#
tex_func = r"""
f(x) = |x| \hspace{2em} (-\pi \leq x < \pi)
"""
tex_sim_or_equals = r"="
tex_series = r"""
f(x) = \dfrac{\pi}{2} +
\sum_{n=1}^{\infty}
    \dfrac{2}{n^{2} \pi}
    \Big( (-1) ^{n}-1 \Big) \cos nx
"""

# Number of terms
series_start, series_end, series_step = 1, 19, 2
series_run_time = 15

series_more_start, series_more_end, series_more_step = 21, 30, 10
series_more_run_time = 10

# Axes
x_min, x_max, x_step = -3.4 * PI, 3.4 * PI, PI
y_min, y_max, y_step = -0.1, PI * 1.3, 1
y_length = 3
include_ticks = False
include_tip = False
is_pi_label = True
show_x_0_label = True

# Function plot
func_x_range_min, func_x_range_max = -3.3 * PI, 3.3 * PI
plot_x_delta = 5e-3

# Color
COLOR_MESSAGE = WHITE
COLOR_FUNC = GREEN
COLOR_PERIODIC = YELLOW
COLOR_SERIES = BLUE
COLOR_TILDE = WHITE
COLOR_N_TERM_COUNT = WHITE

# Message displayed before the formula
message = "Fourier Series for"
