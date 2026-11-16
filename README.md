# Django models relationships

A Django project with 4 models.

## Tech stack

- Python 3
- Django
- Database: SQLite

## Project structure

- `book_project/`: project settings and root URLs
- `book_app/`: Django app
- Tests: `book_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Address` | `book_app` | number, street, city, state, country, postalCode |
| `Editor` | `book_app` | name, email, website, telephoneNumber, address |
| `Book` | `book_app` | esbnCode, title, price, releaseDate, summary, editor |
| `Author` | `book_app` | name, email, photo, writing |

## URL routes

Declared in `urls.py`:

- `/blog/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
