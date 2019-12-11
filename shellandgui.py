import tkinter
import os
import subprocess

#variables

window_width = 700
window_height = 400
background_color = 'black'
text_color = "white"
text_font = "arial"
text_size = 10
insert_background = "white"
root = tkinter.Tk()
root.configure(width=window_width, height=window_height)

#functions

def keyevent(e):
    text_input = text.get("1.0",'end-1c')
    #if str(e.char) == '\r':
    if str(e.char) == '\x08':
        if str(text_input[-1:]) == '\n':
            pass
        else:
            text_input = text_input[:-1]
            text.configure(state='normal')
            text.delete("1.0",'end-1c')
            text.insert("1.0",text_input)
        text.configure(state='disabled')
    elif str(e.char) == '\r':
        text.configure(state='normal')
        #cmd = input(os.getcwd() + "--> ")
        cmd =  text_input
        cmd = cmd.split(">>>")[-1]
       
        if cmd.startswith("cd"):
            cmd = cmd.replace("cd ","")
            cmd = cmd.replace("'","")
            cmd = cmd.replace("\"","")
            print(cmd)
            os.chdir(cmd)
        elif cmd == "exit":
            root.quit()
        elif cmd == "clear":
            text.delete("1.0",'end-1c')
            text.insert('end', ">>>")
        else:
            output = subprocess.Popen(cmd,shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,encoding='utf-8')
            hi = output.stdout.read()
            text.insert('end', '\n')
            text.insert('end', hi)
            text.insert('end', ">>>")
        text.configure(state='disabled')
       
    else:    
        text.configure(state='normal')
        text.insert('end', str(e.char))
        text.configure(state='disabled')
       
text = tkinter.Text(root, bg=background_color,fg=text_color,font=(text_font, text_size),
                             state="disabled")
text.bind("<Key>",keyevent)

text.configure(state='normal')
text.insert('end', ">>>")
text.configure(state='disabled')
text.pack()

root.mainloop()