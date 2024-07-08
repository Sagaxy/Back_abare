from logs.logger import Logger


def read_mock_data(file_name: str, mock_data_path: str = "data/mock/", logger: Logger = None) -> dict:
    """
    Read the json mock data from the file into a dictionary
    """
    try:
        with open(f"{mock_data_path}{file_name}", 'r') as file:
            data = eval(file.read())
            if logger:
                logger.info(f"Read mock data from file: {file_name}")
            return data
    except Exception as e:
        if logger:
            logger.error(f"Failed to read mock data from file: {file_name}")
        print(f"Failed to read mock data from file: {file_name}, error: {str(e)}")