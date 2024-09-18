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

#### Pre-training
Every LLM is trained on different corpora and on different tasks.

BERT was originally pre-trained on English Wikipedia and the BookCorpus. More modern LLMs are trained on datasets thousands of times larger.

Some LLMs are trained on proprietary data sources, including OpenAI’s GPT family of models, to give their parent companies an edge over their competitors.

#### Transfer Learning
Transfer learning is a technique used in machine learning to leverage the knowledge gained from one task to improve performance on another related task. 

#### Fine-Tuning

![](./assets/Figure-1_9.png)



