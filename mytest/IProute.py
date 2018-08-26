#  -*- coding: utf-8 -*-

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        che46 = StringVar()
        che52 = StringVar()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("488x266+396+135")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.29, rely=0.15,height=17, relwidth=0.3)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.12, rely=0.15, height=23, width=17)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''IP''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.12, rely=0.26, height=23, width=41)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''MASK''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.12, rely=0.41, height=23, width=19)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''ID''')

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.29, rely=0.26,height=17, relwidth=0.3)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.29, rely=0.41,height=17, relwidth=0.3)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.18, rely=0.83, height=28, width=43)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=ipRoute_support.count)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''count''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.55, rely=0.83, height=28, width=37)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=ipRoute_support.exec)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''exec''')

        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.68, rely=0.34, relheight=0.1
                , relwidth=0.13)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(overrelief="flat")
        self.Radiobutton1.configure(text='''Radio''')

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.84, rely=0.34, relheight=0.1
                , relwidth=0.13)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Radio''')

        self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.82, rely=0.19, relheight=0.1
                , relwidth=0.13)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Check''')
        self.Checkbutton2.configure(variable=che52)

        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.12, rely=0.53, relheight=0.23, relwidth=0.7)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=344)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)


        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.68, rely=0.19, relheight=0.1
                , relwidth=0.13)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''delete''')
        self.Checkbutton1.configure(variable=che46)

class ipRoute_support():

    def __init__(self,top,gui,*args,**kwargs):
        global w, top_level, root
        w = gui
        top_level = top
        root = top
        w.Checkbutton1.deselect()
        w.Checkbutton2.deselect()
        w.Checkbutton1.onvalue = 1
        w.Checkbutton1.offvalue = 0
        pass

    @classmethod
    def count(self):
        print('ipRoute_support.count')
        sys.stdout.flush()
        ip = w.Entry1.get()
        mask = w.Entry2.get()
        id = w.Entry3.get()
        if 0 == 0:
            w.Listbox1.insert(0,ip + mask + id)
        else:
            w.Listbox1.insert(0,ip+'and'+mask+'and'+id)

    @classmethod
    def delete(self):
        print('ipRoute_support.delete')
        sys.stdout.flush()

    @classmethod
    def exec(self):
        print('ipRoute_support.exec')
        sys.stdout.flush()

    def destroy_window(self):
        # Function which closes the window.
        global top_level
        top_level.destroy()
        top_level = None


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global root
    root = Tk()
    top = New_Toplevel (root)
    ipRoute_support(root, top)
    root.mainloop()

# w = None
# def create_New_Toplevel(root, *args, **kwargs):
#     '''Starting point when module is imported by another program.'''
#     global w, rt
#     rt = root
#     w = Toplevel (root)
#     top = New_Toplevel (w)
#     ipRoute_support(w, top, *args, **kwargs)
#
#     return (w, top)
#
# def destroy_New_Toplevel():
#     global w
#     w.destroy()
#     w = None


if __name__ == '__main__':
    vp_start_gui()


