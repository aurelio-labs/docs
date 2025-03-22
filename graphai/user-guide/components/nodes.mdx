Nodes are the fundamental processing units in GraphAI. They encapsulate discrete pieces of functionality and can be connected to form complex workflows.

## Node Basics

A node in GraphAI is created by decorating an async function with the `@node` decorator:

```python
from graphai import node

@node
async def process_data(input: dict):
    # Process the input data
    result = do_something(input["data"])
    return {"output": result}
```

All nodes must be async functions that:
1. Accept at least an `input` dictionary
2. Return a dictionary containing the processed results

## Creating Different Types of Nodes

GraphAI supports several types of nodes for different purposes:

### Standard Nodes

Standard nodes process data and pass it to the next node:

```python
@node
async def standard_node(input: dict):
    # Process input
    return {"processed_data": result}
```

### Start Nodes

Start nodes mark the entry point to your graph:

```python
@node(start=True)
async def entry_node(input: dict):
    # Initial processing
    return {"initialized_data": input}
```

A graph can have only one start node.

### End Nodes

End nodes mark the exit points from your graph:

```python
@node(end=True)
async def exit_node(input: dict):
    # Final processing
    return {"final_result": processed_result}
```

A graph can have multiple end nodes.

### Streaming Nodes

Nodes that need to stream data (like LLM outputs) can use the `stream` parameter:

```python
@node(stream=True)
async def streaming_node(input: dict, callback):
    # Process with streaming
    for chunk in process_chunks(input["data"]):
        await callback.acall(chunk)
    return {"result": "streaming complete"}
```

Streaming nodes receive a `callback` parameter that can be used to stream data.

## Node Return Values

Nodes must return a dictionary containing their output:

```python
@node
async def my_node(input: dict):
    # Process input
    result = process(input["data"])
    
    # Return a dictionary with results
    return {
        "processed_data": result,
        "metadata": {"timestamp": time.time()}
    }
```

The returned dictionary is merged with the current state and passed to the next node.

## Accessing State

Nodes can access the graph's state by adding a `state` parameter:

```python
@node
async def stateful_node(input: dict, state: dict):
    # Access state
    history = state.get("history", [])
    
    # Process with state awareness
    result = process_with_history(input["data"], history)
    
    # Return updated state (will be merged with current state)
    return {"result": result, "history": history + [result]}
```

## Router Nodes

Routers are special nodes that determine the next node to execute:

```python
from graphai import router

@router
async def route_based_on_content(input: dict):
    # Analyze input and decide on next node
    if "query" in input and "question" in input["query"].lower():
        return {"choice": "question_node", "query": input["query"]}
    else:
        return {"choice": "statement_node", "statement": input["query"]}
```

Routers must return a dictionary with a `"choice"` key containing the name of the next node to execute.

### Router Example with LLM

Routers are often implemented using LLMs for intelligent routing:

```python
@router
async def llm_router(input: dict):
    from semantic_router.llms import OpenAILLM
    from semantic_router.schema import Message
    import openai
    from pydantic import BaseModel, Field
    
    class SearchRoute(BaseModel):
        query: str = Field(description="Route to search when needing external information")
    
    class MemoryRoute(BaseModel):
        query: str = Field(description="Route to memory when information is likely known")
    
    llm = OpenAILLM(name="gpt-4")
    messages = [
        Message(role="system", content="Select the best route for the user query."),
        Message(role="user", content=input["query"])
    ]
    
    response = llm(
        messages=messages,
        function_schemas=[
            openai.pydantic_function_tool(SearchRoute),
            openai.pydantic_function_tool(MemoryRoute)
        ]
    )
    
    # Parse response to get route choice
    import ast
    choice = ast.literal_eval(response)[0]
    
    return {
        "choice": choice["function_name"].lower(),
        "input": {**input, **choice["arguments"]}
    }
```

## Advanced Node Features

### Named Nodes

You can provide explicit names for nodes:

```python
@node(name="data_processor")
async def process_data(input: dict):
    # ...
    return {"processed": result}
```

This is useful when you need to refer to nodes by name in router decisions.

### Function Signatures

GraphAI automatically handles parameter mapping, so you only need to declare the parameters your node uses:

```python
@node
async def selective_processor(query: str, metadata: dict = None):
    # Only uses query and metadata from the input
    # Other fields in the input dictionary are ignored
    result = process(query, metadata)
    return {"result": result}
```

The node will only receive the parameters it declares in its signature.

## Node Input Validation

GraphAI validates that nodes receive the required parameters:

```python
@node
async def validated_node(required_param: str, optional_param: int = 0):
    # Will raise an error if required_param is not provided
    return {"result": process(required_param, optional_param)}
```

If a node's required parameters are missing, the graph execution will fail with a detailed error message.

## Next Steps

- Learn about [Graph](graphs.md) orchestration to connect your nodes
- Explore [State](state.md) management for maintaining context
- Check out [Callbacks](callbacks.md) for implementing streaming responses 