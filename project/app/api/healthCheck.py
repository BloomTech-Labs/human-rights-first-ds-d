import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

@router.post('/healthCheck')
async def healthCheck():
    """
    Returns 200 for a healthcheck for AWS
    """
    return {'ok'}