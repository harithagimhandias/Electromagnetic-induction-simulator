"""
Electromagnetic Induction Simulator
Topic: Lenz's Law

This file introduces the physical idea behind Lenz's law
"""
print("Lenz's law states that the induced current opposes the change that causes it")
print("This simulator helps visualize the process of induced current and undestand how lenz's law work")

# Simple Lenz's law demonstration

magnet_direction = input("Is the magnet oving towards or away from the coil?")

if magnet_direction == "towards":
  current_direction = "anti-clockwise"
elif magnet_direction == "away":
  current_direction = "clockwise"
else:
  current_direction = "unknown"

print("The induced current is:", current_direction)

