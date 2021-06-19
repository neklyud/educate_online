from fastapi import FastAPI
from pydantic import BaseModel, validator, ValidationError

app = FastAPI(root_prefix='/api')

class MathExpressionSchema(BaseModel):
    number1: int
    number2: int
    @validator('number1')
    def validate_number1(cls, v):
        assert v > 0, 'Number 1 must be positive'
        return v

    @validator('number2')
    def validate_number2(cls, v):
        assert v >= 0, 'Number 2 must be non negative'
        return v

class ResultSchema(BaseModel):
    result: int
    @validator('result')
    def validate_result(cls, v):
        assert v > 0, 'Result must be positive'
        return v

@app.post("/calc")
async def calculate(expression_schema: MathExpressionSchema) -> ResultSchema:
    return ResultSchema(result=expression_schema.number1+expression_schema.number2)
