# Parallel Programming in Python

This repository offers a collection of Python examples and exercises focused on parallel programming. It covers various concurrency models, including threading, multiprocessing, asynchronous programming, and inter-process communication.

## 📁 Project Structure

The repository is organized into the following directories and files:

* **`Workers/`**: Contains examples demonstrating the use of worker threads or processes.
* **`asychronos_program/`**: Showcases asynchronous programming techniques using Python's `asyncio` library.
* **`multiprocessing/`**: Includes examples utilizing Python's `multiprocessing` module for parallel execution.
* **`wikipedia_readers/`**: Features scripts that perform concurrent reading of Wikipedia pages, illustrating real-world applications of parallelism.
* **`wikipedia_readers_queue/`**: Demonstrates the use of queues for managing tasks in parallel Wikipedia reading scenarios.
* **`concurrent_program.py`**: A standalone script exemplifying concurrent execution using threads or processes.
* **`locking.py`**: Illustrates synchronization mechanisms like locks to prevent race conditions.
* **`.gitignore`**: Specifies files and directories to be ignored by Git.
* **`requirments.txt`**: Lists Python dependencies required to run the examples.

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or higher
* Recommended: Set up a virtual environment

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/iamkag/Parallel-Programming-Python.git
   cd Parallel-Programming-Python
   ```



2. **Install dependencies:**

   ```bash
   pip install -r requirments.txt
   ```



## 📚 Usage

Navigate to the directory of interest and run the Python scripts to explore different parallel programming concepts. For example:

```bash
python multiprocessing/example_script.py
```



Replace `example_script.py` with the actual script name you wish to execute.

## 🧠 Concepts Covered

* **Threading**: Creating and managing threads for concurrent execution.
* **Multiprocessing**: Running processes in parallel to utilize multiple CPU cores.
* **Asynchronous Programming**: Using `asyncio` for non-blocking I/O operations.
* **Inter-Process Communication**: Sharing data between processes using queues and pipes.
* **Synchronization**: Employing locks and other mechanisms to prevent race conditions.
