# Running App
A simple application to track running progress. Nothing fancy (yet)

## Requirements

- Python 3.12
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

## Setup

### 1. Clone the repository

```bash
git clone git@github.com:charleshb417/running-app.git
cd running-app
```

### 2. Create a virtual environment (optional but recommended)
```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn app.main:app --reload
```

### 5. Access the API

You can access the Swagger API documentation at http://127.0.0.1:8000/docs, which allows you to interact with the API and perform database operations.