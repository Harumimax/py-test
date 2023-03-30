def is_user_exist(login, list_of_user):
    for current_user in list_of_user:
        if current_user.login == login:
            return True
    return False
