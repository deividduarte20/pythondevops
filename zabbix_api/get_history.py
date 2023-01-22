from zabbix_api import ZabbixAPI

URL = 'http://192.168.100.30/zabbix'
USERNAME = 'Admin'
PASSWORD = 'zabbix'

try:
    zapi = ZabbixAPI(URL, timeout=180)
    zapi.login(USERNAME, PASSWORD)
    print(f'Conectado a API do Zabbix. {zapi.api_version()}')
except:
    print(f'Não foi possível conectar! {erro}')
    exit()

# Função que obtem id e nome do host
# def get_hostgroup(hostgroup_name):
#     hostgroup = zapi.hostgroup.get({
#       "output": "extend",
#       "filter" : {"name": hostgroup_name} 
#     })
#     hostgroup_id = hostgroup[0]['groupid']
#     hostgroup_name = hostgroup[0]['name']
#     temp_dict = {}
#     temp_dict['hostgroup_id'] = hostgroup_id
#     temp_dict['hostgroup_name'] = hostgroup_name
#     return temp_dict

# hostgroup_name = 'Zabbix servers'
# hostgroup_info = get_hostgroup(hostgroup_name)
# hostgroup_id = hostgroup_info['hostgroup_id']

# hosts = zapi.host.get({
#     "output": ['name', 'state'],
#     "groupids": hostgroup_id
# })
# print(hosts)

# Cria hostgroup
# new_hostgroup = zapi.hostgroup.create({
#     "name": "Hostgroup_Via_Api"
# })
# print(new_hostgroup)

# Consulta todos os hostgroups
# hostgroups = zapi.hostgroup.get({
#     "output": "extend"
# })
# print(hostgroups)

# Filter hostgroup in especific
# hostgroups = zapi.hostgroup.get({
#     "output": "extend",
#     "filter": {"name": "Zabbix servers"}
# })
# print(hostgroups)

# Filtra todos os hosts
# device = zapi.host.get({
#     "output": "extend"
# })
# print(device)

# Filtra host em especifico
# device = zapi.host.get({
#     # "filter": {"host": "Smartphone deivid"}
# })
# print(device)

