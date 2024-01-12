from plot_functions import plot_radial_bar_chart
from user_responses import collect_user_responses

# Check if the user wants to retake the test
retake_test = input("Do you want to retake the test? (yes/no): ").lower() == "yes"
user_responses = collect_user_responses(retake_test)

# Calculate average scores for each category
average_scores = {}
for category, responses in user_responses.items():
    average_scores[category] = sum(responses.values()) / len(responses)

# Call the function to plot the radial bar chart
plot_radial_bar_chart(list(average_scores.keys()), average_scores)