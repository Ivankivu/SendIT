class User():

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.role = kwargs.get('role')
