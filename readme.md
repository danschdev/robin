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

### 3. Install dependencies

```bash
pip install -r requirements.txt
pre-commit install
```


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