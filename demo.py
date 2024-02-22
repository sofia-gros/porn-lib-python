import pornlib
porn = pornlib.PornLib(engine="xvideos")
res = porn.list(limit=10)
print(res)
link = porn.getDownloadLink(res[0].link)
print(link)