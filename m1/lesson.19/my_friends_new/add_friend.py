def add_f(friend_list, friend_name):
    """Добавляет друга в список друзей."""
    if friend_name not in friend_list:
        friend_list.append(friend_name)
        return f"{friend_name} добавлен в список друзей."
    return f"{friend_name} уже есть в списке друзей."


PI = 3.14
