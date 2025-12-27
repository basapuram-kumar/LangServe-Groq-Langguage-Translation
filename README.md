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

### Example from Potman from 

<img width="672" height="831" alt="Screenshot 2025-12-27 at 16 45 59" src="https://github.com/user-attachments/assets/44e74098-7e74-4f5a-a4e9-0b3181159138" />

### From UI.
<img width="1784" height="1374" alt="Screenshot 2025-12-27 at 16 48 17" src="https://github.com/user-attachments/assets/1516f498-17ba-4040-b0fa-c7a1611f0e6e" />

And
<img width="1742" height="1378" alt="Screenshot 2025-12-27 at 16 49 02" src="https://github.com/user-attachments/assets/3c6e21f8-8a48-4b4b-a216-5d2980db1e01" />


