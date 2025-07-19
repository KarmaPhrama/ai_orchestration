from .context_collector import context_collector
from typing import List

from vellum import (
    ChatMessage,
    ChatMessagePromptBlock,
    PlainTextPromptBlock,
    PromptParameters,
    RichTextPromptBlock,
    VariablePromptBlock,
)
from vellum.workflows.nodes.displayable.tool_calling_node.node import ToolCallingNode as BaseToolCallingNode

from ...inputs import Inputs


class ToolCallingNode(BaseToolCallingNode):
    ml_model = "gemini-1.5-flash"
    prompt_inputs = {
        "chat_history": Inputs.chat_history,
    }
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM", blocks=[RichTextPromptBlock(blocks=[PlainTextPromptBlock(text="""Talk to the user""")])]
        ),
        VariablePromptBlock(input_variable="chat_history"),
    ]
    parameters = PromptParameters(
        stop=[],
        temperature=0,
        max_tokens=8192,
        top_p=1,
        top_k=0,
        frequency_penalty=0,
        presence_penalty=0,
        logit_bias={},
        custom_parameters=None,
    )
    settings = {
        "stream_enabled": True,
    }
    max_prompt_iterations = 5
    functions = [context_collector]

    class Outputs(BaseToolCallingNode.Outputs):
        text: str
        chat_history: List[ChatMessage]
