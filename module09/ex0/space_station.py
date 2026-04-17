from datetime import datetime
from typing import Optional
try:
    from pydantic import BaseModel, Field, ValidationError
except ModuleNotFoundError:
    print("Error: 'pydantic' Module is NotFound")
    exit(0)


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-03-31T10:00:00",
        )
    except ValidationError as e:
        print("Expected validation error:")
        first_error = e.errors()[0]
        print(first_error["msg"].split(',')[1][1:])

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if station.is_operational:
        s = 'Operational'
    else:
        s = 'Non-operational'
    print(f"Status: {s}")
    print("\n========================================")

    try:
        SpaceStation(
            station_id="BAD001",
            name="Broken Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance="2026-03-31T10:00:00",
        )
    except ValidationError as e:
        print("Expected validation error:")
        first_error = e.errors()[0]
        print(first_error["msg"])


if __name__ == "__main__":
    main()
