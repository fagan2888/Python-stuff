import abc
class View():
    def __init__(self, db):
        db.add_view(self)

    @abc.abstractmethod
    def clear(self):
        pass
    @abc.abstractmethod    
    def on_new_record(self, record):
        pass
