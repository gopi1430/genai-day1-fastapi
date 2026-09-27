GenAI – Day 1 Internship Task

Project Overview

This is my Day 1 Generative AI internship project, In this project i created a simple AI API using Python, FastAPI and Google Gemini API, The user can send a text prompt to the API and the prompt is sent to the Gemini model and the generated response is returned as JSON.

Technologies Used:

* Python
* FastAPI
* Uvicorn
* Pydantic
* Google Gemini API
* python-dotenv
* Swagger UI

At first planned to use Ollama with a local LLM for this project but my laptop is operating on an older version of macOS and i was facing some problems while installing and running Ollama So instead of Ollama I used the Google Gemini API as an alternative , With Gemini i was able to connect an LLM to my FastAPI application and complete the required API flow

Project Workflow :

1. The user sends a text prompt
2. FastAPI receives the request
3. The request is validated using Pydantic
4. The prompt is sent to the Google Gemini model
5. Gemini generates a response
6. FastAPI returns the response as JSON
7. The API can be tested using Swagger UI

API Flow :
User 
    -> POST /generate 
            -> FastAPI 
                -> Pydantic Validation 
                    -> Gemini API 
                        -> Generated Response 
                            -> JSON 
                                -> Response 
                                    -> User

API Endpoint

POST /generate :
This endpoint accepts a text prompt and returns the Gemini-generated response.

