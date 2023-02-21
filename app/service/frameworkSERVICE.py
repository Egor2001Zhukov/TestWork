# Создаю сервисы для управления бизнес логикой в приложении, но пока здесь пусто, так сказать заготовка)
class FrameworkService:
    def __init__(self, dao):
        self.dao = dao

    # Метод для работы с ДАО, тут могла быть ваша бизнес логика
    def get_all(self):
        return self.dao.get_all()

    # Метод для работы с ДАО, тут могла быть ваша бизнес логика
    def get_on_language(self, language):
        return self.dao.get_on_language(language)
