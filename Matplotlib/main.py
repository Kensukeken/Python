import pandas as pd
import matplotlib.pyplot as plt

# Skill data with proficiency levels
skill_data = {
    "Skill": [
        "LaTeX", "C++", "Python", "Julia", "Java", "C#", "HTML", "CSS", "PHP", "JavaScript", "Lua", "Ruby", "Go",
        "Spring Boot", "React", "Node.js", "Express",
        "MySQL", "MongoDB",
        "Windows", "macOS", "Linux",
        "Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Procreate",
        "Design Principles (HCI)", "Traditional & Digital Art"
    ],
    "Proficiency": [
        4, 4, 4, 3, 4, 3, 5, 5, 3, 4, 3, 2, 2,  # Programming Languages
        3, 4, 4, 3,  # Development Frameworks
        4, 3,  # Databases
        5, 5, 4,  # Operating Systems
        5, 5, 4, 5,  # Artistic Software & Design
        5, 5  # Traditional & Digital Art
    ]  # Scale: 1 (Basic) - 5 (Advanced)
}

# Convert to DataFrame
df_skills = pd.DataFrame(skill_data)

# Sort by proficiency for better visualization
df_skills = df_skills.sort_values(by="Proficiency", ascending=False)

# Define colors using a green gradient
colors = plt.cm.Greens_r(df_skills["Proficiency"] / df_skills["Proficiency"].max())

# Set figure size
fig, ax = plt.subplots(figsize=(10, 10))

# Create a Donut Chart
wedges, texts, autotexts = ax.pie(
    df_skills["Proficiency"],
    labels=df_skills["Skill"],
    autopct=lambda p: f'{int(round(p * sum(df_skills["Proficiency"]) / 100))}',  # Auto-adjusted numbers
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
    text.set_fontsize(9)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')
    autotext.set_fontweight('bold')  # Make proficiency numbers stand out

# Add a bold and centered title
plt.title("Skill Proficiency Distribution", fontsize=18, fontweight="bold", pad=20)

# Adjust layout for better spacing
plt.tight_layout()

# Show chart
plt.show()
