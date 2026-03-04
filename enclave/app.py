import sys
from risk_engine import calculate_risk
from crypto_utils import encrypt, decrypt


def main():

    encrypted_input = sys.stdin.read().strip()

    if not encrypted_input:
        print("No input provided")
        return

    data = decrypt(encrypted_input)

    result = calculate_risk(data)

    encrypted_result = encrypt(result)

    print(encrypted_result)


if __name__ == "__main__":
    main()
    