def singleton(cl):
    instances = {} # diccionario
    def envoltura(*args, **kwargs): # arguments and dictionary of arguments
        if cl not in instances:
            instances[cl] = cl(*args, **kwargs)
        return instances[cl]
    return envoltura

@singleton # decorator
class User(object):
    def __init__(self, username):
        self.username = username

if __name__ == '__main__':
    user = User('admin')
    user2 = User('guest')
    print(user is user2)