import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from spcalc.add import Add
from spcalc.subtract import Subtract
from spcalc.multiply import Multiply
from spcalc.divide import Divide
from spcalc.calculator import Calculator

app = FastAPI()

operations = {
    "add": Add(),
    "subtract": Subtract(),
    "multiply": Multiply(),
    "divide": Divide(),
}


class Numbers(BaseModel):
    number1: float
    number2: float
    operation: str


@app.get("/")
async def root():
    return {"message": "SPCalc API"}


@app.post("/calculate")
async def add_numbers(request: Numbers):
    if request.operation not in operations:
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "error": "Invalid operation, please use add, subtract, multiply or divide"
                }
            ),
            status_code=400,
        )

    operation = Calculator(
        request.number1, request.number2, operations[request.operation]
    )
    try:
        answer = operation.execute()
    except ZeroDivisionError:
        return JSONResponse(
            content=jsonable_encoder({"error": "Cannot divide by zero"}),
            status_code=400,
        )
    except Exception as e:  # pylint: disable=broad-except
        return JSONResponse(
            content=jsonable_encoder({"error": f"An error occurred: {e}"}),
            status_code=500,
        )
    return JSONResponse(content=jsonable_encoder({"answer": answer}), status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
