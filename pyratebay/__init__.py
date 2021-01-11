from pyratebay.torrent import Torrent, URL
import requests

def search(keyword, audio=False, video=False, applications=False, games=False, porn=False, other=False):
	params = {
		'q':keyword,
		'cat':[]
	}
	if audio: params['cat'].append('100')
	if video: params['cat'].append('200')
	if applications: params['cat'].append('300')
	if games: params['cat'].append('400')
	if porn: params['cat'].append('500')
	if other: params['cat'].append('600')
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