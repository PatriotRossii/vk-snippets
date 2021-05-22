import sys
import time
import vk

from get_members import get_members

token = "TOKEN"
version = "VERSION"

session = vk.Session(access_token=token)
api = vk.API(session, v=version)

first_group = [int(e) for e in input("Please, enter first group of ids: ").replace(" ", "").split(",")]
second_group = [int(e) for e in input("Please, enter second group of ids: ").replace(" ", "").split(",")]
result = set()

first_members = [get_members(api, e) for e in first_group]
second_members = [get_members(api, e) for e in second_group]

for lhs in first_members:
	for rhs in second_members:
		result.update(lhs.intersection(rhs))
print(result)