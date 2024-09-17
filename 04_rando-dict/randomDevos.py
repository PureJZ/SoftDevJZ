# Jackie Zeng
# China Rats plus One
# Soft Dev
# <randomDevos/python dictionaries/function that picks a random key of a dictionary and the from the list corresponding to the key, pick a random element.>
import random

def randomDevos(dict1):
    x=list(dict1.keys())
    key=random.randint(0,len(x)-1) #Select random number for key
    china=x[key]
    devoList=dict1[china] #Isolate the list corresponding to key
    index=random.randint(0,len(devoList)-1) #Pick random element from list
    return devoList[index]
#test case
dict1={
           4: [
'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
],
           5: [
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN'
              ]
         }
for i in range(20):
    print(randomDevos(dict1))