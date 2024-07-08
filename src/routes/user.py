from fastapi import APIRouter, Depends, HTTPException, status, Response
import time

from logs.logger import Logger
from services.databases.database_connector import DatabaseConnector
from models.auth import LoginRequest, Authentication
from models.users import UsersAbbreviated, UserAbbreviated, UserDetails
from controllers.users import UsersController
from security.authenticator import Authenticator



router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

logger = Logger().get_logger()


@router.get("/", response_model=UsersAbbreviated, status_code=status.HTTP_200_OK)
async def get_users():
    """
    List all users with their respective access type.
    """
    logger.info(f"Route /user GET called by user")
    try:
        return UsersController(logger=logger).get_users()
    except Exception as e:
        logger.error(f"Failed to read users table")
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to read users table")

@router.get("/{user_id}", response_model=UserAbbreviated, status_code=status.HTTP_200_OK)
async def get_user(
    user_id
):
    """
    Get specific user data
    """
    logger.info(f"Route /user/{user_id} called by user")
    try:
        return UsersController(logger=logger).get_user(user_id)
    except Exception as e:
        logger.error(f"Failed to find user")
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to find user")
    
@router.get("/{user_id}/details", response_model=UserDetails, status_code=status.HTTP_200_OK)
async def get_user_with_details(
    user_id
):
    """
    Get specific user data
    """
    logger.info(f"Route /user/{user_id}/details called by user")
    try:
        return UsersController(logger=logger).get_user_with_details(user_id)
    except Exception as e:
        logger.error(f"Failed to find user")
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to find user")

@router.post("/authenticate", tags=["Security", "User"], response_model=Authentication, status_code=status.HTTP_202_ACCEPTED)
async def authenticate_user(
    login_request: LoginRequest
):
    """
    Authenticate any type of user, independent of application or access type.
    """
    logger.info(f"Route /user/authenticate GET called by user")
    try:
        return Authenticator(logger=logger).authenticate_login(login_request)
    except Exception as e:
        logger.error(f"Failed to authenticate user: {str(e)}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")