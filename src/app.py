from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dataclasses import asdict
from icecream import ic

import os

from config.configs import DATABASE_CONFIGS, APP_CONFIGS, CORS_CONFIGS
from logs.logger import Logger
from services.databases.database_connector import DatabaseConnector


logger = Logger(log_dir="logs/history").get_logger()

db_connector = DatabaseConnector(**asdict(DATABASE_CONFIGS), logger=logger)

app = FastAPI(**asdict(APP_CONFIGS))

app.add_middleware(
    CORSMiddleware,
    **asdict(CORS_CONFIGS)
)


@app.get('/')
async def root():
    return {'message': f'Welcome to the {APP_CONFIGS.title.capitalize()} API, check the documentation at {APP_CONFIGS.docs_url} or {APP_CONFIGS.redoc_url} endpoints.'}

@app.post('/ping')
async def ping():
    return {'message': 'pong'}


from routes.db import router as db_router
app.include_router(db_router)

from routes.user import router as user_router
app.include_router(user_router)

#from src.routes.child import router as child_router
#app.include_router(child_router)

#from src.routes.school import router as school_router
#app.include_router(school_router)