import logging
from sqlalchemy import create_engine
from config import CONFIG
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.exc import SQLAlchemyError

DEFAULT_DB_ENGINE = create_engine(CONFIG.DB.url, echo=True)

DEFAULT_SESSION_FACTORY = sessionmaker(bind=DEFAULT_DB_ENGINE)

logger = logging.getLogger("uvicorn")


class SqlAlchemyUnitOfWork:
    session_factory: sessionmaker
    session: Session

    def __init__(self, session_fatory: sessionmaker = DEFAULT_SESSION_FACTORY):
        super().__init__()
        self.session_factory = session_fatory
        self.session = None

    def __enter__(self):
        self.session: scoped_session = scoped_session(self.session_factory)
        return self.session

    def __exit__(self, exception_type, exception_value, traceback):
        self.session.close()

        if exception_type and issubclass(exception_type, SQLAlchemyError):
            logger.error(
                "Erro ORM SQLAlchemy. Tipo {}, Valor {}".format(
                    exception_type, exception_value
                ),
                exc_info=traceback,
            )
            raise SQLAlchemyError(exception_type, exception_value, traceback)
