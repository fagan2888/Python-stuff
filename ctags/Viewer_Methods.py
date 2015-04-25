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

#class InheritsView(View):
#    def __init__(self):
#        MainView.addview(self)
#
#    def run(self, database):
#        self.database = database
#        classes = []
#        inheriters = []
#        for i in self.database:
#            if "KIND" in i:
#                if i["KIND"] == "class":
#                    main_class = i["tag"]
#                    classes.append(main_class)


db = Database.CtagsDatabase()
db.load('./tags')
tags_view = TagsView(db)
print(tags_view.info)
for i in tags_view.info:
    if "Busy" in i:
        print(i["Busy"])
        for x in i["Busy"]:
            print(db.records[x])
