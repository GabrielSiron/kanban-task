from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from apiflask import abort

class Session_(scoped_session):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
    
    def commit(self, *args, **kwargs):
        success = True
        
        try:
            super().commit(*args, **kwargs)
        except:
            self.rollback(*args, **kwargs)
            success = False
        finally:
            self.close()

        return success
        
db = SQLAlchemy()
db.session = Session_()
            
