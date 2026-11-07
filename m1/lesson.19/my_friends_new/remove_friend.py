def remove_f(friend_list, friend_name):
    """Удаляет друга из списка друзей."""
    if friend_name in friend_list:
        friend_list.remove(friend_name)
        return f"{friend_name} удален из списка друзей."
    return f"{friend_name} не найден в списке друзей."

