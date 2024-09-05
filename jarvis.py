from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import argparse
import pyttsx3
import speech_recognition as sr
import os
import pickle
import threading
import re
import sys

session_id = "rando34"

llm = ChatOllama(temperature=0.7, model="llama3", base_url="http://localhost:11434")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You're a helpful AI assistant who's good at dealing with people. Respond in 40 words or fewer",
        ),
        ("ai", "How can I help you, sir?"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

runnable = prompt | llm
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

with_message_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# Set up the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', "com.apple.eloquence.en-GB.Eddy")
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 210)

# Set up the speech recognition engine
r = sr.Recognizer()

def speak(text):
  print("Jarvis: " + text)
  engine.say(text)
  engine.runAndWait()

def listen(i):
  with sr.Microphone() as source:
    audio = r.listen(source, phrase_time_limit=i)
  try:
    text = r.recognize_google(audio)
    return text
  except Exception as e:
    #print("Error: " + str(e))
    return None
  
def listen_for_name():
    asleep = True
    while asleep:
      prompt = listen(2)
      if prompt is not None:
        if re.search('Jarvis', prompt) is not None:
          speak("How can I help you, sir?")
          return listen(5)

def generate_response(prompt):
  completions = with_message_history.invoke(
    {"input": prompt},
    config={"configurable": {"session_id": session_id}},
    )
  message = completions.content
  return message

while True:
  prompt = listen_for_name()
  if prompt is not None:
    print("You: " + prompt)
    if prompt == "thank you":
      # Exit the loop
      speak("Any time, sir.")
      sys.exit(0)
    speak("Let me see...")
    response = generate_response(prompt)
    #speak(response)
    # split response into sentences
    sentences = response.split(".")
    for sentence in sentences:
      speak(sentence)
  else:
    speak("I'm sorry, I didn't understand that.")
