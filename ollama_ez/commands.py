#!/usr/bin/env python3

import pathlib
import yaml


history_file = pathlib.Path('history.yaml')


class Commands:

    # the first argument should be the object of AI-chat

    @classmethod
    def greet(cls, obj):
        obj.history = []
        print(f'💻System: Hello, user.')

    @classmethod
    def clear(cls, obj):
        obj.history = []
        print(f'💻System: The history is cleared.')

    @classmethod
    def pop(cls, obj, k):
        obj.history.pop(k)
        print(f'💻System: The k-th message in history is poped.')

    @classmethod
    def save(cls, obj):
        if not history_file.exists():     
            print("💻System: The history is stored in {history_file}!")
            history_file.write_text(yaml.dump(obj.history, allow_unicode=True))
        else:
            print("💻System: {history_file} is available! The history will not be stored")

    @classmethod
    def load(cls, obj):
        if history_file.exists():
            print('💻System: The history is loaded from {history_file}!')
            obj.history = yaml.safe_load(str(history_file))
        else:
            print('💻System: No history is loaded!')

    @classmethod
    def ollama(cls, obj, cmd, *args):
        import ollama
        if cmd == 'search':
            cmd = 'web_search'
        elif cmd == 'fetch':
            cmd = 'web_fetch'
        getattr(ollama, cmd)(*args)
        print(f'💻System: Run ollama command `{cmd}`.')

    @classmethod
    def register(cls, name=None):
        def dec(f):
            _name = name or f.__name__
            setattr(cls, _name, f)
        return dec
