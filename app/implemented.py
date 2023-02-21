from app.dao.frameworkDAO import FrameworkDAO
from app.dao.model.framework import FrameworkSchema
from app.db_setup import db
from app.service.frameworkSERVICE import FrameworkService

framework_dao = FrameworkDAO(db.session)
framework_service = FrameworkService(framework_dao)
frameworks_schema = FrameworkSchema(many=True)
