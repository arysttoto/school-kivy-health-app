from kivy.app import App #connect kivy library
from kivy.uix.button import Button #vidgets from kivy
from kivy.uix.label import Label #vidgets from kivy
from kivy.uix.boxlayout import BoxLayout #vidgets from kivy
from kivy.uix.textinput import TextInput #vidgets from kivy
from kivy.uix.screenmanager import ScreenManager, Screen #vidgets from kivy
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from result_eval import result_comments
import csv
#-------------------------------------------------
age = 0
name =''
p1, p2, p3 = 0, 0, 0
#---------------------First screen----------------------------
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text='Enter your name in the box', halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Enter your age in the box', halign='right')
        self.in_age = TextInput(text='', multiline=False)
        self.submit_btn = Button(text='Continue!', size_hint=(0.8, None), pos_hint={'center_x': 0.5})
        self.submit_btn.on_press = self.next
        instr_layout = BoxLayout(pos_hint={'center_x': 0.5}, padding=30)
        instr_layout.add_widget(instr)
        f_layout = BoxLayout(size_hint=(0.8, None), height='30sp', pos_hint={'center_x':0.5})
        f_layout.add_widget(lbl1)
        f_layout.add_widget(self.in_name)
        s_layout = BoxLayout(size_hint=(0.8, None), height='30sp', pos_hint={'center_x':0.5})
        s_layout.add_widget(lbl2)
        s_layout.add_widget(self.in_age)
        main_vert = BoxLayout(orientation='vertical', padding=8, spacing=80)
        main_vert.add_widget(instr_layout)
        main_vert.add_widget(f_layout)
        main_vert.add_widget(s_layout)
        main_vert.add_widget(self.submit_btn)
        self.add_widget(main_vert)
    def next(self):
        global name, age
        name = self.in_name.text
        age = self.in_age.text
        pulse_1.in_p1.text = ''
        self.manager.current = 'pulse1'

instruction_screen = InstrScr(name='instr')
#--------------------------------
class Pulse1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test1)
        self.in_p1 = TextInput(text="", multiline=False)
        self.submit_btn = Button(text='Continue!')
        self.submit_btn.on_press = self.next
        h1 = BoxLayout(size_hint=(0.8, None), height='40sp', pos_hint={'center_x': 0.5})
        h1.add_widget(self.in_p1)
        h1.add_widget(self.submit_btn)
        main_v1 = BoxLayout(orientation='vertical', padding=30)
        main_v1.add_widget(instr)
        main_v1.add_widget(h1)
        self.add_widget(main_v1)
    def next(self):
        global p1
        p1 = self.in_p1.text
        self.manager.current = 'sits'

pulse_1 = Pulse1(name='pulse1')
class Sits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.continue_btn = Button(text='Done!', size_hint=(0.4, None), height='50sp', pos_hint={'center_x':0.5})
        self.continue_btn.on_press = self.next
        main_v = BoxLayout(orientation='vertical', padding=8)
        main_v.add_widget(instr)
        main_v.add_widget(self.continue_btn)
        self.add_widget(main_v)
    def next(self):
        p1p2.fir_15.text = ''
        p1p2.sec_15.text = ''
        self.manager.current = 'pulse2'

sits = Sits(name='sits')
class PulseTwoThree(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        lbl1 = Label(text='P1', halign='right')
        self.fir_15 = TextInput(multiline=False)
        lbl2 = Label(text='P2', halign='right')
        self.sec_15 = TextInput(text='', multiline=False)
        self.submit_btn = Button(text='Continue!', size_hint=(0.8, None), pos_hint={'center_x': 0.5})
        self.submit_btn.on_press = self.next
        f_layout = BoxLayout(size_hint=(0.8, None), height='30sp', pos_hint={'center_x':0.5})
        f_layout.add_widget(lbl1)
        f_layout.add_widget(self.fir_15)
        s_layout = BoxLayout(size_hint=(0.8, None), height='30sp', pos_hint={'center_x':0.5})
        s_layout.add_widget(lbl2)
        s_layout.add_widget(self.sec_15)
        main_vert = BoxLayout(orientation='vertical', padding=8, spacing=80)
        main_vert.add_widget(instr)
        main_vert.add_widget(f_layout)
        main_vert.add_widget(s_layout)
        main_vert.add_widget(self.submit_btn)
        self.add_widget(main_vert)
    def next(self):
        global p2, p3
        p2 = self.fir_15.text
        p3 = self.sec_15.text
        self.manager.current = 'result_page'

p1p2 = PulseTwoThree(name='pulse2')
class Result_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result_lbl = Label(text='')
        self.btn_get_res = Button(text='Get my results!', size_hint=(0.5, None), height='60sp', pos_hint={'center_x': 0.5})
        self.btn_get_res.on_press = self.count_ruf
        self.btn_restart = Button(text='Try again!', size_hint=(0.5, None), height='60sp', pos_hint={'center_x': 0.5})
        self.btn_restart.on_press = self.next
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
        main_layout.add_widget(self.result_lbl)
        main_layout.add_widget(self.btn_get_res)
        main_layout.add_widget(self.btn_restart)
        self.add_widget(main_layout)
    def count_ruf(self):
        global p1, p2, p3, age, name
        S = 4 * (int(p1)+int(p2)+int(p3))
        result = (S-200)/10
        value = result_comments(result, int(age)) 
        self.result_lbl.text = f'''Your Ruffier index is {result}\n
Your heart assessment is {value}/10'''
        # data addition
        with open('data.csv', 'a', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, result, value])
    def next(self):
        self.result_lbl.text = ''
        instruction_screen.in_name.text = ''
        instruction_screen.in_age.text = ''
        self.manager.current = 'instr'

result = Result_page(name='result_page')
#--------------------------------
class HeartCheck(App):
    def build(self):
        ### each object will have .manager option because it is in it...
        sm = ScreenManager()
        sm.add_widget(instruction_screen)
        sm.add_widget(pulse_1)
        sm.add_widget(sits)
        sm.add_widget(p1p2)
        sm.add_widget(result)
        return sm 
app = HeartCheck()
app.run()