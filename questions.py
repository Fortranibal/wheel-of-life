# Define the questions and categories in a uniform data structure
questions_list = {
    "Work": [
        {"question": "I do everything necessary to advance in my job or company", "key": "Q1"},
        {"question": "I enjoy going to work", "key": "Q2"},
        {"question": "I am motivated to improve or enhance my skills at work", "key": "Q3"},
        {"question": "I have a long-term career plan", "key": "Q4"},
        {"question": "I am committed to achieving and fulfilling my goals", "key": "Q5"},
        {"question": "I do what makes me happy in my career", "key": "Q6"},
        {"question": "I am proud of the contributions I make in my professional life", "key": "Q7"},
        {"question": "Work covers my personal income needs", "key": "Q8"},
        {"question": "I am doing enough to protect my job or company", "key": "Q9"},
        {"question": "I have good relationships with the people I work with", "key": "Q10"},
    ],
    "Health": [
        {"question": "I am in good physical health", "key": "Q1"},
        {"question": "I am satisfied with the type and amount of rest I get in my life", "key": "Q2"},
        {"question": "I manage my emotions appropriately", "key": "Q3"},
        {"question": "I have a balanced diet", "key": "Q4"},
        {"question": "My clothes fit well, and I feel good in them", "key": "Q5"},
        {"question": "I consume at least two liters of water daily", "key": "Q6"},
        {"question": "I exercise regularly", "key": "Q7"},
        {"question": "Stress does not affect my daily activities", "key": "Q8"},
        {"question": "I get enough hours of sleep daily", "key": "Q9"},
        {"question": "I consume alcohol or tobacco in moderation", "key": "Q10"},
    ],
    "Physical Environment": [
        {"question": "There is enough light in my work area", "key": "Q1"},
        {"question": "I have windows that allow free circulation of air or air conditioning equipment that keeps my office with fresh or circulating air", "key": "Q2"},
        {"question": "I am happy with the location of my work and the transportation time I use", "key": "Q3"},
        {"question": "My work does not cause me extraordinary stress", "key": "Q4"},
        {"question": "My house is generally clean and tidy", "key": "Q5"},
        {"question": "The city where I live meets all my expectations of quality of life", "key": "Q6"},
        {"question": "I am happy in the neighborhood where I live", "key": "Q7"},
        {"question": "I acquire the physical things I like", "key": "Q8"},
        {"question": "Environmental pollution does not affect me, nor does it consume additional energy", "key": "Q9"},
        {"question": "The level of noise around my house or work does not bother me", "key": "Q10"},
    ],
    "Personal Development": [
        {"question": "I have clear skills, attributes, or areas that I want to develop in a year", "key": "Q1"},
        {"question": "I have a clear vision of where I am going in my life", "key": "Q2"},
        {"question": "I have an action plan to reach that vision", "key": "Q3"},
        {"question": "I have confidence in myself", "key": "Q4"},
        {"question": "My personal development is aligned with my passion, experience, and skills", "key": "Q5"},
        {"question": "What I have achieved in my career fills me with pride", "key": "Q6"},
        {"question": "I celebrate my successes as a recognition of my achievements", "key": "Q7"},
        {"question": "I use and adjust the lessons learned from my failures", "key": "Q8"},
        {"question": "I am motivated right now to improve my skills and competencies", "key": "Q9"},
        {"question": "My career is what I expected it to be", "key": "Q10"},
    ],
    "Significant Relationships": [
        {"question": "We communicate well among family members and listen to each other", "key": "Q1"},
        {"question": "In the family, we respect each other", "key": "Q2"},
        {"question": "I am happy with my social life", "key": "Q3"},
        {"question": "My family and friends know they can depend on me when they need me", "key": "Q4"},
        {"question": "I can express and show my feelings to the people I care about", "key": "Q5"},
        {"question": "I am very happy with my family life", "key": "Q6"},
        {"question": "We have a strong family sense with traditions and rituals", "key": "Q7"},
        {"question": "I have time to dedicate to the people I care about", "key": "Q8"},
        {"question": "My family and friends know they can depend on me when they need me", "key": "Q9"},
        {"question": "I quickly resolve conflicts with family or friends", "key": "Q10"},
    ],
    "Romance": [
        {"question": "I enjoy being with my partner", "key": "Q1"},
        {"question": "The relationship with my partner is interesting, fun, and stimulating", "key": "Q2"},
        {"question": "I bring out the best in my partner, making them feel good", "key": "Q3"},
        {"question": "I communicate openly and honestly with my partner", "key": "Q4"},
        {"question": "I care about and share the interests of my partner", "key": "Q5"},
        {"question": "I support my partner in times of difficulty", "key": "Q6"},
        {"question": "I am satisfied with the level of intimacy with my partner", "key": "Q7"},
        {"question": "I do everything possible to maintain passion in my romantic relationship", "key": "Q8"},
        {"question": "I have learned to forgive in my romantic relationship", "key": "Q9"},
        {"question": "I have complete confidence in my partner", "key": "Q10"},
    ],
    "Money": [
        {"question": "My lifestyle matches my income", "key": "Q1"},
        {"question": "I save at least 10% of my income", "key": "Q2"},
        {"question": "I budget monthly expenses for my home as well as personal expenses", "key": "Q3"},
        {"question": "I can pay at least 50% of the required amount as payment on my credit cards monthly", "key": "Q4"},
        {"question": "I have adequate health insurance", "key": "Q5"},
        {"question": "I do not live stressed about money matters", "key": "Q6"},
        {"question": "I have clear goals in my investments", "key": "Q7"},
        {"question": "I pay my expenses and debts on time", "key": "Q8"},
        {"question": "I know the total amount of all my assets", "key": "Q9"},
        {"question": "My partner and I communicate well about money matters", "key": "Q10"},
    ],
    "Fun and Recreation": [
        {"question": "I am satisfied with the type and amount of fun and recreation in my life", "key": "Q1"},
        {"question": "I go on vacation at least once a year", "key": "Q2"},
        {"question": "I have hobbies or hobbies that are not related to my work", "key": "Q3"},
        {"question": "I have recreational activities that I enjoy with my family", "key": "Q4"},
        {"question": "I have a fulfilling life outside of my work", "key": "Q5"},
        {"question": "I have fun and recreation on weekends", "key": "Q6"},
        {"question": "I belong to clubs or associations where there are spaces to have fun", "key": "Q7"},
        {"question": "We celebrate the birthdays of all family members", "key": "Q8"},
        {"question": "I have tried something new in the last 6 months", "key": "Q9"},
        {"question": "I am a happy person who enjoys life", "key": "Q10"},
    ],
}