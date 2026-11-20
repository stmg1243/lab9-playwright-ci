import pytest

BASE_URL = "http://127.0.0.1:8000/delivery.html"


@pytest.fixture
def app(page):
    """Открывает страницу расчёта доставки."""
    page.goto(BASE_URL)
    return page
