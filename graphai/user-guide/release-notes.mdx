See below for all notable changes to the GraphAI library.

## [0.0.7] - 2025-08-16

### Added
- Graph constructor methods [`add_node`, `add_router`, `add_edge`, `set_callback`, `set_state`, `update_state`, `reset_state`, `set_start_node`, `set_end_node`, `compile`] can now be chained
- Moved `Callback` class to top-level import, you can now import it with `from graphai import Callback`

### Changed
- Dropped `networkx`, `matplotlib`, and `colorlog` dependencies (note if using `Graph.visualize` one of `networkx` or `matplotlib` must be installed)
- Updated documentation notebooks to use new callback pattern
- Updated old type annotations to use Python 3.10+ syntax, e.g., `List[str]` -> `list[str]` and `Optional[list]` -> `list | None`

## [0.0.6] - 2025-05-28

### Added
- Explicit callback parameter in `execute()` method for better control over callback instances
- `NodeProtocol` type definition for improved type safety and IDE support
- Enhanced documentation examples demonstrating proper parallel execution patterns
- New `set_callback()` method for customizing default callback class

### Changed
- **BREAKING**: Refactored callback handling to eliminate shared state between parallel executions
- Modified `execute()` method signature to accept optional `callback` parameter
- Removed internal `self.callback` attribute
- Updated all documentation notebooks to use new callback pattern
- Improved type hints throughout codebase using `Type[Callback]`

### Fixed
- **Critical**: Fixed callback stream contamination when multiple graphs executed in parallel
- Resolved race conditions in multi-threaded environments
- Fixed inconsistent streaming behavior in concurrent scenarios
- Improved memory management and reduced callback-related memory leaks
- Better cleanup of callback resources after execution

### Security
- Enhanced thread-safety for parallel graph execution
- Eliminated shared state vulnerabilities in callback handling

### Migration Guide
For basic usage, no changes required - the API remains backwards compatible.
For custom callbacks, update from:
```python
# Before (v0.0.5)
cb = graph.get_callback()
graph.callback = cb
result = await graph.execute(input=data)
```
To:
```python
# After (v0.0.6)
cb = graph.get_callback()
result = await graph.execute(input=data, callback=cb)
```

## [0.0.5] - 2025-03-30

### Added
- New function schema functionality for generating standardized function schemas compatible with various LLM providers
- Built-in colored logger with support for different log levels and custom formatting
- Support for generating function schemas from Pydantic models

### Changed
- Removed dependency on semantic router library
- Improved type mapping for function parameters in schemas
- Enhanced documentation and code organization

### Fixed
- Various bug fixes and improvements

### Security
- No security-related changes in this release

[0.0.7]: https://github.com/aurelio-labs/graphai/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/aurelio-labs/graphai/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/aurelio-labs/graphai/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/aurelio-labs/graphai/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/aurelio-labs/graphai/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/aurelio-labs/graphai/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/aurelio-labs/graphai/releases/tag/v0.0.1
