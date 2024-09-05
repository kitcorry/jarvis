from langchain_community.llms import ollama
import warnings
warnings.filterwarnings("ignore")

ol = ollama.Ollama(base_url='http://127.0.0.1:11434', model='llama3')
print(ol('why is the sky blue? be brief as though speaking to a 5 year old'))
