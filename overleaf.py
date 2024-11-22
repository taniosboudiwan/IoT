import matplotlib.pyplot as plt
import numpy as np

# Data
SF = [12, 12, 10, 10, 7, 7]
CR = [1, 4, 4, 1, 1, 4]
ToA_Experimental = [1484400, 1975652, 494584, 371672, 62616, 87196]
ToA_Theoretical = [1482750, 1974270, 493570, 370690, 56580, 78080]

# Combine SF and CR to create unique labels for each bar
labels = [f'SF={sf}, CR={cr}' for sf, cr in zip(SF, CR)]

# Set up the bar width and positions
x = np.arange(len(labels))
width = 0.35

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Bars for experimental and theoretical ToA
bars1 = ax.bar(x - width/2, ToA_Experimental, width, label='Experimental ToA', color='skyblue')
bars2 = ax.bar(x + width/2, ToA_Theoretical, width, label='Theoretical ToA', color='salmon')

# Labels and title
ax.set_xlabel("SF and CR Combinations")
ax.set_ylabel("Time on Air (ToA) in microseconds")
ax.set_title("Comparison of Experimental and Theoretical ToA Values")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()
