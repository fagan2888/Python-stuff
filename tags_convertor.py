fl = open('/home/jhazelden/py/tags')
dicts = []
for line in fl:
   fields = ["save:"]
   pyfields = ["py:"]
   cfields = []
   if line[0] == "!":
      continue
   else:
      words = line.split('\t')
      tag_name = words[0]
      file_name = words[1]
      search_pattern = words[2]
      dictionary = {"tag": tag_name, "file name": file_name, "search pattern": search_pattern}
      colon = words[3].find(':')
      period = file_name.find(".")
      if colon > -1:
         for i in range(len(words)):
            if file_name[period:] == ".py":
               for field in fields:
                  if words[i].find(field) > -1:
                     if words[i].find('\n') == -1:
                        dictionary[field[:-1]] = words[i][colon+1:-1]
                     else:
                        dictionary[field[:-1]] = words[i][colon+1:]
               for field in pyfields:
                  if words[i].find(field) > -1:
                     dictionary[pyfield[:-1]] = words[i][colon+1:]
      else:
         if words[3].find('\n') == -1:
            dictionary["kind"] = words[3]
         else:
            dictionary["kind"] = words[3][:-1]
   dicts.append(dictionary)
print(dicts)

