import math

# Function to calculate the volume of a cube
def cube_volume(side):
    return side ** 3

# Function to calculate the surface area of a cube
def cube_surface_area(side):
    return 6 * side ** 2

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# Function to calculate the surface area of a sphere
def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

# Function to calculate the surface area of a cylinder
def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Function to calculate the volume of a cone
def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

# Function to calculate the surface area of a cone
def cone_surface_area(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

# Example usage:
cube_side = 5
sphere_radius = 3
cylinder_radius = 4
cylinder_height = 7
cone_radius = 6
cone_height = 9

print("Cube:")
print("Volume:", cube_volume(cube_side))
print("Surface Area:", cube_surface_area(cube_side))

print("\nSphere:")
print("Volume:", sphere_volume(sphere_radius))
print("Surface Area:", sphere_surface_area(sphere_radius))

print("\nCylinder:")
print("Volume:", cylinder_volume(cylinder_radius, cylinder_height))
print("Surface Area:", cylinder_surface_area(cylinder_radius, cylinder_height))

print("\nCone:")
print("Volume:", cone_volume(cone_radius, cone_height))
print("Surface Area:", cone_surface_area(cone_radius, cone_height))
