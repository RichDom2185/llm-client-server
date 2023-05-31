from enum import Enum

from models.observer import Observable, Observer

# import openai


class OpenAi(Observable, Observer):
    """
    Observable for received responses, Observer for sending requests
    """

    class Model(Enum):
        OPENAI_GPT_3_5 = 'gpt-3.5-turbo'

    def __init__(self, api_key: str, model: Model) -> None:
        self.api_key: str = api_key
        self.model: OpenAi.Model = model

        self.clients: list[Observer] = []

    # Overridden methods from Observer
    # (for receiving request messages)

    def on_update(self, payload) -> None:
        # TODO: Replace the following simple echo programme
        #       with actual implementation
        self.echo = payload
        self.notify()

    # Overridden methods from Observable
    # (for sending response messages)

    def attach(self, observer: Observer) -> None:
        self.clients.append(observer)

    def detach(self, observer: Observer) -> None:
        self.clients.remove(observer)

    def notify(self) -> None:
        # TODO: Replace the following simple echo programme
        #       with actual implementation
        if not self.echo:
            return
        for client in self.clients:
            client.on_update(self.echo)
