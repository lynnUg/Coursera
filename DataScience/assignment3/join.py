import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #print record
    value = record
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(value[1], value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    list1=[]
    list2=[]
    for v in list_of_values:
        if(v[0]=='order'):
            list1.append(v)
        else:
            list2.append(v)
    for i in list1:
        for j in list2 :
            mr.emit((i+j))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
