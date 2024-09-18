from transformers import pipeline


def classify_text(email):
    """
    Use Facebook's BART model to classify an email into "spam" or "not spam"

    Args:
        email (str): The email to classify
    Returns:
        str: The classification of the email
    """
    # COPILOT START. EVERYTHING BEFORE THIS COMMENT WAS INPUT TO COPILOT
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["spam", "not spam"]
    hypothesis_template = "This email is {}."
    results = classifier(email, labels, hypothesis_template=hypothesis_template)

    return results["labels"][0]
    # COPILOT END

print(classify_text("hi I am spam")) # spam
