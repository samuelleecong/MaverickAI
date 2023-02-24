from qa.bot import GroundedQaBot
import requests
import json
import os

cohere_api_key = os.environ['mavqa']
serp_api_key = os.environ['serp']
rapidapi_key = os.environ['rapid']

bot = GroundedQaBot(cohere_api_key, serp_api_key)


def get_language(payload, api_key):
  url = "https://translate-plus.p.rapidapi.com/language_detect"

  payload = {"text": payload}
  headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "translate-plus.p.rapidapi.com"
  }

  response = requests.request("POST", url, json=payload, headers=headers)
  return json.loads(response.text)["language_detection"]["language"]


#translate
def translate(payload, api_key, detected_lang='en', to_en=True):
  if to_en:
    payload = {
      "langpair": f"{detected_lang}|en",
      "q": payload,
      "mt": "1",
      "onlyprivate": "0",
      "de": "a@b.c"
    }
  else:
    payload = {
      "langpair": f"en|{detected_lang}",
      "q": payload,
      "mt": "1",
      "onlyprivate": "0",
      "de": "a@b.c"
    }
  url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"
  headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host":
    "translated-mymemory---translation-memory.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=payload)

  return json.loads(response.text)["responseData"]["translatedText"]


def MaverickQA(query):
  bot = GroundedQaBot(cohere_api_key, serp_api_key)
  verbosity = 0
  print("querying")
  question = query
  detected_lang = get_language(query, rapidapi_key)
  if detected_lang != 'en':
    question = translate(query, rapidapi_key, detected_lang, True)
    print(question)
  reply, source_urls, source_texts = bot.answer(question,
                                                verbosity=verbosity,
                                                n_paragraphs=5)

  print(reply)
  if detected_lang != 'en':
    reply = translate(reply, rapidapi_key, detected_lang, False)
  # sources_str = "\n".join(list(set(source_urls)))
  # reply_incl_sources = f"{reply}\nSource:\n{sources_str}"
  print(reply)
  return reply
