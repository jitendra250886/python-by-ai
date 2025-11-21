import pytest

from weather_app.src import main as weather_main  # type: ignore[import]


def test_parse_weather_response_basic() -> None:
    payload = {
        "location": {"name": "London"},
        "current": {
            "temp_c": 15.2,
            "condition": {"text": "Cloudy"},
            "humidity": 70,
            "wind_kph": 8.5,
        },
    }
    info = weather_main.parse_weather_response(payload)
    assert info.city == "London"
    assert info.temperature_c == pytest.approx(15.2)
    assert info.condition == "Cloudy"
    assert info.humidity == 70
    assert info.wind_kph == pytest.approx(8.5)


def test_parse_weather_response_defaults() -> None:
    payload = {}
    info = weather_main.parse_weather_response(payload)
    assert info.city == "Unknown"
    assert info.temperature_c == 0.0
    assert info.condition == "Unknown"
    assert info.humidity == 0
    assert info.wind_kph == 0.0


def test_format_weather_output() -> None:
    info = weather_main.WeatherInfo(
        city="Test City",
        temperature_c=10.0,
        condition="Rain",
        humidity=90,
        wind_kph=5.0,
    )
    text = weather_main.format_weather(info)
    assert "Test City" in text
    assert "Rain" in text
    assert "10.0°C" in text
