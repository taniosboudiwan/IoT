import matplotlib.pyplot as plt
import numpy as np

# Data
SF = [12, 12, 10, 10, 7, 7]
CR = [1, 4, 4, 1, 1, 4]
ToA_Experimental = [1484400, 1975652, 494584, 371672, 62616, 87196]
ToA_Theoretical = [1482750, 1974270, 493570, 370690, 56580, 78080]

# Set up the SF and CR mappings
sf_mapping = {7: 0, 10: 1, 12: 2}
cr_mapping = {1: 0, 4: 1}

# Create matrices for the heatmaps
data_exp = np.zeros((3, 2))  # 3 SF values (7, 10, 12) and 2 CR values (1, 4)
data_theo = np.zeros((3, 2))

# Fill in the data matrices
for i in range(len(SF)):
    row = sf_mapping[SF[i]]
    col = cr_mapping[CR[i]]
    data_exp[row, col] = ToA_Experimental[i]
    data_theo[row, col] = ToA_Theoretical[i]

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Function to create a heatmap using matplotlib only
def heatmap(data, ax, title, cmap):
    cax = ax.imshow(data, cmap=cmap, aspect='auto')
    ax.set_xticks([0, 1])
    ax.set_xticklabels([1, 4])  # CR values
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels([7, 10, 12])  # SF values
    ax.set_title(title)
    ax.set_xlabel("Coding Rate (CR)")
    ax.set_ylabel("Spreading Factor (SF)")

    # Add color bar
    fig.colorbar(cax, ax=ax, orientation='vertical', label="ToA (μs)")

    # Add text annotations for each cell
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, f"{int(data[i, j])}", ha='center', va='center', color="black")

# Experimental ToA heatmap
heatmap(data_exp, ax1, "Experimental ToA", cmap="YlGnBu")

# Theoretical ToA heatmap
heatmap(data_theo, ax2, "Theoretical ToA", cmap="YlOrRd")

plt.suptitle("Heatmap of Experimental and Theoretical ToA Values by SF and CR")
plt.tight_layout()
plt.show()
