import json
from questions import questions_list

def collect_user_responses(retake_test=False):
    user_responses = {}

    # Load existing user responses if the file exists
    try:
        with open("user_responses.json", "r") as json_file:
            user_responses = json.load(json_file)
    except FileNotFoundError:
        user_responses = {}

    # Check if the user wants to retake the test
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
        with open("user_responses.json", "w") as json_file:
            json.dump(user_responses, json_file, indent=2)

    return user_responses
