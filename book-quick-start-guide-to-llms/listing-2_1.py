# Importing the necessary modules for the script to run
import openai
import os


def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.embeddings.create(input=text, model=model)
    return response["data"][0]["embedding"]


# Setting the OpenAI API key using the value stored in the environment variable "OPENAI_API_KEY"
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Setting the model to be used for text embedding
MODEL = "text-embedding-ada-002"

# Generating the vector representation of the given text using the specified model
embedded_text = get_embedding("I love to be vectorized", model=MODEL)

# Checking the length of the resulting vector to ensure it is the expected size (1536)
print(len(embedded_text))  # Output the actual length of the embedding vector
