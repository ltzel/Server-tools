from tkinter import *
import logging
import configuration
import remote
logging.basicConfig(level=logging.DEBUG)


class DiskCheckerTab(Frame):
    """"""

   #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        Frame.__init__(self, parent)


        self.group = LabelFrame(self, text="Double click a node to get the disk size.", padx=5, pady=5)
        self.group.pack(padx=10, pady=10)

        self.left_column = LabelFrame(self.group)
        self.left_column.pack(padx=10, pady=10,side=LEFT)

        self.rightColumn = LabelFrame(self.group)
        self.rightColumn.pack(padx=10, pady=10,side=LEFT)


        self.select_label=Label(self.left_column, text="Select node")
        self.select_label.pack()
        self.listbox = Listbox(self.left_column, height=30, width=30)

        i=0
        for server in configuration.nodes:
            node=server[1].split(',')
            self.listbox.insert(i,node[0])
            i=i+1
        self.listbox.bind("<Double-Button-1>", self.OnDouble)
        self.listbox.pack(side="top", fill="both", expand=True)

        self.result_label=Label(self.rightColumn, text="Response")
        self.result_label.pack()
        self.text1=Text(self.rightColumn, height=30, width=50)
        self.text1.pack()

        self.check_all_button = Button(self.group, text="Check all", command=self.checkAll)
        self.check_all_button.pack(side="bottom")
        self.clear_button = Button(self.group, text="Clear text", command=self.clear_text)
        self.clear_button.pack(side="bottom")



    def clear_text(self):
        self.text1.delete("1.0", 'end')

    def checkAll(self):
        i=0
        response=''
        for server in configuration.nodes:
            node=server[1].split(',')
            response_value=remote.connectNode(i)
            response=node[0]+":"+node[3]+"="+response_value
            i=i+1
            self.text1.tag_config("fail", foreground="red")
            tags = ("")
            text = re.search(' \d{1,2}', response_value)
            if int(text.group(0))>90:
                tags = ("fail",)
            self.text1.insert(END, response, tags)



    def OnDouble(self, event):

        #widget = event.widget
        #selection=widget.curselection()
        value = re.search('(\()(\d{1,2})(,\))', str(self.listbox.curselection())).group(2)
        logging.debug(value)
        server = configuration.nodes[int(value)]
        node=server[1].split(',')

        #value = widget.get(selection[0])
        response_value = remote.connectNode(value)
        response= node[0]+":"+node[3]+response_value

        self.text1.tag_config("fail", foreground="red")
        tags = ("")
        text = re.search(' \d{1,2}', response_value)

        if int(text.group(0))>90:
            tags = ("fail",)
        self.text1.insert(END, response, tags)





