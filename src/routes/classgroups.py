from fastapi import APIRouter, Depends, HTTPException, status, Response
import time

from logs.logger import Logger
from services.databases.database_connector import DatabaseConnector
from controllers.classgroups import ClassGroupsController
from models.classgroups import ClassGroupsWithChildren


router = APIRouter(
    prefix="/classgroups",
    tags=["Class Groups"],
    responses={404: {"description": "Not found"}},
)

logger = Logger().get_logger()


@router.get("/", response_model=ClassGroupsWithChildren, status_code=status.HTTP_200_OK)
async def get_class_groups_with_children():
    return ClassGroupsController(logger=logger).get_classgroups_with_children()