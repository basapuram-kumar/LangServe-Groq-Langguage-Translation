from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
## From groq home page, choose the required model from Inference page- Eg: openai/gpt-oss-120b
model=ChatGroq(model="openai/gpt-oss-120b",api_key=groq_api_key)

## install langserve, sse_starlette
## pip install langserve sse_starlette
from langserve import add_routes

### 1.Create prompt template
system_template="Translate the question to {language}:"
prompt_template= ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)

parser=StrOutputParser()

### Create Chain
chain=prompt_template|model|parser

## Add Define routes
app=FastAPI(title="Langchain Demo using Groq model",
            version="1.0",
            description="A simple API to translate question to any language using Groq model")

add_routes(app,
           chain,
           path="/chain")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)
