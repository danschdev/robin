## Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pre-commit install
```
Remember to list dependencies in .pre-commit-config.yaml.

### 4. Set up database

```bash
python.exe .\setup\setupDatabase.py
```

### 5. Run Flask server

```bash
python -m flask --app=server/server.py run

## Code Quality Tools

### Ruff usage
Static analysis / linting
```bash
ruff check --fix
```

Layout style
```bash
ruff format .
```

### Pyright Usage
```bash
pyright .
```