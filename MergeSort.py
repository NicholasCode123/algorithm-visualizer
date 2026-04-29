import pygame as py
import random as rr
import copy
class Value:
    def __init__(self,text,text_color,x,y,box_x,box_y,box_width,box_height,box_color,level,parent_index):
        self.text=text
        self.text_color=text_color
        self.x=x
        self.y=y
        self.speed=0.8
        self.rect=py.Rect(box_x,box_y,box_width,box_height)
        self.level=level
        self.box_color=box_color
        self.parent_index=parent_index
        
    def swap_places(self,pos_2):
        if self.x<=pos_2:
            self.x+=a
        elif self.x>=pos_2:
            self.x-=b
    def draw(self):
    
        value_text=font2.render(self.text,True,self.text_color)
        py.draw.rect(display,self.box_color,self.rect,4)
        inner_rect =self.rect.inflate(-4*2, -4*2)
        py.draw.rect(display, white, inner_rect)
        if len(str(self.text))==1:
            display.blit(value_text,(self.x+19,self.y))
        elif len(str(self.text))==2:
            display.blit(value_text,(self.x+15,self.y))
    
class Box:
    def __init__(self,x,y,w,h,color):
        self.rect=py.Rect(x,y,w,h)
        self.color=color
    def draw(self,display):
        py.draw.rect(display,self.color,self.rect)
    def clicked(self,pos):
        return self.rect.collidepoint(pos)


def move_box(list_value,a,b,c,d):
    n=len(list_value)
    if n==1:
        return
    left=(n+1)//2
    right=n
    for i in range(left):
        list_value[i].x -= a
        list_value[i].y += b
        list_value[i].rect.x = int(list_value[i].x)-c
        list_value[i].rect.y = int(list_value[i].y)-d 
    for i in range(left,right):
        list_value[i].x += a
        list_value[i].y += b
        list_value[i].rect.x = int(list_value[i].x)-c
        list_value[i].rect.y = int(list_value[i].y)-d
    return list_value[:left],list_value[left:right]

def increase_level(list_value):
    for i in list_value:
        i.level+=1
# def merge_box(list_value,a,b):
#     n=len(list_value)
#     if n==1:
#         return
#     left=(n+1)//2
#     right=n
#     for i in range(left):
#         list_value[i].x += a
#         list_value[i].y -= b
#     for i in range(left,right):
#         list_value[i].x -= a
#         list_value[i].y -= b
      


# def merge_value(left, right):
#     merged_list = []
#     i=0
#     j=0
#     while i < len(left) and j < len(right):
#         if int(left[i].text) <= int(right[j].text):
#             merged_list.append(left[i])
#             i += 1
#         else:
#             merged_list.append(right[j])
#             j += 1

#     if i < len(left):
#         merged_list.extend(left[i:])
#     if j < len(right):
#         merged_list.extend(right[j:])

#     return merged_list

def array_border(x,user_text):
    for i in range(int(user_text)):
        list_box.append(Box(x-4,95,60,60,'red'))
        x+=50+8
    return list_box
def screen_simulation_next():
    next_box.draw(display)
    for text in texts_simulation:
        simul_text=font2.render(text[0],True,text[1])
        display.blit(simul_text,text[2])
        
py.init()
b=7
c=7
d=22
start_box=Box(400,300,200,80,"#2E2F4A")
box2=Box(565,23,60,50,'white')
box3=Box(50,111,300,70,"#2E2F4A")
next_box=Box(447,80,100,50,"#187B59")
display=py.display.set_mode((1000,600))
font=py.font.Font(None,50)
font2=py.font.Font(None,30)
font3=py.font.Font(None,40)
screen='menu'
running=True
user_text=''
active_input=True
invalid=False
values=[]
list_box=[]
list_value=[]
all_list_value=[]
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
split_start_time=None
split_duration=250   
splitting=False
a=5
split_counter=1
pki=0
combine=False
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
merge_index=0
clock = py.time.Clock() 
texts_menu=[["Merge sort visualization",white,(300,200)],["Start",white,(460,325)]]
texts_main=[["Input length of array (max = 8) :",white,(30,30)],["Start simulation",white,(70,130)]]
all_combine_value=[]
texts_simulation=[["Blue = Lower Value",blue,(20,20)],["Green = Higher value",green,(20,50)],["Next",black,(475,95)]]
text_complete=[['Array has been sorted',green,(320,20)]]
parent_idx=0
copy_original=True
merge_state='compare'
merge_winner=''
left_flush=False
right_flush=True
parent_box_index=0
left_index=0
right_index=0
merge=False
merge_done=False
sorted_complete=False
while running:
    display.fill(black)
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
                        if user_text.isdigit() and int(user_text)<=8:
                            screen='simulation'
                            values=[rr.randint(1,99) for _ in range(int(user_text))]
                            x=500-int(user_text)*29
                            list_box=array_border(x,user_text)
                            for idx in range(len(values)):
                                list_value.append(Value(str(values[idx]),black,x,160,x-5,140,60,60,red,0,None))
                                x+=50+8
                            all_list_value.append(copy.deepcopy(list_value))
                            
                        else:   
                            invalid=True
                            
            if active_input and event.type==py.KEYDOWN:
                if event.key==py.K_BACKSPACE:
                    user_text=user_text[:-1]
                else:
                    user_text+=event.unicode
        
        if (screen=='simulation' or screen == "next") and combine==False:
            if event.type==py.MOUSEBUTTONDOWN:
                if event.button==1:
                    if next_box.clicked(event.pos): 
                        splitting=True
                        split_start_time=py.time.get_ticks()
                        
        elif (screen == 'simulation' or screen == 'next') and combine == True:
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if next_box.clicked(event.pos):

                        if len(all_combine_value)==1:
                            sorted_complete=True

                        elif merge_state == 'compare':

                            if not merge:
                                merge = True
                                left_index = 0
                                right_index = 0
                                parent_box_index = 0
                                
                               
                                merge_index=0
                                left_array  = all_combine_value[merge_index]
                                right_array = all_combine_value[merge_index + 1]
                                index_parent = left_array[0].parent_index
                                length_left_array  = len(left_array)
                                length_right_array = len(right_array)
            
                            if left_index < length_left_array and right_index < length_right_array:
                                if int(left_array[left_index].text) < int(right_array[right_index].text):
                                    left_array[left_index].box_color  = blue
                                    right_array[right_index].box_color = green
                                    merge_winner = 'right'
                                else:
                                    left_array[left_index].box_color  = green
                                    right_array[right_index].box_color = blue
                                    merge_winner = 'left'
                                merge_state = 'swap'

                        elif merge_state == 'swap':
                            if merge_winner == 'right':
                                all_list_value[index_parent][parent_box_index].text = right_array[right_index].text
                                right_array[right_index].text = ''
                                right_index += 1
                            else:
                                all_list_value[index_parent][parent_box_index].text = left_array[left_index].text
                                left_array[left_index].text = ''
                                left_index += 1
                            parent_box_index += 1

                   
                            for item in left_array:  item.box_color = red
                            for item in right_array: item.box_color = red

               
                            if left_index == length_left_array and right_index == length_right_array:
                                merge_done = True  
                            elif left_index == length_left_array:
                                merge_state = 'flush_right'
                            elif right_index == length_right_array:
                                merge_state = 'flush_left'
                            else:
                                merge_state = 'compare' 

                        elif merge_state == 'flush_left':
                            left_array[left_index].box_color = blue
                            merge_state = 'flush_left_confirm'

                        elif merge_state == 'flush_left_confirm':
                            all_list_value[index_parent][parent_box_index].text = left_array[left_index].text
                            left_array[left_index].text = ''
                            left_index += 1
                            parent_box_index += 1
                            for item in left_array: item.box_color = red

                            if left_index >= length_left_array:
                                merge_done = True
                            else:
                                merge_state = 'flush_left'

                        elif merge_state == 'flush_right':
                            right_array[right_index].box_color = green
                            merge_state = 'flush_right_confirm'

                        elif merge_state == 'flush_right_confirm':
                            all_list_value[index_parent][parent_box_index].text = right_array[right_index].text
                            right_array[right_index].text = ''
                            right_index += 1
                            parent_box_index += 1
                            for item in right_array: item.box_color = red

                            if right_index >= length_right_array:
                                merge_done = True
                            else:
                                merge_state = 'flush_right'

                   
                        if merge_done:
                            merge_done = False
                            finished_parent = all_list_value[index_parent]
                            all_combine_value.append(finished_parent)
                            merge_index += 2
                            del all_combine_value[:2]
                            if len(set(arr[0].level for arr in all_combine_value)) == 1:
                                print(0000000000000000000)
                                all_combine_value.sort(key=lambda arr: arr[0].x)
                            
                            merge = False      
                            merge_state = 'compare'
                            left_index = 0
                            right_index = 0
                            parent_box_index = 0
                        





                        # print('=========================')
                        # for idx, u in enumerate(all_list_value):  
                        #     print(idx, [(v.text,v.level,v.parent_index,v.x,v.y) for v in u])
                        print('=========================')
                        for idx, u in enumerate(all_combine_value):  
                            print(idx, [(v.text,v.level,v.parent_index,v.x,v.y) for v in u])
                            


  



                        
                    
    if splitting:
        current_time=py.time.get_ticks()
        if copy_original:
            xo=[]
            for u in range(1,split_counter+1):
                xo.append(copy.deepcopy(all_list_value[-u]))
            for k in range(1,split_counter+1):
                all_list_value.append(copy.deepcopy(xo[-k]))
        copy_original=False
        if current_time-split_start_time<=split_duration:
            for e in range(1,split_counter+1):
                move_box(all_list_value[-e],a,b,c,d)
        else:
            copy_original=True
            leaf=0
            splitting=False
            p=[]
            print("ACTIVE LISTS:")
            for idx, u in enumerate(all_list_value):  
                print(idx, [(v.text,v.level,v.parent_index,v.x,v.y) for v in u])
            for y in range(1,split_counter+1):
                p.append(move_box(all_list_value[-y],a,b,c,d))
            
            for _ in range(split_counter):
                all_list_value.pop()
            for q in range(1,len(p)+1):
                if p[-q]:
                    all_list_value.append(copy.deepcopy(p[-q][0]))
                    increase_level(all_list_value[-1])
                    for k in all_list_value[-1]:
                        k.parent_index=parent_idx
                    all_list_value.append(copy.deepcopy(p[-q][1]))
                    increase_level(all_list_value[-1])
                    for j in all_list_value[-1]:
                        j.parent_index=parent_idx
                parent_idx+=1
                    
                    
            print("ACTIVE LISTS:")
            for idx, u in enumerate(all_list_value):  
                print(idx, [(v.text,v.level,v.parent_index,v.x,v.y) for v in u])
            split_counter*=2
            if split_counter>=int(user_text):
                split_counter=int(user_text)
            a-=2
            all_combine_value=[]
            for idx,v in enumerate(all_list_value):
                if len(v)==1:
                    all_combine_value.append(v)
                    leaf+=1
            if leaf==int(user_text):
                for v in all_list_value:
                    if len(v)==1:
                        continue
                    for l in v:
                        l.text=''

                all_combine_value = sorted(
                    all_combine_value,
                    key=lambda x: x[0].level,
                    reverse=True
                )
                combine=True
                
                
           
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
        input_text=font.render(user_text,True,black)
        display.blit(input_text,(570,32))
        if invalid==True:
            invalid_text=font2.render("Invalid input",True,red)
            display.blit(invalid_text,(52,200))
    if screen=='simulation':
        x=500-int(user_text)*29
        for l in all_list_value:
            for value in l:
                value.draw()
        screen_simulation_next()
    
    if sorted_complete==True:
        for text in text_complete:
            render_text=font.render(text[0],True,text[1])
            display.blit(render_text,text[2])


    py.display.update()
    clock.tick(60)


py.quit()
