import requests
from bs4 import BeautifulSoup
import dataclasses
import re
import datetime
# from robobrowser import RoboBrowser


class PornLib():
  def __init__(self, engine = "xvideos"):
    self.engine = engine
  
  def list(self, limit=10):
    self.limit = limit
    
    if self.engine == "xvideos":
      return self._xvideos_list()
    else:
      pass
  
  def search(self, keyword=None, tag=None, best=None, limit=100):
    self.keyword = keyword
    self.tag = tag
    self.best = best if best else f"{datetime.date.today().year}-{datetime.date.today().month}"
    self.limit = limit
    
    if self.engine == "xvideos":
      return self._xvideos_search()
    else:
      pass
  
  def getDownloadLink(self, link):
    if self.engine == "xvideos":
      return self._xvideos_getDownloadLink(link)
    else:
      pass

  def getSoup(self, url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    return soup

  def _xvideos_list(self, root=False):
    if not root: root = self.getSoup("https://www.xvideos.com/")
    list = root.select(".mozaique .thumb-block", limit=self.limit)
    res = []
    for item in list:
      title = item.select_one(".title a").text
      img = item.select_one(".thumb a img").get("data-src")
      link = "https://www.xvideos.com" + item.select_one(".thumb a").get("href")
      quality = item.select_one(".video-hd-mark")
      if not quality: quality = False
      else: quality = int(re.sub(r"\D", "", quality.text))
      time = item.select_one(".duration").text
      channel_name = item.select_one(".metadata .name").text
      channel_link = f"https://www.xvideos.com{item.select_one(".metadata a").get("href")}"
      res.append(VideoDataClass(title, img, link, quality, time, channel_name, channel_link))
    return res
  
  def _xvideos_search(self):
    if self.keyword:
      root = self.getSoup(f"https://www.xvideos.com/?k={self.keyword}")
      return self._xvideos_list(root=root)
    elif self.tag:
      root = self.getSoup(f"https://www.xvideos.com/c/{self.tag}")
      return self._xvideos_list(root=root)
    elif self.best:
      root = self.getSoup(f"https://www.xvideos.com/best/{self.best}")
      return self._xvideos_list(root=root) 
    
  def _xvideos_getDownloadLink(self, url):
    root = self.getSoup(url)
    script = str(root.select("#video-player-bg script")[4])
    
    low = re.findall(r"setVideoUrlLow\('(.*)'", script)
    high = re.findall(r"setVideoUrlHigh\('(.*)'", script)
    hls = re.findall(r"setVideoUrlHLS\('(.*)'", script)
    return VideoDownloadDataClass(low, High, hls)

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

