from app.settings import server_settings
from app.application import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=server_settings.host,
        port=server_settings.port,
        root_path=server_settings.root_path,
        log_level=server_settings.log_level,
        log_config="logging.yaml",
        debug=server_settings.debug,
        reload=server_settings.reload,
        reload_dirs=server_settings.reload_dirs,
        workers=server_settings.workers,
    )
