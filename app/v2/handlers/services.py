from fastapi import APIRouter
from fastapi_versioning import version

from ..schemas.response import Message


services_router_v2 = APIRouter()


@version(2)
@services_router_v2.get(
    "/",
    response_model=Message,
    summary="Check whether the web service running",
    description="This API endpoint can serve for Kubernetes liveness probe.",
)
async def healthcheck():
    return {"detail": "API v0.2 is down 🔴"}
