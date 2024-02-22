# porn-lib-python

Nodejs version reconstituted version https://github.com/sofia-gros/porn-lib

The python version is superior in speed.
The download function and thumbnail acquisition were broken in the nodejs version, but we fixed it here.


```python
import pornlib

xvideos = pornlib.PornLib(engine="xvideos")
list = xvideos.list(limit=12)
for item in list:
  # item == VideoDataClass

list = xvideos.list(keyword="cute") # same
list = xvideos.list(tag="Asian_Woman-32") # same

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

@dataclasses.dataclass
class VideoDownloadDataClass:
  low: str | None
  High: str | None
  hls: str | None
```
