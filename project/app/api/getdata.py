from fastapi import APIRouter, HTTPException
import pandas as pd
from .update import backlog_path
from ast import literal_eval

router = APIRouter()


@router.get('/getdata')
async def getdata():
    '''
    Get data from backlog database.
    '''
    try:
        with open(backlog_path) as f:
            pass  # file can be opened successfully
        # load backlog and return it
        backlog = pd.read_csv(
            backlog_path,
            converters={
                'links': literal_eval,
                'geocoding': literal_eval
            }
        )
        return backlog.to_json(orient='records')
    except IOError:
        # file cannot be opened successfully and needs to be created
        return HTTPException(
            404,
            'Backlog has not been created yet or cannot be found, please run /update first.'
        )
