from sys import argv
import Database_Creator as db

class View():
    def __init__(self, fl):
        self.db = db.CtagsDatabase(fl)
        self.db.addview(self)
        self.db.generate()
        question = input("\nMethod to run?\n")
        for i in self.db.methods:
            if question in i:
                i[1](fl)

    def clear(self, data):
        data = None
        
    def update(self):


class tags_view(ViewFramework):
    def __init__(self, fl):
        ViewFramework.__init__(self, fl)

    def findtag(self, tag_name):
        tags_display = input("\nDisplay tags? y/n\n")
        if tags_display == "y":
            for i in self.db.dicts:
                print(i["tag"])
        tag_name = input("\nSearch a tag name\n")
        self.data = self.db.dicts
        pos = -1
        self.tag_indexes = []
        for x in self.data:
            pos += 1
            if x["tag"] == tag_name:
                self.tag_indexes.append(pos)
        tags_mapping = {tag_name:self.tag_indexes}
        print(tags_mapping)

tags_view('./tags')
