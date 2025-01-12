OpenAI compatibility
Together's API is compatible with OpenAI's libraries, making it easy to try out our open-source models on existing applications.

Suggest Edits
Together's API endpoints for chat, language and code, images, and embeddings are fully compatible with OpenAI's API.

If you have an application that uses one of OpenAI's client libraries, you can easily configure it to point to Together's API servers, and start running your existing applications using our open-source models.

Configuring OpenAI to use Together's API
To start using Together with OpenAI's client libraries, pass in your Together API key to the api_key option, and change the base_url to https://api.together.xyz/v1:

Python
TypeScript

import os
import openai

client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)
You can find your API key in your settings page. If you don't have an account, you can register for free.

Querying an Inference model
Now that your OpenAI client is configured to point to Together, you can start using one of our open-source models for your inference queries.

For example, you can query one of our chat models, like Llama 3.1 8B:

Python
TypeScript

import os
import openai

client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)

response = client.chat.completions.create(
  model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  messages=[
    {"role": "system", "content": "You are a travel agent. Be descriptive and helpful."},
    {"role": "user", "content": "Tell me the top 3 things to do in San Francisco"},
  ]
)

print(response.choices[0].message.content)
Or you can use a language model to generate a code completion:

Python
TypeScript

import os
import openai

client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)

response = client.completions.create(
  model="meta-llama/Llama-2-70b-hf",
  prompt="def bubbleSort(): ",
  max_tokens=175
)

print(response.choices[0].text)
Streaming with OpenAI
You can also use OpenAI's streaming capabilities to stream back your response:

Python
TypeScript

import os
import openai

system_content = "You are a travel agent. Be descriptive and helpful."
user_content = "Tell me about San Francisco"

client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)

stream = client.chat.completions.create(
  model="Qwen/Qwen2.5-7B-Instruct-Turbo",
  messages=[
    {"role": "system", "content": system_content},
    {"role": "user", "content": user_content},
  ],
  stream=True,
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="", flush=True)
Generating embeddings
Use our embedding models to generate an embedding for some text input:

Python
TypeScript

import os
import openai

client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)

response = client.embeddings.create(
  model = "togethercomputer/m2-bert-80M-8k-retrieval",
  input = "Our solar system orbits the Milky Way galaxy at about 515,000 mph"
)

print(response.data[0].embedding)
Community libraries
The Together API is also supported by most OpenAI libraries built by the community.

Feel free to reach out to support if you come across some unexpected behavior when using our API.