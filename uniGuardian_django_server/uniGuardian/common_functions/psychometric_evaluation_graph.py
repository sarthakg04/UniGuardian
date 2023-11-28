import matplotlib.pyplot as plt
import json
from math import pi

# Sample JSON data - replace this with your actual data
data = '{"Learning": 8, "Decision Making": 6, "Emotion": 7, "Focus": 5, "Risk Tolerance": 9, "Generosity": 4}'

# Parsing JSON data
values = json.loads(data)

# Create a list of labels and values
labels = list(values.keys())
stats = list(values.values())

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
stats += stats[:1]
angles += angles[:1]

# Plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=7)
plt.ylim(0,10)

# Plot data
ax.plot(angles, stats, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, stats, 'b', alpha=0.1)

# Show the plot
plt.show()
