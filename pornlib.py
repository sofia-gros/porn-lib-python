import requests
from bs4 import BeautifulSoup
import dataclasses
import re
from selenium import webdriver
import time

driver = None
bs4_start = False
def bs4_init():
  global bs4_start
  global driver
  if bs4_start is True:
    return
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  driver = webdriver.Chrome(options=options)

class PornLib():
  def __init__(self, engine = "xvideos", soupSleep=0.5):
    self.engine = engine
    self.soupSleep = soupSleep

  def list(self, limit=10):
    self.limit = limit
    
    if self.engine == "xvideos":
      return self._xvideos_list()
    else:
      pass
  
  def _tags(self):
    if self.engine == "xvideos":
      return self._xvideos_tags()
    else:
      pass
  
  def tags(self, keyword = None):
    if keyword is None:
      return self._tags()
    else:
      for tags in self._tags():
        if re.findall(keyword, tags.name) or re.findall(keyword, tags.id):
          return tags
      return None
  
  def search(self, keyword=None, channel=None, tag=None, best=None, limit=100):
    self.keyword = keyword
    self.channel = channel
    self.tag = tag
    self.best = best
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
  
  def getSeleniumSoup(self, url):
    bs4_init()
    driver.get(url)
    time.sleep(self.soupSleep)
    html = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
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
      channel_link = f'https://www.xvideos.com{item.select_one(".metadata a").get("href")}'
      res.append(VideoDataClass(title, img, link, quality, time, channel_name, channel_link))
    return res
  
  def _xvideos_search(self):
    if self.keyword:
      root = self.getSoup(f"https://www.xvideos.com/?k={self.keyword}")
      return self._xvideos_list(root=root)
    elif self.channel:
      root = self.getSeleniumSoup(f"https://www.xvideos.com/profiles/{self.channel}#_tabVideos")
      return self._xvideos_list(root=root)
    elif self.tag:
      root = self.getSoup(f"https://www.xvideos.com/c/{self.tag}")
      return self._xvideos_list(root=root)
    elif self.best:
      root = self.getSoup(f"https://www.xvideos.com/best/{self.best}")
      return self._xvideos_list(root=root) 
    
  def _xvideos_tags(self):
    root = self.getSoup("https://www.xvideos.com/tags")
    list = root.select("#tags li")
    res = []
    for item in list:
      id = item.select_one("a b").get_text()
      id = str.strip(id)
      res.append(Tags(id, id))
    return res
    
  def _xvideos_getDownloadLink(self, url):
    root = self.getSoup(url)
    script = str(root.select("#video-player-bg script")[4])
    
    low = re.findall(r"setVideoUrlLow\('(.*)'", script)
    high = re.findall(r"setVideoUrlHigh\('(.*)'", script)
    hls = re.findall(r"setVideoUrlHLS\('(.*)'", script)
    return VideoDownloadDataClass(low, high, hls)

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