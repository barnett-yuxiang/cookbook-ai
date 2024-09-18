# Importing the SentenceTransformer library
from sentence_transformers import SentenceTransformer

# Initializing a SentenceTransformer model with the 'multi-qa-mpnet-base-cos-v1' pre-trained model
model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-cos-v1")

# Defining a list of documents to generate embeddings for
docs = [
    "Around 9 million people live in London",
    "London is known for its financial district",
]

# Generate vector embeddings for the documents
doc_emb = model.encode(
    docs,  # Our documents (an iterable of strings)
    batch_size=32,  # Batch the embeddings by this size
    show_progress_bar=True,  # Display a progress bar
)

# The shape of the embeddings is (2, 768), indicating a length of 768 and two embeddings generated
doc_emb.shape  #  == (2, 768)
