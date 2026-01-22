#!/usr/bin/env python3

import shlex
from .commands import Commands

MAX_LEN = 1000


class ChatMixin:

    @property
    def history(self):
        return self._history

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, v):
        self._description = v
        if bool(self.history) and self.history[0]["role"] == "system":
            self.history[0] = {"role": "system", "content": v}
        else:
            self.history.insert(0, {"role": "system", "content": v})

    def init(self):
        print(f'💻System: The chat has started. Agent `{self.name.capitalize()}` will serve you.')

    def run(self, description=None):
        # To chat with AI

        self.init()

        while True:
            user_input = input("👨User: ")
            if user_input.strip().lower() in {'exit', 'quit', 'bye'}:
                print(f"🤖{self.name.capitalize()}: Bye.")
                break
            self.reply(user_input)
            self.post_process()

    def post_process(self):
        max_len = 20
        while len(self.history) > max_len:
            self.history.pop(1)

    def demo(self, prompts):
        self.init()
        for p in prompts:
            print("👨User:", p)
            self.reply(p)

    def reply(self, user_input, messages=[], memory_flag=True, max_retries=10):
        """The reply of the AI chat assistant
        
        Args:
            user_input (str): The query inputed by the user
            messages (list, optional): Additional information before user input
            memory_flag (bool, optional): save the messages
            max_retries (int, optional): The maximum of retries
        """

        if user_input.startswith(':'):
            a, v = user_input[1:].split()
            self.chat_params[a] = convert(v)
            print(f'💻System: The parameter `{a}` of chat method is set to be `{v}`.')
        elif user_input.startswith('#'):
            a, v = user_input[1:].split()
            setattr(self, a, v)
            print(f'💻System: The attribute `{a}` of chat object is set to be `{v}`.')
        elif user_input.startswith('!'):
            cmd = user_input.lstrip('! ')
            cmd, *args = shlex.split(cmd)
            try:
                getattr(Commands, cmd)(self, *args)
            except AttributeError:
                print(f"💻System: {cmd} is not registered yet!")
            except Exception as e:
                print(f"💻System: The execution of {cmd} raise an error: {e}!")
        else:
            message = {"role": "user", "content": user_input}
            messages.append(message)
            print("🤖" + self.name.capitalize(), end=": ")
            assistant_reply = self._reply(self.history + messages)
            print(assistant_reply)

            if memory_flag:
                messages.append({"role": "assistant", "content": assistant_reply})
                self.history.extend(messages)

    @property
    def history_size(self):
        return sum(len(d["content"]) for d in self.history)

    
