def read_file(fname: str) -> None:
    try:
        with open(fname, "r") as file1:
            print(f"SUCCESS: Archive recovered - ``{file1.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    read_file("lost_archive.txt")
    print(end="\n")
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    read_file("classified_vault.txt")
    print(end="\n")
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    read_file("standard_archive.txt")
    print(end="\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
