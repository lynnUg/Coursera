import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
common=[]
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    common.append(key+" "+value)
    if (not ((value+" "+key) in common)):
        mr.emit_intermediate(key, value)
        mr.emit_intermediate(value,key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      if(not( ((v+" "+key) in common) and ((key+" "+v) in common))):
         mr.emit((key, v))
        
      #print common
   
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  #print common
