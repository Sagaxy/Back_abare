from fastapi import APIRouter, Depends, HTTPException, status, Response
import time

from logs.logger import Logger
from services.databases.database_connector import DatabaseConnector


router = APIRouter(
    prefix="/database",
    tags=["Database"],
    responses={404: {"description": "Not found"}},
)

logger = Logger().get_logger()

db_connector = DatabaseConnector()


@router.get("/", tags=["Admin"])
async def ping_db():
    """
    Get all users
    """
    logger.info(f"Route /db GET called by user at {time.time()}")
    return Response(content={"message": "Hello you are trying to make operations with the database."}, status_code=status.HTTP_200_OK)

@router.get("/create-tables", tags=["Admin"])
async def create_tables():
    """
    Create tables in the database
    """
    logger.info(f"Route /db/create-tables GET called by user at {time.time()}")
    db_connector.create_tables()
    return Response(content={"message": "Tables created."}, status_code=status.HTTP_200_OK)

@router.get("/drop-tables", tags=["Admin"])
async def drop_tables():
    """
    Drop tables from the database
    """
    logger.info(f"Route /db/drop-tables GET called by user at {time.time()}")
    db_connector.drop_tables()
    return Response(content={"message": "Tables dropped."}, status_code=status.HTTP_200_OK)

@router.get("/recreate-tables", tags=["Admin"])
async def recreate_tables():
    """
    Recreate tables in the database
    """
    logger.info(f"Route /db/recreate-tables GET called by user at {time.time()}")
    db_connector.recreate_tables()
    return Response(content={"message": "Tables recreated."}, status_code=status.HTTP_200_OK)