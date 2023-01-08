
import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize

LENGTH = 10 * 60
SAMPLES = 600

t = np.random.rand(SAMPLES) * LENGTH

COOLING_CONSTANT = 0.00918
START_TEMP = 212
AMB_TEMP = 70

y = AMB_TEMP + (START_TEMP - AMB_TEMP) * np.exp(-COOLING_CONSTANT * t)

noise = np.random.normal(0, 1, SAMPLES)

y += noise


# CUT = 0.5
params = scipy.optimize.curve_fit(
    lambda t, k, c: c + (START_TEMP - c) * np.exp(-k * t),
    t[:50], y[:50]
)
g_k, g_amb = params[0]

print(g_k, g_amb)

# plt.scatter(t, y)
# plt.show()
