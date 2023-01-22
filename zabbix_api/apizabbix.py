from zabbix_api import ZabbixAPI
from pprint import pprint
 
server = "http://192.168.100.30/zabbix"
username = "Admin"      #Usuário
password = "zabbix"     # Senha

#Instanciando a API
zapi = ZabbixAPI(server = server, path="", log_level=6)
zapi.login(username, password)

# Obtendo lista de hosts
hosts = zapi.host.get({"output": ["hostid","name"], "sortfield": "hostid"})


#Instanciando a API
# zapi = ZabbixAPI(server = server, path="", log_level=6)
# zapi.login(username, password)

# Obtendo uma lista com os hosts que já estão no zabbix
# hosts = zapi.host.get({"output": ["hostid","name"], "sortfield": "name"}) 
# pprint(hosts)

# Cadastro  de hosts
# zapi.host.create({"host": "Centos", 
#                  "interfaces": [ {"type": "1",
#                  "main": "1",
#                  "useip": "1",
#                  "ip": "19.168.0.1",
#                  "dns": "",
#                  "port": "10052"}],
#                  "groups": [{ "groupid": "2"}],
#                  "templates": [{ "templateid": "10001"}]})

# Delete de host
# zapi.host.delete({"hostid": "10185"}

#Obtendo lista dos hostgroup
#hostgroups = zapi.hostgroup.get({"output": "extend", "sortfield": "name"})