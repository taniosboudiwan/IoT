import matplotlib.pyplot as plt

# Data for ToA and Taille
taille = [33, 48, 60, 77]  # Packet sizes in bytes
toa = [1070360, 1316320, 1562272, 1808264]  # ToA in microseconds

# Convert ToA from microseconds to milliseconds
toa_ms = [t / 1000 for t in toa]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(taille, toa_ms, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# Add titles and labels
plt.title("Time on Air (ToA) as a Function of Packet Size (Taille)", fontsize=16)
plt.xlabel("Packet Size (bytes)", fontsize=14)
plt.ylabel("Time on Air (ToA) (milliseconds)", fontsize=14)

# Add grid for better readability
plt.grid(True)

# Show the plot
plt.show()
