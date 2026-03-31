from app.db import models  # noqa: F401
from app.db.base import Base


def test_metadata_contains_required_tables() -> None:
    expected = {
        "users",
        "nodes",
        "subscriptions",
        "device_slots",
        "profiles",
        "profile_nodes",
        "audit_logs",
    }
    assert expected.issubset(set(Base.metadata.tables.keys()))
