def chars_list() -> list[str]:
    chars = [str(i) for i in range(26)]
    return chars


def counter(chars: list, text: str) -> list[int]:
    counts = [text.count(i) for i in chars]
    return counts


f = open("./message.txt", "r")
chars = chars_list()
print(counter(chars, f.read()))
