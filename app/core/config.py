import os
from pathlib import Path
from typing import Optional


def _load_env_file(env_path: Path) -> None:
    """
    Minimal .env loader without external dependencies.
    Sets environment variables only if not already set.
    """
    if not env_path.is_file():
        return

    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip("'\"")
                if key and key not in os.environ:
                    os.environ[key] = value
    except Exception:
        pass


class Settings:
    """
    Application settings and configuration.
    """

    def __init__(self) -> None:
        self.api_root: Path = Path(__file__).resolve().parent.parent.parent
        # Load .env from API root if present
        _load_env_file(self.api_root / ".env")

        # Database path: env var DATABASE_PATH or default to ../InvestMap-DB/investmap.db
        default_db_path = (self.api_root.parent / "InvestMap-DB" / "investmap.db").resolve()
        raw_db_path = os.getenv("DATABASE_PATH")

        if raw_db_path:
            configured_path = Path(raw_db_path)
            if not configured_path.is_absolute():
                self.database_path: Path = (self.api_root / configured_path).resolve()
            else:
                self.database_path = configured_path.resolve()
        else:
            self.database_path = default_db_path

    @property
    def db_path_str(self) -> str:
        return str(self.database_path)


settings = Settings()
