import tkinter as tk

LARGE_FRONT_STYLE=('Arial',24,'bold')
SMALL_FRONT_STYLE=('Arial',16)
LIGHT_GRAY='#ccc'
LABEL_COLOR='#25265E'
WHITE='#FFFFFF'
DIGITS_FRONT_STYLE=('Arial',24,'bold')
DEFAULT_FRONT_STYLE=('Arial',20)
OFF_WHITE='#F8FAFF'
LIGHT_BLUE='#CCEDFF'


class calculator:
    def __init__(self):

        ''' hàm khởi tạo toàn bộ máy tính'''

        #tạo khung máy tính cầm tay
        self.window=tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(0,0)
        self.window.title('calculator')

        #khởi tạo giá trị đầu cho label
        self.total_expression=''
        self.curent_expression=''

        #tạo ra frame chứa label
        self.display_frame=self.create_display_frame()

        #tạo ra 2 label
        self.total_label, self.label=self.creat_display_labels()

        #tạo vị trí cho các nút bấm số
        self.digits={
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2),
            '.': (4, 1)
        }

        #khia báo các toán tử
        self.operations={'/':'\u00F7','*':'\u00D7','-':'-','+':'+'}


        #tạo frame chứa các nút bấm
        self.button_frame=self.create_buttons_frame()

        #cân đều
        self.button_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x, weight=1)


        #tạo các nút bấm số
        self.creat_digits_buttons()

        #tạo nút bấm toán tử
        self.creat_operator_button()
        #tạo 2 nút = và clear
        self.creat_special_button()


    #hàm để tạo label
    def creat_display_labels(self):

        '''
        nhiệm vụ tạo ra 1 hiển thị 2 label , ở phần tính toán
        '''

        total_label=tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOR,padx=24,font=SMALL_FRONT_STYLE)
        total_label.pack(expand=True,fill='both')

        label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=LARGE_FRONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label,label

    #hàm 2 nút
    def creat_special_button(self):
        self.creat_clear_button()
        self.creat_equal_button()

    #hàm tạo hiển thị frame label
    def create_display_frame(self):

        '''
        nhiệm vụ tạo ra frame chứa hai label hiển thị
        '''

        frame=tk.Frame(self.window,height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill='both')
        return frame

    #hàm tạo hiển thị khung frame chứa button
    def create_buttons_frame(self):

        '''
        nhiệm vụ tạo ra frame chứa toàn bộ nút bấm
        '''

        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill='both')
        return frame

    # hàm hiển thị tất cả các nút bấm số:
    def creat_digits_buttons(self):

        '''
        nhiệm vụ là hiển thị các nút bấm số, dấn chấm,
        '''

        for digit,grid_value in self.digits.items():
            button =tk.Button(self.button_frame, text= str(digit), bg=WHITE,fg=LABEL_COLOR,font=DIGITS_FRONT_STYLE,borderwidth=0,command=lambda x=digit: self.add_to_expression(x) )
            button.grid(row = grid_value[0], column = grid_value[1],sticky=tk.NSEW)

    #hàm xử lí khi bấm nút clear
    def clear(self):

        '''
        nhiệm vụ là sẽ xóa toàn bộ màn hình label, bằng cách cập nhật 2 text bằng xâu rỗng
        '''

        self.curent_expression=''
        self.total_expression=''
        self.update_total_label()
        self.update_label()

    #hàm tạo nút bấm phép toán:
    def creat_operator_button(self):

        '''
        nhiệm vụ tạo hiểu thị 4 nút bấm toán tử
        '''

        i=0
        for operator, symbol in self.operations.items():
            button=tk.Button(self.button_frame,text=symbol,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FRONT_STYLE,borderwidth=0,command=lambda x=operator: self.append_operator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    #hàm xử lí khi bấm phím toán tử
    def append_operator(self,operator):

        '''

        '''

        self.curent_expression+=operator
        self.total_expression+=self.curent_expression
        self.curent_expression=''
        self.update_total_label()
        self.update_label()

    #hàm tạo nút clear:
    def creat_clear_button(self):

        '''
        nhiệm vụ tạo nút clear
        '''

        button = tk.Button(self.button_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FRONT_STYLE,
                           borderwidth=0,command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW,columnspan=3)

    #hàm tạo nút bằng
    def creat_equal_button(self):

        '''
        nhiệm vụ tạo nút bằng '='
        '''

        button = tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FRONT_STYLE,
                           borderwidth=0,command=self.evalue)
        button.grid(row=4, column=3, sticky=tk.NSEW,columnspan=2)

    #hàm cập nhật giá trị total_label
    def update_total_label(self):

        '''
        nhiệm vụ cập nhật giá trị hiển thị cho total_label
        '''

        self.total_label.config(text=self.total_expression)


    #hàm cập nhật giá trị label
    def update_label(self):


        '''
        cập nhật giá trị text mới cho label
        '''

        self.label.config(text=self.curent_expression)


    #hàm thêm giá trị khi ấm nút số
    def add_to_expression(self,value):

        '''
        nhiệm vụ khi bấm phím số:
        cập nhật giá trị mới vào label
        '''

        self.curent_expression+=str(value)
        self.update_label()

    #hàm tính toán giá trị khi bấm nút bằng
    def evalue(self):

        '''
        #tính giá trị sau đso thêm vào label kết quả
        #xóa toàn text của phần label chữ nhỏ 
        '''

        self.total_expression+=self.curent_expression
        self.update_total_label()
        self.curent_expression=str(eval(self.total_expression))
        self.total_expression=''
        self.update_label()

    #hàm chạy vòng loop của giao diện máy tính cầm tay
    def run(self):
        self.window.mainloop()

if __name__=='__main__':
    calc=calculator()
    calc.run()