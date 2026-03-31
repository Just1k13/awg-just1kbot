"""Service-layer errors."""


class PreflightError(ValueError):
    """Raised when application-level preflight validation fails."""
