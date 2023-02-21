class FrameworkService:
    def __init__(self, dao):
        self.dao = dao

    def get(self):
        return self.dao.get()

    def get_on_language(self, language):
        return self.dao.get_on_language(language)
