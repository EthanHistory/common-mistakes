from source.database import Database

class UserService:
    def __init__(self):
        self.db = Database()
    
    def get_user(self, user_id):
        result = self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
        return result