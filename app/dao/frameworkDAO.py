from app.dao.model.framework import FrameworkModel


class FrameworkDAO:
    def __init__(self, session):
        self.session = session

    def get(self):
        return self.session.query(FrameworkModel)

    def get_on_language(self, language):
        return self.session.query(FrameworkModel).filter(FrameworkModel.language == language)