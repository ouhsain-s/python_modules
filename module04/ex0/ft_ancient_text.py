def main():
    try:
        file1 = open("ancient_fragment.txt", "r")
    except FileNotFoundError as e:
        e = "ERROR: Storage vault not found. Run data generator first."
        print(e)
        return
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault:", file1.name)
    print("Connection established...\n")
    print("RECOVERED DATA:")
    for line in file1.readlines():
        print(line, end="")
    print("\n\nData recovery complete. Storage unit disconnected.")
    file1.close()


if __name__ == "__main__":
    main()
