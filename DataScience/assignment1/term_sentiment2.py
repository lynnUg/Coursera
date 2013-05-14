import sys
import re
import json
def hw():
    print 'Hello, world!'

def lines1(fp,the_dict):
    data=fp.readlines()
    out=[]
    for line in data:
        text=json.loads(line)
        number=0
        if(text.get('text')) :
                # split the text
                words=text.get('text')
                words = words.split()

                # for each word in the line:
                for word in words:
                    if(the_dict.get(word)):
                        number=number+the_dict.get(word)
        out.append(number)
        #print out
    other={}
    number=0
    for line in data:
         text=json.loads(line)
         if(text.get('text')) :
                # split the text
                words=text.get('text')
                words = words.split()

                # for each word in the line:
                for word in words:
                    if(not(the_dict.get(word))):
                        #print word
                        if(other.get(word)):
                           other[word]=float (other[word]+out[number])/2
                           #print out[number]
                        else:
                            other[word]=out[number]
         number+=1
         #print other
    for key,value in other.items():
        if(value!=0):
            print "%s %.3f" %(key.encode('utf-8'), value)
       
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
