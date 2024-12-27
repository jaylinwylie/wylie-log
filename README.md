# WylieLog: 
## *A Python Logging Utility with Layered Call Tracking*

## Use Cases

- Monitoring class methods and function behavior at runtime.
- Providing structured, verbose and human-readable logs during development and testing.


## Features


   - Adds visual depth indicators (`⎢`) to logs based on the call hierarchy, making it easier to trace the flow of execution.


   - The `log_callable` decorator automatically logs inputs, outputs, and exceptions for a given function, along with the current call depth.


   - The `log_class` decorator applies logging to all callable methods of a class, ensuring comprehensive input-output tracking.


   - Automatically logs exceptions occurring within decorated functions or methods, making debugging more straightforward.


   - Integrates with the standard Python logging module using `LayeredLogAdapter` for seamless layered logging.

## Installation

No external dependencies are required beyond Python's built-in `logging` module. Ensure you have Python 3.11 or higher for compatibility.

