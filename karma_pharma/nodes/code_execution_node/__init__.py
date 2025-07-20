from typing import Union

from vellum.client.types import CodeExecutionPackage
from vellum.workflows.nodes.displayable import CodeExecutionNode as BaseCodeExecutionNode
from vellum.workflows.state import BaseState


class CodeExecutionNode(BaseCodeExecutionNode[BaseState, Union[float, int]]):
    filepath = "./script.py"
    code_inputs = {}
    runtime = "PYTHON_3_11_6"
    packages = [
        CodeExecutionPackage(name="requests", version="2.32.4"),
    ]
