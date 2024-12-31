import unittest
from unittest.mock import patch
from source.user_service import UserService

class TestUserService(unittest.TestCase):
    # ❌ WRONG WAY - using the path where Database is defined
    @patch('source.database.Database')
    def test_get_user_wrong(self, MockDatabase):
        # This won't work! The UserService will still create a real Database
        mock_db = MockDatabase()
        mock_db.query.return_value = {"id": 1, "name": "Test User"}
        
        service = UserService()
        user = service.get_user(1)
        
        mock_db.query.assert_called_once()  # This will fail!

    # ✅ CORRECT WAY - using the path where Database is imported
    @patch('source.user_service.Database')
    def test_get_user_correct(self, MockDatabase):
        # This works! The mock intercepts Database creation in UserService
        mock_db = MockDatabase()
        mock_db.query.return_value = {"id": 1, "name": "Test User"}
        
        service = UserService()
        user = service.get_user(1)
        
        mock_db.query.assert_called_once()
        
        mock_db.query.assert_called_once_with(
            "SELECT * FROM users WHERE id = 1"
        )

if __name__ == '__main__':
    unittest.main()