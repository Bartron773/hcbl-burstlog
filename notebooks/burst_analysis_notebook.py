# burst_analysis_notebook.py
# Local Simulation Notebook for Bart’s Human Creative Burst Log (HCBL)

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# --------------------------
# Step 1: Simulated Burst History
# --------------------------
past_bursts = [
    {"timestamp": "2025-04-01T02:11:00Z", "distance": 0.33},
    {"timestamp": "2025-04-04T17:25:00Z", "distance": 0.28},
    {"timestamp": "2025-04-07T23:09:00Z", "distance": 0.38},
    {"timestamp": "2025-04-12T12:40:00Z", "distance": 0.36},
    {"timestamp": "2025-04-16T01:55:00Z", "distance": 0.31}
]

# --------------------------
# Step 2: New Burst Input
# --------------------------
new_burst_distance = 0.46  # Simulated value from today
k = 3

# Extract distances for analysis
distances = np.array([b["distance"] for b in past_bursts])
sorted = np.sort(distances)
k_closest = sorted[:k]
k_avg = np.mean(k_closest)
mean = np.mean(distances)
std = np.std(distances)
z_score = (new_burst_distance - mean) / std
relative_score = min(1, z_score / 3)

# --------------------------
# Step 3: Output and Insight
# --------------------------
print("📊 Novelty Analysis Result")
print("--------------------------")
print(f"Past Distances: {distances.tolist()}")
print(f"New Burst Distance: {new_burst_distance:.3f}")
print(f"Mean: {mean:.3f}, StdDev: {std:.3f}")
print(f"k={k} Avg Closest Distances: {k_avg:.3f}")
print(f"Z-Score: {z_score:.2f}")
print(f"Relative Novelty Score: {relative_score:.2f}")
print(f"Is Novel: {z_score > 1.5}")

# --------------------------
# Step 4: Visualization
# --------------------------
fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(distances, bins=8, color='#d0e1ff', edgecolor='black', label='Past Bursts')
ax.axvline(new_burst_distance, color='red', linestyle='--', label=f"New Burst ({new_burst_distance:.2f})")
ax.axvline(mean, color='green', linestyle=':', label=f"Mean ({mean:.2f})")
ax.set_title("HCBL Semantic Distance Novelty Distribution")
ax.set_xlabel("Cosine Distance from Previous Bursts")
ax.set_ylabel("Frequency")
ax.legend()
plt.tight_layout()
plt.show()
