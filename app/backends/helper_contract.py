"""Helper command contract for future kernel AWG integration."""

from enum import StrEnum


class HelperCommand(StrEnum):
    """Stable command names expected from future node-helper."""

    PEER_ADD = "peer-add"
    PEER_DISABLE = "peer-disable"
    PEER_DELETE = "peer-delete"
    PEER_SHOW = "peer-show"
    PEER_LIST = "peer-list"
    CONFIG_RENDER = "config-render"
    RECONCILE = "reconcile"
    HEALTHCHECK = "healthcheck"
