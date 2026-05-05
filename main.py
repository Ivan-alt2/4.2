def decode_string(s: str) -> str:

# ID успешной попытки: 161571272	

    def decode_recursive(index: int) -> tuple[str, int]:
        result = []
        current_num = 0

        while index < len(s):
            char = s[index]

            if char.isdigit():
                current_num = current_num * 10 + int(char)
                index += 1

            elif char == '[':
                substring, next_index = decode_recursive(index + 1)
                result.append(substring * current_num)
                current_num = 0
                index = next_index

            elif char == ']':
                return ''.join(result), index + 1

            else:
                result.append(char)
                index += 1

        return ''.join(result), index

    decoded_string, _ = decode_recursive(0)
    return decoded_string


if __name__ == "__main__":
    compressed_input = input().strip()
    print(decode_string(compressed_input))
