The function schema functionality in GraphAI provides a powerful way to generate standardized function schemas that can be used with various LLM providers. This feature allows you to automatically generate function schemas from your Python functions, making it easier to integrate with LLM function calling capabilities.

## Overview

The `FunctionSchema` class is designed to consume Python functions and generate schemas that are compatible with different LLM providers (OpenAI, Ollama, LiteLLM, etc.). It automatically extracts:

- Function name
- Function description (from docstring)
- Function signature
- Return type
- Parameters (including types, defaults, and required status)

## Basic Usage

Here's a simple example of how to use the function schema functionality:

```python
from graphai.utils import FunctionSchema

def scrape_webpage(url: str, name: str = "test") -> str:
    """Provides access to web scraping. You can use this tool to scrape a webpage.
    Many webpages may return no information due to JS or adblock issues, if this
    happens, you must use a different URL.
    """
    return "hello there"

# Generate schema from function
schema = FunctionSchema.from_callable(scrape_webpage)

# Convert to dictionary format (compatible with LLM providers)
schema_dict = schema.to_dict()
```

## Schema Structure

The generated schema follows a standardized format:

```python
{
    "type": "function",
    "function": {
        "name": "function_name",
        "description": "function_description",
        "parameters": {
            "type": "object",
            "properties": {
                "param_name": {
                    "description": "param_description",
                    "type": "param_type"
                }
            },
            "required": ["required_param1", "required_param2"]
        }
    }
}
```

## Parameter Types

The schema automatically maps Python types to LLM-compatible types:

- `int` → `number`
- `float` → `number`
- `str` → `string`
- `bool` → `boolean`
- Other types → `object`

## Working with Multiple Functions

You can generate schemas for multiple functions at once using the `get_schemas` utility:

```python
from graphai.utils import get_schemas

def function1(x: int) -> str:
    """First function"""
    return str(x)

def function2(y: str, z: bool = False) -> int:
    """Second function"""
    return len(y)

# Generate schemas for multiple functions
schemas = get_schemas([function1, function2])
```

## Pydantic Model Support

The function schema functionality also supports generating schemas from Pydantic models:

```python
from pydantic import BaseModel
from graphai.utils import FunctionSchema

class SearchQuery(BaseModel):
    """A search query model"""
    query: str
    max_results: int = 10

# Generate schema from Pydantic model
schema = FunctionSchema.from_pydantic(SearchQuery)
```

## Best Practices

1. **Documentation**: Always include docstrings for your functions. The schema generator will use these as descriptions.
2. **Type Hints**: Use type hints for all parameters and return values to ensure proper type mapping.
3. **Default Values**: Consider using default values for optional parameters.
4. **Required Parameters**: Parameters without default values are automatically marked as required.

## Integration with LLM Providers

The generated schemas are compatible with major LLM interfaces such as OpenAI, LiteLLM, Ollama, and others. Most providers use the same schema format which can be generated with `to_dict`.