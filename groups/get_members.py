import time
import vk

def get_members(api: vk.API, group_id: int, delay: float = 0.4):
	spy_requests = api.groups.getMembers(group_id=group_id)
	count = spy_requests["count"]
	members = set(spy_requests["items"])
	
	if count > 1000:
		for i in range(1, (count // 1000) + 1):
			time.sleep(delay)
			members.update(
				set(api.groups.getMembers(group_id=group_id, offset=i*1000)["items"])
			)
	return members
