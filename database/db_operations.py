class DbOperation:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.connection = None
        