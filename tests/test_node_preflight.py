from app.backends import KernelAwgBackend
from app.config.settings import AppRuntimeSettings, DatabaseSettings, Settings
from app.db.models import Node
from app.services import PreflightError, run_node_preflight


def _build_settings(default_node_code: str | None) -> Settings:
    return Settings(
        bot={"token": "123456:token"},
        db=DatabaseSettings(dsn="postgresql+asyncpg://u:p@localhost:5432/test"),
        app=AppRuntimeSettings(default_node_code=default_node_code),
    )


def _build_node() -> Node:
    return Node(
        code="main",
        public_host="vpn.example.com",
        public_port=51820,
        interface_name="awg0",
        subnet_cidr="10.8.0.0/24",
        is_active=True,
    )


def test_node_preflight_success() -> None:
    result = run_node_preflight(
        settings=_build_settings(default_node_code="main"),
        node=_build_node(),
        backend=KernelAwgBackend(),
    )

    assert result.node_code == "main"
    assert result.backend_name == "KernelAwgBackend"


def test_node_preflight_fails_for_missing_default_node_code() -> None:
    try:
        run_node_preflight(
            settings=_build_settings(default_node_code=None),
            node=_build_node(),
            backend=KernelAwgBackend(),
        )
    except PreflightError as exc:
        assert "DEFAULT_NODE_CODE" in str(exc)
    else:
        raise AssertionError("Expected PreflightError")


def test_node_preflight_fails_for_inactive_node() -> None:
    node = _build_node()
    node.is_active = False

    try:
        run_node_preflight(
            settings=_build_settings(default_node_code="main"),
            node=node,
            backend=KernelAwgBackend(),
        )
    except PreflightError as exc:
        assert "active" in str(exc)
    else:
        raise AssertionError("Expected PreflightError")


def test_node_preflight_fails_for_invalid_port() -> None:
    node = _build_node()
    node.public_port = 70000

    try:
        run_node_preflight(
            settings=_build_settings(default_node_code="main"),
            node=node,
            backend=KernelAwgBackend(),
        )
    except PreflightError as exc:
        assert "1..65535" in str(exc)
    else:
        raise AssertionError("Expected PreflightError")


def test_node_preflight_fails_for_empty_subnet() -> None:
    node = _build_node()
    node.subnet_cidr = ""

    try:
        run_node_preflight(
            settings=_build_settings(default_node_code="main"),
            node=node,
            backend=KernelAwgBackend(),
        )
    except PreflightError as exc:
        assert "subnet_cidr" in str(exc)
    else:
        raise AssertionError("Expected PreflightError")
