from logs.logger import Logger
from models.users import UserAbbreviated, UsersAbbreviated, UserDetails
from utils.mock_data_loader import read_mock_data


class UsersController:
    def __init__(self, logger: Logger = None) -> None:
        """
        Initialize the users controller
        """
        if logger:
            self.logger = logger
            self.logger.info("Users controller instance created.")

    def get_users(self) -> UsersAbbreviated:
        """
        Get brief information about all users in database
        """
        self.logger.info("Reading all users")
        users_data = read_mock_data("users.json", logger=self.logger)
        users = []
        for user_type in users_data:
            for user_data in user_type:
                user = UserAbbreviated(user_data)
                users.append(user)
        return UsersAbbreviated(users)

    def get_user(self, user_id: int) -> UserAbbreviated:
        self.logger.info("Reading all users and seeking for one")
        users_data = read_mock_data("users.json", logger=self.logger)
        for user_type in users_data:
            for user_data in users_data:
                if user_data["id"] == user_id:
                    return UserAbbreviated(user_data)
        
    def get_user_with_details(self, user_id: int) -> UserDetails:
        self.logger.info("Reading all users and seeking for one")
        users_data = read_mock_data("users.json", logger=self.logger)
        for user_type in users_data:
            for user_data in users_data:
                if user_data["id"] == user_id:
                    return UserAbbreviated(user_data)