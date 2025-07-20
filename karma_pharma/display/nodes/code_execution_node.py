from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseCodeExecutionNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.code_execution_node import CodeExecutionNode


class CodeExecutionNodeDisplay(BaseCodeExecutionNodeDisplay[CodeExecutionNode]):
    label = "Code Execution Node"
    node_id = UUID("4e076a76-1c8c-4ef5-a2d7-e316312b6d20")
    target_handle_id = UUID("67d024b3-1f05-4f61-b145-c99b14059c8c")
    output_id = UUID("ff21693c-2a4b-4768-9929-f93ba11b3db8")
    log_output_id = UUID("f8b812be-3e08-45de-8cbe-d43a8bb125e1")
    node_input_ids_by_name = {
        "code": UUID("73235928-9a01-4a31-848a-77f7e14a9b4e"),
        "runtime": UUID("e57096c9-5173-42a1-9bb1-cdd1bc8351a7"),
    }
    output_display = {
        CodeExecutionNode.Outputs.result: NodeOutputDisplay(
            id=UUID("ff21693c-2a4b-4768-9929-f93ba11b3db8"), name="result"
        ),
        CodeExecutionNode.Outputs.log: NodeOutputDisplay(id=UUID("f8b812be-3e08-45de-8cbe-d43a8bb125e1"), name="log"),
    }
    port_displays = {
        CodeExecutionNode.Ports.default: PortDisplayOverrides(id=UUID("65d24666-1d7e-4c45-ae69-f005671117aa"))
    }
    display_data = NodeDisplayData(
        position=NodeDisplayPosition(x=2665.912410464427, y=-189.9939624368748), width=554, height=310
    )
