import matplotlib.pyplot as plt

# Ordered skill data (matching your request)
skills = ["LaTeX", "C++", "Python", "Julia", "Java", "C#", "HTML", "CSS", "PHP", "JavaScript", "Lua", "Ruby", "Go"]
proficiency = [5, 2, 5, 4, 4, 1, 5, 5, 4, 3, 2, 1, 1]  # Matching order

# Define colors using a green gradient
colors = plt.cm.Greens_r([i / max(proficiency) for i in proficiency])

# Set figure size
fig, ax = plt.subplots(figsize=(10, 10))

# Create a Donut Chart
wedges, texts, autotexts = ax.pie(
    proficiency,
    labels=skills,
    autopct=lambda p: f'{int(round(p * sum(proficiency) / 100))}',  # Auto-adjusted numbers
    startangle=140,
    colors=colors,
    pctdistance=0.85,  # Keeps numbers inside without overlap
    wedgeprops={'edgecolor': 'black'}
)

# Create the donut hole in the center
center_circle = plt.Circle((0, 0), 0.65, fc='white')
ax.add_artist(center_circle)

# Improve text readability
for text in texts:
    text.set_fontsize(10)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('black')
    autotext.set_fontweight('bold')  # Make proficiency numbers stand out

# Add a bold and centered title
plt.title("Ordered Skill Proficiency Distribution", fontsize=18, fontweight="bold", pad=20)

# Adjust layout for better spacing
plt.tight_layout()

# Show chart
plt.show()
