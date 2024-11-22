import matplotlib.pyplot as plt

# Data
delay_values = ['Delay = 1 second', 'Delay = 10 seconds']
successful_frames = [78, 226]
total_frames = [240, 240]

# Calculate success percentages
success_percentages = [successful / total * 100 for successful, total in zip(successful_frames, total_frames)]

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Bar chart
bar_width = 0.35
index = range(len(delay_values))

# Plot successful percentage
ax.bar(index, success_percentages, bar_width, color='b', label='Successful Frames (%)')

# Plot failed percentage (calculated as 100% - success percentage)
ax.bar(index, [100 - percent for percent in success_percentages], bar_width, bottom=success_percentages, color='r', label='Failed Frames (%)')

# Add labels, title, and customize axes
ax.set_xlabel('Delay Configuration')
ax.set_ylabel('Percentage (%)')
ax.set_title('Transmission Success vs Failure for SF=9 with Different Delays')
ax.set_xticks(index)
ax.set_xticklabels(delay_values)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()

# Output success ratios as text
for delay, success, total in zip(delay_values, successful_frames, total_frames):
    success_ratio = success / total * 100
    print(f"For {delay}: {success} out of {total} frames were successfully transmitted ({success_ratio:.2f}%)")
