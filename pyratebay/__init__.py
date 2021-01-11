from pyratebay.torrent import Torrent, URL
from pyratebay.categories import categories
import requests

def search(keyword, cats=[]):
	params = {
		'q':keyword,
		'cat':[]
	}
	for cat in cats:
		if cat in categories:
			params['cat'].append(str(categories[cat]['code']))
	params['cat'] = ','.join(params['cat'])

	r = requests.get(URL+'q.php', params=params)

	torrents = []
	try:
		for tor in r.json():
			torrent = Torrent(tor['id'], tor['name'], tor['info_hash'], tor['leechers'], tor['seeders'],
					tor['num_files'], tor['size'], tor['username'], tor['added'], tor['status'], tor['category'])
			torrents.append(torrent)
	except Exception as e:
		print('Error: ', e)
		return None

	return torrents

def get_torrent(torrent_id):
	r = requests.get(URL+'t.php', params={'id':torrent_id})

	try:
		tor = r.json()
	except Exception as e:
		print('Error: ', e)
		return None

	torrent = Torrent(str(tor['id']), tor['name'], tor['info_hash'], tor['leechers'], tor['seeders'],
			tor['num_files'], tor['size'], tor['username'], tor['added'], tor['status'], tor['category'])
	torrent.description = tor['descr']
	return torrent

def recent():
	r = requests.get(URL+'precompiled/data_top100_recent.json')
	torrents = []
	try:
		for tor in r.json():
			torrent = Torrent(tor['id'], tor['name'], tor['info_hash'], tor['leechers'], tor['seeders'],
					tor['num_files'], tor['size'], tor['username'], tor['added'], tor['status'], tor['category'])
			torrents.append(torrent)
	except Exception as e:
		print('Error: ', e)
		return None

	return torrents

def top100(category=None, subc=None):
	if category is None:
		r = requests.get('https://apibay.org/precompiled/data_top100_all.json')
	else:
		if category not in categories:
			raise Exception(f"{category} is not a valid category!")
		cat_n = categories[category]['code']
		if subc is not None and subc not in categories[category]['subs']:
			raise Exception(f"{subc} is not a valid sub-category!")
		elif subc is not None:
			cat_n += categories[category]['subs'][subc]
		r = requests.get(URL+f'precompiled/data_top100_{cat_n}.json')
	torrents = []
	try:
		for tor in r.json():
			torrent = Torrent(str(tor['id']), tor['name'], tor['info_hash'], tor['leechers'], tor['seeders'],
					tor['num_files'], tor['size'], tor['username'], tor['added'], tor['status'], tor['category'])
			torrents.append(torrent)
	except Exception as e:
		print('Error: ', e)
		return None
	return torrents

