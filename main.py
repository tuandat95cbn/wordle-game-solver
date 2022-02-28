import re
possible_words="aback abase abate abbey abbot abhor abide abled"
with open('possible_words.txt', 'r') as file:
    possible_words = file.read().replace('\n', ' ')
position_rule=[None,None,None,None,None]
not_in_position_rule=[]
contain_rule=set()
restrict_rule=set()
def add_contain_rule(char):
    contain_rule.add(char)
def add_restrict_rule(char):
    restrict_rule.add(char)
def add_position_rule(char, position):
    position_rule[position]=char
def add_not_in_position_rule(char, position):
    not_in_position_rule.append((char,position))
def build_not_in_position_regex(tu):
    regx=""
    for i in range(5):
        if i==tu[1]:
            regx+=tu[0]
        else:
            regx+=r'\w'
    return regx
def suggest():
    regx=r'('
    for index,character in enumerate(position_rule):
        if character != None:
            regx+=character
        else:
            regx+=r'\w'
    regx+=r'\b)'
    list_m=re.findall(regx,possible_words)
    list_n=[]
    for s in list_m:
        b=True
        for character in contain_rule:
            regx=r'.*'+character+'.*'
            if not re.match(regx,s):
                b=False
                break
        if b:
            list_n.append(s)
    list_o=[]
    for s in list_n:
        b=True
        for character in restrict_rule:
            regx=r'.*'+character+'.*'
            if re.match(regx,s):
                b=False
                break
        if b:
            list_o.append(s)
    list_p=[]
    for s in list_o:
        b=True
        for tu in not_in_position_rule:
            regx=build_not_in_position_regex(tu)
            if re.match(regx,s):
                b=False
                break
        if b:
            list_p.append(s)
    print(list_p)
    return regx
def search(regx):
    result = re.findall(regx, possible_words)
    print(result)
def process():
    while (True):
        choice=input("which rule you want to add (1: position rule,2: not in position, 3: contain rule,4: restrict rule): \n")
        choice=int(choice)
        if not isinstance(choice, int) :
            print("Please enter an interger!!!!\n")
            continue
        if choice==1:
            character=input("Please specify the character:").lower()
            position=input("Please specify the position:")
            add_position_rule(character,int(position))
        elif choice==2:
            character=input("Please specify the character:").lower()
            position=input("Please specify the position:")
            add_not_in_position_rule(character,int(position))
        elif choice==3:
            character=input("Please specify the character:").lower()
            add_contain_rule(character)

        elif choice==4:
            character=input("Please specify the character:")
            add_restrict_rule(character)
        else:
            print("Please enter 1,2,3,4!!!\n")
            continue
        suggest()
        #search(regx)
process()

