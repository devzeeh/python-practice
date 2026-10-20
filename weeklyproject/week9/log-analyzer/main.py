from pathlib import Path
from time import perf_counter
from functools import wraps

# Decorator to measure the execution time of a function
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        return result, elapsed

    return wrapper

# Function to read a log file line by line
def read_log_file(filename):
    file_path = Path(__file__).parent / filename

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

# Function to analyze the log file for ERROR entries and count total lines
@measure_time
def analyze_log(filename):
    entries = read_log_file(filename)

    # List comprehension: filter lines containing ERROR
    error_entries = [
        entry for entry in entries
        if "ERROR" in entry
    ]

    # Count all lines separately
    total_lines = sum(
        1 for _ in read_log_file(filename)
    )

    return len(error_entries), total_lines

# Main function to execute the log analysis and print results
def main():
    (error_count, total_lines), elapsed = analyze_log("sample.log")

    print(
        f"Found {error_count} ERROR entries "
        f"out of {total_lines} total lines."
    )
    print(f"Analysis completed in {elapsed:.3f}s.")

# Entry point for the script
if __name__ == "__main__":
    main()
