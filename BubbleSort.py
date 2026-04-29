import pygame as py
import random as rr
import sys

print(sys.version)
def bubblesort(arr):
    for i in range(len(arr)-1):
        swap=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swap=True
        if swap==False:
            break
    return arr

def screen_simulation_next(dist,user_text):
    for i in range(int(user_text)):
        box_array=Box(dist,100,50,50,"white")
        list_box[i].draw(display)
        box_array.draw(display)
        dist+=58
        next_box.draw(display)
        for text in texts_simulation:
            simul_text=font2.render(text[0],True,text[1])
            display.blit(simul_text,text[2])


def array_border(x,user_text):
    for i in range(int(user_text)):
        list_box.append(Box(x-4,95,60,60,'red'))
        x+=50+8
    return list_box


class Value:
    def __init__(self,text,color,x,y):
        self.text=text
        self.color=color
        self.x=x
        self.y=y
        self.speed=0.8
    def swap_places(self,pos_2):
        if self.x<=pos_2:
            self.x+=self.speed
        elif self.x>=pos_2:
            self.x-=self.speed
    def draw(self):
        value_text=font2.render(self.text,True,self.color)
        if len(str(self.text))==1:
            display.blit(value_text,(self.x+19,self.y))
        elif len(str(self.text))==2:
            display.blit(value_text,(self.x+15,self.y))
        
       

# def value_box(user_text,text,color,x_pos,y_pos):
#     for i in range(int(user_text)):
#         list_value.append(Value(text[i],color[i],x_pos[i],y_pos[i]))
#     return list_value
            


        
class Box:
    def __init__(self,x,y,w,h,color):
        self.rect=py.Rect(x,y,w,h)
        self.color=color
    def draw(self,display):
        py.draw.rect(display,self.color,self.rect)
    def clicked(self,pos):
        return self.rect.collidepoint(pos)
start_box=Box(400,300,200,80,"#2E2F4A")
box2=Box(410,23,60,50,'white')
box3=Box(50,111,300,70,"#2E2F4A")
next_box=Box(447,200,100,50,"#187B59")

py.init()
display=py.display.set_mode((1000,600))
font=py.font.Font(None,50)
font2=py.font.Font(None,30)
font3=py.font.Font(None,40)

running=True
user_text=''
active_input=True
invalid=False
values=[]
list_box=[]
list_value=[]
counter=0
i=0
swap=False
x=0
x_ax=120
y_ax=120
swap2=False
swap_click=0
sorted_array=False
reset_index=False
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
texts_menu=[["Bubble sort visualization",white,(300,200)],["Start",white,(460,325)]]
texts_main=[["Input length of array :",white,(30,30)],["Start simulation",white,(70,130)]]
texts_simulation=[["Blue = Dont swap",blue,(20,20)],["Green = Swap",green,(20,50)],["Next",(0,0,0),(475,217)]]
screen='menu'
while running:
    display.fill((0,0,0))
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
        if event.type==py.KEYDOWN:
            if event.key==py.K_q:
                running=False
        if screen=='menu':
            if event.type==py.MOUSEBUTTONDOWN:
                if event.button==1:
                    if start_box.clicked(event.pos):
                        screen='main'
        if screen=='main':
            if event.type==py.MOUSEBUTTONDOWN:
                if event.button==1:
                    if box3.clicked(event.pos):
                        if user_text.isdigit():
                            screen='simulation'
                            values=[rr.randint(1,100) for _ in range(int(user_text))]
                            x=500-int(user_text)*29
                            list_box=array_border(x,user_text)
                            for idx in range(len(values)):
                                list_value.append(Value(str(values[idx]),(0,0,0),x,115))
                                x+=50+8
                        else:   
                            invalid=True
                            
            if active_input and event.type==py.KEYDOWN:
                if event.key==py.K_BACKSPACE:
                    user_text=user_text[:-1]
                else:
                    user_text+=event.unicode
        if screen=='simulation' or screen == "next":
            if event.type==py.MOUSEBUTTONDOWN:
                if event.button==1:
                    if next_box.clicked(event.pos):   
                        reset_index=False
                        for box in list_box:
                            box.color='red'
                        screen='next'
                        swap_click+=1
                        if counter<len(values)-1-i:
                            if values[counter]>values[counter+1]:
                                list_box[counter].color='green'
                                list_box[counter+1].color='green'
                                if swap_click%2==0:
                                    value_1=list_value[counter].x
                                    value_2=list_value[counter+1].x
                                    values[counter],values[counter+1]=values[counter+1],values[counter]
                                    swap=True
                                    swap2=True
                            elif values[counter]<=values[counter+1]:
                                list_box[counter+1].color='blue'
                                list_box[counter].color='blue'
                                swap_click+=1
                        if swap_click%2==0:
                            counter+=1                      
                        if counter>len(values)-1-i:
                            if swap==False:
                                sorted_array=True
                               
                                print(1)
                                
                            else:      
                                i+=1
                                counter=0
                              
                                reset_index=True
                              
                                swap=False
                                
                                
                    # elif previous_box.clicked(event.pos):
                    #     screen='previous'

                            
    if screen=='menu':
        start_box.draw(display)
        for text in texts_menu:
            render_text=font.render(text[0],True,text[1])
            display.blit(render_text,text[2])
    if screen=='main':
      
        box2.draw(display)
        box3.draw(display)
        for text in texts_main:
            render_text=font.render(text[0],True,text[1])
            display.blit(render_text,text[2])
        input_text=font.render(user_text,True,(0,0,0))
        display.blit(input_text,(421,32))
        if invalid==True:
            invalid_text=font2.render("Invalid input",True,(255,0,0))
            display.blit(invalid_text,(52,200))
    if screen=='simulation':
   
        x=500-int(user_text)*29
        screen_simulation_next(x,user_text)
        for value in list_value:
            value.draw()
    if screen =='next':
      
        x=500-int(user_text)*29
        screen_simulation_next(x,user_text)
        if swap2==True and swap_click%2==0:
        
            list_value[counter-1].swap_places(value_2)
            list_value[counter].swap_places(value_1)
            if abs(list_value[counter-1].x - value_2) < 1 and abs(list_value[counter].x - value_1) < 1:
                list_value[counter-1],list_value[counter]=list_value[counter], list_value[counter-1]
                swap2=False
                swap_click=False
        for value in list_value:
            value.draw()
        
        if reset_index==True:
            reset_text="Reset to index 0"
            reset_render=font2.render(reset_text,True,'white')
            display.blit(reset_render,(423,65))
        if sorted_array==True:
            sorted_text="Array has been sorted"
            sorted_render=font2.render(sorted_text,True,'white')
            display.blit(sorted_render,(397,65))

            

       
            



        

        
    
    py.display.update()


py.quit()

