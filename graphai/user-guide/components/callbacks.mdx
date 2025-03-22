The Callback system in GraphAI provides a powerful mechanism for streaming data between nodes, particularly useful for handling streaming LLM outputs or other incremental data processing.

## Callback Basics

At its core, the Callback is an asyncio-based system that:

1. Provides a queue for passing streaming data between components
2. Handles special tokens to mark node start/end events
3. Structures streaming content for easy consumption by downstream processes
4. Can be integrated with any async compatible streaming system

## Creating a Callback

The Graph automatically creates a callback when needed, but you can also create and customize one:

```python
from graphai import Callback

# Create a callback with default settings
callback = Callback()

# Create a callback with custom settings
callback = Callback(
    identifier="custom_id",  # Used for special tokens
    special_token_format="<{identifier}:{token}:{params}>",  # Format for special tokens
    token_format="{token}"  # Format for regular tokens
)
```

## Callback In Nodes

To use callbacks in a node, mark it with `stream=True`:

```python
from graphai import node

@node(stream=True)
async def streaming_node(input: dict, callback):
    """This node receives a callback parameter because stream=True."""
    # Process input
    for chunk in process_chunks(input["data"]):
        # Stream output chunks
        await callback.acall(chunk)
    
    # Return final result
    return {"result": "streaming complete"}
```

Important points:
- The `stream=True` parameter tells GraphAI to inject a callback
- The node must have a `callback` parameter
- The callback can be used to stream output chunks

## Streaming from LLMs

A common use case is streaming output from an LLM:

```python
@node(stream=True)
async def llm_node(input: dict, callback):
    """Stream output from an LLM."""
    from openai import AsyncOpenAI
    
    client = AsyncOpenAI()
    
    # Start streaming response
    stream = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input["query"]}
        ],
        stream=True
    )
    
    response_text = ""
    
    # Stream chunks through the callback
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            response_text += content
            await callback.acall(content)
    
    # Return the complete response
    return {"response": response_text}
```

## Callback Methods

The Callback provides several key methods:

### Streaming Content

```python
# Synchronous callback (use in sync contexts)
callback(token="chunk of text")

# Async callback (preferred)
await callback.acall(token="chunk of text")
```

### Node Management

```python
# Mark the start of a node
await callback.start_node(node_name="my_node")

# Mark the end of a node
await callback.end_node(node_name="my_node")

# Close the callback stream
await callback.close()
```

## Consuming a Callback Stream

You can consume a callback's stream using its async iterator:

```python
async def consume_stream(callback):
    async for token in callback.aiter():
        # Process each token
        print(token, end="", flush=True)
```

This is especially useful for web applications that need to provide real-time updates.

## Special Tokens

GraphAI uses special tokens to mark events in the stream:

```
<graphai:node_name:start>  # Marks the start of a node
<graphai:node_name>        # Identifies the node
<graphai:node_name:end>    # Marks the end of a node
<graphai:END>              # Marks the end of the stream
```

These tokens can be customized using the `special_token_format` parameter.

## Example: Web Server with Streaming

Here's how to use callbacks with a FastAPI server:

```python
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from graphai import Graph, node
import asyncio

app = FastAPI()

@node(start=True, stream=True)
async def llm_stream(input: dict, callback):
    # Streaming LLM implementation...
    for chunk in get_llm_response(input["query"]):
        await callback.acall(chunk)
    return {"status": "complete"}

@node(end=True)
async def final_node(input: dict):
    return {"status": "success"}

# Create graph
graph = Graph()
graph.add_node(llm_stream())
graph.add_node(final_node())
graph.add_edge(llm_stream, final_node)

@app.post("/stream")
async def stream_endpoint(request: Request):
    data = await request.json()
    
    # Get a callback from the graph
    callback = graph.get_callback()
    
    # Start graph execution in background
    asyncio.create_task(graph.execute({"query": data["query"]}))
    
    # Return streaming response
    return StreamingResponse(
        callback.aiter(),
        media_type="text/event-stream"
    )
```

## Callback Configuration

You can customize the callback's behavior:

```python
callback = Callback(
    # Custom identifier (default is "graphai")
    identifier="myapp",
    
    # Custom format for special tokens
    special_token_format="<[{identifier}|{token}|{params}]>",
    
    # Custom format for regular tokens
    token_format="TOKEN: {token}"
)
```

## Advanced: Custom Processing of Special Tokens

You can implement custom processing of special tokens:

```python
async def process_stream(callback):
    current_node = None
    buffer = ""
    
    async for token in callback.aiter():
        # Check if it's a special token
        if token.startswith("<graphai:") and token.endswith(">"):
            # Handle node start
            if ":start" in token:
                node_name = token.split(":")[1].split(":start")[0]
                current_node = node_name
                # Handle node start event
                
            # Handle node end
            elif ":end" in token:
                # Handle node end event
                current_node = None
                
            # Handle stream end
            elif token == "<graphai:END>":
                # Handle end of stream
                break
                
        # Regular token
        else:
            # Process regular token
            buffer += token
            # Maybe do something with buffer
            
    return buffer
```

## Best Practices

1. **Use async whenever possible**: The callback system is built on asyncio
2. **Close the callback when done**: Always call `await callback.close()` when finished
3. **Keep streaming chunks small**: Don't stream large objects; break them into manageable chunks
4. **Handle special tokens correctly**: When consuming streams, handle special tokens appropriately

## Next Steps

- Learn about [Graphs](graphs.md) for orchestrating node execution
- Explore [Nodes](nodes.md) for processing logic
- Check out [State](state.md) for maintaining context across nodes 