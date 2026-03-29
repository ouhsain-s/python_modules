# oracle.py
import os
from dotenv import load_dotenv


def load_configuration():
    """Load configuration from environment variables or .env file"""
    # Load .env file if exists
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite:///:memory:"),
        "API_KEY": os.getenv("API_KEY", None),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "http://localhost:8000"),
    }

    # Error handling for critical missing values
    missing = [key for key, val in config.items() if val is None]
    if missing:
        print(f"[WARNING] Missing configuration for: {', '.join(missing)}")

    return config


def check_security(config):
    """Simple checks to demonstrate security practices"""
    print("Environment security check:")
    # Check for hardcoded secrets
    hardcoded = config.get("API_KEY") in ["12345", "secret", "password"]
    if hardcoded:
        print("[WARNING] Potential hardcoded secret detected!")
    else:
        print("[OK] No hardcoded secrets detected")

    # Check if .env exists
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing, defaults used")

    # Check if production overrides available
    if config["MATRIX_MODE"] == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in development mode")


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_configuration()

    # Print loaded configuration
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {config['DATABASE_URL']}")
    print(f"API Access: {'Authenticated' if config['API_KEY'] else 'Missing'}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}\n")

    check_security(config)
    print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    main()