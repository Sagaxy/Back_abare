from fastapi import APIRouter, Depends, HTTPException, status, Response
import time

from logs.logger import Logger
from services.databases.database_connector import DatabaseConnector


router = APIRouter(
    prefix="/children",
    tags=["Children"],
    responses={404: {"description": "Not found"}},
)

logger = Logger().get_logger()