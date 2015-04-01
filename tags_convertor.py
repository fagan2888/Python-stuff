fl = open('/home/jhazelden/py/tags')
dicts = []
for line in fl:
   line = line.strip()
   if line[0] == "!":
      continue
   else:
      words = line.split('\t')
      tag_name = words[0]
      file_name = words[1]
      search_pattern = words[2]
      dictionary = {"tag": tag_name, "file name": file_name, "search pattern": search_pattern}
      colon = words[3].find(':')
      kind_type = len(words[3])
      starter = 3
#      import pdb; pdb.set_trace()
      if colon == -1 and kind_type == 1:
         dictionary["kind"] = words[3]
         starter = 4
      elif colon == -1 and kind_type > 1:
         dictionary["KIND"] = words[3]
         starter = 4
 
      for i in range(starter, len(words)):
         colon = words[i].find(':')
         field = words[i][:colon+1]
         dictionary[field]= words[i][colon+1:]

   dicts.append(dictionary)
print(dicts)

