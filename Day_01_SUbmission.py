from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
import uvicorn
from dotenv import load_dotenv
load_dotenv()


api = FastAPI(
    title="GenAI API",
    description="FastAPI connected with Gemini",
    version="1.0"
)


client = genai.Client(
    api_key=os.getenv("gemiapi")
)


class GenerateRequest(BaseModel):
    text: str


@api.post("/generate")
def generate_response(request: GenerateRequest):

    response = client.models.generate_content(
        model="models/gemini-3.5-flash-lite",
        contents=request.text
    )

    return {
        "input": request.text,
        "response": response.text
    }


if __name__ == "__main__":
    uvicorn.run(
        api,
        host="127.0.0.1",
        port=8002
    )