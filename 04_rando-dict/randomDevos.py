import random

def randomDevos(dict1):
    x=list(dict1.keys())
    key=random.randint(0,len(x)-1)
    china=x[key]
    devoList=dict1[china]
    index=random.randint(0,len(devoList)-1)
    return devoList[index]

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