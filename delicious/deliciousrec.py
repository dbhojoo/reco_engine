##new file for pydelicious

from pydelicious import get_popular, get_userposts, get_urlposts

def initialiseUserDict(tag, count=5):
	user_dict={}
	#get the top count of the popular posts
	for p1 in get_popular(tag=tag)[0:count]:
		#find all users who posted this
		for p2 in get_urlposts(p1['href']):
			user=p2['user']
			user_dict[user]={}
	return user_dict