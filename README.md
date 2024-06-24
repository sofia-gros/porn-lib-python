# porn-lib-python

Past Libraries Node.js https://github.com/sofia-gros/porn-lib

The python version is superior in speed.
The download function and thumbnail acquisition were broken in the nodejs version, but we fixed it here.

Please download and import the file or copy and paste it, as it is not uploaded to PyPI.

- [x] 動画リンクからダウンロードリンクの発行
- [x] チャンネル名で検索
- [ ] カテゴリー・タグリストの取得 
- [ ] 他のサイトを追加する(Pornhub系は別ライブラリに任せるので対応しない)

```cmd
pip install -r requirements.txt
```

```python
import pornlib

xvideos = pornlib.PornLib(engine="xvideos")
# xvideos = pornlib.PornLib(engine="xvideos", soupSleep=1) # soupSleepはサイトの読み込み遅延です。サイトが重かったりネット速度が遅いときに使用します。
list = xvideos.list(limit=12)
for item in list:
  # item == VideoDataClass

list = xvideos.search(keyword="cute") # same
list = xvideos.search(channel="xiaomaomi12138") # same
list = xvideos.search(tag="Asian_Woman-32") # same
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
```
