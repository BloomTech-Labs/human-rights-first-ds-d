from fastapi import APIRouter, HTTPException
import pandas as pd

import psycopg2

router = APIRouter()


@router.get('/getdata')
async def getdata():
    '''
    Get data from backlog database.
    '''

    return {'return': 'not implemented yet!'}
