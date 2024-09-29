def fill_in_the_blanks():
    print("Fill in the blanks with the correct idioms from the list:")
    idioms = [
        "strike a balance",
        "(not) think twice",
        "at short notice",
        "wait and see",
        "take (something) at face value",
        "the best of both worlds",
        "in the public eye",
        "get a grip (on yourself)",
        "off the record",
        "up to speed",
        "rule of thumb",
        "in hot water"
    ]
    
    # Questions and corresponding correct answers
    questions = [
        ("When making decisions, it's important to __________ between work and personal life to avoid burnout.", "strike a balance"),
        ("He tends to __________ before making major life decisions, which often frustrates his friends.", "(not) think twice"),
        ("She was called for an interview __________, so she didn’t have much time to prepare.", "at short notice"),
        ("We'll have to __________ and see if the new policy will actually work.", "wait and see"),
        ("I wouldn't __________ what she said; she might not know all the details.", "take (something) at face value"),
        ("He loves his job because he gets __________, being able to work from home while earning a good salary.", "the best of both worlds"),
        ("The CEO is constantly __________ due to her high-profile status.", "in the public eye"),
        ("If you feel overwhelmed, just __________ and take a deep breath.", "get a grip (on yourself)"),
        ("I was given this information __________, so I can’t share it with anyone else.", "off the record"),
        ("It took me a while to get __________ after returning from vacation, but now I’m fully caught up.", "up to speed"),
        ("As a __________, always double-check the facts before making a decision.", "rule of thumb"),
        ("After missing the deadline, he found himself __________ with his boss.", "in hot water")
    ]
    
    score = 0
    
    # Ask each question
    for i, (question, correct_answer) in enumerate(questions):
        print(f"{i + 1}. {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        # Check if the user's answer matches the correct answer
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: '{correct_answer}'.\n")
    
    # Show the final score
    print(f"Your final score is {score}/{len(questions)} correct!")

# Run the fill-in-the-blanks quiz
fill_in_the_blanks()

