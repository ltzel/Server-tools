from tkinter import *
from tkinter import ttk

import configuration_tab
import disk_checker_tab
import server_check_tab

class Core(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()


        self.group = LabelFrame(self.myContainer1, text="Double click a node to get the disk size.", padx=5, pady=5)
        self.group.pack(padx=10, pady=10)


        note = ttk.Notebook(root)
        server_checker=server_check_tab.ServerCheckTab(note)
        disk_checker=disk_checker_tab.DiskCheckerTab(note)
        configuration = configuration_tab.ConfigurationTab(note)
        note.add(server_checker, text = "Server check")
        note.add(disk_checker, text = "Disk check")
        note.add(configuration, text = "Configuration")
        note.pack()



def getTab(parent,name):
        tab = Frame(parent)
        Button(tab, text='Exit', command=root.destroy).pack(padx=100, pady=100)
        parent.add(tab, text = name)

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    root.wm_title("Server tools")
    main_app = Core(root)
    root.mainloop()
