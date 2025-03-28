This guide will help you build a simple LLM-powered agent using GraphAI and the OpenAI API. By the end, you'll have a functional agent that can:

1. Determine whether to search for information or use memory
2. Execute the appropriate action
3. Generate a response to the user's query

## Prerequisites

- Python 3.9+
- An OpenAI API key
- Basic understanding of async Python

## Installation

```bash
pip install graphai-lib
```

## Building a Simple Agent

Let's build a simple agent that can route user questions to either search or memory retrieval.

### Step 1: Set Up Your Dependencies

```python
import os
from getpass import getpass
import ast
from graphai import router, node, Graph
from semantic_router.llms import OpenAILLM
from semantic_router.schema import Message
from pydantic import BaseModel, Field
import openai

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass("Enter OpenAI API Key: ")

# Initialize the LLM
llm = OpenAILLM(name="gpt-4o-2024-08-06")  # Use your preferred model here
```

### Step 2: Define Your Tool Schemas

We'll create Pydantic models for our tools:

```python
class Search(BaseModel):
    query: str = Field(description="Search query for internet information")

class Memory(BaseModel):
    query: str = Field(description="Self-directed query to search information from your long-term memory")
```

### Step 3: Define Your Nodes

GraphAI uses the concept of nodes to process information. Let's define our nodes:

```python
@node(start=True)
async def node_start(input: dict):
    """Entry point for our graph."""
    return {"input": input}

@router
async def node_router(input: dict):
    """Routes the query to either search or memory."""
    query = input["query"]
    messages = [
        Message(
            role="system",
            content="You are a helpful assistant. Select the best route to answer the user query. ONLY choose one function.",
        ),
        Message(role="user", content=query),
    ]
    response = llm(
        messages=messages,
        function_schemas=[
            openai.pydantic_function_tool(Search),
            openai.pydantic_function_tool(Memory),
        ],
    )
    choice = ast.literal_eval(response)[0]
    return {
        "choice": choice["function_name"].lower(),
        "input": {**input, **choice["arguments"]},
    }

@node
async def memory(input: dict):
    """Retrieves information from memory."""
    query = input["query"]
    # In a real implementation, this would query a vector database
    return {"input": {"text": "The user is in Bali right now.", **input}}

@node
async def search(input: dict):
    """Searches for information."""
    query = input["query"]
    # In a real implementation, this would make a web search
    return {
        "input": {
            "text": "The most famous photo spot in Bali is the Uluwatu Temple.",
            **input,
        }
    }

@node
async def llm_node(input: dict):
    """Generates a response using the retrieved information."""
    chat_history = [
        Message(role=message["role"], content=message["content"])
        for message in input["chat_history"]
    ]

    messages = [
        Message(role="system", content="You are a helpful assistant."),
        *chat_history,
        Message(
            role="user",
            content=(
                f"Response to the following query from the user: {input['query']}\n"
                "Here is additional context. You can use it to answer the user query. "
                f"But do not directly reference it: {input.get('text', '')}."
            ),
        ),
    ]
    response = llm(messages=messages)
    return {"output": response}

@node(end=True)
async def node_end(input: dict):
    """Exit point for our graph."""
    return {"output": input["output"]}
```

### Step 4: Set Up the Graph

The Graph connects all the nodes and defines the flow of information:

```python
# Initialize the graph
graph = Graph()

# Add nodes to the graph
graph.add_node(node_start())
graph.add_node(node_router())
graph.add_node(memory())
graph.add_node(search())
graph.add_node(llm_node())
graph.add_node(node_end())

# Add edges to create the flow
graph.add_edge(node_start, node_router)  # Start -> Router
graph.add_edge(search, llm_node)          # Search -> LLM
graph.add_edge(memory, llm_node)          # Memory -> LLM
graph.add_edge(llm_node, node_end)        # LLM -> End

# The router doesn't need explicit edges because it uses the 'choice' output to determine the next node
```

### Step 5: Execute the Graph

Now we can run our agent with a user query:

```python
import asyncio

async def run_agent():
    # Define input with a query and empty chat history
    input_data = {
        "query": "What's the best photo spot in Bali?",
        "chat_history": [
            {"role": "user", "content": "I'm planning a trip to Bali."},
            {"role": "assistant", "content": "That's wonderful! Bali is a beautiful destination with rich culture, stunning beaches, and vibrant scenery. How can I help with your trip planning?"}
        ]
    }
    
    # Execute the graph
    result = await graph.execute(input_data)
    
    # Print the result
    print(result["output"])

# Run the async function
asyncio.run(run_agent())
```

## How It Works

1. The `node_start` node receives the initial input and passes it to the router.
2. The `node_router` uses an LLM to decide whether to use search or memory based on the query.
3. The chosen node (either `search` or `memory`) retrieves information.
4. The `llm_node` generates a response using the retrieved information.
5. The `node_end` node returns the final output.

This simple example demonstrates GraphAI's flexibility. By changing the node implementations, you can easily modify the agent's behavior without changing its overall structure.
