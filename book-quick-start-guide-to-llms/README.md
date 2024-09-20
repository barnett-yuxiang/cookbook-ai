## Quick Start Guide to Large Language Models: Strategies and Best Practices for Using ChatGPT and Other LLMs

by Sinan Ozdemir

https://github.com/sinanuozdemir/quick-start-guide-to-llms

### I: Introduction to Large Language Models

Mechanisms such as attention, transfer learning, and scaling up neural networks, which provide the scaffolding for Transformers, were seeing breakthroughs right around the same time.

The original Transformer architecture, as devised in 2017, was a **sequence-to-sequence model**, which means it had two main components:
- An encoder, which is tasked with taking in raw text, splitting it up into its core components (more on this later), converting those components into vectors (similar to the Word2vec process), and using attention to understand the context of the text
- A decoder, which excels at generating text by using a modified type of attention to predict the next best token

[]

The original Transformer has two main components: an encoder, which is great at understanding text, and a decoder, which is great at generating text. Putting them together makes the entire model a “sequence-to-sequence” model.

How an LLM is **pre-trained** and **fine-tuned** makes all the difference between an okay-performing model and a state-of-the-art, highly accurate LLM. 

##### Pre-training
Every LLM is trained on different corpora and on different tasks.

BERT was originally pre-trained on English Wikipedia and the BookCorpus. More modern LLMs are trained on datasets thousands of times larger.

Some LLMs are trained on proprietary data sources, including OpenAI’s GPT family of models, to give their parent companies an edge over their competitors.

##### Transfer Learning
Transfer learning is a technique used in machine learning to leverage the knowledge gained from one task to improve performance on another related task. 

##### Fine-Tuning

![](./assets/Figure-1_9.png)

##### Attention

Attention is a mechanism used in deep learning models (not just Transformers) that assigns different weights to different parts of the input, allowing the model to prioritize and emphasize the most important information while performing tasks like translation or summarization. 

Modern LLMs that rely on attention can dynamically focus on different parts of input sequences, allowing them to weigh the importance of each part in making predictions.

##### Embeddings

Embeddings are the mathematical representations of words, phrases, or tokens in a large-dimensional space.

LLMs learn different embeddings for tokens based on their pre-training and can further update these embeddings during fine-tuning.

##### Tokenization

breaking text down into the smallest unit of understanding—tokens. 

#### Beyond Language Modeling: Alignment + RLHF

#### Popular Modern LLMs

BERT: is an autoencoding model that uses attention to build a bidirectional representation of a sentence.

GPT-3 and ChatGPT: contrast to BERT, is an autoregressive model that uses attention to predict the next token in a sequence based on the previous tokens.

T5: is a pure encoder/decoder Transformer model that was designed to perform several NLP tasks, from text classification to text summarization and generation, right off the shelf. 

#### Classical NLP Tasks

1. Text Classification
2. Translation Tasks
3. SQL Generation
4. Free-Text Generation

>I will not often use the term “generative AI,” as the word “generative” has its own meaning in machine learning as the analogous way of learning to a “discriminative” model. 

#### Semantic Search with LLMs

OpenAI’s Embedding Engines

Open-Source Embedding Alternatives: sentence_transformer package

Document Chunking

Vector Databases

#### First Steps with Prompt Engineering

Prompt Engineering

Alignment in Language Models

Few-Shot Learning

Output Structuring

Prompting Personas

Working with Prompts Across Models

### II: Getting the Most Out of LLMs

#### Optimizing LLMs with Customized Fine-Tuning



