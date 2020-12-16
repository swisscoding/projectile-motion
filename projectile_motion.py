#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
import math

# decoration
print(stylize("\n---- | Calculate projectile motion (max. height & range) | ----\n", fg("red")))

# user interaction
initial_speed = float(input("Enter initial speed of the projectile (in m/s): "))
throw_angle = float(input("Enter throw angle of the projectile (in degrees): "))

print("\nIt is assumed that the initial height is 0.")

# variables
# g is standard acceleration of gravity
g = 9.81
horizontal_velocity = initial_speed * round(math.cos(throw_angle))
vertical_velocity = initial_speed * round(math.sin(throw_angle))

# function / main program
def p_motion(h_velocity, v_velocity):
    # variables
    time_of_flight = 2 * v_velocity / g
    maximum_range = (2 * h_velocity * v_velocity / g) / 2
    maximum_height = (v_velocity**2 / (2 * g)) / 2

    return round(maximum_range), round(maximum_height), round(time_of_flight, 2)

output = p_motion(horizontal_velocity, vertical_velocity)
max_h = stylize(output[1], fg("red"))
max_r = stylize(output[0], fg("red"))
time = stylize(output[2], fg("red"))

print(f"\nThe maximum height that the projectile reached: {max_h} m")
print(f"The distance that the projectile reached: {max_r} m")
print(f"The flight time of the projectile was: {time} s\n")
