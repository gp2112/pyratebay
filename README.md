# pyratebay
A python module for The Pirate Bay's API

# Get a Torrent by TPB's id:
```
>>> import pyratebay
>>> 
>>> torrent = pyratebay.get_torrent('3212527')
>>> print(torrent)
Name: metallica-garage inc 1998 -TFaMP3
Hash: 5837662C9310A6ACBA78A2E730783734C6E542DD
URL: https://thepiratebay.org/description.php?id=3212527
```
# Generating a Magnet URI
```
>>> import pyratebay
>>> 
>>> torrent = pyratebay.get_torrent('3212527')
>>> torrent.magnet()
'magnet:?xt=urn:btih:5837662C9310A6ACBA78A2E730783734C6E542DD&dn=metallica-garage inc 1998 -TFaMP3'
```
# Searching Torrents:
```
>>> import pyratebay
>>>
>>> torrents = pyratebay.search('metallica', audio=True)
>>> for torrent in torrents:
...      print(torrent)
Name: metallica-garage inc 1998 -TFaMP3
Hash: 5837662C9310A6ACBA78A2E730783734C6E542DD
URL: https://thepiratebay.org/description.php?id=3212527
Name: metallica-live in gothenburg se 0213-(sbd)-1987-fkk
Hash: 854611944C4DD918BFB223EFE4B402EC46F7D8D2
URL: https://thepiratebay.org/description.php?id=3212531
Name: Metallica Collection
Hash: 732D2EFCA88A2C36F988FFF890C67E1EA0426D35
URL: https://thepiratebay.org/description.php?id=3213928
Name: Metallica St anger
Hash: 6D55908EE11BE679607B58C66562C15A1B837A19
URL: https://thepiratebay.org/description.php?id=3216427
Name: Metallica-Kill Em All-1983-RETAIL-FRAiS
Hash: 192338F006C66EA36DA29D3D33980B1C56D757EF
URL: https://thepiratebay.org/description.php?id=3217679
...
```
