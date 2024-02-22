# porn-lib-python

Nodejs version reconstituted version https://github.com/sofia-gros/porn-lib

The python version is superior in speed.
The download function and thumbnail acquisition were broken in the nodejs version, but we fixed it here.


```python

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
