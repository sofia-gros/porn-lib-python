# porn-lib-python

https://github.com/sofia-gros/porn-lib-python

- [x] 動画リンクからダウンロードリンクの発行
- [x] チャンネル名で検索
- [x] カテゴリー・タグリストの取得 
- [ ] 他のサイトを追加する(Pornhub系は別ライブラリに任せるので対応しない)


```python
import pornLib

xvideos = pornLib.PornLib(engine="xvideos")
# xvideos = pornlib.PornLib(engine="xvideos", soupSleep=1) # soupSleepはサイトの読み込み遅延です。サイトが重かったりネット速度が遅いときに使用します。
list = xvideos.list(limit=12)
for item in list:
  # item == VideoDataClass

tags = xvideos.tags()
tags = xvideos.tags(keyword="jap")
# Tags or [ ...Tags ]

list = xvideos.search(keyword="cute") # same
list = xvideos.search(channel="xiaomaomi12138") # same
list = xvideos.search(tag="Asian_Woman-32") # same
list = xvideos.search(tag=tags) # same
list = xvideos.search(best="2024-01") # same

link = xvideos.getDownloadLink( list[0].link ) # xvideos video url 
# link == VideoDownloadDataClass
```


```python
@dataclasses.dataclass
class VideoDataClass:
  title: str
  img: str  
  link: str
  quality: int
  time: str
  channel_name: str
  channel_link: str

@dataclasses.dataclass
class VideoDownloadDataClass:
  low: str | None
  high: str | None
  hls: str | None

@dataclasses.dataclass
class Tags:
  name: str | None
  id: str | None
```
