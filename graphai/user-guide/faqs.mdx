
## TypeError: object dict can't be used in 'await' expression

This is a common mistake when defining the graph. The internals of `graphai` expect _all_ nodes to be defined with `async def`. When defining a node with `def` we will see this error:

```
Traceback (most recent call last):
  File "/app/.venv/lib/python3.13/site-packages/graphai/graph.py", line 351, in execute
    output = await current_node.invoke(input=state, state=self.state)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/graphai/nodes/base.py", line 152, in invoke
    out = await instance.execute(**input)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/graphai/nodes/base.py", line 74, in execute
    return await func(**params_dict)  # Pass only the necessary arguments
           ^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: object dict can't be used in 'await' expression
```

The solution is to always define nodes using `async def`. For example:

```python

# WRONG:
@node
def my_node(input: dict) -> dict:
    return {"output": "Hello, world!"}

# DO THIS INSTEAD:
@node
async def my_node(input: dict) -> dict:
    return {"output": "Hello, world!"}
```
