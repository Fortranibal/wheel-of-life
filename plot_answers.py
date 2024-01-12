import json                         # for reading JSON file      
import matplotlib.pyplot as plt     # for plotting
import numpy as np                  # for math
import seaborn as sns               # dark theme

def plot_general_results(json_file_path):
    # Load user responses from the JSON file
    try:
        with open(json_file_path, "r") as json_file:
            user_responses = json.load(json_file)
    except FileNotFoundError:
        print("No user responses found.")
        return

    # Calculate average scores for each category
    categories = list(user_responses.keys())
    scores = [sum(category.values()) / len(category) for category in user_responses.values()]

    # Plot the bar graph with customized x-axis labels
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, scores, color='#86bf91', width=0.4)

    plt.title('Wheel of Life - General Results')
    plt.xlabel('Categories')
    plt.ylabel('Average Score')
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Customize x-axis labels
    plt.xticks(rotation=45, ha='right', color='black')

    # Display the bar values on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

    plt.show()

def plot_all_answers(json_file_path):
    # Load user responses from the JSON file
    try:
        with open(json_file_path, "r") as json_file:
            user_responses = json.load(json_file)
    except FileNotFoundError:
        print("No user responses found.")
        return

    # Plotting the user responses
    num_categories = len(user_responses)
    num_rows = (num_categories - 1) // 3 + 1
    num_cols = min(num_categories, 3)

    plt.figure(figsize=(15, 8))
    for i, (category, responses) in enumerate(user_responses.items(), start=1):
        plt.subplot(num_rows, num_cols, i)
        plt.bar(responses.keys(), responses.values(), color='#86bf91', width=0.4)
        plt.title(f'{category} - Individual Answers')
        plt.xlabel('Questions')
        plt.ylabel('Score')
        plt.ylim(0, 10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

# Example usage
# json_file_path = "user_responses.json"
# plot_general_results(json_file_path)
# plot_all_answers(json_file_path)





import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_radial_bar_chart(categories, scores):
    # Set seaborn dark style explicitly
    sns.set(style="darkgrid", rc={"axes.facecolor": "#282828", "grid.color": "#656565", 'text.color': 'white'})

    # Plot a radial bar chart with the DataFrame
    fig = plt.figure(figsize=(12, 12))
    fig.patch.set_facecolor('#282828')  # Set background color

    ax = plt.subplot(111, polar=True)
    plt.axis()

    # Set min and max value
    lower_limit = 0

    # Set heights and width
    heights = [scores[category] for category in categories]
    width = 2 * np.pi / len(categories)

    # Set index and angle
    indexes = list(range(1, len(categories) + 1))
    angles = [element * width for element in indexes]

    # Plot the radial bar chart
    bars = ax.bar(x=angles, height=heights, width=width, bottom=lower_limit,
                  linewidth=1, edgecolor="white", color=plt.cm.viridis(np.linspace(0, 1, len(categories))))

    label_padding = 2.7

    # Add labels to the chart with horizontal alignment
    for bar, angle, height, label in zip(bars, angles, heights, categories):
        rotation = 0  # Horizontal alignment
        alignment = "center"

        ax.text(x=angle, y=lower_limit + bar.get_height() + label_padding,
                s=f"{label}: {height:.1f}", ha=alignment, va='center', rotation=rotation,
                rotation_mode="anchor", color='white')

        ax.set_thetagrids([], labels=[])

    # Separate title and make it bigger
    plt.suptitle("Wheel of Life - Radial Bar Chart", fontsize=20, y=0.95, color='white')

    # Show the radial bar chart
    plt.show()

# Example usage
categories = ['Work', 'Health', 'Relationships', 'Personal Development', 'Finance', 'Leisure']
scores = {'Work': 7.5, 'Health': 8.2, 'Relationships': 6.8, 'Personal Development': 9.0, 'Finance': 7.2, 'Leisure': 8.5}

plot_radial_bar_chart(categories, scores)
