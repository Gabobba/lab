from string import ascii_lowercase

def removeDuplicate(s1: str) -> str:
    seen = set()
    return "".join(chr for chr in s1 if not (chr in seen or seen.add(chr)))

def generate_alphabets(keyword: str) -> str:
    charactersInKeyword = removeDuplicate(keyword.lower())
    alphabetWithoutKeyword = "".join(chr for chr in ascii_lowercase if chr not in charactersInKeyword)[::-1]
    return charactersInKeyword + alphabetWithoutKeyword

def encrypt_text(text: str, keyword: str) -> str:
    alphabet = ascii_lowercase
    encryptionAlphabet = generate_alphabets(keyword)
    encrypt_dict = {alphabet[i]: encryptionAlphabet[i] for i in range(len(alphabet))}

    result = []
    for chr in text:
        if chr.isalpha():
            is_upper = chr.isupper()
            result.append(encrypt_dict[chr.lower()].upper() if is_upper else encrypt_dict[chr.lower()])
        else:
            result.append(chr)
    return "".join(result)

def decrypt_text(text: str, keyword: str) -> str:
    alphabet = ascii_lowercase
    encryptionAlphabet = generate_alphabets(keyword)
    decrypt_dict = {encryptionAlphabet[i]: alphabet[i] for i in range(len(alphabet))}

    result = []
    for chr in text:
        if chr.isalpha():
            is_upper = chr.isupper()
            result.append(decrypt_dict[chr.lower()].upper() if is_upper else decrypt_dict[chr.lower()])
        else:
            result.append(chr)
    return "".join(result)

def process_file(input_filename: str, output_filename: str, keyword: str, operation: int) -> None:
    try:
        with open(input_filename, "r", encoding="UTF-8") as infile, \
             open(output_filename, "w", encoding="UTF-8") as outfile:
            text = infile.read()
            if operation == 1:
                result = encrypt_text(text, keyword)
            elif operation == 2:
                result = decrypt_text(text, keyword)
            else:
                raise ValueError("Invalid operation. Choose 1 for encryption or 2 for decryption.")
            outfile.write(result)
            print(f"{'Encryption' if operation == 1 else 'Decryption'} completed successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: Missing key during decryption. {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    try:
        keyword = input("What is the decrypting/encrypting keyword? ").strip()
        if not keyword.isalpha() or not keyword:
            raise ValueError("The keyword must contain only letters and cannot be empty.")

        operationToExecute = int(input("What would you like to do? Encrypt (press 1) a file or Decrypt (press 2)? "))
        if operationToExecute not in [1, 2]:
            raise ValueError("Invalid operation. Enter 1 for encryption or 2 for decryption.")
        
        inputFileName = input("What is the input file name? ").strip()
        outputFileName = input("What is the output file name? ").strip()

        process_file(inputFileName, outputFileName, keyword, operationToExecute)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
