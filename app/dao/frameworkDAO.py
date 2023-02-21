# Создаю ДАО для работы с базой данных
from app.dao.model.framework import FrameworkModel


# Класс для работы с моделью FrameworkModel в базе данных
class FrameworkDAO:
    def __init__(self, session):
        self.session = session

    # Метод для получения всех объектов модели Фреймворк из базы данных
    def get_all(self):
        return self.session.query(FrameworkModel).all()

    # Метод для получения объектов модели Фреймворк отфильтрованных по названию языка из базы данных
    def get_on_language(self, language):
        return self.session.query(FrameworkModel).filter(FrameworkModel.language == language)
