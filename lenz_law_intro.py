"""
Electromagnetic Induction Simulator
Topic: Lenz's Law

This file introduces the physical idea behind Lenz's law
"""
print("Lenz's law states that the induced current opposes the change that causes it")
print("This simulator helps visualize the process of induced current and undestand how lenz's law work")

# Simple Lenz's law demonstration

print("Assume that the coil is viewed from the side where the magnet enters.")
magnet_direction = input("Is the magnet oving towards or away from the coil?").lower()
print("According to Lenz's law, the induced current always opposes the change in magnetic flux linkage of the coil")

if magnet_direction == "towards":
  current_direction = "anti-clockwise"
  arrow = "⟲"
elif magnet_direction == "away":
  current_direction = "clockwise"
  arrow = "⟳"
else:
  current_direction = "unknown"

print("So the induced current is:", current_direction, arrow)

