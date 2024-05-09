from fastapi import FastAPI
from routers.followers import router
from redis import Redis
# import httpx

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.state.redis = Redis(host="localhost", port=6379, db=1)
    # app.state.http_client = httpx.AsyncClient()

@app.on_event("shutdown")
async def shutdown_event():
    app.state.redis.close()

app.include_router(router)
