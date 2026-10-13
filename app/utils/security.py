from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.config import settings

# TODO: create the API key header scheme here.
# Reminder: APIKeyHeader is already imported above.
# Reminder: it is used below in Security(api_key_header).
api_key_header= APIKeyHeader(name="OPENAI_API_KEY", auto_error=False)

# VALID_API_KEYS = {"dev-key-123" : "ahmed", "dev-key-456" : "ali", "dev-key-789" : "mona"}

async def verify_api_key(api_key: str | None = Security(api_key_header)) -> str:
    """Resolve an API key to an internal user id.

    TODO: implement.
    """
    if api_key not in settings.api_keys:
        # logger.warning("invalide key")
        raise HTTPException(status_code=403, detail="this key is not authorized")
    
    user_name = settings.api_keys[api_key]
    # logger.info(f"Authanticated user: {user_name}")
    
    return user_name