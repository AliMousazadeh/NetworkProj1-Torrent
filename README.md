# NetworkProj1-Torrent
https://github.com/AliMousazadeh/NetworkProj1-Torrent

p2p.py is server.py merged with client.py. These files are not directly executed.

Run p2p with the same format as in the project:

first run:
python p2p.py -serve -name [file name] -path [path]

Example:
python p2p.py -serve -name rectest.txt -path E:\\Beheshti\\term8\\network\\proj1\\torrent\\rectest.txt

Now all future clients connected to this machine that request [file name] will receive it, with downloaded__ prefix added to [file name].

Then run:
python p2p.py -receive [file name]

Example:
python p2p.py -receive rectest.txt

Now if a machine is connected to this machine, a request for [file name] will be sent to it and if it exists and the other machine is executed with the same [file name] in its arguments, the file will be transfered with a downloaded__ prefix added to [file name].