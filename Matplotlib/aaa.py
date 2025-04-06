import matplotlib.pyplot as plt

# Specified skill data (skills in the exact order you requested)
skills = ["LaTeX", "C++", "Python", "Julia", "Java", "C#", "HTML", "CSS", "PHP", "JavaScript", "Lua", "Ruby", "Go"]
proficiency = [5, 2, 5, 4, 4, 1, 5, 5, 4, 3, 2, 1, 1]  # Proficiency levels

# Sort the proficiency and skills together by proficiency (to ensure correct order in the chart)
skills_ordered = [x for _, x in sorted(zip(proficiency, skills))]
proficiency_ordered = sorted(proficiency)

# Define colors using a green gradient
colors = plt.cm.Greens_r([i / max(proficiency_ordered) for i in proficiency_ordered])

# Set figure size
fig, ax = plt.subplots(figsize=(10, 10))

# Create a Donut Chart
wedges, texts, autotexts = ax.pie(
    proficiency_ordered,
    labels=skills_ordered,
    autopct=lambda p: f'{int(round(p * sum(proficiency_ordered) / 100))}',  # Auto-adjusted numbers
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
