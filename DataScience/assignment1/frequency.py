import sys
import re
import json
def hw():
    print 'Hello, world!'

def lines1(fp):
    data=fp.readlines()
    for line in data:
        text=json.loads(line)
        number=float(0)
        if(text.get('text')) :
                # split the text
            words=text.get('text')
            words = words.split()

                # for each word in the line:
            for word in words:
                    number+=float(1)
    other={}
    for line in data:
        text=json.loads(line)
        if(text.get('text')):
           words=text.get('text')
           words=words.split()
           for word in words:
              if(other.get(word)):
                    other[word]=float (other[word]+float(1))
                           #print out[number]
              else:
                    other[word]=float(1)

    for key,value in other.items():
         print "%s %.3f" %(key.encode('utf-8'), value/number)
         
           
       

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #the_dict =lines(sent_file)
    #print the_dict.get('worried')
    lines1(tweet_file)

if __name__ == '__main__':
    main()
