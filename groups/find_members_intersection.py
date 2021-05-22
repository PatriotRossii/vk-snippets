import sys
import time
import vk

from get_members import get_members

def find_intersection(api, *group_ids):
	members = [get_members(api, group_id) for group_id in group_ids]
	return set.intersection(*members)

if __name__ == "__main__":
	token = "TOKEN"
	version = "VERSION"

	session = vk.Session(access_token=token)
	api = vk.API(session, v=version)

	group_ids = [int(e.strip()) for e in sys.stdin.readlines()]
	print(api, *group_ids)