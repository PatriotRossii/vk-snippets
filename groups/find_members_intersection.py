import sys
import vk
import time

token = "TOKEN"
version = "VERSION"

session = vk.Session(access_token=token)
api = vk.API(session, v=version)

def get_members(api, group_id):
	spy_requests = api.groups.getMembers(group_id=group_id)
	count = spy_requests["count"]
	members = set(spy_requests["items"])
	
	if count > 1000:
		for i in range(1, (count // 1000) + 1):
			time.sleep(0.4)
			members.update(
				set(api.groups.getMembers(group_id=group_id, offset=i*1000)["items"])
			)
	return members

first_group = [int(e) for e in input("Please, enter first group of ids: ").replace(" ", "").split(",")]
second_group = [int(e) for e in input("Please, enter second group of ids: ").replace(" ", "").split(",")]
result = set()

first_members = [get_members(api, e) for e in first_group]
second_members = [get_members(api, e) for e in second_group]

for lhs in first_members:
	for rhs in second_members:
		result.update(lhs.intersection(rhs))
print(result)