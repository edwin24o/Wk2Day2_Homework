#Task 1
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(python_reviews, keywords):
    for review in python_reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)

highlight_keywords(python_reviews, keywords)

# Task2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def review_counter(python_reviews, positive_words, negative_words):
    for review in python_reviews:
        positive_count = sum(word in review.lower() for word in positive_words)
        negative_count = sum(word in review.lower() for word in negative_words)
        print(f"Positive: {positive_count}, Negative: {negative_count}")

review_counter(python_reviews, positive_words, negative_words)

#Task 3

def summarize_review(review, length=30):
    if len(review) <= length:
        return review
    truncated = review[:length].rsplit(' ', 1)[0]
    return truncated + "…"

for review in python_reviews:
    print(summarize_review(review))