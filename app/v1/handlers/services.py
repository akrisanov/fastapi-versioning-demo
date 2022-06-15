from fastapi import APIRouter
from fastapi_versioning import version

from ..schemas.response import Message


services_router_v1 = APIRouter()


@version(1)
@services_router_v1.get(
    "/",
    response_model=Message,
    summary="Check whether the web service running",
    description="This API endpoint can serve for Kubernetes liveness probe.",
)
async def healthcheck():
    return {"detail": "API v0.1 is OK 🟢"}
