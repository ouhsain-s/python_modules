import os
import sys
try:
    from dotenv import load_dotenv
except ModuleNotFoundError as e:
    print(e)
    sys.exit(1)


def load_configuration():
    if os.path.exists(".env"):
        load_dotenv(".env")

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", "Not configured"),
        "API_KEY": os.getenv("API_KEY", "Not configured"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "Not configured"),
    }
    if config["MATRIX_MODE"] != "production":
        config["MATRIX_MODE"] = "development"
    return config


def check_security(config):
    checks = []

    if config["API_KEY"] == "Not configured" or config["API_KEY"] != "key":
        checks.append("[OK]  No hardcoded secrets detected")
    else:
        checks.append("[WARNING] hardcoded secrets detected")

    if os.path.exists(".env"):
        checks.append("[OK] .env file properly configured")
    else:
        checks.append("[WARNING] .env file missing")

    if os.getenv("MATRIX_MODE") or os.getenv("API_KEY"):
        checks.append("[OK] Production overrides available")
    else:
        checks.append("[WARNING] No environment overrides detected")

    return checks


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {config['DATABASE_URL']}")
    print(f"API Access: {'Authenticated' if config['API_KEY'] != 'Not\
                          configured' else 'Not configured'}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}\n")

    print("Environment security check:")
    for check in check_security(config):
        print(check)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
