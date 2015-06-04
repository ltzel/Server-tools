import paramiko
import logging

import configuration
import re


def connectNode(s):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    command= "df"#sys.argv[1]
    logging.debug(s)
    node=configuration.nodes[int(s)]
    data=node[1].split(',')
    try:
        ssh.connect(data[0],22,data[1], data[2])
    except paramiko.SSHException:
        logging.error ("Connection Failed")
        return "Connection Failed"
    except:
        logging.error ("Connection Error")
        return "Connection Error"

    stdin,stdout,stderr = ssh.exec_command(command)
    return_value=""
    for line in stdout.readlines():
        text = re.search('(/dev/sda3)(.*)(\s\d{1,2}%).*', line)
        if text is not None:
            logging.debug (text.group(1)+": "+text.group(3)+"\n")
            return_value=return_value+text.group(1)+": "+text.group(3)+"\n"
    for line in stderr.readlines():
        logging.debug (line.strip())
        return_value=return_value+line.strip()
    return return_value
    ssh.close()
