import pytest
from playwright.sync_api import expect


def calculate(page, amount, delivery):
    page.fill("#amount", amount)
    page.select_option("#delivery", delivery)
    page.click("#calc")


# 9 тестов: корректные суммы, включая границу 10000 для city и region
@pytest.mark.parametrize(
    "delivery, amount, expected_cost",
    [
        ("city", "5000", 500),
        ("region", "5000", 1500),
        ("city", "9999", 500),
        ("region", "9999", 1500),
        ("city", "10000", 0),
        ("region", "10000", 0),
        ("city", "10001", 0),
        ("region", "10001", 0),
        ("region", "20000", 0),
    ],
)
def test_delivery_cost(app, delivery, amount, expected_cost):
    calculate(app, amount, delivery)
    expect(app.locator("#result")).to_have_text(f"Стоимость доставки: {expected_cost} ₸")
    expect(app.locator("#error")).to_have_text("")


# 3 теста: некорректный ввод
@pytest.mark.parametrize("amount", ["", "-100", "0"])
def test_invalid_amount(app, amount):
    calculate(app, amount, "city")
    expect(app.locator("#error")).to_have_text("Введите корректную сумму заказа")
    expect(app.locator("#result")).to_have_text("")
