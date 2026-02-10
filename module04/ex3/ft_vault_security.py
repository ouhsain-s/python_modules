def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        with open("classified_data.txt", "r") as file1:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for chr in file1.read():
                print(chr, end="")
    except FileNotFoundError as e:
        e = "//"
        print("ERROR:", e)
    try:
        with open("security_protocols.txt", "r") as file2:
            print("SECURE PRESERVATION:")
            file2.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
    except:
        e = "//"
        print("ERROR:", e)


if __name__ == "__main__":
    main()
