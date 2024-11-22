import matplotlib.pyplot as plt

# Data
payload_sizes = [33, 48, 60, 77]  # Payload sizes in bytes
toa_values = [1070360, 1316320, 1562272, 1808264]  # ToA in microseconds

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(payload_sizes, toa_values, marker='o', color='b', linestyle='-')
plt.title("Relationship between Payload Size and Time on Air (ToA)")
plt.xlabel("Payload Size (bytes)")
plt.ylabel("Time on Air (ToA) in microseconds")

# Adding constant parameters as text
constant_params = "SF = 11\nBandwidth = 125000 Hz\nCoding Rate = 1"
plt.text(60, 1500000, constant_params, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

# Display the plot
plt.grid(True)
plt.show()
