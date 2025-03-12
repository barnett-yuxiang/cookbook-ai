from openai import OpenAI

client = OpenAI()

# 1. Generate text from a model
# response = client.responses.create(
#     model="gpt-4o", input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)

# 2. Analyze the content of an image
# response = client.responses.create(
#     model="gpt-4o",
#     input=[
#         {"role": "user", "content": "what teams are playing in this image?"},
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_image",
#                     "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg",
#                 }
#             ],
#         },
#     ],
# )

# print(response.output_text)

# 3. Get information for the response from the Internet
# response = client.responses.create(
#     model="gpt-4o",
#     tools=[{"type": "web_search_preview"}],
#     input="What was a positive news story from today?",
# )

# print(response.output_text)

# 4. Using either the new Realtime API or server-sent streaming events,
# you can build high performance, low-latency experiences for your users.

# 5. Build agents
from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
)


async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
