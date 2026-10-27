
# Student Feedback Sentiment Scoring

positive_words = [
    "good", "excellent", "helpful", "clear", "interesting",
    "best", "easy", "great"
]

negative_words = [
    "bad", "poor", "boring", "difficult", "worst",
    "unclear", "slow", "confusing"
]

feedback_list = [
    "The teacher is good and helpful",
    "The explanation is poor and confusing",
    "The class is excellent and interesting",
    "The subject is difficult",
    "The teaching is clear but slow"
]

# Process each feedback
for feedback in feedback_list:
    words = feedback.lower().split()

    positive_count = 0
    negative_count = 0

    for word in words:
        word = word.strip(".,!?")
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    score = positive_count - negative_count

    if score >= 2:
        sentiment = "Positive"
    elif score <= -1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("\nFeedback:", feedback)
    print("Positive indicators:", positive_count)
    print("Negative indicators:", negative_count)
    print("Sentiment score:", score)
    print("Classification:", sentiment)
