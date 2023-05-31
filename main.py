
import os

from dotenv import load_dotenv

from models.chat import ChatClient
from models.llm import OpenAi


def main():
    # Set up bidirectional links
    llms = [OpenAi(os.getenv("OPENAI_API_KEY"), OpenAi.Model.OPENAI_GPT_3_5)]
    chat_client = ChatClient()
    for llm in llms:
        chat_client.attach(llm)
        llm.attach(chat_client)

    chat_client.send_message("Hello, world!")


if __name__ == "__main__":
    load_dotenv()
    main()
