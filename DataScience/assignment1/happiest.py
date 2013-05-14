import sys
import re
import json
import operator
from operator import itemgetter
def hw():
    print 'Hello, world!'

def lines1(fp,the_dict):
    data=fp.readlines()
    for line in data:
        text=json.loads(line)
        number=0
        happiest_state={}
        if(text.get('text')) :
                # split the text
                words=text.get('text')
                words = words.split()
                #print text ,"\n"
                if(text.get('place')):
                    print text['place']['country'],"\n"
                    if(text['place']['country_code']=='US'):
                         for word in words:
                           if(the_dict.get(word)):
                               number=number+the_dict.get(word)
                         state=text['place']['full_name'][-2:].encode('utf-8')
                         if state in happiest_state.keys():
                             happiest_state[state]=happiest_state[state]+number
                         else :
                              happiest_state[state]=number

    for w in sorted(happiest_state, key=happiest_state.get,reverse=True)[0:1]:		
        print w     
    
                       
def lines(fp):
    data=fp.readlines()
    mydict={}
    for line in data:
        nums = re.compile(r"[+-]?\d+(?:\.\d+)?")
        for m in nums.finditer(line):
            key=m.start()
            value=int(m.group())
        the_key=line[0:key].strip()
        mydict[the_key]=value

    return mydict
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    the_dict =lines(sent_file)
    #print the_dict.get('worried')
    lines1(tweet_file,the_dict)

if __name__ == '__main__':
    main()
