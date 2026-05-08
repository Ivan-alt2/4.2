# ID успешной попытки: 161671605

BASE_NUMERAL_SYSTEM = 10

def decode_string(encoded_str: str) -> str:
    stack = []
    current_result = []
    current_number = 0

    for char in encoded_str:
        if char.isdigit():
            current_number = current_number * BASE_NUMERAL_SYSTEM + int(char)
        elif char == '[':
            stack.append((''.join(current_result), current_number))
            current_result = []
            current_number = 0
        elif char == ']':
            previous_result, repeat_count = stack.pop()
            current_result = [previous_result + ''.join(current_result) * repeat_count]
        else:
            current_result.append(char)

    return ''.join(current_result)

def main() -> None:
    compressed_input = input().strip()
    decoded_output = decode_string(compressed_input)
    print(decoded_output)

if __name__ == "__main__":
    main()
