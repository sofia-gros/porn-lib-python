import pornlib
porn = pornlib.PornLib(engine="xvideos", soupSleep=1)
# res = porn.list(limit=10)
# print(res)

res = porn.search(limit=10, channel="xiaomaomi12138")
link = porn.getDownloadLink(res[0].link)
print(link)