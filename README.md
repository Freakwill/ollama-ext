# ollama_ext
An easy extension of ollama(-python)

See https://github.com/ollama/ollama-python

## Examples

```python
from ollama_ext import OllamaChat

with OllamaChat(name="Asistant") as chat:
    chat.run()
```
