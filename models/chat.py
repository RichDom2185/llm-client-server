from models.message import Message, UserMessage
from models.observer import Observable, Observer


class ChatClient(Observer, Observable):
    """
    Observer for received responses, Observable for sending requests
    """

    def __init__(self) -> None:
        super().__init__()
        self.message_history: list[Message] = []

        self.message_handlers: list[Observer] = []

    def send_message(self, content: str) -> None:
        user_message: UserMessage = UserMessage(content)
        self.message_history.append(user_message)
        self.notify()

    # Overridden methods from Observable
    # (for sending request messages)

    def attach(self, observer: Observer) -> None:
        self.message_handlers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.message_handlers.remove(observer)

    def notify(self) -> None:
        if not self.message_history:
            return
        for observer in self.observers:
            observer.on_update(self.message_history[-1])

    # Overridden methods from Observer
    # (for receiving response messages)

    def on_update(self, payload) -> None:
        pass
