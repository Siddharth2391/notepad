from tkinter import *
import tkinter.messagebox as msg
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename

class Notepad(Tk):
    global file
    file=None
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        # self.resizable(0,0)
        icon = PhotoImage(file='res/notepad.png')
        self.iconphoto(False,icon)
        self.title('Notepad')
        head=Label(self,text='Developed by Siddharth Dyamgond',bg='black',fg='tomato',font='Helvicta 8 bold').pack(fill=X,side=BOTTOM)
        self.navbar()
    
    def showinfo(self):
        msg1='This software is developed by Siddharth Dyamgond\ncopright@2021 SD Tech pvt. lmt.'
        a=msg.showinfo('About',msg1)
    
    #theme changing function
    def dtheme(self):
        textentry.config(bg='grey',fg='black')
    def ptheme(self):
        textentry.config(bg='pink',fg='black')
    def wtheme(self):
        textentry.config(bg='white',fg='black')

    #cut copy paste 
    def cut(self):
        textentry.event_generate('<<Cut>>')
    def copy(self):
        textentry.event_generate('<<Copy>>')
    def paste(self):
        textentry.event_generate('<<Paste>>')

    def save(self):
        global file
        if file==None:
            file=asksaveasfilename(initialfile='notepad.txt',defaultextension='.txt',filetypes=[('All files','*.*'),('Text Documents','*.txt')])
            if file=='':
                file=None
            else:
                f=open(file,'a')
                f.write(textentry.get(1.0,END))
                f.close()

    # def saveas(self):
    #     global file
    #     if file==None:
    #         file=asksaveasfilename(initialfile='notepad.txt',defaultextension='.txt',filetypes=[('All files','*.*'),('Text Documents','*.txt')])
    #         if file=='':
    #             file=None
    #         else:
    #             f=open(file,'w')
    #             f.write(textentry.get(1.0,END))
    #             f.close()
    #     else:
    #         f=open(file,'w')
    #         f.write(textentry.get(1.0,END))
    #         f.close()

    def openn(self):
        global file
        file=askopenfilename(defaultextension='.txt',filetypes=[('All files','*.*'),('Text Documents','*.txt')])
        if file=='':
            file=None
        else:
            self.title(os.path.basename(file)+'-Notepad')
            textentry.delete(1.0,END)
            f =open(file,'r')
            textentry.insert(1.0, f.read())
            f.close()

    def newfile(self):
        global file
        self.title('Untitled file -notepad')
        file=None
        textentry.delete(1.0,END)

    def navbar(self):
        n_menu=Menu(self)
        #menu1
        filemenu=Menu(n_menu,tearoff=0)
        filemenu.add_command(label='Open',command=self.openn)
        filemenu.add_command(label='New file',command=self.newfile)
        filemenu.add_separator()
        filemenu.add_command(label='Save',command=self.save)
        # filemenu.add_command(label='Save as',command=self.saveas)
        n_menu.add_cascade(label='File',menu=filemenu)
        #menu2
        editmenu=Menu(n_menu,tearoff=0)
        editmenu.add_command(label='Cut',command=self.cut)
        editmenu.add_command(label='Copy',command=self.copy)
        editmenu.add_command(label='Paste',command=self.paste)
        n_menu.add_cascade(label='Edit',menu=editmenu)
        #menu3
        thememenu=Menu(n_menu,tearoff=0)
        thememenu.add_command(label='Dark theme',command=self.dtheme)
        thememenu.add_command(label='White theme',command=self.wtheme)
        thememenu.add_command(label='Pink theme',command=self.ptheme)
        n_menu.add_cascade(label='Theme',menu=thememenu)

        n_menu.add_command(label='About',command=self.showinfo)
        n_menu.add_command(label='Quit',command=quit)
        global textentry
        textentry=Text(self,relief=FLAT,font='Times 18',cursor='arrow')
        textentry.pack(expand=True,fill=BOTH)
        #added scrollbar
        scroll=Scrollbar(textentry)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=textentry.yview)
        textentry.config(yscrollcommand=scroll.set)
        # textentry.bind('<Motion>',self.motion)
        self.config(menu=n_menu)


if __name__=='__main__':
    app = Notepad()
    app.mainloop()
