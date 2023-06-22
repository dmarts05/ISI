import matplotlib.pyplot as plt
import numpy as np

# Create angle arrays
alpha = np.arange(0, 6 * np.pi, 0.01)
beta = alpha + (np.pi / 4.0)

# Create figure
fig, ax = plt.subplots(3, 1, figsize=(8, 8))

# Padding
fig.tight_layout(pad=2.5)

# Graph 1
cos_alpha = np.cos(alpha)
cos_beta = np.cos(beta)

(line_cos_red,) = ax[0].plot(alpha, cos_alpha, color="red")
(line_cos_black,) = ax[0].plot(alpha, cos_beta, "k--")

ax[0].set_title("Cosine function")
ax[0].legend(handles=[line_cos_red, line_cos_black], labels=["α", "α + π/4"])
ax[0].grid()
ax[0].axis([0.0, 20.0, -1.0, 1.0])

# Graph 2
sin_alpha = np.sin(alpha)
sin_beta = np.sin(beta)

(line_sin_red,) = ax[1].plot(alpha, sin_alpha, color="red")
(line_sin_black,) = ax[1].plot(alpha, sin_beta, "k--")

ax[1].set_title("Sine function")
ax[1].legend(
    handles=[line_sin_red, line_sin_black], labels=["α", "α + π/4"], loc="upper right"
)
ax[1].grid()
ax[1].axis([0.0, 20.0, -1.0, 1.0])

# Graph 3
tan_alpha = np.tan(alpha)
tan_beta = np.tan(beta)

(line_tan_red,) = ax[2].plot(alpha, tan_alpha, color="red")
(line_tan_black,) = ax[2].plot(alpha, tan_beta, "k--")

ax[2].set_title("Tangent function")
ax[2].legend(
    handles=[line_tan_red, line_tan_black], labels=["α", "α + π/4"], loc="upper right"
)
ax[2].grid()
ax[2].axis([0.0, 20.0, -10.0, 10.0])


plt.show()
