from typing import List

# ID успешной попытки: 12345678

def calculate_min_platforms(weights: List[int], limit: int) -> int:
    sorted_weights = sorted(weights)
    platforms = 0
    left = 0
    right = len(sorted_weights) - 1

    while left <= right:
        if sorted_weights[left] + sorted_weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms


def main() -> None:
    weights_input = list(map(int, input().split()))
    limit_input = int(input())

    result = calculate_min_platforms(weights_input, limit_input)

    print(result)


if __name__ == "__main__":
    main()
