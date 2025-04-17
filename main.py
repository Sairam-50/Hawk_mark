from fastapi import FastAPI, Request, Query, HTTPException
import jwt
from datetime import datetime, timezone

app = FastAPI()
JWT_SECRET = "my_secret"
JWT_ALGO = "HS256"

@app.get("/generate")
def generate_token(domain: str = Query(...), request: Request = None):
    # Log context
    client_ip = request.client.host if request else "unknown"
    user_agent = request.headers.get("user-agent", "unknown") if request else "unknown"
    print(f"Issuing for {domain} | IP: {client_ip} | UA: {user_agent}")
    
    # Issue token
    payload = {
        "domain": domain,
        "issued_at": datetime.now(timezone.utc).isoformat()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)
    return {"token": token}
