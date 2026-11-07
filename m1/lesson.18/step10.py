def add_key(my_dict: dict, key: str, value: str) -> dict:
    if key in my_dict:
        raise KeyError(f"Ключ уже существует. Нельзя его перезаписывать. Текущее значение: {my_dict.get(key)}")
    my_dict[key] = value
    return my_dict


data = {
    "one": "один",
    "two": "два",
    "three": "три",
}

print(data)

add_key(data, "four", "четыре")
print(data)


add_key(data, "four", "четыре1")
print(data)