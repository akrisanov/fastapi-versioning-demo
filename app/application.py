from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from .v1.handlers.services import services_router_v1
from .v2.handlers.services import services_router_v2
from .settings import app_settings


tags_metadata = [
    {"name": "services", "description": "Service methods"},
]

app = FastAPI(
    title="My Private API",
    version="0.1",
    description="Private HTTP API for testing API versioning.",
    openapi_tags=tags_metadata,
    docs_url=app_settings.docs_url,
    openapi_url=app_settings.openapi_url,
    redoc_url=None,
)

app.include_router(services_router_v1, tags=["services"])
app.include_router(services_router_v2, tags=["services"])

app = VersionedFastAPI(
    app,
    version_format="{major}",
    prefix_format="/v{major}",
)
