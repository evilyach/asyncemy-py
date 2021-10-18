import databases
from sqlalchemy import create_engine, MetaData


MODE = "postgres"
URL = "postgresql://postgres:postgres@localhost/ipavlov"
# MODE = "sqlite"
# URL = "sqlite:///./ipavlov.sqlite"


database = databases.Database(URL)
engine = create_engine(
    URL,
    connect_args={"check_same_thread": False}
) if MODE == "sqlite" else create_engine(
    URL
)
metadata = MetaData()
