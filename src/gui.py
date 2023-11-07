import lexerpy as lex
import prepare as prep
from tkinter import Event
from tkinter import *
from tkinter import constants
from tkinter import ttk
from tkinter import filedialog

# run lexer function
def run_lex():
    print("Button pressed")
    code=txt_editor_pane.get("1.0", END)
    tokens,category,error=lex.tokenize(code)
    print(tokens)
    print_lex(tokens, category)
    print_error(error)
    lex_table_pane.config(state="disabled")
    error_pane.config(state="disabled")

# run prints lexeme table  
def print_lex(value, type):                      
    print("Printing lex")
    lex_table_pane.config(state="normal")
    lex_table_pane.delete('1.0', constants.END)
    lex_table_pane.insert(constants.END, "LEXEME\t\t\tTOKEN\n\n")
    token,category=prep.remove_whitespace_type(value,type)
    for i in range(len(token)):
        # if type[i] == 'Error Category' or type[i] == 'Whitespace' or type[i] == 'None':
        #     continue
        # else:  
        lex_table_pane.insert(
            constants.END, f'{str(token[i]) if len(str(token[i]))<=15 else str(token[i])[:10] + "..."}\t\t\t{str(category[i])}\n')

# executes error handling and reporting
def print_error(error):
    error_pane.config(state="normal")
    error_pane.delete('1.0', constants.END)
    for err in range(len(error)):
        if err+1 == len(error):
            if error[err] != '':
                error_pane.insert(constants.END, f'{error[err]}\n')
        else:
            if error[err] != '':
                if error[err] != error[err+1]:
                    error_pane.insert(constants.END, f'{error[err]}\n')
            else:
                continue


def load_file():
    filepath = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r") as file:
            txt_editor_pane.delete("1.0", END)
            txt_editor_pane.insert("1.0", file.read())

# sets the tab spaces to be 4 every time it's pressed
def tab_pressed(event:Event) -> str:
    txt_editor_pane.insert("insert", " "*4)
    # Prevent the default tkinter behaviour
    return "break"

root = Tk()

root.geometry("939x617")
root.resizable(False,False)
root.title("Sheesh Compiler")

# config color collection
clr_bg = "#2D2D2D"
clr_black = "#202020"
clr_gray = "#272727"

root.configure(bg=clr_bg)

# style scrollbar
style = ttk.Style()
style.theme_use("clam")  
style.configure("Vertical.TScrollbar", troughcolor=clr_black, background=clr_black, gripcount=0, gripcolor=clr_black)

# setting main layout
mainpane = Canvas(
    root,
    bg=clr_black,
    height=617,
    width=939,
    bd=0,
    highlightthickness=0,
    relief="ridge")

mainpane.place(x=0,y=0)

# setting editor section
txt_editor_pane = Text(
    bd=0,
    bg=clr_gray,
    # highlightcolor=
    highlightthickness=0,
    fg="#FFFFFF",
    insertbackground="white",
    padx=10,
    pady=10,
    font=('Open Sans', 11,),) 

txt_editor_pane.place(x=10,y=40,width=600,height=390)
txt_editor_pane.bind("<Tab>", tab_pressed)

# setting lexer output section
lex_table_pane = Text(
    bd=0,
    bg=clr_gray,
    highlightthickness=0,
    fg="#FFFFFF",
    padx=10,
    pady=10,
    font=('Open Sans', 10),
    state = "disabled",)

lex_table_pane.place(
    x=620,
    y=40,
    width=310,
    height=565)

# header section
header_pane = Text(
    bd = 0,
    bg = clr_gray,
    padx = 10,
    pady = 10,
    font = ('Open Sans', 10),
)

header_pane.place(
    x=10,
    y=10,
    width=920,
    height=25,
)

# setting lexer output section
error_pane = Text(
    bd=0,
    bg=clr_gray,
    highlightthickness=0,
    fg="#FFFFFF",
    padx=10,
    pady=10,
    font=('Open Sans', 10),
    state = "disabled",)

error_pane.place(x=10,y=435,
               width=600,height=170)


# run lexer function button
run_img = PhotoImage(file="../assets/run.png") 
lex_btn = Button(
        image=run_img,
        compound=LEFT,
        bg=clr_gray,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#AAAAAA",
        fg="#079AD2",
        activeforeground="#FFFFFF",
        justify="center",
        command=run_lex,
)
lex_btn.place(x=15,y=10,width=25,height=25)

load_img = PhotoImage(file = "../assets/load.png")
load_btn=Button(
    image=load_img,
    compound=LEFT,
    bg=clr_gray,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#AAAAAA",
    fg="#079AD2",
    justify="center",
    command=load_file,

)
load_btn.place(x=50,y=10,width=25,height=25)

scrollbar = ttk.Scrollbar(
    txt_editor_pane, 
    orient='vertical',
    command=txt_editor_pane.yview,
)
scrollbar.pack(side=RIGHT, fill=Y)

txt_editor_pane['yscrollcommand'] = scrollbar.set

root.mainloop()