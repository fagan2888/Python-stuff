import inspect
class CtagsDatabase():
    def __init__(self):
        self.records = []
        self.views = [] 

    def add_view(self, view):
        view.clear()
        for record in self.records:
            view.on_new_record(record)
        self.views.append(view)

    def load(self, fl):
        self.fl = open(fl)
        for view in self.views:
            view.clear()
        
        for line in self.fl:
            line = line.strip()
            if line[0] == "!":
                continue
            words = line.split('\t')
            tag_name = words[0]
            file_name = words[1]
            search_pattern = words[2]
            dictionary = {"tag": tag_name, "file name": file_name, "search pattern": search_pattern}
            colon = words[3].find(':')
            kind_type = len(words[3])
            starter = 3

            if colon == -1 and kind_type == 1:
                dictionary["kind"] = words[3]
                starter = 4

            elif colon == -1 and kind_type > 1:
                dictionary["KIND"] = words[3]
                starter = 4

            for i in range(starter, len(words)):
                colon = words[i].find(':')
                field = words[i][:colon]
                dictionary[field]= words[i][colon+1:]
                self.records.append(dictionary)
            for view in self.views:
                view.on_new_record(line)
            

