# TestFastAPI
Requirements
1)API Users: Create, update, delete addresses.
2)Address Details:
Contain coordinates (latitude and longitude).
Saved to an SQLite database.
Validated.
3)Retrieval: Retrieve addresses within a given distance from specified coordinates.
4)No GUI: Use built-in FastAPI’s Swagger Doc for testing.
5)Delivery: Provide a link to a public repository with the code and execution instructions.
6)Review Criteria: Code structure, logging, libraries used, comments, and best practices for Python and FastAPI.

## How to Run

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Start the application: `uvicorn main:app --reload`
4. Access the API documentation at `http://127.0.0.1:8000/docs`
