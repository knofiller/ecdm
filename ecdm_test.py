import ecdm

res = ecdm.log_in()

if res.status_code != 200:
	print("fail to login ecdm!")
	# raise ApiError('Cannot log in : {}'.format(res.status_code))
# printf('login success. token is {}'.format(res.json()["x-auth-token"]))
print("login success!")

ecdm_token = res.json()["x-auth-token"]


# get tenants
res = ecdm.get_tenants(ecdm_token)

# Create vCenter creds
res = ecdm.create_creds(ecdm_token)
print res.status_code
print res.json()