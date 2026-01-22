# ollama-easy
An easy extension of ollama(-python)

See [Ollama](https://ollama.com/), https://github.com/ollama/ollama-python

Also see https://github.com/Freakwill/chat-tools

## Requirements
1. install ollama and its SDK
2. save API Key in path `ollama_ez/.env`

## Clients

- OllamaChat: gpt-oss:120b by default (set api key)
- LocalOllamaChat: use local model, gemma3 by default (download the model by ollama)

## Attributes
Main attributes of OllamaChat
- description="......"
- history=[]
- name='Assistant'
- model='gpt-oss:120b'
- api_key=`<your api key>`

## Examples

```python
from ollama_ext import OllamaChat # or LocalOllamaChat

with OllamaChat() as chat:
    chat.run()
```
