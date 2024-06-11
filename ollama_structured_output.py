from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.llms.ollama_functions import OllamaFunctions

class Person(BaseModel): 
    name: str = Field(description="The person's name", required=True)
    height: float = Field(description="The person's height in meters", required=True)
    profession: str = Field(description="The person's profession", required=True)
    hair_color: str = Field(description="The person's hair color")
    
context = """Alex is 196 cm tall and has no hair. He is a software engineer.
Claudia is 10 feet tall and has black hair. She is a doctor. She has a blonde hair.
"""

prompt = PromptTemplate.from_template(
    """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are a smart assistant take the following context and question below and return your answer in JSON.
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    QUESTION: {question} \n
    CONTEXT: {context} \n
    JSON:
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """
)

llm = OllamaFunctions(model="llama3", format="json", temperature=0)
structured_llm = llm.with_structured_output(Person)
chain = prompt | structured_llm

response = chain.invoke({
    "question": "Who is taller?",
    "context": context
})

print(response)
