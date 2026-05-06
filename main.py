def decode_string(encoded_str: str) -> str:
   
# ID успешной попытки: 161571272
    
    BASE_NUMERAL_SYSTEM = 10

    result_stack = []
    count_stack = []
    current_result = []
    current_num = 0

    for char in encoded_str:
        if char.isdigit():
            current_num = current_num * BASE_NUMERAL_SYSTEM + int(char)
        elif char == '[':
            count_stack.append(current_num)
            result_stack.append(''.join(current_result))
            current_num = 0
            current_result = []
        elif char == ']':
            count = count_stack.pop()
            prev_result = result_stack.pop()
            current_result = [prev_result + ''.join(current_result) * count]
        else:
            current_result.append(char)

    return ''.join(current_result)


def main() -> None:
    compressed_input = input().strip()
    decoded_output = decode_string(compressed_input)
    print(decoded_output)


if __name__ == "__main__":
    main()
