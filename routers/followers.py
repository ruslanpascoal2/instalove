from fastapi import APIRouter, Request
from instagrapi import Client

router = APIRouter(
    prefix="/followers"
)

@router.get("/")
def read_root(request: Request):
    return {"followers": get_followers(request)}

def get_followers(request: Request):
    followers = request.app.state.redis.get("seguidores")

    if followers is None:
        ACCOUNT_USERNAME = "ruslanwebdev"
        ACCOUNT_PASSWORD = "7?HofEHLKz9&cqLm"
        cl = Client()
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
        user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
        followers = cl.user_followers(user_id)
        request.app.state.redis.set("seguidores", followers)

    return followers


