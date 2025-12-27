# LangServe-Groq-Langguage-Translation

## Verify Python Version , make sure 3.11.x is used.
```
 python -V                      
Python 3.11.13
```

## Create Groq API Keys
https://console.groq.com/keys
Add into the .env file

## Install required packages
```
 pip install -r requirements.txt
```

Execue the project
```
python serve.py
```

Response
```

➜ python serve.py
INFO:     Started server process [89688]
INFO:     Waiting for application startup.

     __          ___      .__   __.   _______      _______. _______ .______     ____    ____  _______
    |  |        /   \     |  \ |  |  /  _____|    /       ||   ____||   _  \    \   \  /   / |   ____|
    |  |       /  ^  \    |   \|  | |  |  __     |   (----`|  |__   |  |_)  |    \   \/   /  |  |__
    |  |      /  /_\  \   |  . `  | |  | |_ |     \   \    |   __|  |      /      \      /   |   __|
    |  `----./  _____  \  |  |\   | |  |__| | .----)   |   |  |____ |  |\  \----.  \    /    |  |____
    |_______/__/     \__\ |__| \__|  \______| |_______/    |_______|| _| `._____|   \__/     |_______|
    
LANGSERVE: Playground for chain "/chain/" is live at:
LANGSERVE:  │
LANGSERVE:  └──> /chain/playground/
LANGSERVE:
LANGSERVE: See all available routes at /docs/
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
```

## Access the browser
http://localhost:8000/docs

Play it out on /chain POST calls for sample data on UI or from POSTMAN tool.
