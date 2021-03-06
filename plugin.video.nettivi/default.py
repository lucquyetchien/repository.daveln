# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/>  
'''                                                                           

import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon

mysettings=xbmcaddon.Addon(id='plugin.video.nettivi')
profile=mysettings.getAddonInfo('profile')
home=mysettings.getAddonInfo('path')
fanart=xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon=xbmc.translatePath(os.path.join(home, 'icon.png'))
logos=xbmc.translatePath(os.path.join(home, 'logos\\'))
localm3u=mysettings.getSetting('local_m3u')
onlinem3u=mysettings.getSetting('online_m3u')
localxml=mysettings.getSetting('local_xml')
onlinexml=mysettings.getSetting('online_xml')
#m3u_regex='#EXTINF.+,(.+)\s(.+?)\s'
m3u_regex='#EXTINF.+,(.+)\s(.+?)\n'
xml_regex='<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
hotChannels='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/hotchannels.xml'
viet_tv='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/viet_tv.m3u'
sctv='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/SCTV.m3u'
tvchannels='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/tvchannels.json'
haotivi='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/haotivi.json'
vietnamtv='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/vietnamtv.xml'
giniko='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/giniko.xml'
thanh51='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/thanh51.m3u'
ATF01='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/ATF01.m3u'
htvonline='http://www.htvonline.com.vn/livetv'
wezatv='http://www.wezatv.com'
fptplay='http://fptplay.net'
tv24vn='http://www.tv24.vn'
anluongtv='http://tv.anluong.info/'
tvreplay='http://103.31.126.20/tvcatchup/'
zuitv='http://zui.vn/livetv.html'
token = 'token=1b#K8!3zc65ends!'
   
def makeRequest(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    response=urllib2.urlopen(req)
    link=response.read()
    response.close()  
    return link
  except urllib2.URLError, e:
    print 'We failed to open "%s".' % url
    if hasattr(e, 'code'):
      print 'We failed with error code - %s.' % e.code	
    if hasattr(e, 'reason'):
      print 'We failed to reach a server.'
      print 'Reason: ', e.reason
 	  
def main():
  addDir('[COLOR yellow]M3U PLAYLIST[COLOR magenta] ***** [COLOR lime]MY OWN CHANNELS[/COLOR]','mym3u',30,logos+'mychannel.png')  #play direct and plugin links.
  addDir('[COLOR cyan]XML PLAYLIST[COLOR magenta] ***** [COLOR orange]XML CỦA TUI [COLOR red][B] (NO REGEX)[/B][/COLOR]','myxml',30,logos+'myxml.png')	#play direct and plugin links (change "&amp;" to "&") 
  addDir('[COLOR lime]HD [COLOR cyan]Channels[/COLOR]','hdchannels',8,logos+'hd.png')  
  addDir('[COLOR yellow]TV Hải Ngoại   ++   [COLOR cyan]Âm Nhạc   ++   [COLOR lime]Radio[/COLOR]',tvchannels,7,logos+'tivihn.png')
  addDir('[COLOR cyan]TV Trong Nước   ++   [COLOR lime]Radio[/COLOR]',vietnamtv,6,logos+'vietnamtvradio.png')
  addDir('[COLOR orange]TV Tổng Hợp   ++   [COLOR yellow]SCTV HD  ++  [COLOR lime]Radio[/COLOR]','tonghop',13,logos+'vietsimpletv.png')  
  #addDir('[COLOR orange]TV Tổng Hợp   ++   [COLOR lime]Radio[/COLOR]',viet_tv,11,logos+'vietsimpletv.png') 
  #addDir('[COLOR lime]TV24VN    [COLOR lime]>[COLOR magenta]>[COLOR orange]>[COLOR yellow]>    [COLOR yellow]SCTV[/COLOR]',tv24vn,6,logos+'tv24vn.png')				  
  #addDir('[COLOR lime]SCTV  ++  [COLOR yellow]SCTV HD [/COLOR]',anluongtv,6,logos+'sctv.png')
  addDir('[COLOR lime]TV Tổng Hợp[COLOR magenta] - [COLOR cyan]Links provided by thanh51[/COLOR]',thanh51,51,logos+'thanh51.png')  
  addDir('[COLOR yellow]Live TV[COLOR magenta] - [COLOR red]Playlist posted by ATF01[/COLOR]',ATF01,51,logos+'atf01.png')    
  addDir('[COLOR lime]Replay[COLOR magenta] - [COLOR white]TV được chiếu lại (VN server)[/COLOR]',tvreplay,20,logos+'replay.png')
  addDir('[COLOR deeppink]Access Asia Network[/COLOR]',tvchannels,7,logos+'accessasia.png')  
  #addDir('[COLOR blue]FPTPlay[/COLOR]',fptplay+'/livetv',6,logos+'fptplay.png')  
  addDir('[COLOR cyan]Haotivi[/COLOR]',haotivi,1,logos+'hao.png')		
  #addDir('[COLOR orange]VTCPlay[/COLOR]',vtcplay,7,logos+'vtcplay.png')
  addDir('[COLOR silver]VTC[/COLOR]',tvchannels,7,logos+'vtccomvn.png')		
  addDir('[COLOR magenta]HTVOnline[/COLOR]',htvonline,6,logos+'htvonline.png')
  #addDir('SCTV Extras',sctv,6,logos+'sctv.png')
  #addDir('[COLOR white]Zui Live TV[/COLOR]',zuitv,6,logos+'zui.png') 
  addDir('[COLOR lime]World TV[/COLOR]','worldtv',12,logos+'worldtv.png') #World and Sport TV
  content=makeRequest(hotChannels)
  match=re.compile(xml_regex).findall(content)
  for name,url,thumb in match:
    addLink('[COLOR cyan]'+name+'[/COLOR]',url,logos+thumb)  
 
def my_playlist_directories(name):
  if 'XML' in name:
    addDir('[COLOR cyan]My Online XML Playlist[/COLOR]','onlinexml',31,logos+'myxml.png')
    addDir('[COLOR orange]My Local XML Playlist[/COLOR]','localxml',31,logos+'myxml.png')  
  else:
    addDir('[COLOR yellow]My Online M3U Playlist[/COLOR]','onlinem3u',31,logos+'mychannel.png')
    addDir('[COLOR lime]My Local M3U Playlist[/COLOR]','localm3u',31,logos+'mychannel.png')
 
def my_playlist_links(name):
  if 'Local M3U' in name:
    if len(localm3u) <= 0:
      mysettings.openSettings()
    else:  
      try:
        mym3u=open(localm3u, 'r')  
        link=mym3u.read()
        mym3u.close()
        match=re.compile(m3u_regex).findall(link)
        for title,url in match:
	      playLink(title,url,logos+'mychannel.png')
      except:
        pass 
  elif 'Online M3U' in name:
    if len(onlinem3u) > 0: 
      content=makeRequest(onlinem3u)
      match=re.compile(m3u_regex).findall(content)
      for title,url in match:
	    playLink(title,url,logos+'mychannel.png')
    else:		
      mysettings.openSettings()			
  elif 'Local XML' in name:
    if len(localxml) <= 0:
      mysettings.openSettings()
    else:     
      try:
        myxml=open(localxml, 'r')  
        link=myxml.read()
        myxml.close()
        match=re.compile(xml_regex).findall(link)
        for title,url,thumb in match:
	      if len(thumb) > 0:
	        playLink(title,url,thumb) 
	      else:	
	        playLink(title,url,logos+'myxml.png')	
      except:
        pass  	  
  elif 'Online XML' in name:
    if len(onlinexml) > 0:	
      content=makeRequest(onlinexml)
      match=re.compile(xml_regex).findall(content)
      for title,url,thumb in match:
	    if len(thumb) <= 0:
	      playLink(title,url,logos+'myxml.png') 
	    else:	
	      playLink(title,url,thumb)
    else:		  
      mysettings.openSettings()	
		  	  
def thanh51_atf01(url,name):
  content=makeRequest(url)
  match=re.compile(m3u_regex).findall(content)
  for title,url in match:
    if 'thanh51' in name:  
	  addLink(title,url,logos+'thanh51.png')
    else:  
      addLink(title,url,logos+'atf01.png')
	  
def tv_replay(url):
  content=makeRequest(url)
  match=re.compile('href="(\d+)/">(\d+)/<').findall(content)
  for url, name in match:
    addDir('[COLOR lime]'+name+'[/COLOR]',tvreplay+url,21,logos+'replay.png')

def worldtv():
  content=makeRequest(giniko)
  match=re.compile(xml_regex).findall(content)
  for name,url,thumb in match:
    add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumb)
'''
  content=makeRequest(wezatv)
  match=re.compile('href="http://www.wezatv.com/dooball/(.+?)" title="ดูทีวีออนไลน์ช่อง(.+?)"><img src="../(.+?)"').findall(content)
  for url,name,thumb in match:
    add_Link('[COLOR lime]'+name+'[/COLOR]',wezatv+'/dooball/'+url,wezatv+'/'+thumb)
'''	
    
def vietsimpletv(url):
  content=makeRequest(url)	
  match=re.compile(m3u_regex).findall(content)
  for name,url in match:
    if 'htvonline' in url:
      add_Link('[COLOR cyan]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')
    elif 'tv24.vn' in url:  
      addLink('[COLOR lime]'+name+'[/COLOR]',url.replace('rtmp://$OPT:rtmp-raw=',''),logos+'vietsimpletv.png')
    elif 'torrent-tv.ru' in url:  
      addLink('[COLOR magenta]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')
    elif 'xemphimso' in url:  
      addDir('[COLOR blue]'+name+'[/COLOR]',url,7,logos+'vietsimpletv.png')	  
    elif 'radiovietnam' in url or 'VOA News' in name  or 'NHK Vietnam' in name  or 'RFI Vietnam' in name  or 'VOH' in name:  
      addLink('[COLOR orange]'+name+'  -  [COLOR lightgreen]Radio[/COLOR]',url,logos+'vietsimpletv.png')	 
    elif 'accessasia' in url:  
      addLink('[COLOR silver]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')		  
    else:  
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')		  

def tvtonghop_linklist(url):
  content=makeRequest(url)
  match=re.compile('onclick="configurator\(this\)" name="(.+?)">(.+?)<').findall(content)
  for url, sname in match:
	if 'f4m' in url:
	  url=url.split('=')[-1]
	  url='plugin://plugin.video.f4mTester/?url='+url
	  addLink('[COLOR yellow]'+sname.replace(' sever','Link')+'[COLOR lime] (f4m)[/COLOR]',url,iconimage)
	else:
	  get_Link('[COLOR cyan]'+sname.replace(' sever','Link')+'[/COLOR]',url,iconimage)  

def url_Resolver(url):
  if 'm3u8' in url:
	mediaUrl=url.split('=')[-1]
  elif 'rtmp' in url:
	mediaUrl=url.split('=')[-1]
  else:
    content=makeRequest(url)
    try: 
      try:	
	    mediaUrl=re.compile('file: "(.+?)",').findall(content)[0]
      except:
	    mediaUrl=re.compile('iframe src=".+?src=(.+?)"').findall(content)[0]	  
    except:
      try:
        mediaUrl=re.compile('<param name="flashvars" value="src=(.+?)\?').findall(content)[0]	
      except:
		mediaUrl=re.compile("'streamer': '(.+?)',").findall(content)[0]+' playpath='+re.compile("'file': '(.+?)',").findall(content)[0]
		#mediaUrl=re.compile("'streamer': '(.+?)',").findall(content)[0]+'/'+re.compile("'file': '(.+?)',").findall(content)[0]		
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return
	   	  	  
def dirs(url):
  content=makeRequest(url)
  match=re.compile("<h3><a href=\"(.+?)\">(.+?)<\/a><\/h3>").findall(content)
  for url,name in match:	
    addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,3,logos+'fptplay.png')

def tvreplay_link(url):
  content=makeRequest(url)
  match=re.compile('href="(.+?)">(.+?)\.mp4</a></td><td align="right">.+?</td><td align="right">(.+?)<').findall(content)
  for href, name, vsize in match:
    name=name.split('_')
    name=name[0]+'_'+name[-1]
    addLink('[COLOR cyan]'+name+'   [COLOR yellow]'+vsize+'[/COLOR]',url+'/'+href,logos+'replay.png')
	
def index(url):
  content=makeRequest(url)
  if 'tv24' in url:
	  match=re.compile("<SPAN id=\".+?\"><a href='(.+?)'><img src='(.+?)' onmouseover=\"this.src='http:\/\/tv24.vn\/WebMedia\/Channels\/\d+\/(.+?).png'").findall(content)
	  for url,thumbnail,name in match:
	    if 'vtv' in name:
	      add_Link('[COLOR yellow][UPPERCASE]'+name+'[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),thumbnail)	  
	    else:	  
	      add_Link('[COLOR lime][UPPERCASE]'+name.replace('b','')+'[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),thumbnail)
  elif 'vietnamtv' in url:
    match=re.compile(xml_regex).findall(content)
    for name,url,thumbnail in match:
      if 'Truyền Hình' in name:
        add_Link('[COLOR yellow]'+name+'[/COLOR]',url,logos+thumbnail)
      elif 'Radio' in name:
        add_Link('[COLOR lime]'+name+'[/COLOR]',url,logos+thumbnail)        
  elif 'SCTV.m3u' in url:
    match=re.compile(m3u_regex).findall(content)
    for name,url in match: 
      add_Link(name,url,logos+'sctv.png')
  elif 'htvonline' in url:
	  match=re.compile("<a class=\"mh-grids5-img\".*?href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"").findall(content)
	  for url,name,thumbnail in match:
	    add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail) 
  elif 'fptplay' in url:
    #match=re.compile("channel=\"(.*?)\" href=\".+?\" data=\"(.+?)\" adsstatus.+?>\s+<img src=\"(.*?)\"").findall(content)
    match=re.compile('channel="(.*?)" href=".+?" data="(.+?)" adsstatus="">\s\s*\s*\s*\s*<img class="img-responsive" src="(.+?)\?.+?"').findall(content)	
    for name,url,thumbnail in match:
            #print >> open (xbmc.translatePath(os.path.join(home, 'FPTPlayLiveTV.txt')),'a+'),fptplay+url
	    #if 'VOVTV' in name or 'OneTV' in name or 'VTV3' in name or 'VTV6' in name:
	      #add_Link('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,thumbnail)	  
	    #else:
	      add_Link('[COLOR lime]'+name.replace('&#39;','\'')+'[/COLOR]',fptplay+url,thumbnail)
  elif 'zui' in url:
    match=re.compile("alt='(.+?)' href='(.+?)'><img src='(.+?)'").findall(content)[3:36]
    for name,url,thumbnail in match:
      if 'SCTV1' in name or 'VTC14' in name or 'ITV' in name or 'Nhạc của tui' in name or 'Thuần Việt' in name:
	      add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)	  
      else:
        pass
  elif 'tv.anluong.info' in url:		
    match=re.compile('href="\?tab=kenhhd&xem=(.+?)"><img title="([^"]+)" class="images-kenh".+?src="([^"]*)"').findall(content)
    for url,name,thumbnail in match:	
      addDir('[COLOR magenta]SCTV HD [COLOR lime]- [COLOR yellow]'+name.replace('HD','').replace('SCTV ','')+'[/COLOR]',anluongtv+'?tab=kenhhd&xem='+url,5,anluongtv+thumbnail)
    match=re.compile('href="(.+?)"><img class="images-kenh1"  src="(.+?)"').findall(content)
    for url,thumbnail in match:
      name=url.replace('?tab=sctv&xem=','').upper()
      addDir('[COLOR cyan]'+name.replace('SCTV','SCTV ')+'[/COLOR]',anluongtv+url,5,anluongtv+thumbnail)	

def sctv_serverlist(url):
  content=makeRequest(url)
  if 'kenhhd' in url:
	match=re.compile('onclick="configurator\(this\)" name="(.+?)">(.+?)<').findall(content)
	for url, sname in match:
	  if 'f4m' in url:
	    pass
	  else:
	    getLink('[COLOR magenta]'+sname.replace(' sever','Link')+'[/COLOR]',url,iconimage)
  else:
    match=re.compile('onclick="configurator\(this\)" name="(.+?)">(.+?)<').findall(content)
    for url, sname in match:
      getLink('[COLOR cyan]'+sname.replace(' sever','Link')+'[/COLOR]',url,iconimage)  

def add_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=9"+"&iconimage="+urllib.quote_plus(iconimage)  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  

def tvtonghop():
  content=makeRequest(anluongtv)
  match=re.compile('href="(.+?)"><img title="(.+?)".+?\s*src="(.+?)"').findall(content)
  for url,name,thumbnail in match:
    if 'SCTV' in name or 'SAO TV HD' in name:
      addDir('[COLOR lime]'+name+'[/COLOR]',anluongtv+url,14,anluongtv+thumbnail)
    else:
	  pass
  match=re.compile('href="(.+?)"><img class="images-kenh1"  src="(.+?)"').findall(content)
  for url,thumbnail in match:
    name=url.replace('?tab=sctv&xem=','').upper()
    addDir('[COLOR cyan]'+name.replace('SCTV','SCTV ')+'[/COLOR]',anluongtv+url,14,anluongtv+thumbnail)	  
  match=re.compile('href="(.+?)"><img title="(.+?)".+?\s*src="(.+?)"').findall(content)
  for url,name,thumbnail in match:	  
    if 'SCTV' in name or 'SAO TV HD' in name or 'NHẠC CÁCH MẠNG' in name:
      pass
    else: 
      addDir('[COLOR yellow]'+name.replace('SOPPING','SHOPPING')+'[/COLOR]',anluongtv+url,14,anluongtv+thumbnail)
  content=makeRequest(viet_tv)	
  match=re.compile(m3u_regex).findall(content)
  for name,url in match:
    if 'radiovietnam' in url or 'VOA News' in name  or 'NHK Vietnam' in name  or 'RFI Vietnam' in name  or 'VOH' in name:  
      addLink('[COLOR orange]'+name+'  -  [COLOR lightgreen]Radio[/COLOR]',url,logos+'vietsimpletv.png') 
    else:
	  pass
	  
def videoLinks(url,name):
  content=makeRequest(url)
  if 'xemphimso' in url:
    match=re.compile("file: '(.+?)'").findall(content)
    for url in match:
      addLink(name,url,logos+'vietsimpletv.png')	  	  
  elif 'Access Asia Network' in name:
    match=re.compile("\"BroadcastStation\":\"accessasia\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(content)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)								
  elif 'TV Hải Ngoại' in name:
    match=re.compile("\"BroadcastStation\":\"haingoaitv\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(content)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)												      
  elif 'VTCPlay' in name:
    match=re.compile("\"Name\":\"(.*?)\".+?\"Thumbnail2\":\"(.+?)\".+?\"Path\":\"([^\"]*)\"").findall(content)
    for name,thumbnail,url in match:
      addLink('[COLOR yellow]'+name.decode("utf-8")+'[/COLOR]',url,thumbnail)						
  elif 'VTC' in name:
    match=re.compile("\"BroadcastStation\":\"vtccomvn\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(content)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)								
  elif 'Việt Nam' in name:
    match=re.compile("\"lang\":\"vi\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,logos+'vn.png')
  elif 'Spain' in name:		
    match=re.compile("\"lang\":\"sp\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR pink]'+name+'[/COLOR]',url,logos+'sp.png')
  elif 'France' in name:						
    match=re.compile("\"lang\":\"fr\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR orange]'+name+'[/COLOR]',url,logos+'fr.png')
  elif 'Hong Kong' in name:						
    match=re.compile("\"lang\":\"hk\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR blue]Hong Kong - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'hk.png')
  elif 'Taiwan' in name:			
    match=re.compile("\"lang\":\"tw\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR magenta]Taiwan - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'tw.png')
  elif 'US' in name:		
    match=re.compile("\"lang\":\"us\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR lime]'+name+'[/COLOR]',url,logos+'us.png')
  elif 'China' in name:						
    match=re.compile("\"lang\":\"cn\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR cyan]China - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'cn.png')
  elif 'Brazil' in name:		
    match=re.compile("\"lang\":\"br\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR silver]'+name+'[/COLOR]',url,logos+'br.png')
  elif 'Korea' in name:		
    match=re.compile("\"lang\":\"ko\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR deeppink]Korea - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'ko.png')
  elif 'Thailand' in name:		
    match=re.compile("\"lang\":\"th\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR gold]'+name+'[/COLOR]',url,logos+'th.png')
  elif 'Japan' in name:						
    match=re.compile("\"lang\":\"ja\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR tomato]'+name+'[/COLOR]',url,logos+'ja.png')
  elif 'Indonesia' in name:		
    match=re.compile("\"lang\":\"id\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR tan]'+name+'[/COLOR]',url,logos+'id.png')
  elif 'Malaysia' in name:						
    match=re.compile("\"lang\":\"my\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR coral]'+name+'[/COLOR]',url,logos+'my.png')

def get_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=15"+"&iconimage="+urllib.quote_plus(iconimage)  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  
 	  
def hao():						
  #addDir('[COLOR yellow]Việt Nam[/COLOR]',haotivi,7,logos+'vn.png')
  addDir('[COLOR lime]US[/COLOR]',haotivi,7,logos+'us.png')
  addDir('[COLOR orange]France[/COLOR]',haotivi,7,logos+'fr.png')
  addDir('[COLOR blue]Hong Kong[/COLOR]',haotivi,7,logos+'hk.png')
  addDir('[COLOR magenta]Taiwan[/COLOR]',haotivi,7,logos+'tw.png')
  addDir('[COLOR cyan]China[/COLOR]',haotivi,7,logos+'cn.png')
  addDir('[COLOR silver]Brazil[/COLOR]',haotivi,7,logos+'br.png')
  addDir('[COLOR pink]Spain[/COLOR]',haotivi,7,logos+'sp.png')
  addDir('[COLOR tomato]Japan[/COLOR]',haotivi,7,logos+'ja.png')
  addDir('[COLOR deeppink]Korea[/COLOR]',haotivi,7,logos+'ko.png')
  addDir('[COLOR gold]Thailand[/COLOR]',haotivi,7,logos+'th.png')
  addDir('[COLOR tan]Indonesia[/COLOR]',haotivi,7,logos+'id.png')
  addDir('[COLOR coral]Malaysia[/COLOR]',haotivi,7,logos+'my.png')

def urlResolver(url):
  if 'm3u8' in url:
	mediaUrl=url.split('=')[-1]
  else:
    content=makeRequest(url)
    try:  
	  mediaUrl=re.compile('file: "(.+?)",').findall(content)[0]
    except:
      try:
        mediaUrl=re.compile('<param name="flashvars" value="src=(.+?)\?').findall(content)[0]	
      except:
		mediaUrl=re.compile("'streamer': '(.+?)',").findall(content)[0]+' playpath='+re.compile("'file': '(.+?)',").findall(content)[0]
		#mediaUrl=re.compile("'streamer': '(.+?)',").findall(content)[0]+'/'+re.compile("'file': '(.+?)',").findall(content)[0]		
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return

def getLink(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=3"+"&iconimage="+urllib.quote_plus(iconimage)  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  

def playLink(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=32"+"&iconimage="+urllib.quote_plus(iconimage)  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  

def play_my_playlists(url):
  if 'plugin://plugin' in url:
    mediaUrl=url.replace('&amp;','&')
  else:
    mediaUrl=url  
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
  return
   
def HD():
  content=makeRequest(hotChannels)
  match=re.compile(xml_regex).findall(content)
  for name,url,thumb in match:
    if 'CBSN Live HD' in name or 'NBC Sports Live Extra - Golf & New Events Live HD' in name or 'VEVO ' in name:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',url,logos+thumb) 
  add_Link('[COLOR lime]National Geographic HD[/COLOR]','http://www.htvonline.com.vn/livetv/national-geographic-3132366E61.html',logos+'natgeohd.png')
  add_Link('[COLOR lime]Discovery World HD[/COLOR]','http://www.htvonline.com.vn/livetv/discovery-hd-3132336E61.html',logos+'dischd.png')
  add_Link('[COLOR lime]FOX SPORTS PLUS HD[/COLOR]','http://www.htvonline.com.vn/livetv/espn-hd-3132346E61.html',logos+'foxsporthd.png')	  
  content=makeRequest(htvonline)  
  match=re.compile("<a class=\"mh-grids5-img\".*?href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"").findall(content)
  for url,name,thumbnail in match:	
    if 'HTV7' in name or 'HTV9' in name or ' HD' in name or 'htv2-31336E61' in url:
	    add_Link('[COLOR cyan]'+name+'[/COLOR]',url,thumbnail)
  add_Link('[COLOR cyan]FBNC HD[/COLOR]','http://www.htvonline.com.vn/livetv/fbnc-34306E61.html',logos+'fnbchd.png')     
	  
def resolveUrl(url):
  if 'fptplay' in url:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    req.add_header('Referer', fptplay)	
    response=urllib2.urlopen(req)
    link=response.read()
    response.close()
    mediaUrl='plugin://plugin.video.f4mTester/?url='+re.compile('"adapt_hds": "(.+?)"').findall(link)[0]
  elif 'htvonline' in url:
    content=makeRequest(url)
    mediaUrl=re.compile("file: \"([^\"]*)\"").findall(content)[0]
  elif 'hplus' in url:
    content=makeRequest(url)  
    mediaUrl=re.compile("var iosUrl = \"(.+?)\"").findall(content)[0]	
  elif 'tv24' in url:
    content=makeRequest(url)  
    videoUrl=re.compile('\'file\': \'http([^\']*)\/playlist.m3u8').findall(content)[0]
    mediaUrl='rtmpe' + videoUrl + ' swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://tv24.vn/ ' + token   
  elif 'zui' in url:
    content=makeRequest(url)  
    mediaUrl=re.compile('livetv_play\(\'player\', \'1\', \'(.+?)\'\)').findall(content)[0]	
  elif 'wezatv' in url or 'giniko' in url:
    content=makeRequest(url)  
    mediaUrl=re.compile('file: "(.+?)"').findall(content)[0]  
  else:
    mediaUrl=url  
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return
 	  	
def get_params():
  param=[]
  paramstring=sys.argv[2]
  if len(paramstring)>=2:
    params=sys.argv[2]
    cleanedparams=params.replace('?','')
    if (params[len(params)-1]=='/'):
      params=params[0:len(params)-2]
    pairsofparams=cleanedparams.split('&')
    param={}
    for i in range(len(pairsofparams)):
      splitparams={}
      splitparams=pairsofparams[i].split('=')
      if (len(splitparams))==2:
        param[splitparams[0]]=splitparams[1]
  return param
	
def addDir(name,url,mode,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
  return ok
 	
def addLink(name,url,iconimage):
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
  return ok
   
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:
  url=urllib.unquote_plus(params["url"])
except:
  pass
try:
  name=urllib.unquote_plus(params["name"])
except:
  pass
try:
  mode=int(params["mode"])
except:
  pass
try:
  iconimage=urllib.unquote_plus(params["iconimage"])
except:
  pass  
 
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "iconimage: "+str(iconimage)

if mode==None or url==None or len(url)<1:
  main()

elif mode==1:
  hao()

elif mode==3:
  urlResolver(url)
  
elif mode==4:
  dirs(url)

elif mode==5:
  sctv_serverlist(url)
  
elif mode==6:
  index(url)
		
elif mode==7:
  videoLinks(url,name)

elif mode==8:
  HD()
  
elif mode==9:
  resolveUrl(url)
  
elif mode==11:
  vietsimpletv(url) 

elif mode==12:
  worldtv()  

elif mode==13:
  tvtonghop()

elif mode==14:
  tvtonghop_linklist(url)

elif mode==15:
  url_Resolver(url)

elif mode==20:
  tv_replay(url)

elif mode==21:
  tvreplay_link(url)

elif mode==30:
  my_playlist_directories(name)

elif mode==31:
  my_playlist_links(name)

elif mode==32:
  play_my_playlists(url)
  
elif mode==51:
  thanh51_atf01(url,name) 
   
xbmcplugin.endOfDirectory(int(sys.argv[1]))

