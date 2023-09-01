# Standard Library
import base64

# External
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

# Project
from app.config import LOGGER
from app.config.config import JWT_ALGORITHM, JWT_PRIVATE_KEY, JWT_PUBLIC_KEY


class Settings(BaseModel):
    authjwt_algorithm: str = JWT_ALGORITHM
    authjwt_decode_algorithms: list[str] = [JWT_ALGORITHM]
    authjwt_token_location: set = {"cookies", "headers"}
    authjwt_access_cookie_key: str = "access_token"
    authjwt_refresh_cookie_key: str = "refresh_token"
    authjwt_cookie_csrf_protect: bool = True
    authjwt_public_key: str = base64.b64decode(JWT_PUBLIC_KEY).decode("utf-8")
    authjwt_private_key: str = base64.b64decode(JWT_PRIVATE_KEY).decode("utf-8")


@AuthJWT.load_config
def get_config():
    try:
        if not JWT_ALGORITHM or not JWT_PRIVATE_KEY or not JWT_PUBLIC_KEY:
            raise ValueError("Missing essential JWT environment variables.")

        config_jwt = [
            ("authjwt_algorithm", JWT_ALGORITHM),
            ("authjwt_decode_algorithms", [JWT_ALGORITHM]),
            ("authjwt_token_location", {"cookies", "headers"}),
            ("authjwt_access_cookie_key", "access_token"),
            ("authjwt_refresh_cookie_key", "refresh_token"),
            ("authjwt_cookie_csrf_protect", True),
            (
                "authjwt_public_key",
                base64.b64decode(JWT_PUBLIC_KEY).decode("utf-8") if JWT_PUBLIC_KEY else "",
            ),
            (
                "authjwt_private_key",
                base64.b64decode(JWT_PRIVATE_KEY).decode("utf-8") if JWT_PRIVATE_KEY else "",
            ),
        ]

        LOGGER.info("JWT configuration loaded successfully.")
        return config_jwt

    except Exception as e:
        LOGGER.error(f"Failed to load JWT configuration: {e}")
        raise
