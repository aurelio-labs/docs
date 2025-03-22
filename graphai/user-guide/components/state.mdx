GraphAI provides a state management system that allows data to persist across node executions. This state is essential for maintaining context throughout the execution of a graph.

## State Basics

The graph state is a dictionary that:

1. Is initialized when the graph is created
2. Persists throughout the execution of the graph
3. Can be accessed by nodes during execution
4. Can be modified and updated as the graph executes

## Initializing State

You can initialize the graph state when creating a Graph:

```python
from graphai import Graph

# Initialize a graph with initial state
graph = Graph(initial_state={
    "history": [],
    "context": "initial context",
    "metadata": {
        "user_id": "user123",
        "session_start": 1625097600
    }
})
```

If no initial state is provided, an empty dictionary is used.

## Accessing State Methods

The Graph class provides several methods for working with state:

```python
# Get the current state
current_state = graph.get_state()

# Set a new state (replaces existing state)
graph.set_state({"new_state": "value"})

# Update the state (merges with existing state)
graph.update_state({"additional": "data"})

# Reset the state to an empty dictionary
graph.reset_state()
```

## Accessing State in Nodes

Nodes can access the graph state by including a `state` parameter in their function signature:

```python
from graphai import node

@node
async def stateful_node(input: dict, state: dict):
    # Access the state
    history = state.get("history", [])
    context = state.get("context", "")
    
    # Use the state in processing
    processed_data = process_with_context(input["data"], context)
    
    # Return updated information
    return {"result": processed_data}
```

The state is passed automatically to any node that includes a `state` parameter.

## Modifying State

There are two ways to modify the graph state:

### 1. Return State Changes in Node Output

The most common way to modify state is to include state changes in the node's return value:

```python
@node
async def update_history(input: dict, state: dict):
    # Get current history
    history = state.get("history", [])
    
    # Add new entry to history
    new_history = history + [input["query"]]
    
    # Return with updated history
    return {
        "result": process(input["query"]),
        "history": new_history  # This updates the state's history
    }
```

When the node returns, any keys in the return dictionary are merged with the current state.

### 2. Directly Update Graph State

For more complex workflows, you can use graph methods directly:

```python
@node
async def complex_state_update(input: dict, graph):
    # Process data
    result = process(input["data"])
    
    # Get current state
    current_state = graph.get_state()
    
    # Make complex updates
    current_state["history"].append(input["query"])
    current_state["metadata"]["last_processed"] = datetime.now().isoformat()
    
    # Set the updated state
    graph.set_state(current_state)
    
    return {"result": result}
```

This approach is less common but provides more flexibility for complex state manipulations.

## State Persistence

The state persists for the lifetime of the graph object. If you need to persist state between graph executions:

```python
# Save state after execution
result = await graph.execute(input_data)
saved_state = graph.get_state()

# Store saved_state somewhere (e.g., database)
store_state(saved_state)

# Later, restore state
restored_state = load_state()
graph.set_state(restored_state)
```

## State Scoping

State is scoped to the graph instance. If you create multiple graph instances, each will have its own independent state:

```python
graph1 = Graph(initial_state={"id": "graph1"})
graph2 = Graph(initial_state={"id": "graph2"})

# These operate on different state objects
graph1.update_state({"value": 1})
graph2.update_state({"value": 2})
```

## State vs. Input

It's important to understand the difference between state and input:

- **Input**: Data passed to the current node execution
- **State**: Persistent data that's available across multiple node executions

For example:

```python
@node
async def process_with_both(input: dict, state: dict):
    # Input is specific to this execution
    query = input["query"]
    
    # State persists across executions
    history = state.get("history", [])
    
    # Use both
    result = process_with_history(query, history)
    
    return {
        "result": result,
        "history": history + [query]  # Update state for future nodes
    }
```

## Best Practices

1. **Keep state serializable**: Only store data that can be easily serialized (e.g., dicts, lists, strings, numbers)
2. **Be selective**: Only use state for data that truly needs to persist across nodes
3. **Document state structure**: Create a clear structure for your state and document it
4. **Consider state size**: Don't let your state grow unbounded, especially for long-running applications

## Next Steps

- Learn about [Graphs](graphs.md) for orchestrating node execution
- Explore [Nodes](nodes.md) for processing logic
- Check out [Callbacks](callbacks.md) for implementing streaming 