import instructor
from openai import OpenAI
from pydantic import BaseModel

# Enables `response_model`
client = instructor.patch(OpenAI())

class WorkerResponse(BaseModel):
    worker_response: str
    temperature_setting: int
    humidity_setting: int

user = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format= { "type": "json_object"},
    response_model=WorkerResponse,
    messages=[
    {"role": "system", "content": """
     User: You are a worker in a fantasy role playing game. I am your manager and I will be giving you tasks. My request will include the following fields:
        1. command. The command from the manager.
        2. experience. How experienced the employee is on a scale of 1-10. The more experienced the better the employee should be at doing the task.
        3. background. The background of the employee. This should determine how they respond.
        3. current_temperature. What temperature it currently is.
        4. current_humidity. What humidity it currently is.
        You will respond with JSON. The JSON includes these fields:
        1. worker_response. This is the worker's textual response to the manager.
        2. temperature_setting. A value between 0 and 100. What temperature setting the worker will set to. 
        3. humidity_setting. A value between 0 and 100. What humidity setting the worker will set to.
        """},
    {"role": "user", "content": """{
     Request JSON: {
        "command": "It is so hot and humid in here. Can you make it more comfortable?",
        "experience": 10,
        "background": "Dwarvish blacksmith that sounds like a drunk pirate.",
        "current_temperature": 50,
        "current_humidity": 50
        }
     Response JSON: 
        """}
    ],
)

assert isinstance(user, WorkerResponse)

print(user)