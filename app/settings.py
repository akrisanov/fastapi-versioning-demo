from typing import Optional, Set

from pydantic import BaseSettings, PositiveInt


class ServerSettings(BaseSettings):
    """
    A full list of Uvicorn configs can be found here:
    https://www.uvicorn.org/#command-line-options
    """

    host: str = "127.0.0.1"
    port: PositiveInt = 8000
    root_path: str = ""  # e.g. "/api/datasets"
    log_level: str = "info"
    debug: bool = False
    reload: bool = False
    reload_dirs: Set[str] = {"app"}  # в yaml: '["app"]'
    workers: Optional[PositiveInt] = None


class AppSettings(BaseSettings):
    sentry_dsn: Optional[str] = None
    docs_url: str = "/docs"
    openapi_url: str = "/openapi.json"


server_settings = ServerSettings()
app_settings = AppSettings()
