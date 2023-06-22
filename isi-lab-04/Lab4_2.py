import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt


class Particle:
    def __init__(self, x: float, y: float, mass: float) -> None:
        self.x = x
        self.y = y
        self.mass = mass


def get_num_particles_input() -> int:
    num_particles = 0
    while True:
        try:
            num_particles = int(input("Insert the number of particles: "))
            if num_particles > 0:
                break
            else:
                print("Invalid number of particles, try again...")
        except ValueError:
            print("Invalid number of particles, try again...")

    return num_particles


def get_particles_input(num_particles: int) -> list:
    particles = []
    while num_particles > 0:
        try:
            x = float(input(f"Particle {len(particles) + 1}. Position x: "))
            y = float(input(f"Particle {len(particles) + 1}. Position y: "))
            mass = float(input(f"Particle {len(particles) + 1}. Mass: "))

            p = Particle(x, y, mass)
            particles.append(p)

            num_particles -= 1
        except ValueError:
            print("Invalid particle, try again...")

    return particles


def get_center_of_mass(
    points_x: npt.ArrayLike, points_y: npt.ArrayLike, points_mass: npt.ArrayLike
) -> Particle:
    total_mass = np.sum(points_mass)
    x = np.sum(points_mass * points_x) / total_mass
    y = np.sum(points_mass * points_y) / total_mass

    com = Particle(x, y, total_mass)
    return com


if __name__ == "__main__":
    num_particles = get_num_particles_input()
    particles = get_particles_input(num_particles=num_particles)

    points_x = np.array([p.x for p in particles])
    points_y = np.array([p.y for p in particles])
    points_mass = np.array([p.mass for p in particles])

    com = get_center_of_mass(
        points_x=points_x, points_y=points_y, points_mass=points_mass
    )

    # Create figure
    fig, ax = plt.subplots()

    # Padding
    fig.tight_layout(pad=2.5)

    # Graph
    ax.scatter(points_x, points_y, color="blue")
    ax.scatter(com.x, com.y, color="green", marker="^")
    ax.grid()
    ax.axis([points_x.min(), points_x.max(), points_y.min(), points_y.max()])
    ax.set_xlim(points_x.min() - 0.075, points_x.max() + 0.075)
    ax.set_ylim(points_y.min() - 0.075, points_y.max() + 0.075)

    # Add mass labels
    for i in range(num_particles):
        ax.text(
            points_x[i] + 0.03, points_y[i] + 0.03, f"{points_mass[i]:.2f}", fontsize=8
        )

    # Add com mass label
    ax.text(com.x + 0.03, com.y + 0.03, f"{com.mass:.2f}", fontsize=8)

    plt.show()
