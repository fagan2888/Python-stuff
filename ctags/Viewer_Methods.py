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

class InheritsView(View):
    def __init__(self, db):
        self.inheriters = []
        self.classes = []
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
        if "inherits" in record and record["inherits"] != '':
            inherit = {record["tag"]:record["inherits"]}
            self.inheriters.append(inherit)

db = Database.CtagsDatabase()
db.load('./tags')
tags_view = TagsView(db)
inherits_view = InheritsView(db)
print(inherits_view.inheriters)
print(inherits_view.classes)

for i in tags_view.info:
    if "Turing" in i:
        print(i["Turing"])
        for x in i["Turing"]:
            print(db.records[x])
