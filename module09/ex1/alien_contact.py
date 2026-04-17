from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
import warnings
warnings.filterwarnings("error")
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print("Error: 'pydantic' Module is NotFound")
    exit(0)


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self) -> AlienContact:
        if not self.contact_id.startswith("AC"):
            raise ValueError('contact_id must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError("Telepathic contact"
                             " requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")

        return self


def print_contact_report(contact: AlienContact) -> None:
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received!r}")


def demo_valid_contact() -> None:
    valid_contact_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-10-31T22:15:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False,
    }

    try:
        contact = AlienContact(**valid_contact_data)
        print_contact_report(contact)
    except UserWarning as w:
        print(w)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].split(',')[1][1:])


def demo_invalid_contact() -> None:
    invalid_contact_data = {
        "contact_id": "AC_TELE_01",
        "timestamp": "2024-10-31T23:00:00",
        "location": "Desert site",
        "contact_type": "telepathic",
        "signal_strength": 4.2,
        "duration_minutes": 12,
        "witness_count": 2,
        "message_received": None,
        "is_verified": False,
    }

    try:
        AlienContact(**invalid_contact_data)
    except UserWarning as w:
        print(w)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].split(',')[1][1:])


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)
    print()

    demo_valid_contact()
    print()
    print("=" * 38)
    demo_invalid_contact()


if __name__ == "__main__":
    main()
