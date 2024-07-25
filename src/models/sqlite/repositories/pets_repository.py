from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    # List da lib typing é do python 3.8 pra baixo
    def list_pets(self) -> list[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
