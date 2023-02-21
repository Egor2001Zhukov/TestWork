from flask_restx import Namespace, Resource

from app.implemented import framework_service, frameworks_schema

framework_ns = Namespace('frameworks')

@framework_ns.route('/')
class FrameworksView(Resource):
    def get(self):
        return frameworks_schema.dump(framework_service.get())


@framework_ns.route('/<string:language>')
class FrameworkView(Resource):
    def get(self, language):
        return frameworks_schema.dump(framework_service.get_on_language(language))
