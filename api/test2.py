
###count the number of upper case letters in file
with open('/tmp/upper.txt') as fh:
    count = 0
    text = fh.read()
    for character in text:
        if character.isupper():
            count +=1
    print(count)

###find largest files in a directory python