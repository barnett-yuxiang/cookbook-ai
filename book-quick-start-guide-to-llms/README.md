## Quick Start Guide to Large Language Models: Strategies and Best Practices for Using ChatGPT and Other LLMs

by Sinan Ozdemir

https://github.com/sinanuozdemir/quick-start-guide-to-llms

### I: Introduction to Large Language Models

Mechanisms such as attention, transfer learning, and scaling up neural networks, which provide the scaffolding for Transformers, were seeing breakthroughs right around the same time.

The original Transformer architecture, as devised in 2017, was a **sequence-to-sequence model**, which means it had two main components:
- An encoder, which is tasked with taking in raw text, splitting it up into its core components (more on this later), converting those components into vectors (similar to the Word2vec process), and using attention to understand the context of the text
- A decoder, which excels at generating text by using a modified type of attention to predict the next best token



The original Transformer has two main components: an encoder, which is great at understanding text, and a decoder, which is great at generating text. Putting them together makes the entire model a “sequence-to-sequence” model.

