# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

from plot_functions import plot_radial_bar_chart
from questions import questions_list

import json

# Define the path to the JSON file
json_file_path = "user_responses.json"

# Load existing user responses if the file exists
try:
    with open(json_file_path, "r") as json_file:
        user_responses = json.load(json_file)
except FileNotFoundError:
    user_responses = {}

# Check if the user wants to retake the test
retake_test = input("Do you want to retake the test? (yes/no): ").lower() == "yes"

# If the user wants to retake the test, clear existing responses
if retake_test:
    user_responses = {}

# Display existing user responses
print("Existing User Responses:")
print(user_responses)


# Collect user responses to each question
if retake_test:
    for category, questions in questions_list.items():
        print(f"\n*** {category} ***")
        user_responses[category] = {}
        for question_dict in questions:
            question_text = question_dict["question"]
            question_key = question_dict["key"]

            # Get valid user response
            while True:
                try:
                    response = int(input(f"{question_text} (1-10): "))
                    if 1 <= response <= 10:
                        break
                    else:
                        print("Please enter a number between 1 and 10.")
                except ValueError:
                    print("Please enter a valid numeric value.")

            user_responses[category][question_key] = response

# Save the updated user responses to the JSON file
with open(json_file_path, "w") as json_file:
    json.dump(user_responses, json_file, indent=2)


# Calculate average scores for each category
average_scores = {}
for category, responses in user_responses.items():
    average_scores[category] = sum(responses.values()) / len(responses)

# Call the function to plot the radial bar chart
plot_radial_bar_chart(list(average_scores.keys()), average_scores)