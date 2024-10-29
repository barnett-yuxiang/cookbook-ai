# create a FastAPI app
# run with uvicorn first_flight:app --reload

from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/", response_model=dict)
def read_root() -> dict:
    """
    Root endpoint that returns a greeting message.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}", response_model=dict)
def read_item(item_id: int, q: str = None) -> dict:
    """
    Endpoint to read an item by its ID.

    Args:
        item_id (int): The ID of the item.
        q (str, optional): An optional query parameter.

    Returns:
        dict: A dictionary containing the item ID and the query parameter.
    """
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
