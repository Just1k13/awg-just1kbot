"""Application-level preflight checks for future single-node runtime wiring."""

from dataclasses import dataclass

from app.backends import AwgBackend
from app.config import Settings
from app.db.models import Node
from app.services.errors import PreflightError


@dataclass(slots=True, frozen=True)
class NodePreflightResult:
    """Successful application-level node preflight result."""

    node_code: str
    backend_name: str


def run_node_preflight(settings: Settings, node: Node, backend: AwgBackend) -> NodePreflightResult:
    """Run lightweight preflight checks without touching OS/runtime state."""
    if not node.interface_name.strip():
        raise PreflightError("Node interface_name must be configured")
    if not node.public_host.strip():
        raise PreflightError("Node public_host must be configured")
    if node.public_port <= 0 or node.public_port > 65535:
        raise PreflightError("Node public_port must be in range 1..65535")
    if not node.subnet_cidr.strip():
        raise PreflightError("Node subnet_cidr must be configured")
    if not node.is_active:
        raise PreflightError("Node must be active for runtime usage")

    default_node_code = settings.app.default_node_code
    if not default_node_code:
        raise PreflightError("DEFAULT_NODE_CODE must be configured")
    if default_node_code != node.code:
        raise PreflightError("Configured DEFAULT_NODE_CODE does not match selected node")

    backend_name = backend.__class__.__name__
    if not backend_name:
        raise PreflightError("Backend instance is invalid")

    return NodePreflightResult(node_code=node.code, backend_name=backend_name)
