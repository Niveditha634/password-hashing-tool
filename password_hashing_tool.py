import bcrypt

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

def main():
    print("Password Hashing Tool")
    print("1. Hash a password")
    print("2. Verify a password")

    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        password = input("Enter the password: ")
        hashed = hash_password(password)
        print("\nHashed password:")
        print(hashed.decode("utf-8"))

    elif choice == "2":
        password = input("Enter the password: ")
        stored_hash = input("Enter stored hash: ").encode("utf-8")

        if verify_password(password, stored_hash):
            print("\nPassword is correct")
        else:
            print("\nPassword is incorrect")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
