def main() -> None:

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        file1 = open("ancient_fragment.txt", "r")
        print("Accessing Storage Vault:", file1.name)
        print("Connection established...\n")
        print("RECOVERED DATA:")
        for chr in file1.read():
            print(chr, end="")
        print("\n\nData recovery complete. Storage unit disconnected.")
        file1.close()
    except FileNotFoundError as e:
        e = "Storage vault not found. Run data generator first."
        print("ERROR:", e)


if __name__ == "__main__":
    main()
