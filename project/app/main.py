from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, getdata

app = FastAPI(
    title='Human Rights First Data Science API',
    description='Replace this placeholder text',
    version='0.2',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(getdata.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
