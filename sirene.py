import requests
from dateutil import parser
import datetime
import os

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = open(os.path.join(pasta, "jira.txt"), "r")
jira = arquivo.read()

r = requests.get('https://3itconsultoria.atlassian.net/rest/api/2/search?jql=status%20in%20(Open%2C%20Reopened)%20AND%20priority%20%3D%20"URGENTE!!!"%20ORDER%20BY%20created%20DESC', 
	headers={"Content-type": "application/json", "Authorization": jira.rstrip('\n')})

lista = r.json()

for atv in lista["issues"]:
	dt = parser.parse(atv["fields"]["created"])
	agora = datetime.datetime.now()

	dt = dt.replace(second=0, microsecond=0) 
	agora = agora.replace(second=0, microsecond=0)

	print(agora)

	if agora == dt:
		print(dt)
		print(datetime.datetime.now())
	break