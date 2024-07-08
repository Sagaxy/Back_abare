from icecream import ic

from logs.logger import Logger
from models.auth import LoginRequest, Authentication
from utils.mock_data_loader import read_mock_data


class Authenticator:
    def __init__(self, logger: Logger = None) -> None:
        """
        Initialize the authenticator
        """
        if logger:
            self.logger = logger
            self.logger.info("Authenticator instance created.")

    def authenticate_login(self, login_user_request: LoginRequest) -> bool:
        """
        Authenticate the login request
        """
        self.logger.info(f"Authenticating user with email: {login_user_request.email} with password: {login_user_request.password}")
        # [TODO] Implement authentication logic here with JWT and password hashing and real database query
        mock_users = read_mock_data(f"users.json", logger=self.logger)
        for user_type, users in mock_users.items():
            for user in users:
                if login_user_request.email == user["email"] and login_user_request.password == user["password"]:
                    self.logger.info(f"User email and password matched: {login_user_request.email}, user type: {user_type}")
                    return Authentication(access_type=int(user["access_type"]), user_id=int(user["id"]))
        raise ValueError("Invalid credentials")


