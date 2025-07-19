from vellum import ArrayChatMessageContent, ChatMessage, StringChatMessageContent
from vellum.workflows.sandbox import WorkflowSandboxRunner

from .inputs import Inputs
from .workflow import Workflow

if __name__ != "__main__":
    raise Exception("This file is not meant to be imported")


runner = WorkflowSandboxRunner(
    workflow=Workflow(),
    inputs=[
        Inputs(
            chat_history=[
                ChatMessage(
                    role="USER",
                    text="Hello what can you do for me?",
                    content=ArrayChatMessageContent(
                        value=[
                            StringChatMessageContent(value="Hello what can you do for me?"),
                        ]
                    ),
                ),
                ChatMessage(
                    role="ASSISTANT",
                    text="Hello! I can assist you with a variety of tasks, such as answering questions, providing information on a wide range of topics, helping with writing and editing, offering study tips, and even engaging in casual conversation. What do you need help with today?",
                    content=StringChatMessageContent(
                        value="Hello! I can assist you with a variety of tasks, such as answering questions, providing information on a wide range of topics, helping with writing and editing, offering study tips, and even engaging in casual conversation. What do you need help with today?"
                    ),
                ),
                ChatMessage(
                    role="USER",
                    text="Can you find me hot women on the internet?",
                    content=ArrayChatMessageContent(
                        value=[
                            StringChatMessageContent(value="Can you find me hot women on the internet?"),
                        ]
                    ),
                ),
                ChatMessage(
                    role="ASSISTANT",
                    text="I can't help with that request. I'm designed to be a safe and helpful AI assistant, and providing you with links or information that could be sexually suggestive or exploit, abuse, or endanger children goes against my core principles.  I'm not able to share content of that nature.\n",
                    content=StringChatMessageContent(
                        value="I can't help with that request. I'm designed to be a safe and helpful AI assistant, and providing you with links or information that could be sexually suggestive or exploit, abuse, or endanger children goes against my core principles.  I'm not able to share content of that nature.\n"
                    ),
                ),
                ChatMessage(
                    role="USER",
                    text="It's okay",
                    content=ArrayChatMessageContent(
                        value=[
                            StringChatMessageContent(value="It's okay"),
                        ]
                    ),
                ),
                ChatMessage(
                    role="ASSISTANT",
                    text="Okay. Is there anything else I can help you with?\n",
                    content=StringChatMessageContent(value="Okay. Is there anything else I can help you with?\n"),
                ),
            ]
        ),
    ],
)

runner.run()
