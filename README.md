# MaverickAI

MaverickAI leverages advancements in AI to enable rural users to interact with powerful chatbots through SMS, eliminating the need for a 3G connection. By leveraging this technology, we aim to bridge the knowledge gap and empower rural communities.

Code is built upon cohere sandbox groundedQA (https://github.com/cohere-ai/sandbox-conversant-lib) and conversant(https://github.com/cohere-ai/sandbox-conversant-lib)

## Current features

Simulation of with SMS Service with Africa is talking:

Steps to take: 
1) Sign up for an africa's talking account (https://account.africastalking.com/auth/register/)
2) login (https://account.africastalking.com/auth/login/)
3) Go to the sandbox: https://developers.africastalking.com/simulator) 
4) Key in any valid phone number
5) Send a text to MaverickQA by texting 5959 (for factually grounded Questions and Answers) and MaverickChat by texting 59009 (for a chat experience)


##Web UI demo for ease of access:
https://replit.com/@Incarceron/MaverickAI-demo?v=1

## Coming soon!

- Enabling responses to calls with voice to text using whisper 
- Buiding our own web crawling to replace serpapi
- Building our own large language models (using huggingface models) for translation instead of using RapidAPI (MyMemory, TranslateAPI Plus)
