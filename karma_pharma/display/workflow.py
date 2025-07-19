from uuid import UUID

from vellum_ee.workflows.display.base import (
    EdgeDisplay,
    EntrypointDisplay,
    WorkflowDisplayData,
    WorkflowDisplayDataViewport,
    WorkflowInputsDisplay,
    WorkflowMetaDisplay,
    WorkflowOutputDisplay,
)
from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.workflows import BaseWorkflowDisplay

from ..inputs import Inputs
from ..nodes.final_output import FinalOutput
from ..nodes.tool_calling_node import ToolCallingNode
from ..workflow import Workflow


class WorkflowDisplay(BaseWorkflowDisplay[Workflow]):
    workflow_display = WorkflowMetaDisplay(
        entrypoint_node_id=UUID("732f8d98-896c-4412-a02c-862200fcd8af"),
        entrypoint_node_source_handle_id=UUID("afd7816c-ddc4-4e89-8e3c-0c0bd393a8df"),
        entrypoint_node_display=NodeDisplayData(position=NodeDisplayPosition(x=1545, y=330), width=124, height=48),
        display_data=WorkflowDisplayData(
            viewport=WorkflowDisplayDataViewport(x=-853.578209717324, y=243.5335803432779, zoom=0.6000947518029163)
        ),
    )
    inputs_display = {
        Inputs.chat_history: WorkflowInputsDisplay(
            id=UUID("b261e76e-ae85-4902-b32f-3a98c41f8c49"), name="chat_history", color="tomato"
        )
    }
    entrypoint_displays = {
        ToolCallingNode: EntrypointDisplay(
            id=UUID("732f8d98-896c-4412-a02c-862200fcd8af"),
            edge_display=EdgeDisplay(id=UUID("d8f3ac63-57dc-4aae-9c4a-b3d6d9b4560c")),
        )
    }
    edge_displays = {
        (ToolCallingNode.Ports.default, FinalOutput): EdgeDisplay(id=UUID("1762938c-60f3-4326-bf71-635e3587e6ea"))
    }
    output_displays = {
        Workflow.Outputs.final_output: WorkflowOutputDisplay(
            id=UUID("53a3b97c-461e-4441-a513-36a8545a20cd"), name="final-output"
        )
    }
