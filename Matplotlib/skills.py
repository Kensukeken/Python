import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk

# Get screen width and height
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Scale figure size dynamically (adjust ratio as needed)
fig_width = screen_width / 100
fig_height = screen_height / 100

# Enhanced skill categories with proficiency levels
expanded_skill_data = {
    "Category": [
        "Programming Languages", "Programming Languages", "Programming Languages", "Programming Languages", "Programming Languages",
        "Programming Languages", "Programming Languages", "Programming Languages", "Programming Languages", "Programming Languages",
        "Programming Languages", "Programming Languages", "Programming Languages",
        "Development Frameworks", "Development Frameworks", "Development Frameworks", "Development Frameworks",
        "Databases", "Databases",
        "Operating Systems", "Operating Systems", "Operating Systems",
        "Artistic Software & Design", "Artistic Software & Design", "Artistic Software & Design", "Artistic Software & Design", 
        "Artistic Software & Design", "Artistic Software & Design"
    ],
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
df_expanded = pd.DataFrame(expanded_skill_data)

# Pivot table for better visualization
pivot_df = df_expanded.pivot(index="Category", columns="Skill", values="Proficiency")

# Set up the figure for the heatmap
plt.figure(figsize=(fig_width, fig_height))
sns.heatmap(pivot_df, annot=True, cmap="Greens", linewidths=0.5, cbar=True)  # Changed to 'Greens'

# Add titles and labels
plt.title("Skills & Proficiency Levels", fontsize=16, fontweight="bold")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

# Show plot
plt.show()
