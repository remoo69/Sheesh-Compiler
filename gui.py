from tkinter import *
from tkinter import constants
from tkinter import ttk


# run error reporting
def fill_err_table():
    pass

# run lexer function
def fill_lex_table():
    pass




root = Tk()

root.geometry("939x617")
root.resizable(False,False)
root.title("Sheesh Compiler")



# configure background color
root.configure(bg="#2D2D2D")

style = ttk.Style()
style.theme_use("clam")  # Use the "clam" theme, which works well with customizations
style.configure("Vertical.TScrollbar", troughcolor="#202020", background="#202020", gripcount=0, gripcolor="#202020")

# setting main layout
mainpane = Canvas(
    root,
    bg="#202020",
    height=617,
    width=939,
    bd=0,
    highlightthickness=0,
    relief="ridge")

mainpane.place(x=0,y=0)

# setting editor section
txt_editor_pane = Text(
    bd=0,
    bg="#272727",
    # highlightcolor=
    highlightthickness=0,
    fg="#FFFFFF",
    insertbackground="white",
    padx=10,
    pady=10,
    font=('Open Sans', 11,),) 

txt_editor_pane.place(x=10,y=40,
                      width=600,height=390)

# setting lexer output section
lex_table_pane = Text(
    bd=0,
    bg="#272727",
    highlightthickness=0,
    fg="#211B36",
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
    bg = "#272727",
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

# title = mainpane.create_text(
#     10, 20,
#     text="Sheesh",
#     font=('Open Sans ExtraBold', 20),
#     fill="#211B36",
# )

# setting lexer output section
err_pane = Text(
    bd=0,
    bg="#272727",
    highlightthickness=0,
    fg="#211B36",
    padx=10,
    pady=10,
    font=('Open Sans', 10),
    state = "disabled",)

err_pane.place(x=10,y=435,
               width=600,height=170)


# run lexer function button
run_img = PhotoImage(file="assets/run.png") 
lex_btn = Button(
        image=run_img,
        compound=LEFT,
        bg="#272727",
        borderwidth=0,
        highlightthickness=0,
        activebackground="#AAAAAA",
        fg="#079AD2",
        # activeforeground="#FFFFFF",
        justify="center",
        # command=run_lex,
)

lex_btn.place(x=15,y=10,width=25,height=25)


scrollbar = ttk.Scrollbar(
    txt_editor_pane, 
    orient='vertical',
    command=txt_editor_pane.yview,
)
scrollbar.pack(side=RIGHT, fill=Y)

txt_editor_pane['yscrollcommand'] = scrollbar.set

root.mainloop()