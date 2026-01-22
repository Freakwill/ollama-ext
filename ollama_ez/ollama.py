#!/usr/bin/env python3

from .mixin import ChatMixin
import ollama
from ollama import Client, ResponseError

from dotenv import dotenv_values
config = dotenv_values(".env")
api_key = config.get('OLLAMA_API_KEY', '')


class ModelNotFoundError(Exception):
    """
    Do not find the model locally
    """
    def __init__(self, model):
        self.model = model
        super().__init__(f"Model `{self.model}` is not found in locally!")


class OllamaChat(ChatMixin, Client):
    # see https://github.com/ollama/ollama-python

    get_reply = lambda response: response.message.content

    def __init__(self, description='You are a very intelligent agent', history=[], name='Assistant', model='gpt-oss:120b', api_key=api_key, *args, **kwargs):
        if ':' not in model:
            model += ':latest'
        if api_key:
            super().__init__(host='https://ollama.com',
                headers={'Authorization': 'Bearer ' + api_key}, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
            if any(self.model==m.model for m in ollama.list().models):
                raise ModelNotFoundError(self.model)
        self._history = history
        self.description = description
        self.name = name
        self.model = model
        self.chat_params = {}

    def _reply(self, messages, max_retries=10):
        """Wrapper of `chat.completions.create` method of LLM
        The reply method of the AI chat assistant
        as a mapping message --> response

        Args:
            message: the prompt object inputed by the user
            max_retries (int, optional): the number of times to get response
        """

        try:
            response = self.chat(
                model=self.model,
                messages = messages,
                **self.chat_params)
            return response.message.content
        except Exception as e:
            print(f"💻System: An error occurred after {max_retries} attempts: {e}")

    def __enter__(self, *args, **kwargs):
        import sh
        sh.brew.services.start.ollama()
        return self

    def __exit__(self, *args, **kwargs):
        import sh
        sh.brew.services.stop.ollama()


class LocalOllamaChat(OllamaChat):

    def __init__(self, model='gemma3', *args, **kwargs):
        super().__init__(model=model, *args, **kwargs)
    
    def init(self, *args, **kwargs):        
        if any(self.model==m.model for m in ollama.list().models):
            raise ModelNotFoundError(self.model)
        super().init(*args, **kwargs)

