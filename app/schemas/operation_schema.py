from pydantic import BaseModel


class OperationElemSchema(BaseModel):
    name: str
    symbol: str
    description: str


class OperationSchema(BaseModel):
    elements: list[OperationElemSchema]
