import qsbi.crud.sql  # noqa: F401
from qsbi.api.main import qsbi_api

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(qsbi_api, host="0.0.0.0", port=8001, log_level="debug")
