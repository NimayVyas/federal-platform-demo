""" Health check endpoints for the Federal Deployment Platform. """

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/healthz", summary="Liveness check")
def healthz() -> dict[str, str]:
    """Report that the process is running. Kept dependency-free on purpose."""
    return {"status": "ok"}

