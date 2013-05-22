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
    value = record
    
    if(value[0]=='a'):
        for i in range(0,5):
            mr.emit_intermediate(str(value[1])+" "+str(i),value)
    else:
        for j in range(0,5):
            mr.emit_intermediate(str(j)+" "+str(value[2]),value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total=0
    lista=[0]*5
    listb=[0]*5
    print key
    print list_of_values
    print " "
    for v in list_of_values:
      if (v[0]=='a'):
          lista[v[2]]=v[3]
      else:
          listb[v[1]]=v[3]
    for j in range(0,5):
        total+=lista[j]*listb[j]
    mr.emit((int(key[0]),int(key[2]),total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
