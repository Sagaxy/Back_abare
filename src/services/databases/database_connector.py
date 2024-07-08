import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from logs.logger import Logger


Base = declarative_base()


class DatabaseConnector:
    db_connector_instance = None

    def __init__(self, user = None, password = None, host = None, port = None, db_name = None, db_url = None, logger: Logger = None):
        """
        Initialize the database connection
        """
        if DatabaseConnector.db_connector_instance is None:
            try:
                self.logger = logger
                if (user == None or password == None or host == None or port == None or db_name == None) and (db_url == None):
                    self.logger.error("Database connection failed due to missing connection details.")
                    raise ValueError("Please provide either the database connection details or the database URL.")
                if db_url is None:
                    db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
                self.logger.info(f"Database URL: {db_url}")
                self.engine = sa.create_engine(db_url)
                self.Session = scoped_session(sessionmaker(bind=self.engine))
                self.logger.info("Database connection established successfully.")
            except Exception as e:
                self.logger.error(f"Database connection failed: {str(e)}")
                raise e
            DatabaseConnector.db_connector_instance = self
        else:
            self.logger = DatabaseConnector.db_connector_instance.logger
            self.engine = DatabaseConnector.db_connector_instance.engine
            self.Session = DatabaseConnector.db_connector_instance.Session

    def create_tables(self):
        """
        Create tables in the database
        """
        try:
            self.logger.info("Creating tables...")
            Base.metadata.create_all(self.engine)
            self.logger.info("Tables created successfully.")
        except Exception as e:
            self.logger.error(f"Failed to create tables: {str(e)}")

    def drop_tables(self):
        """
        Drop tables from the database
        """
        try:
            self.logger.info("Dropping tables...")
            Base.metadata.drop_all(self.engine)
            self.logger.info("Tables dropped successfully.")
        except Exception as e:
            self.logger.error(f"Failed to drop tables: {str(e)}")

    def recreate_tables(self):
        """
        Recreate tables in the database
        """
        self.drop_tables()
        self.create_tables()

    def get_session(self):
        """
        Get a session object
        """
        self.logger.debug("Session fetched.")
        return self.Session()

    def query_data(self, model):
        """
        Query data from the database
        """
        with self.Session() as session:
            try:
                data = session.query(model).all()
                self.logger.info(f"Data queried successfully: {len(data)} records found.")
                return data
            except Exception as e:
                self.logger.error(f"Failed to query data: {str(e)}")
                raise e