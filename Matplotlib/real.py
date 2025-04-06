import matplotlib.pyplot as plt
import numpy as np

COLORS = {
    'Programming': '#4e79a7',
    'Frameworks': '#f28e2b',
    'Databases': '#e15759',
    'Systems': '#76b7b2',
    'Design': '#59a14f',
    'Tools': '#8c6d31',
    'text': '#2e2e2e',
    'background': '#f8f9fa'
}

SKILLS = {
    "Programming": {
        "Python": 5,
        "LaTeX": 5,
        "C++": 2,
        "Java": 4,
        "Julia": 4,
        "JavaScript": 3,
        "HTML/CSS": 5,
        "PHP": 4,
        "C#": 1
    },
    "Frameworks": {
        "React": 4,
        "Node.js": 4,
        "Spring Boot": 3,
        "Express": 3
    },
    "Databases": {
        "MySQL": 4,
        "MongoDB": 3
    },
    "Systems": {
        "Windows": 5,
        "macOS": 4,
        "Linux": 2
    },
    "Design": {
        "Photoshop": 5,
        "Illustrator": 5,
        "Procreate": 5,
        "InDesign": 4,
        "UI/UX": 5
    },
    "Tools": {
        "VSCode": 5,
        "IntelliJ": 4,
        "Git": 4,
        "Vim": 2,
        "Notepad++": 4,
        "FileZilla": 4
    }
}

def create_skills_chart():
    plt.figure(figsize=(10, 9), facecolor=COLORS['background'])
    ax = plt.gca()
    ax.set_facecolor(COLORS['background'])
    
    y_pos = 0
    bar_height = 0.8
    category_spacing = 1.5
    
    max_category_length = max(len(category) for category in SKILLS.keys())
    
    for category_idx, (category, items) in enumerate(SKILLS.items()):
        plt.text(-1.2 - (max_category_length * 0.05), y_pos + len(items)/2 - 0.5, category,
                ha='right', va='center', fontsize=11,
                fontweight='bold', color=COLORS[category])
        
        for skill, level in items.items():
            plt.barh(y_pos, level, height=bar_height,
                    color=COLORS[category], alpha=0.7,
                    edgecolor='white', linewidth=0.5)
            
            plt.text(-0.5, y_pos, skill, ha='right', va='center',
                    fontsize=10, color=COLORS['text'])
            
            for i in range(1, 6):
                plt.plot(i, y_pos, 'o', markersize=8,
                        color=COLORS[category] if i <= level else '#e0e0e0',
                        markeredgecolor='white')
            
            y_pos += 1
        
        y_pos += category_spacing
    
    plt.xlim(0, 6)
    plt.ylim(-1, y_pos - category_spacing + 1)
    plt.xticks(range(1, 6), ['Basic', 'Intermediate', 'Advanced', 'Expert', 'Master'])
    plt.yticks([])
    
    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
    ax.spines['bottom'].set_color('#dddddd')
    
    plt.title("Technical Skills & Tools Proficiency", pad=20,
              fontsize=12, fontweight='bold',
              color=COLORS['text'])
    
    plt.tight_layout(pad=2.0)
    
    try:
        plt.savefig('my_skills.png', dpi=120, bbox_inches='tight', facecolor=COLORS['background'])
        print("Successfully saved to 'my_skills.png'")
    except Exception as e:
        print(f"Error saving: {e}")
    
    try:
        plt.show()
    except:
        pass

if __name__ == "__main__":
    create_skills_chart()