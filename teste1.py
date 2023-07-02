from tkinter import *
  
root = Tk() 
root.geometry("700x700") 
   
w = Label(root, text ='GeeksForGeeks', 
          font = "50")  
  
w.pack() 
   
scroll_bar = Scrollbar(root) 
  
scroll_bar.pack( side = RIGHT, 
                fill = Y ) 
   
mylist = Listbox(root,  
                 yscrollcommand = scroll_bar.set,width=600 ) 
   
for line in range(1, 100): 
    mylist.insert(END, "Geeks " + str(line)+"grees"+"Geeks " + str(line)+"grees"+"Geeks " + str(line)+"grees"+"Geeks " + str(line)+"grees""Geeks " + str(line)+"grees") 
  
mylist.pack( side = LEFT, fill = BOTH ) 
  
scroll_bar.config( command = mylist.yview ) 
   
root.mainloop() 