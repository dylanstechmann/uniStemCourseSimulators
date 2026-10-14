"""Stable browser-facing serialization helpers."""


def timestamp(value) -> str:
    """Expose naive database UTC as unambiguous ISO8601 UTC to browsers."""
    return value.isoformat(timespec="microseconds") + "Z"
