from abc import ABC, abstractmethod
from enum import Enum


class MessageRole(Enum):
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT = 'assistant'


class Message(ABC):
    # TODO: Investigate if the following class methods are appropriate

    # @abstractmethod
    # def from_dict(self, json: dict):
    #     pass

    # def to_dict(self) -> dict:
    #     return {
    #         'role': self.role,
    #         'content': self.content
    #     }
    pass


class SystemMessage(Message):
    role: MessageRole = MessageRole.SYSTEM

    def __init__(self, content: str) -> None:
        self.content: str = content


class UserMessage(Message):
    role: MessageRole = MessageRole.USER

    def __init__(self, content: str) -> None:
        self.content: str = content


class AssistantMessage(Message):
    role: MessageRole = MessageRole.ASSISTANT

    def __init__(self, content: str) -> None:
        self.content: str = content
