from fastapi import FastAPI
from routes import users
from scheduler import scheduler

app = FastAPI()

app.include_router(users.router)
scheduler.start()


