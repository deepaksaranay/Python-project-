# 🧪 API Automation Testing with Pytest

A complete REST API test suite using `pytest` + `requests`.

## Tech Stack
- Python 3.x
- pytest
- requests
- pytest-html

## Project Structure
```
api_test_project/
├── conftest.py
├── test_users.py
├── test_posts.py
├── utils/
│   ├── __init__.py
│   └── api_client.py
├── requirements.txt
├── pytest.ini
└── .gitignore
```

## Setup & Run

```bash
# Dependencies install karo
pip install -r requirements.txt

# Tests run karo
pytest

# HTML report ke saath
pytest --html=report.html
```

## Test Coverage
- ✅ GET / POST / PUT / DELETE
- ✅ Schema validation
- ✅ Parametrized tests
- ✅ Performance testing
- ✅ Negative testing (404)
- ✅ Response header validation
