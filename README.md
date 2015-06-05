# Server-tools
# Synopsis
I have created this project to share some Python scripts that I use to monitor remote servers. 
The Server-tools include the following tools:

1. Server check. Checks whether a node (e.g. localhost:8080) is up
2. Disk check. Shows the percentage of the disk usage of a remote server(ssh).

The tool provides a GUI using the tkinter library. 

#Screenshots
###### Configuration
![configuration](/screenshots/configuration.png)

###### Server check
![Server check](/screenshots/server_check.png)

###### Disk check
![Disk check](/screenshots/disk_check.png)

#Environments 
The tool has been tested only in Windows 7.

#Requirements
The tool requires Python 3.4. You should also install the 'paramiko' library.

#Running the tool
execute:
```python core.pyw```

###### Server check
Double click on a server to check its status or click on the *Check all* button to check all the servers.

###### Disk check
Double click on a server to check its disk usage or click on the *Check all* button to check all the servers.

#Configuration
For every node the following information is required:
1. server name
2. username
3. password
4. port

You can manualy edit an existing node or add a server file by adding new entries under [NODES] in the config.conf:
```[NODES]
0 = test.webisite1.com,test,test123!,8080
1 = test.webisite2.com,test,test123!,8080
2 = test.webisite3.com,test,test123!,8080
```
Every row should have a unique index number and then the server information:
*x=server,username,password,port*


###### Add new server using configuration
1. Go to the configuration tab
2. Add the information to the *Add new node* section
3. Click on the *Add node* button
4. Click on the *Save changes* button
5. Restart the program

###### Edit existing server using configuration
1. Go to the configuration tab
2. Edit an exiting node
3. Click on the *Save changes* button
4. Restart the program







