# ollama_ext
An easy extension of ollama(-python)

See https://github.com/ollama/ollama-python
Also see https://github.com/Freakwill/chat-tools

## Examples

```python
from ollama_ext import OllamaChat

with OllamaChat(name="Asistant") as chat:
    chat.run()
```
