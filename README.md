# Inefficient Code Test Repository

This repository contains deliberately inefficient Python code used to test automated code optimization and improvement processes.

## Purpose

This codebase is designed to:
- Demonstrate common performance anti-patterns in Python
- Serve as a test bed for automated code analysis and optimization tools
- Provide examples of code that can be improved through refactoring

## Contents

### `inefficient_code.py`

A Python module containing various inefficient implementations:

- **`slow_fibonacci(n)`**: Inefficient recursive Fibonacci calculator with exponential time complexity
- **`inefficient_string_concatenation(n)`**: String concatenation using `+` operator instead of join
- **`slow_search(items, target)`**: Linear search that doesn't short-circuit properly
- **`nested_loops_processing(data)`**: Nested loops that could be replaced with list comprehensions
- **`repeated_calculations(data, threshold)`**: Redundant calculations within loops
- **`global_variable_function()`**: Function using global state (anti-pattern)
- **`InefficientClass`**: Class with inefficient methods and repeated attribute access

## Usage

Run the module directly to see the inefficient code in action:

```bash
python inefficient_code.py
```

## Testing

Run the test suite to verify functionality:

```bash
pytest test_inefficient_code.py -v
```

## Optimization Opportunities

This code intentionally contains:
- ❌ Exponential time complexity algorithms
- ❌ Inefficient string operations
- ❌ Redundant calculations
- ❌ Poor loop structures
- ❌ Global variable usage
- ❌ Repeated attribute access

These are left unoptimized on purpose to test automated improvement tools.

## Requirements

- Python 3.7+
- No external dependencies for the main code
- pytest for running tests (optional)

## Contributing

This repository is used for testing automated improvements. See `CLAUDE.md` for guidelines on what can be modified.

## License

This is a test repository for demonstration purposes.
