# Task 1: Keyword Highlighter

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "avergae"]

def capitalize_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    return review

def main():
    for review in reviews:
        print(capitalize_keywords(review, keywords))

if __name__ == "__main__":
    main()

# Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_sentiments(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()
        for word in words:
            cleaned_word = word.strip(".,!?")
            if cleaned_word in positive_words:
                positive_count += 1
            elif cleaned_word in negative_words:
                negative_count += 1
    return positive_count, negative_count

def main():
    positive_count, negative_count = tally_sentiments(reviews, positive_words, negative_words)
    print(f"Total positive words: {positive_count}")
    print(f"Total negative words:{negative_count}")

if __name__ == "__main__":
    main()

# Task 3: Review Summary
def create_summary(review, max_length=30):
    if len(review) <= max_length:
        return review
    else:
        truncated_review = review[:max_length]
        last_space_index = truncated_review.rfind(" ")
        if last_space_index == -1:
            return truncated_review + "..."
        else:
            return truncated_review[:last_space_index] + "..."
def main():
    for review in reviews:
        summary = create_summary(review)
        print(summary)

if __name__ == "__main__":
    main()
    