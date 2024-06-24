import pornlib
xvideos = pornlib.PornLib(engine="xvideos", soupSleep=1)
# list = xvideos.list(limit=12)
# for item in list:
#   pass

# tags = xvideos.tags()
# tags = xvideos.tags(keyword="jap")

# list = xvideos.search(keyword="cute") # same
# list = xvideos.search(channel="xiaomaomi12138") # same
# list = xvideos.search(tag="Asian_Woman-32") # same
# list = xvideos.search(tag=tags) # same
# list = xvideos.search(best="2024-01") # same

# link = xvideos.getDownloadLink( list[0].link ) # xvideos video url 

list = xvideos.search(channel="japaneserxrx")
print(list)
link = xvideos.getDownloadLink( list[2].link )
print(link)