from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.llms.ollama_functions import OllamaFunctions

model = OllamaFunctions(
    model="llama3",
    format="json"
)

model = model.bind_tools(
    tools=[
        {
            "name": "get_current_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "description": "The location to get the weather for, e.g. Kyiv",
                        "type": "string"
                    },
                    "unit": {
                        "description": "The unit to return the temperature in, e.g. Celsius or Fahrenheit",
                        "type": "string",
                        "enum": ["C", "F"]
                    }
                },
            },
            "required": ["location"],
        },
    ],
    function_call={"name": "get_current_weather", "parameters": {"location": "Kyiv", "unit": "C"}}
)

response = model.invoke("what is the weather in Warsaw?")

print(response)
