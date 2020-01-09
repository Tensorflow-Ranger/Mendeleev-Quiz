import ipywidgets as widgets
from IPython.display import HTML
from ipywidgets import Layout, Button, Box
from ipywidgets import Button, Layout, jslink, IntText, IntSlider,VBox,HBox
from IPython.display import clear_output
import mendeleev as md
import random
from mendeleev import element

Layout10 = Layout(flex='1', width='500px',height="50px",margin="10px 10px 20px 10px")

box_layout1 = Layout(display='flex',
                    flex_flow='row',
                    align_items='stretch',
                    width='100%')

box_layout = Layout(display='flex',
                    flex_flow='column',
                    align_items='stretch',
                    border='solid',
                    width='100%')
form_item_layout = Layout(
    display='flex',
    flex_flow='row',
    justify_content='center',
    margin="10px 10px 20px 10px",
    width="100%"
)

# atomic_number = random.randint(1,118)
element_ = element(atomic_number)
element_symbol = element_.symbol
element_name = element_.name

sub_text = widgets.HTML(('<center><h3>'+'Guess the the symbol of the element using the atomic number'+'</h3></center>'))
sub_text1 = widgets.HTML(('<center><h3>'+'Atomic Number:'+'</h3></center>'))

Horiz = widgets.HBox([sub_text],layout=Layout(justify_content='center'))
Horiz1 = widgets.HBox([sub_text1],layout=Layout(justify_content='center'))

Btn1 = Button(description='Submit',layout=Layout10, button_style='info')
Btn2 = Button(description="Again",layout=Layout10, button_style='info')
Btn10 = Button(description='Go to home page',layout=Layout10, button_style='info')
Btn11 = Button(description='Go to home page',layout=Layout10, button_style='info')

Btn1.style.button_color = 'DeepSkyBlue'
Btn2.style.button_color = 'LightCoral'
Btn10.style.button_color = 'DeepSkyBlue'
Btn11.style.button_color = 'LightCoral'


Title = widgets.HTML(('<center><h2>'+'Mendeleev Table'+'</h2></center>'))

def new_element(b):
    global atomic_number,element_,element_symbol,element_name
    atomic_number = random.randint(1,118)
    element_ = element(atomic_number)
    element_symbol = element_.symbol
    element_name = element_.name
    print(atomic_number)
    atomic_number_display = widgets.HTML(('<center><h2>'+str(atomic_number)+'</h2></center>'))
    Horizontal4 = widgets.HBox([atomic_number_display],layout=Layout(justify_content='center'))
    homepage1 = widgets.HBox([Btn11],layout=Layout(justify_content='center'))
    Screen1 = widgets.VBox([right_box1,Horiz,Horiz1,Horizontal4,Horizontal3,Horizontal2,Horizontal],layout=box_layout)
    clear_output()
    display(Screen1)
    
def win(b):
    if element_symbol == Text_box10.value:
        status_img = widgets.HTML('<img src="correct.png" height="500" width="500">')
        answer = widgets.HTML(('<center><h2>'+element_name+' or '+element_symbol+" is the "+str(atomic_number)+" element of the periodic table "+'</h2></center>'))
        Loading_box = widgets.HBox([status_img],layout=Layout(justify_content='center'))
        Loading_box_txt = widgets.HBox([answer],layout=Layout(justify_content='center'))
        homepage = widgets.HBox([Btn10],layout=Layout(justify_content='center'))
        Screen7 = VBox([Loading_box_txt,Loading_box,homepage],layout=box_layout)
        clear_output()
        display(Screen7)
                               
    else:
        status_img = widgets.HTML('<img src="wrong.png" height="500" width="500">')
        answer = widgets.HTML(('<center><h2>'+element_name+" or "+element_symbol+" is the "+str(atomic_number)+" element of the periodic table "+'</h2></center>'))
        Loading_box = widgets.HBox([status_img],layout=Layout(justify_content='center'))
        Loading_box_txt = widgets.HBox([answer],layout=Layout(justify_content='center'))
        homepage1 = widgets.HBox([Btn10],layout=Layout(justify_content='center'))
        Screen7 = VBox([Loading_box_txt,Loading_box,homepage1],layout=box_layout)
        clear_output()
        display(Screen7)

def home(b):
    clear_output()
    display(Screen1)
atomic_number_display = widgets.HTML(('<center><h2>'+str(atomic_number)+'</h2></center>'))


Text_box10 = widgets.Text(layout=form_item_layout)

right_box1 = widgets.HBox([Title],layout=Layout(justify_content='center'))
Horizontal = widgets.HBox([Btn2])
Horizontal2 = widgets.HBox([Btn1])
Horizontal3 = widgets.HBox([Text_box10])
Horizontal4 = widgets.HBox([atomic_number_display],layout=Layout(justify_content='center'))
Screen1 = widgets.VBox([right_box1,Horiz,Horiz1,Horizontal4,Horizontal3,Horizontal2,Horizontal],layout=box_layout)
Btn2.on_click(new_element)
Btn1.on_click(win)
Btn11.on_click(home)
Btn10.on_click(home)
display(Screen1)