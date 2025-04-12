class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        print(f"Connecting to {self.database} at {self.host} as {self.user}")
        return True

    def disconnect(self):
        print(f"Disconnecting from {self.database}")
        return True