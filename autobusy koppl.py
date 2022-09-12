import tkinter
canvas = tkinter.Canvas()
canvas.pack()
subor = open('autobusy.txt', 'r',encoding='utf-8')
s=0

def autobusy():
    
    riadok = subor.readline()
       
        
    for riadok in subor:
        y=10
        
            
        canvas.create_text(50,y+50,text=str(riadok))
        y += 50
    y1=-10
    color=''
    for i in range(9):
        canvas.create_rectangle(150,y1+20,270,y1+40,fill=color)
        y1 = y1 + 25
        if s == 1:
            color = 'red'
            
        
def naplnenost():
    s=1
        
        
                
    subor.close()
    
    
    

autobusy()
canvas.bind_all('<Key>', naplnenost)    
