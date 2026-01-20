# ollama_ext
An easy extension of ollama(-python)

See https://github.com/ollama/ollama-python
Also see https://github.com/Freakwill/chat-tools

## Clients

- OllamaChat: gpt-oss:120b by default (set api key)
- LocalOllamaChat: use local model (download the model by ollma; gemma3 by default)

## Attributes
Main attributes of OllamaChat
- description="......"
- history=[]
- name='Assistant'
- model='gpt-oss:120b'
- api_key=`<your api key>`

## Examples

```python
from ollama_ext import OllamaChat

with OllamaChat(name="Asistant") as chat:
    chat.run()
```
