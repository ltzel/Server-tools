from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.conf')
nodes=parser.items("NODES")
