
import os

from dotenv import load_dotenv

# from models.chat import ChatClient
from models.chat_test import TestChatClient
# from models.llm import OpenAi
from models.llm_test import EchoAi


def main():
    # Set up bidirectional links
    llms = [
        # OpenAi(os.getenv("OPENAI_API_KEY"), OpenAi.Model.OPENAI_GPT_3_5),
        EchoAi(),
    ]
    chat_client = TestChatClient()
    for llm in llms:
        chat_client.attach(llm)
        llm.attach(chat_client)

    chat_client.send_message("Hello, world!")


if __name__ == "__main__":
    load_dotenv()
    main()
