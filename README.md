#  API Rate Limiter

A backend rate limiting service built with FastAPI that enforces API request quotas using a sliding window algorithm. Provides per-client rate limiting through API key authentication with standard rate limit response headers.

---

## Overview

This project implements a rate limiting solution for API traffic control. It uses a sliding window algorithm to track and enforce request limits per client, ensuring fair usage and protecting APIs from abuse or overuse.

---

## Features

-  **API Key Authentication** — Client identification via custom `x-api-key` header  
-  **Sliding Window Algorithm** — Time-based request tracking with dynamic window sliding  
-  **Standard Rate Limit Headers**:
  - `X-RateLimit-Limit` — Maximum requests allowed in the window  
  - `X-RateLimit-Remaining` — Remaining requests in current window  
  - `Retry-After` — Seconds until the next request is permitted  
-  **FastAPI Framework** — High-performance Python web framework  
-  **Modular Architecture** — Clean separation of concerns  

---

## Tech Stack

- Python  
- FastAPI  
- Uvicorn  

---

## Project Structure

```
api-rate-limiter/
├── rate-limiter/
│   ├── app/
│   │   ├── main.py              # Application entry point
│   │   ├── api/
│   │   │   └── routes.py        # API endpoint definitions
│   │   ├── limiter/
│   │   │   └── rate_limiter.py  # Rate limiting logic
│   │   ├── auth/
│   │   │   └── api_key.py       # API key authentication
│   │   └── core/
│   │       └── config.py        # Configuration management
│   └── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/api-rate-limiter.git
cd api-rate-limiter/rate-limiter

# Install dependencies
pip install -r requirements.txt
```

### Running the Server

```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`

## API Usage

### Making Requests

Include your API key in the `x-api-key` header:

```bash
curl -H "x-api-key: 12345" http://127.0.0.1:8000/
```

### Response Format

**Success Response:**
```json
{
  "message": "Request successful"
}
```

**Rate limit Exceed(HTTP 429):**
``` json
{
  "error": "Rate limit exceeded"
}
```

**Rate Limit Headers:**
```
X-RateLimit-Limit: 5
X-RateLimit-Remaining: 3
Retry-After: 60
```

## How It Works

1. **Client Identification** — Each request is authenticated using the `x-api-key` header
2. **Request Tracking** — Timestamps are recorded for each client request
3. **Window Enforcement** — A fixed number of requests are allowed within the configured time window
4. **Dynamic Expiration** — Old requests slide out of the window as time progresses
5. **Rate Exceeded** — When the limit is exceeded, the server returns a `429 Too Many Requests` response with the `Retry-After` header

## License

MIT