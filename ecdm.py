import requests
import json

ecdm_ip = '10.25.80.114'
port = 8443
headers = {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
}

#log on ecdm to get token
def log_in(headers=headers):
	
	payload = {
		'username': 'admin',
		'password': 'admin',
		'tenant': 'qaLandlord'
	}
	return requests.post(_url('/api/v1/login'), headers = headers, json=payload,verify=False)

def get_tenants(ecdm_token, headers=headers):
	headers['X-Auth-Token'] = ecdm_token
	return requests.get(_url('/api/v1/tenants'), headers=headers, verify=False)

def create_creds(ecdm_token, headers=headers):
	headers['X-Auth-Token'] = ecdm_token
	payload = '''
	{
		"id": null,
		"name": "vcenterCred",
		"attributes": {

		},
		"userTags": [

		],
		"links": [
			{
				"rel": "tenant",
				"href": "/tenants/00000000-0000-4000-a000-000000000000",
				"id": "00000000-0000-4000-a000-000000000000"
			}
		],
		"username": "administrator@vsphere.local",
		"password": "P3t3rPan@1",
		"type": "STANDARD"
	}
	'''
	return requests.post(_url('/api/v1/credentials'), headers=headers, json=json.loads(payload), verify=False)

def create_inventory_source():
	pass

def create_shallow_discovery_job():
	pass

def create_full_discovery_job():
	pass

def get_assets():
	pass

def _url(path):
	# return '{1}'.format('https://',ecdm_ip, str(port), path)
	return 'https://' + ecdm_ip + ':' + str(port) + path
