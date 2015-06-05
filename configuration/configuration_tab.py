from tkinter import *
import functools
import logging

from configuration import configuration
logging.basicConfig(level=logging.ERROR)


class ConfigurationTab(Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        Frame.__init__(self, parent)

        groups=[]
        self.master_group = LabelFrame(self)
        self.master_group.pack(side=LEFT)
        self.left_group = LabelFrame(self.master_group, text="Edit existing nodes")
        self.left_group.pack(side=LEFT)
        self.entries=[]
        i=0
        for server in configuration.nodes:
            if i%7==0:
                self.group = LabelFrame(self.left_group, padx=5)
                self.group.pack(padx=10, pady=10,side=LEFT)

                groups.append(self.group)

            current_group= groups[int(i/7)]

            data=server[1].split(',')

            self.node_group = LabelFrame( current_group,  padx=1, pady=1)
            self.node_group.pack(padx=2, pady=2)

            self.entry_name=Entry(self.node_group,width=25)
            self.entry_name.insert(0, data[0])
            self.entry_name.pack(side=LEFT)

            self.entry_username=Entry(self.node_group,width=10)
            self.entry_username.insert(0, data[1])
            self.entry_username.pack(side=LEFT)

            self.entry_password=Entry(self.node_group,width=10,show = "*")
            self.entry_password.insert(0, data[2])
            self.entry_password.pack(side=LEFT)

            self.entry_port=Entry(self.node_group,width=10)
            self.entry_port.insert(0, data[3])
            self.entry_port.pack(side=LEFT)

            self.path_group = LabelFrame( self.group,  padx=1, pady=1)
            self.path_group.pack(padx=1, pady=1)

            self.delete_button = Button(self.node_group, text="Delete node", command=functools.partial(self.deleteEntry,i) )
            self.delete_button.pack()
            self.entries.append([self.entry_name,self.entry_username,self.entry_password,self.entry_port,self.delete_button,self.node_group])
            self.separator = Frame(self.group,height=5, bd=5, relief=SUNKEN)
            self.separator.pack(fill=X, padx=1, pady=1)
            i=i+1


        self.new_node_general_group = LabelFrame( self.master_group, text="Add new node")
        self.new_node_general_group.pack(padx=2, pady=2)
        self.new_node_group = LabelFrame( self.new_node_general_group,  padx=1, pady=1)
        self.new_node_group.pack(padx=2, pady=2)

        self.selectLabel=Label(self.new_node_group)
        self.selectLabel.pack()
        self.label = LabelFrame(self.new_node_group, text="Node name", padx=1, pady=1)
        self.label.pack(padx=1, pady=1,side=LEFT)

        self.new_node_name_group=Entry(self.label ,width=35)
        self.new_node_name_group.pack(side=LEFT)

        self.label = LabelFrame(self.new_node_group, text="Username", padx=1, pady=1)
        self.label.pack(padx=1, pady=1,side=LEFT)
        self.username_group=Entry(self.label ,width=10)
        self.username_group.pack(side=LEFT)

        self.label = LabelFrame(self.new_node_group, text="Password", padx=1, pady=1)
        self.label.pack(padx=1, pady=1,side=LEFT)
        self.password_group=Entry(self.label ,width=10)
        self.password_group.pack(side=LEFT)

        self.label = LabelFrame(self.new_node_group, text="Port", padx=1, pady=1)
        self.label.pack(padx=1, pady=1,side=LEFT)
        self.portGroup=Entry(self.label ,width=10)
        self.portGroup.pack(side=LEFT)

        self.newNodePathGroup = LabelFrame( self.new_node_general_group,  padx=1, pady=1)
        self.newNodePathGroup.pack(padx=1, pady=1)

        self.addNode_button = Button(self.new_node_general_group, text="Add node", command=self.addEntry )
        self.addNode_button.pack()


        self.save_button = Button(self.master_group , text="Save changes", command=self.saveNodes)
        self.save_button.pack()

    def deleteEntry(self,position):
        logging.debug("Removing "+str(position))
        entry = self.entries[position]
        entry[0].destroy()
        entry[1].destroy()
        entry[2].destroy()
        entry[3].destroy()
        entry[4].destroy()
        entry[5].destroy()


    def addEntry(self):
        if self.new_node_name_group.get() and self.username_group.get() and self.password_group.get() :
            position=len(self.entries)
            self.node_group = LabelFrame( self.group,  padx=1, pady=1)
            self.node_group.pack(padx=2, pady=2)

            self.entry_name=Entry(self.node_group,width=25)
            self.entry_name.insert(0, self.new_node_name_group.get())
            self.entry_name.pack(side=LEFT)

            self.entry_username=Entry(self.node_group,width=10)
            self.entry_username.insert(0,self.username_group.get())
            self.entry_username.pack(side=LEFT)

            self.entry_password=Entry(self.node_group,width=10)
            self.entry_password.insert(0, self.password_group.get())
            self.entry_password.pack(side=LEFT)

            self.entry_port=Entry(self.node_group,width=10)
            self.entry_port.insert(0, self.portGroup.get())
            self.entry_port.pack(side=LEFT)

            self.delete_button = Button(self.node_group, text="Delete node", command=functools.partial(self.deleteEntry,position) )
            self.delete_button.pack(side="left")
            self.entries.append([self.entry_name,self.entry_username,self.entry_password,self.entry_port,self.delete_button,self.node_group])



    def saveNodes(self):

        i=0
        for entry in self.entries:
            if  entry[0].winfo_exists() and entry[1].winfo_exists() and entry[2].winfo_exists() and entry[3].winfo_exists():
                logging.debug(entry[0].get()+","+entry[1].get()+","+entry[2].get())
                configuration.parser.set('NODES',str(i), entry[0].get()+","+entry[1].get()+","+entry[2].get()+","+entry[3].get())
            else:
                configuration.parser.remove_option('NODES',str(i))
            i=i+1
        configuration.parser.write(open('config.conf','w'))
        self.update()
        self.save_button.destroy()
        w = Message(self.master_group, text="Please restart the application to use the new configuration.", width=400)
        w.pack()


