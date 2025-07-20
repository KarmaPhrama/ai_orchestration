from vellum.workflows import BaseWorkflow
from vellum.workflows.state import BaseState

from .inputs import Inputs
from .nodes.code_execution_node import CodeExecutionNode
from .nodes.final_output import FinalOutput
from .nodes.tool_calling_node import ToolCallingNode


class Workflow(BaseWorkflow[Inputs, BaseState]):
    graph = ToolCallingNode >> FinalOutput
    unused_graphs = {CodeExecutionNode}

    class Outputs(BaseWorkflow.Outputs):
        final_output = FinalOutput.Outputs.value
