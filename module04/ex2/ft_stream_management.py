import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Enter archivist ID: ")
    status = input("Enter status report: ")
    sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels"
                     " verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
