"""Weather App core logic.

This module focuses on **parsing and presenting** weather data returned from
a weather API. To keep tests reliable and offline-friendly, the HTTP client
is not hard-coded; instead, parsing logic is pure and easily testable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class WeatherInfo:
    city: str
    temperature_c: float
    condition: str
    humidity: int
    wind_kph: float


def parse_weather_response(data: Dict[str, Any]) -> WeatherInfo:
    """Parse a minimal JSON-like dict into WeatherInfo.

    Expected input format (example)::

        {
            "location": {"name": "London"},
            "current": {
                "temp_c": 12.3,
                "condition": {"text": "Partly cloudy"},
                "humidity": 81,
                "wind_kph": 14.4,
            },
        }

    This structure is similar to many public weather APIs.
    """

    location = data.get("location", {})
    current = data.get("current", {})
    condition = current.get("condition", {})

    return WeatherInfo(
        city=str(location.get("name", "Unknown")),
        temperature_c=float(current.get("temp_c", 0.0)),
        condition=str(condition.get("text", "Unknown")),
        humidity=int(current.get("humidity", 0)),
        wind_kph=float(current.get("wind_kph", 0.0)),
    )


def format_weather(info: WeatherInfo) -> str:
    """Format WeatherInfo into a human-readable string."""
    return (
        f"Weather for {info.city}: {info.condition}, "
        f"{info.temperature_c:.1f}°C, humidity {info.humidity}% "
        f"with wind {info.wind_kph:.1f} km/h"
    )


def run_demo() -> None:
    """Run a small demo using hard-coded sample data."""
    sample = {
        "location": {"name": "Demo City"},
        "current": {
            "temp_c": 21.5,
            "condition": {"text": "Sunny"},
            "humidity": 40,
            "wind_kph": 10.0,
        },
    }
    info = parse_weather_response(sample)
    print(format_weather(info))


if __name__ == "__main__":
    run_demo()
