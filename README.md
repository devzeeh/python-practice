# aug-to-dec-2026-Python-Practice

# Daily Beginner's Python Programming Guide (August – December 2026)

---

Date Started: August 19, 2026

## August: Python Fundamentals

### Week 1: Python Basics

- [x] Day 1: Install Python, set up your editor (VS Code recommended)
- [x] Day 2: Understand variables and basic syntax
- [x] Day 3: Learn data types (`int`, `float`, `str`, `bool`) and type conversion
- [x] Day 4: Practice `print()` and `input()`
- [x] Day 5: Combine variables, types, and operators to write small scripts

### Week 1 Side Project:

Build a Personal Information CLI that collects and displays basic user info.

### Side Project
**[Personal Information CLI](weeklyproject/week1.py)**

---

The Week 01 project. Practice variables, input, output, and type conversion by building a simple CLI that collects and displays personal info.

Requirements:

Ask the user for their name, age, and favorite hobby using input()
Convert age to an int
Print a formatted summary using an f-string
Calculate and print the year they were born (based on current year - age)

Bonus (optional, try only if the core version works):

Ask for height in cm and convert it to feet/inches
Validate that age input is actually a number before converting

output example:

```cmd
Enter your name: Alex
Enter your age: 20
Enter your favorite hobby: coding

Hi Alex! You are 20 years old and you were born around 2006.
You enjoy: coding
```

---

### Week 2: Conditions & Loops

- [x] Day 1: Learn `if / elif / else` and boolean logic
- [x] Day 2: Understand `while` loops
- [x] Day 3: Understand `for` loops and `range()`
- [x] Day 4: Practice `break` and `continue`
- [x] Day 5: Write programs using nested loops

### Week 2 Side Project:

Build a Number Guessing Game that gives hints if the guess is too high or low.

### Side Project
**[Number Guessing Game](weeklyproject/week2.py)**

---

The Week 02 project. You've got everything you need now: if/elif/else, while, break, and you just proved you understand how ranges and loops behave, so this should click.

Requirements:

Set secret_number = 7 (hardcoded for now — we'll swap in random module in Week 6)
Use a while True: loop that keeps asking the user to guess
Convert their input to an int
Compare their guess to secret_number:
Too high → tell them "Too high, try again"
Too low → tell them "Too low, try again"
Correct → print a success message and break out of the loop
Keep a count variable that increases by 1 on every guess
When they win, print how many guesses it took

Bonus (optional, try only if the core version works):

Limit them to 5 total attempts. If they run out without guessing correctly, print "Game over" and end the game (no need to reveal the number).

output example:

```cmd
Guess number: 4 
Too low, try again
You have 4 tries left.
Guess number: 5
Too low, try again
You have 3 tries left.
Guess number: 6
Too low, try again
You have 2 tries left.
Guess number: 7
Correct! You guessed it in 4 tries.
```

---

### Week 3: Collections

- [x] Day 1: Learn lists
- [x] Day 2: Learn tuples and sets
- [x] Day 3: Learn dictionaries
- [x] Day 4: Practice indexing & slicing
- [x] Day 5: Practice nested collections and collection methods

### Week 3 Side Project:

### Side Project
**[Student Record CLI](weeklyproject/week3.py)**

---

The Week 03 project. Store and manage student records using everything from Week 03 — lists, dictionaries, loops, and conditionals.

Requirements:

Store students as a list of dictionaries, each with name, age, and grade
Build a menu using a while True: loop with these options: Add student, View all students, Search by name, Delete a student, Exit
Add student — ask for name/age/grade via input(), append a new dict to the list
View all — loop through and print each student's info
Search by name — loop through, check if a student's name matches, print if found
Delete — find the student and remove them from the list
Exit — break out of the main loop

Bonus (optional, try only if the core version works):

Prevent duplicate names when adding a student
Sort students by grade before displaying them

output example:

```cmd
=== Student Record CLI ===
1. Add Student
2. View All Students
3. Search by Name
4. Delete Student
5. Exit
Choose an option: 1

Enter name: Alex
Enter age: 20
Enter grade: 88
Student added!
```

---

## September: Core & Intermediate Python

### Week 4: Functions & Error Handling

- [x] Day 1: Learn functions, parameters, and arguments
- [x] Day 2: Learn return values and default arguments
- [x] Day 3: Practice `*args` and `**kwargs`
- [x] Day 4: Learn `try / except` error handling
- [x] Day 5: Use `raise` to build input validation

### Week 4 Side Project:

Build a CLI Calculator that handles invalid input safely.

### Side Project
**[CLI Calculator](weeklyproject/week4.py)**

---

The Week 04 project. Build a calculator that uses functions and handles bad input safely with error handling.

Requirements:

Write separate functions for add, subtract, multiply, divide
Ask the user to choose an operation and enter two numbers
Use try/except to catch invalid input (non-numbers) and division by zero
Loop so the user can perform multiple calculations until they choose to exit

Bonus (optional, try only if the core version works):

Support a history list of past calculations, printable on request
Add a power/exponent operation using extra arguments

output example:

```cmd
1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit
Choose: 4
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero. Try again.
```

---

### Week 5: Files & Data

- [ ] Day 1: Learn file reading
- [ ] Day 2: Learn file writing and `pathlib`
- [ ] Day 3: Practice working with CSV files
- [ ] Day 4: Practice working with JSON and serialization
- [ ] Day 5: Build persistent data patterns

### Week 5 Side Project:

Build an Expense Tracker that saves and loads data.

### Side Project
**[Expense Tracker](weeklyproject/week5.py)**

---

The Week 05 project. Build an app that saves and loads expense data using files and JSON.

Requirements:

Store expenses as a list of dictionaries (description, amount, date)
Save expenses to a JSON file after every change
Load existing expenses from the file on startup (if the file exists)
Menu options: Add expense, View all, Total spent, Exit

Bonus (optional, try only if the core version works):

Filter expenses by date range
Show spending broken down by category

output example:

```cmd
1. Add Expense  2. View All  3. Total Spent  4. Exit
Choose: 3
Total spent: $245.50
```

---

### Week 6: Modules & Packages

- [ ] Day 1: Learn `import` and custom modules
- [ ] Day 2: Learn packages and `__init__.py`
- [ ] Day 3: Explore the standard library
- [ ] Day 4: Practice `datetime` and `random`
- [ ] Day 5: Practice `pathlib` and `os`

### Week 6 Side Project:

Build a Contact Manager organized into multiple modules.

### Side Project
**[Contact Manager](weeklyproject/week6.py)**

---

The Week 06 project. Organize a small application into multiple modules, using standard library tools like datetime and random.

Requirements:

Split code into at least 2 files/modules (e.g. main.py and contacts.py)
Store contacts as a list of dictionaries (name, phone, email)
Add, view, search, and delete contacts
Use datetime to timestamp when each contact was added

Bonus (optional, try only if the core version works):

Generate a random contact ID using the random module
Save/load contacts using pathlib + JSON

output example:

```cmd
1. Add  2. View All  3. Search  4. Delete  5. Exit
Choose: 1
Name: Jamie
Phone: 555-0192
Email: jamie@example.com
Added on: 2026-09-21
```

---

### Week 7: Object-Oriented Programming

- [ ] Day 1: Learn classes and objects
- [ ] Day 2: Learn attributes, methods, and `__init__`
- [ ] Day 3: Learn encapsulation
- [ ] Day 4: Learn inheritance and polymorphism
- [ ] Day 5: Learn composition

### Week 7 Side Project:

Build a Library Management System using OOP.

### Side Project
**[Library Management System](weeklyproject/week7.py)**

---

The Week 07 project. Practice OOP by modeling a library with classes, inheritance, and encapsulation.

Requirements:

Create a Book class (title, author, is_checked_out)
Create a Library class that holds a list of Book objects
Methods: add_book, checkout_book, return_book, list_available_books
Use encapsulation — keep internal book list private-ish (_books), expose via methods

Bonus (optional, try only if the core version works):

Add a Member class and track which member has which book checked out
Add an EBook subclass that inherits from Book (polymorphism)

output example:

```cmd
1. Add Book  2. Checkout  3. Return  4. List Available  5. Exit
Choose: 4
Available Books:
- "Python Basics" by J. Doe
- "Clean Code" by R. Martin
```

---

## October: Professional Python

### Week 8: Environments & Dependencies

- [ ] Day 1: Learn `venv` and `pip`
- [ ] Day 2: Learn third-party packages and `requirements.txt`
- [ ] Day 3: Learn `.env` and environment variables
- [ ] Day 4: Learn `.gitignore`
- [ ] Day 5: Practice proper project structure

### Week 8 Side Project:

Build an Inventory Management CLI as an isolated, well-structured project.

### Side Project
**[Inventory Management CLI](weeklyproject/week8.py)**

---

The Week 08 project. Set up a properly structured project with virtual environments and dependency management.

Requirements:

Set up a venv, create a requirements.txt
Structure the project with folders (e.g. src/, .gitignore, .env)
Store inventory items with name, quantity, price
Add, update stock, remove item, view total inventory value

Bonus (optional, try only if the core version works):

Read config (like low-stock threshold) from a .env file
Warn when an item's stock falls below the threshold

output example:

```cmd
Item: USB Cable | Qty: 3 | Low stock!
Total inventory value: $482.75
```

---

### Week 9: Advanced Python

- [ ] Day 1: Learn list and dictionary comprehensions
- [ ] Day 2: Learn set comprehensions and iterators
- [ ] Day 3: Learn generators and `yield`
- [ ] Day 4: Learn decorators
- [ ] Day 5: Learn context managers

### Week 9 Side Project:

Build a Log Analyzer using Python's advanced language features.

### Side Project
**[Log Analyzer](weeklyproject/week9.py)**

---

The Week 09 project. Use comprehensions, generators, and decorators to process log data efficiently.

Requirements:

Read a text log file line by line
Use a list comprehension to filter lines containing "ERROR"
Use a generator function to yield one parsed log entry at a time (for memory efficiency)
Use a decorator to time how long the analysis takes

Bonus (optional, try only if the core version works):

Use a context manager (with) to safely handle file access
Count occurrences of each log level (INFO/WARNING/ERROR) using a dict comprehension

output example:

```cmd
Found 12 ERROR entries out of 340 total lines.
Analysis completed in 0.014s.
```

---

### Week 10: Type Hints & Data Modeling

- [ ] Day 1: Learn type annotations and function types
- [ ] Day 2: Learn collection types
- [ ] Day 3: Learn `Optional` and `Union`
- [ ] Day 4: Learn `TypedDict` and dataclasses
- [ ] Day 5: Learn type aliases

### Week 10 Side Project:

Build a Task Management System with type-aware, maintainable code.

### Side Project
**[Task Management System](weeklyproject/week10.py)**

---

The Week 10 project. Add type hints and structured data modeling to a task manager using dataclasses.

Requirements:

Define a Task dataclass with title: str, done: bool, priority: int
Use type hints on all functions (parameters and return types)
Use Optional for a task's due date that may not be set
Store tasks in a List[Task]

Bonus (optional, try only if the core version works):

Use TypedDict for a config dictionary (e.g. sort settings)
Add a Union type for priority that accepts either int or str labels ("high"/"low")

output example:

```cmd
[ ] Buy groceries (priority: 2)
[x] Finish report (priority: 1)
```

---

### Week 11: Testing & Clean Code

- [ ] Day 1: Practice debugging and assertions
- [ ] Day 2: Learn `pytest` and unit testing
- [ ] Day 3: Learn integration testing and fixtures
- [ ] Day 4: Learn logging
- [ ] Day 5: Study SOLID principles, separation of concerns, and refactoring

### Week 11 Side Project:

Refactor the Expense Tracker into a fully Tested Expense Tracker.

### Side Project
**[Tested Expense Tracker](weeklyproject/week11.py)**

---

The Week 11 project. Revisit the Week 05 Expense Tracker, but refactor it with clean code principles and add automated tests.

Requirements:

Refactor Week 05's code to follow separation of concerns (e.g. split file I/O from business logic)
Write pytest unit tests for at least: adding an expense, calculating totals, filtering by category
Use assertions and proper logging instead of print() for debug output

Bonus (optional, try only if the core version works):

Add pytest fixtures for reusable test data
Add an integration test that saves and reloads from a real file

output example:

```cmd
$ pytest
====== 8 passed in 0.32s ======
```

---

## November: Python Backend Development

### Week 12: HTTP & REST

- [ ] Day 1: Learn HTTP and request/response basics
- [ ] Day 2: Learn HTTP methods and status codes
- [ ] Day 3: Learn headers and JSON
- [ ] Day 4: Learn REST principles
- [ ] Day 5: Learn CRUD design

### Week 12 Side Project:

Build a Todo REST API Prototype.

### Side Project
**[Todo REST API Prototype](weeklyproject/week12.py)**

---

The Week 12 project. Understand HTTP fundamentals by building a simple REST API prototype (no framework yet, or a minimal one).

Requirements:

Design CRUD endpoints conceptually: GET /todos, POST /todos, PUT /todos/{id}, DELETE /todos/{id}
Implement using Python's built-in http.server or a minimal framework
Return proper HTTP status codes (200, 201, 404, etc.)
Return JSON responses

Bonus (optional, try only if the core version works):

Add basic request validation (e.g. reject empty todo titles)
Add query parameter support for filtering (?done=true)

output example:

```cmd
POST /todos {"title": "Learn FastAPI"} -> 201 Created
GET /todos -> 200 OK [{"id":1,"title":"Learn FastAPI","done":false}]
```

---

### Week 13: FastAPI

- [ ] Day 1: Set up FastAPI and learn routes
- [ ] Day 2: Learn path and query parameters
- [ ] Day 3: Learn request bodies and Pydantic
- [ ] Day 4: Learn validation and response models
- [ ] Day 5: Learn error handling and API documentation

### Week 13 Side Project:

Build a Todo FastAPI application.

### Side Project
**[Todo FastAPI](weeklyproject/week13.py)**

---

The Week 13 project. Rebuild the Todo API properly using FastAPI, with validation and auto-generated docs.

Requirements:

Set up a FastAPI app with routes for full CRUD on todos
Use Pydantic models for request/response validation
Use path parameters (/todos/{id}) and query parameters (?done=true)
Handle errors properly (404 for missing todos, 422 for bad input)

Bonus (optional, try only if the core version works):

Add response models to control exactly what's returned
Explore the auto-generated docs at /docs

output example:

```cmd
$ uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000
GET /docs -> interactive Swagger UI
```

---

### Week 14: SQL & PostgreSQL

- [ ] Day 1: Learn relational databases and tables
- [ ] Day 2: Learn primary keys and foreign keys
- [ ] Day 3: Practice CRUD SQL
- [ ] Day 4: Learn JOINs and indexes
- [ ] Day 5: Learn transactions and PostgreSQL setup

### Week 14 Side Project:

Build a Bookstore API backed by PostgreSQL.

### Side Project
**[Bookstore API](weeklyproject/week14.py)**

---

The Week 14 project. Connect FastAPI to a real PostgreSQL database and model relational data.

Requirements:

Design tables: books, authors (with a foreign key relationship)
Set up PostgreSQL connection (e.g. via SQLAlchemy)
Implement CRUD endpoints that read/write to the database
Use a JOIN query to return books with their author's name

Bonus (optional, try only if the core version works):

Add indexes on frequently queried columns
Wrap multi-step operations in a transaction

output example:

```cmd
GET /books/1 -> {"title": "Dune", "author": {"name": "Frank Herbert"}}
```

---

### Week 15: Authentication & Authorization

- [ ] Day 1: Build registration and login
- [ ] Day 2: Learn password hashing
- [ ] Day 3: Learn JWT and access tokens
- [ ] Day 4: Build protected routes
- [ ] Day 5: Learn roles, permissions, and authorization

### Week 15 Side Project:

Build an Authentication API with protected endpoints and user roles.

### Side Project
**[Authentication API](weeklyproject/week15.py)**

---

The Week 15 project. Add user accounts, password security, and protected routes to an API.

Requirements:

Build /register and /login endpoints
Hash passwords before storing (never store plaintext)
Issue a JWT on successful login
Protect at least one route so it requires a valid token

Bonus (optional, try only if the core version works):

Add role-based permissions (e.g. "admin" vs "user")
Add token expiration and a refresh endpoint

output example:

```cmd
POST /login {"email": "...", "password": "..."} -> {"access_token": "eyJ..."}
GET /profile (with token) -> 200 OK
GET /profile (no token) -> 401 Unauthorized
```

---

## December: Advanced Python & Production

### Week 16: Async Python

- [ ] Day 1: Learn synchronous vs. asynchronous code
- [ ] Day 2: Learn `asyncio` and coroutines
- [ ] Day 3: Learn tasks and concurrent operations
- [ ] Day 4: Learn async HTTP
- [ ] Day 5: Learn async database operations

### Week 16 Side Project:

Build an Async API Aggregator.

### Side Project
**[Async API Aggregator](weeklyproject/week16.py)**

---

The Week 16 project. Use asyncio to fetch data from multiple sources concurrently instead of sequentially.

Requirements:

Write async functions that each call a different external API (or mock endpoint)
Use asyncio.gather() to run them concurrently
Compare and print the time difference between running them sync vs async

Bonus (optional, try only if the core version works):

Add async database queries if your DB driver supports it
Handle one source failing without crashing the whole aggregation

output example:

```cmd
Sequential fetch: 3.21s
Async fetch: 0.89s
```

---

### Week 17: Production Practices

- [ ] Day 1: Learn application configuration and environment variables
- [ ] Day 2: Learn logging and error handling
- [ ] Day 3: Learn health checks and database migrations
- [ ] Day 4: Learn pagination and filtering
- [ ] Day 5: Learn API versioning and security basics

### Week 17 Side Project:

Upgrade the Todo API toward a Production-Ready Todo API.

### Side Project
**[Production-Ready Todo API](weeklyproject/week17.py)**

---

The Week 17 project. Take an earlier API and harden it with production practices.

Requirements:

Move secrets/config into environment variables
Add structured logging and basic error handling middleware
Add a /health check endpoint
Add pagination and filtering to list endpoints
Add API versioning (e.g. /v1/todos)

Bonus (optional, try only if the core version works):

Add a database migration tool (e.g. Alembic)
Add basic rate limiting

output example:

```cmd
GET /health -> {"status": "ok"}
GET /v1/todos?page=2&limit=10 -> paginated results
```

---

### Week 18: CI/CD & Deployment

- [ ] Day 1: Learn GitHub Actions and workflow files
- [ ] Day 2: Learn YAML basics
- [ ] Day 3: Set up automated testing on push and pull request
- [ ] Day 4: Build the build/check pipeline and environment configuration
- [ ] Day 5: Set up the deployment workflow and production configuration

### Week 18 Side Project:

Turn a previous FastAPI project into an Automated Python REST API: add automated tests, a GitHub Actions workflow, test-on-push and test-on-PR, environment configuration, a deployment process, and an updated README with CI/CD instructions.

### Side Project
**[Automated Python REST API](weeklyproject/week18.py)**

---

The Week 18 project. Automate testing and deployment checks using GitHub Actions.

Requirements:

Write a GitHub Actions workflow file (.github/workflows/)
Run automated tests on every push and pull request
Configure environment variables/secrets in the workflow
Document the CI/CD setup in the README

Bonus (optional, try only if the core version works):

Add a deployment step triggered only on merges to main
Add a build/check step that fails the pipeline on lint errors

output example:

```cmd
Build passed
Tests: 12 passed
Deploy to staging: success
```

---

### Week 19: Final Portfolio Project — Transaction / Payment Management API

- [ ] Day 1: Build authentication (registration, login, password hashing, JWT, role-based authorization)
- [ ] Day 2: Build user profile and user management
- [ ] Day 3: Build transactions (create, history, status, reference, balance calculation)
- [ ] Day 4: Design the database (PostgreSQL, relationships, indexes, migrations)
- [ ] Day 5: Build REST endpoints, validation, error handling, API docs, and tests (unit, integration, auth, transaction)

### Week 19 Side Project:

Build the complete Transaction / Payment Management API.

### Side Project
**[Transaction / Payment Management API](weeklyproject/week19.py)**

---

The Week 19 project (final portfolio project). Combine everything from the roadmap into one complete backend application.

Requirements:

Full authentication system (register, login, JWT, roles)
User profile and management endpoints
Transaction endpoints: create, view history, check status, calculate balance
PostgreSQL with proper relationships, indexes, and migrations
Full REST API with validation, error handling, and docs
Unit and integration tests covering auth and transactions

Bonus (optional, try only if the core version works):

Add transaction categories/tags
Add an admin dashboard endpoint summarizing all transactions

output example:

```cmd
POST /transactions {"amount": 50, "type": "deposit"} -> 201 Created
GET /transactions/history -> [...]
GET /balance -> {"balance": 320.00}
```

---

### Week 20: Finalization & Deployment

- [ ] Day 1: Final testing and bug fixing
- [ ] Day 2: Refactor and Dockerize
- [ ] Day 3: Configure CI/CD and deploy
- [ ] Day 4: Update README, document API/architecture, and prepare the portfolio

### Week 20 Side Project:

Finalize, document, containerize, and deploy the Transaction / Payment Management API as the portfolio capstone.

### Side Project
**[Finalized Portfolio Deployment](weeklyproject/week20.py)**

---

The Week 20 project. Polish, test, containerize, and deploy the final project as a portfolio piece.

Requirements:

Fix any remaining bugs from Week 19
Refactor for clean code and consistency
Write a Dockerfile and containerize the app
Set up CI/CD deployment for the final project
Write full documentation: setup instructions, API docs, architecture overview

Bonus (optional, try only if the core version works):

Deploy to a live host (e.g. Render, Railway, Fly.io)
Record a short demo (GIF or video) for the README

output example:

```cmd
$ docker build -t transaction-api .
$ docker run -p 8000:8000 transaction-api
Deployed: https://your-api-url.example.com
```

---

## Tips for Learning Python as a Beginner

- Use the official Python docs: [https://docs.python.org/3/](https://docs.python.org/3/)
- Practice coding daily (20–30 minutes)
- Start small, build step-by-step
- Ask questions on Python forums or Stack Overflow
- Since the Go mental model is already familiar, lean on it when learning FastAPI/Pydantic — routes, handlers, and middleware map closely to `net/http` patterns

---

Date Started: <b>August 19, 2026</b> <br>
Actual Date Completed: <b></b> <br>
Estimated Date Completed: December 31, 2026

---

references
FastAPI docs: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)