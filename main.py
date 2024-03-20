import typer
import uvicorn

from app import db

app = typer.Typer()


@app.command()
def serve(port: int = 1378, debug: bool = False):
    """
    Run the uvicorn server
    """
    print(f"FastAPI101 is coming up 0.0.0.0:{port}")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=debug,
        workers=5,
        backlog=1024,
        log_level="debug" if debug else "info",
        use_colors=True,
        access_log=debug,
    )


@app.command()
def migrate():
    """
    Create database and tables
    """
    db.migrate()


if __name__ == "__main__":
    app()
