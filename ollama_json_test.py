import json
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

json_schema = {
    "title": "Person",
    "description": "Identifying information about a person",
    "type": "object",
    "properties": {
        "name": {
            "description": "The person's name",
            "type": "string"
        },
        "age": {
            "description": "Age of the person",
            "type": "integer"
        },
        "is_alive": {
            "description": "Is the person alive?",
            "type": "boolean"
        }
    },
    "requried": ["name", "age"]
}

# Local Llama3
llm = ChatOllama(
    model="llama3",
    format="json",
    keep_alive=1,
    temperature=0.1,
    max_new_tokens=512
)

messages = [
    HumanMessage(content="Please tell me about a person using the following JSON schema:"),
    HumanMessage(content="{schema}"),
    HumanMessage(content="Now, considering the schema, tell me about a person named John who is 30 years old and is alive."),
]

prompt = ChatPromptTemplate.from_messages(messages)

dumps = json.dumps(json_schema, indent=2)

# chain = prompt | llm | StrOutputParser()
chain = prompt | llm | JsonOutputParser()

response = chain.invoke({"schema": dumps})
print(response)
print(type(response))

