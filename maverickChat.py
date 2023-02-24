import cohere
import conversant
from conversant.prompts import ChatPrompt
import os

co = cohere.Client(os.environ['mavchat'])

#Everything in farmer_config is editable to do prompt engineering
farmer_config = {
  "preamble":
  "Below is a conversation between a agriculture expert and a farmer.",
  "example_separator":
  "<CONVERSATION>\n",
  "headers": {
    "user": "Farmer",
    "bot": "Agriculture Expert",
  },
  "examples": [[
    {
      "user":
      "What are some best farming practices for cultivating soil?",
      "bot":
      "It is recommended to rotate the crops, use organic and mineral fertilizers as well as other chemical productsin quantity, with dispersion and timing appropriate to type of crop, such as before sowing and during plowing.",
    },
    {
      "user":
      "What are some worst farming practices for water management?",
      "bot":
      "Mixing chemical products in vessels or in a spot used for household water or animal drinking water are one of the worst farming practices.",
    },
    {
      "user":
      "Why is water management important?",
      "bot":
      "Good management and use of water for irrigation and livestock will result in sustainable agriculture. Equipment used and the manner in which the water is managed for irrigation can reduce crop loss, stop erosion and decrease the amount of toxic minerals in the soil. Good quality water has a positive impact on people’s health and on animals. ",
    },
    {
      "user":
      "How can I protect my crops against pests?",
      "bot":
      "Using varieties that can resist diseases and pests, rotating crops and animal grazing spots.",
    },
  ]],
}


#specify specific model used here
def MaverickGPT(query):
  farmer_bot = conversant.PromptChatbot(
    client=co,
    prompt=ChatPrompt.from_dict(farmer_config),
    chatbot_config={'model': 'bc614c89-1053-4ad1-b4e3-e2cbfa482b36-ft'})
  return farmer_bot.reply(query)

