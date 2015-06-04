from tkinter import *
import logging
import os

import configuration
import server_checker



class ServerCheckTab(Frame):
    """"""

   #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        Frame.__init__(self, parent)

        self.group = LabelFrame(self, text="Double click on a node to check server status.", padx=5, pady=5)
        self.group.pack(padx=10, pady=10)

        self.left_column = LabelFrame(self.group)
        self.left_column.pack(padx=10, pady=10,side=LEFT)

        self.right_column = LabelFrame(self.group)
        self.right_column.pack(padx=10, pady=10,side=LEFT)

        self.select_label=Label(self.left_column, text="Select node")
        self.select_label.pack()
        self.listbox = Listbox(self.left_column, width=30, height=30)

        i=0
        for server in configuration.nodes:
            node=server[1].split(',')
            self.listbox.insert(i,node[0]+":"+node[3])
            i=i+1
        self.listbox.bind("<Double-Button-1>", self.OnDouble)
        self.listbox.pack(side="top", fill="both", expand=True)



        self.check_all_button = Button(self.group, text="Check all", command=self.checkAll)
        self.check_all_button.pack(side="bottom")
        self.clear_button = Button(self.group, text="Clear text", command=self.clear_text)
        self.clear_button.pack(side="bottom")


        self.ResultLabel=Label(self.right_column, text="Response")
        self.ResultLabel.pack()
        self.text1=Text(self.right_column, height=30, width=50)
        self.text1.pack()



    def clear_text(self):
        self.text1.delete("1.0", 'end')

    def OnDouble(self, event):
        value = re.search('(\()(\d{1,2})(,\))', str(self.listbox.curselection())).group(2)
        logging.debug(value)
        response= self.checkSelection(value)
        self.text1.tag_config("fail", foreground="red")
        tags = ("")
        if response.__contains__("Server not available"):
            print("fail")
            tags = ("fail",)
        self.text1.insert(END, response, tags)

    def checkSelection(self,selection):
        node=configuration.nodes[int(selection)]
        data=node[1].split(',')
        logging.debug(data)
        return server_checker.checkNode(data[0],data[3])

    def checkAll(self):
        message =""
        for node in configuration.nodes:
            data=node[1].split(',')
            logging.debug(data)
            message =server_checker.checkNode(data[0],data[3])
            self.text1.tag_config("fail", foreground="red")
            tags = ("")
            if message.__contains__("Server not available"):
                print("fail")
                tags = ("fail",)
            self.text1.insert(END, message, tags)




        #self.text1.insert(END, message)
       # self.text1.tag_config("Server not available", foreground="blue", font="Arial 10 italic")



