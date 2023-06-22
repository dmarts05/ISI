from Vector3D import Vector3D

v = Vector3D(0, 0, 0)
v.print_vector()

v.change_coordinates(-6, 10, 5)
v.print_vector()

add_v = Vector3D(5, -1, 0)
v.add_vector(add_v)
v.print_vector()

sub_v = Vector3D(-1, -1, -9)
v.subtract_vector(sub_v)
v.print_vector()

v.multiply_scalar(3.5)
v.print_vector()

print(f"Modulus {v.get_modulus()}")

v.save_txt("vector")
v.save_pickle("vector")
