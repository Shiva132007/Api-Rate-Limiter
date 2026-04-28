from fastapi import APIRouter, Request, Header, Response
from app.limiter.rate_limiter import check_limit
from app.auth.api_key import get_user

router = APIRouter()

@router.get("/")
def home(request: Request, response: Response, x_api_key: str = Header(None)):
    
    user = get_user(x_api_key)

    if not user:
        return {"error": "Invalid API Key"}

    allowed, remaining = check_limit(user)

    # Add headers
    response.headers["X-RateLimit-Limit"] = str(5)
    response.headers["X-RateLimit-Remaining"] = str(remaining)

    if not allowed:
        response.headers["Retry-After"] = "60"
        return {"error": "Rate limit exceeded"}

    return {"message": "Request successful"}