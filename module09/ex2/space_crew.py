from __future__ import annotations
import warnings
from enum import Enum
from datetime import datetime
from typing import List
warnings.filterwarnings("error")
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print("Error: 'pydantic' Module is NotFound")
    exit(0)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=2, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = datetime.now()
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_rules(self) -> SpaceMission:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")
        if not any([crew.rank in [Rank.COMMANDER, Rank.CAPTAIN] for crew in
                    self.crew]):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            crew_half = len(self.crew) // 2
            exp_crew = len([m for m in self.crew if m.years_experience >= 5])
            if crew_half >= exp_crew:
                raise ValueError("Long missions (> 365 days) need 50% \
experienced crew (5+ years)")
        if not all([m.is_active for m in self.crew]):
            raise ValueError("All crew members must be active")

        return self


def print_info(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - \
{member.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    try:
        sarah = CrewMember(member_id="SARAH001", name="Sarah Connor",
                           rank=Rank.COMMANDER,
                           specialization="Mission Command",
                           years_experience=8, age=30)
        john = CrewMember(member_id="JOHN001", name="John Smith",
                          rank=Rank.LIEUTENANT,
                          specialization="Navigation",
                          years_experience=3, age=36)
        alice = CrewMember(member_id="ALICE001", name="Alice Johnson",
                           rank=Rank.OFFICER,
                           specialization="Engineering",
                           years_experience=8, age=36)
        valid_mission = SpaceMission(mission_id="M2024_MARS",
                                     mission_name="Mars Colony Establishment",
                                     destination="Mars", duration_days=900,
                                     crew=[sarah, john, alice],
                                     budget_millions=2500.0)
        print_info(valid_mission)
    except UserWarning as w:
        print(w)
    except ValidationError as e:
        print(e.errors()[0]['msg'].split(',')[1][1:])
    print("\n=========================================")
    print("Expected validation error:")
    try:
        alex = CrewMember(member_id="ALEX001", name="Alex Connor",
                          rank=Rank.LIEUTENANT,
                          specialization="Mission Command",
                          years_experience=5, age=30)
        remy = CrewMember(member_id="REMY001", name="Remy Smith",
                          rank=Rank.LIEUTENANT,
                          specialization="Navigation",
                          years_experience=5, age=36)
        david = CrewMember(member_id="DAVID001", name="David Johnson",
                           rank=Rank.OFFICER,
                           specialization="Engineering",
                           years_experience=8, age=36)
        valid_mission = SpaceMission(mission_id="M2024_MARS",
                                     mission_name="Mars Colony Establishment",
                                     destination="Mars", duration_days=900,
                                     crew=[alex, remy, david],
                                     budget_millions=2500.0)
        print_info(valid_mission)
    except UserWarning as w:
        print(w)
    except ValidationError as e:
        print(e.errors()[0]['msg'].split(',')[1][1:])


if __name__ == "__main__":
    main()
