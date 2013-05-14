import sys
import re
import json
import operator
from operator import itemgetter
def hw():
    print 'Hello, world!'

def lines1(fp):
    data=fp.readlines()
    htags=[]
    for line in data:
        text=json.loads(line)
        if( text.get("entities") ):
            if(text["entities"].get("hashtags")):
               for tags in text["entities"].get("hashtags"):
                   htags.append(tags["text"].encode('utf-8'))
    hcount={}
    for htag in htags:
        if(not(hcount.get(htag))):
            hcount[htag]=htags.count(htag)
    hcount_sorted=sorted([(value,key) for (value,key) in hcount.items()] ,key=itemgetter(1), reverse=True)
    #print hcount
    count=1
    for key,value in hcount_sorted:
       if(count<=10):
           print "%s %.3f" %(key.decode('utf-8',), value)
           count+=1
        

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #the_dict =lines(sent_file)
    #print the_dict.get('worried')
    lines1(tweet_file)

if __name__ == '__main__':
    main()
