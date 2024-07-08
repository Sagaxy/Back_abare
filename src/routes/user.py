from fastapi import APIRouter, Depends, HTTPException, status, Response
import time

from logs.logger import Logger
from services.databases.database_connector import DatabaseConnector
from models.auth import LoginRequest, Authentication
from security.authenticator import Authenticator


router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

logger = Logger().get_logger()


@router.get("/")
async def read_users():
    """
    Get all users
    """
    logger.info(f"Route /user GET called by user")
    return Response(content={"message": "Hello you are trying to make operations with users."}, status_code=status.HTTP_200_OK)

@router.post("/authenticate", tags=["Security", "User"], response_model=Authentication, status_code=status.HTTP_202_ACCEPTED)
async def authenticate_user(
    login_request: LoginRequest
):
    """
    Authenticate user
    """
    logger.info(f"Route /user/authenticate GET called by user")
    try:
        return Authenticator(logger=logger).authenticate_login(login_request)
    except Exception as e:
        logger.error(f"Failed to authenticate user: {str(e)}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")