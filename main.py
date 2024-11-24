from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Dict, Any
import httpx

app = FastAPI()

# Define the data model
class ContextData(BaseModel):
    context_title: str = Field(..., description="Title of the context")
    context_details: Dict[str, Any] = Field(..., description="Dynamic key-value data related to the context")

# Define the endpoint
@app.post("/send-json/")
async def send_json(
    context_data: ContextData,
    target_url: str = Body(..., embed=True, description="Target URL to forward the JSON data")
):
    """
    Sends a JSON object to the specified target API URL.

    Parameters:
        - context_data: JSON object with dynamic fields.
        - target_url: URL of the API to forward the JSON.
    """
    try:
        # Log incoming request data (for debugging)
        print(f"Received context_data: {context_data.dict()}")
        print(f"Target URL: {target_url}")

        # Validate target_url
        if not target_url.startswith("http"):
            raise HTTPException(status_code=400, detail="Invalid target URL")

        # Send the data using httpx
        async with httpx.AsyncClient() as client:
            response = await client.post(target_url, json=context_data.dict())

        # Check for a successful response
        if response.status_code >= 400:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Error from target API: {response.text}",
            )

        return {
            "message": "Data sent successfully!",
            "response_status": response.status_code,
            "response_body": response.json(),
        }
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
