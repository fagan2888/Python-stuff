import Database
from Viewer import View  

#Basic Syntax:
#class DebugView(View):
#    def __init__(self, db):
#        super().__init__(db)
#
#    def on_new_record(self, record):
#        do something with records 
#        
#    def clear(self):
#        clear main information 


class TagsView(View):
    def __init__(self, db):
        self.pos = -1
        self.names = []
        self.info = []
        super().__init__(db)

    def clear(self):
        try:
            self.info == None
        except AttributeError:
            pass

    def on_new_record(self, record):
        self.pos += 1
        name = record["tag"]
        try:
            if self.names.index(name) > -1:
                for i in self.info:
                    if name in i:
                        if type(i[name]) == list:
                            i[name].append(self.pos)
                        else:
                            i[name] = [i[name]]
                            i[name].append(self.pos)
        except ValueError:
            self.names.append(name)
            self.info.append({name:self.pos})

#Inherits view isn't completed
class RecordClasses(View):
    def __init__(self, db):
        self.classes = []
        self.cdb = []
        super().__init__(db)

    def clear(self):
        try:
            self.inheriters = []
            self.classes = []
        except AttributeError:
            pass


    def on_new_record(self, record):
        if "KIND" in record:
            if record["KIND"] == "class":
                main_class = record["tag"]
                self.classes.append(main_class)
        if "kind" in record:
            if record["kind"] == "c":
                main_class = record["tag"]
                self.classes.append(main_class)
        self.cdb.append(record) 


#Some messing about:
db = Database.CtagsDatabase()
db.load('./tags')
tags_view = TagsView(db)
inherits_view = RecordClasses(db)
def InheritsView():
    inherit = 0
    dic = []
    class_mapping = {}
    for ass in inherits_view.classes:
        for line in inherits_view.cdb:
            if 'inherits' in line and line['inherits'] == ass:
                try:
                    if line["tag"] in class_mapping[ass]:
                        pass
                except KeyError:
                    if ass in class_mapping:
                        class_mapping[ass] = class_mapping[ass], line["tag"]
                    else:
                        class_mapping[ass] = line["tag"]
                dic.append(class_mapping)
    print(dic)
InheritsView()
