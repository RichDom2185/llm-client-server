from models.observer import Observable, Observer


class EchoAi(Observable, Observer):
    """
    Observable for received responses, Observer for sending requests
    """

    def __init__(self) -> None:
        self.clients: list[Observer] = []
        self.echo = None

    # Overridden methods from Observer
    # (for receiving request messages)

    def on_update(self, payload) -> None:
        self.echo = payload
        self.notify()

    # Overridden methods from Observable
    # (for sending response messages)

    def attach(self, observer: Observer) -> None:
        self.clients.append(observer)

    def detach(self, observer: Observer) -> None:
        self.clients.remove(observer)

    def notify(self) -> None:
        if not self.echo:
            return
        for client in self.clients:
            client.on_update(self.echo)
        self.echo = None
