def main():
    discovered = ["[ENTRY 001] New quantum algorithm discovered\n",
                  "[ENTRY 002] Efficiency increased by 347%\n",
                  "[ENTRY 003] Archived by Data Archivist trainee\n"]
    file1 = open("new_discovery.txt", "w")
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {file1.name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    for line in discovered:
        file1.write(line)
        print(line, end="")
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file1.name}' ready for long-term preservation.")
    file1.close()


if __name__ == "__main__":
    main()
