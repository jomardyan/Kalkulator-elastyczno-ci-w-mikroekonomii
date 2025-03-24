import pytest
from calculator_ec import (
    oblicz_elastycznosc,
    oblicz_elastycznosc_cenowa,
    oblicz_elastycznosc_dochodowa,
    oblicz_elastycznosc_cenowa_krzyzowa,
    pobierz_kurs_wymiany
)

def test_oblicz_elastycznosc_cenowa():
    elastycznosc, opis = oblicz_elastycznosc("cenowa", 100, 120, 50, 60)
    assert elastycznosc == 1.0
    assert opis == "Jednostkowa elastyczność"

def test_oblicz_elastycznosc_dochodowa():
    elastycznosc, opis = oblicz_elastycznosc("dochodowa", 1000, 1200, 50, 60)
    assert elastycznosc == 1.0
    assert opis == "Dobro luksusowe"

def test_oblicz_elastycznosc_cenowa_krzyzowa():
    elastycznosc, opis = oblicz_elastycznosc("krzyzowa", 100, 120, 50, 60)
    assert elastycznosc == 1.0
    assert opis == "Substytuty"

def test_pobierz_kurs_wymiany(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {"rates": {"PLN": 4.0}}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    kurs = pobierz_kurs_wymiany()
    assert kurs == 4.0
