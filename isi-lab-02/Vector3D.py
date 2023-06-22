import math
import pickle


class Vector3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def change_coordinates(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def to_string(self) -> str:
        return f"({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})"

    def print_vector(self):
        print(self.to_string())

    def add_vector(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def subtract_vector(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z

    def multiply_scalar(self, scalar: float):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def get_modulus(self) -> float:
        return round(math.sqrt(self.x**2 + self.y**2 + self.z**2), 2)

    def save_txt(self, filename: str):
        if ".txt" not in filename:
            filename += ".txt"
        with open(filename, "w") as f:
            f.write(self.to_string())

    def save_pickle(self, filename: str):
        if ".pkl" not in filename:
            filename += ".pkl"
        with open(filename, "wb") as f:
            pickle.dump(self, f)
