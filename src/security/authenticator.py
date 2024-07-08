from icecream import ic

from logs.logger import Logger
from models.auth import LoginRequest, Authentication


class Authenticator:
    mock_data_path = "data/mock/"

    def __init__(self, logger: Logger = None) -> None:
        """
        Initialize the authenticator
        """
        if logger:
            self.logger = logger
            self.logger.info("Authenticator instance created.")

    def read_mock_data(self, file_name: str) -> dict:
        """
        Read the json mock data from the file
        """
        try:
            with open(f"{self.mock_data_path}{file_name}", 'r') as file:
                # read json into dictionary
                data = eval(file.read())
                self.logger.info(f"Read mock data from file: {file_name}")
                return data
        except Exception as e:
            self.logger.error(f"Failed to read mock data from file: {file_name}")

    def authenticate_login(self, login_user_request: LoginRequest) -> bool:
        """
        Authenticate the login request
        """
        self.logger.info(f"Authenticating user with email: {login_user_request.email} with password: {login_user_request.password}")
        # [TODO] Implement authentication logic here with JWT and password hashing and real database query
        mock_users = self.read_mock_data(f"users.json")
        for user_type, users in mock_users.items():
            for user in users:
                if login_user_request.email == user["email"] and login_user_request.password == user["password"]:
                    self.logger.info(f"User email and password matched: {login_user_request.email}, user type: {user_type}")
                    return Authentication(access_type=int(user["access_type"]), user_id=int(user["id"]))
        raise ValueError("Invalid credentials")


