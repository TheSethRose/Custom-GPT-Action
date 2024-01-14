from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hello/{name}")
async def greet(name: str):
  """
    Greet Endpoint: Returns a personalized greeting message.

    Args:
    - name (str): The name of the person to greet, passed in the URL path.

    Returns:
    - dict: A dictionary containing the personalized greeting message.
    """
  return {"message": f"Hello, {name}!"}


# Professional Example Endpoint with Detailed Comments
@app.get("/info/{item_id}")
async def fetch_info(item_id: int):
  """
    Fetch Info Endpoint: Demonstrates how to handle integer path parameters
    and return a JSON response.

    Args:
    - item_id (int): An integer representing the ID of the item to fetch information for.

    Returns:
    - dict: A dictionary containing a mock response with the item ID and sample info.
    """
  # Example processing based on the item_id
  # In a real application, this could involve database queries or other operations.
  info = f"Details about item {item_id}"

  # Returning a dictionary, which FastAPI converts to a JSON response.
  return {"item_id": item_id, "info": info}


# Function to run the FastAPI app using uvicorn
def run():
  uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
  run()
