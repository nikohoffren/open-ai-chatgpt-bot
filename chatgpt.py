import os
import sys

import constants
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ['OPENAI_API_KEY'] = constants.APIKEY

query = sys.argv[1]
print(query)

#loader = TextLoader('data.txt')
loader = DirectoryLoader(".", glob="*.txt")

index = VectorIndexCreator().from_loaders([loader])

print(index.query(query, llms=ChatOpenAI()))
