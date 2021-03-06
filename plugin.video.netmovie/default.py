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

mysettings=xbmcaddon.Addon(id='plugin.video.netmovie')
profile=mysettings.getAddonInfo('profile')
home=mysettings.getAddonInfo('path')
fanart=xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon=xbmc.translatePath(os.path.join(home, 'icon.png'))
logos=xbmc.translatePath(os.path.join(home, 'logos\\'))
mode_opt=int(mysettings.getSetting('Mode_Number'))
anhtrang='http://phim.anhtrang.org/'
m_anhtrang='http://m.anhtrang.org/'
hd_caphe='http://phim.hdcaphe.com/'
phimmobile='http://www.phimmobile.com/'
dangcapmovie='http://dangcapmovie.com/'
dchd='http://dangcaphd.com/'
phim3s='http://phim3s.net/'
pgt='http://phimgiaitri.vn/'
fptplay='http://fptplay.net'
megaboxvn='http://megabox.vn/'
hayhd='http://phimhayhd.tv/'
phimb='http://www.phimb.net'
phim14='http://phim14.net/'
phim7='http://phim7.com'
zui='http://zui.vn/'

def makeRequest(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    req.add_header ('Cookie' , 'window.location.href') 
    response=urllib2.urlopen(req, timeout=120)
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
  addDir('[COLOR yellow]phim3s.net[/COLOR]',phim3s,2,logos+'phim3s.png') 
  addDir('[COLOR magenta]phim14.net[/COLOR]',phim14,2,logos+'phim14.png')   
  addDir('[COLOR lime]phim7.com[/COLOR]',phim7,2,logos+'phim7.png')
  addDir('[COLOR cyan]phimb.net[/COLOR]',phimb,40,logos+'phimb.png')    
  addDir('[COLOR orange]anhtrang.org[/COLOR]',anhtrang,2,logos+'anhtrang.png')  
  addDir('[COLOR violet]megabox.vn[/COLOR]',megaboxvn,2,logos+'megabox.png')  
  #addDir('[COLOR lightgreen]phimhayhd.tv[/COLOR]',hayhd,2,logos+'hayhd.png')
  addDir('[COLOR lightblue]hdcaphe.com[/COLOR]',hd_caphe+'camera-quan-sat.html',2,logos+'hdcaphe.png')  
  addDir('[COLOR cyan]phimgiaitri.vn[/COLOR]',pgt,5,logos+'pgt.png')
  addDir('[COLOR lime]dangcaphd.com[/COLOR]',dchd,2,logos+'dchd.png') 
  addDir('[COLOR blue]dangcapmovie.com[/COLOR]',dangcapmovie,2,logos+'dcm.png')  
  addDir('[COLOR chocolate]phimmobile.com[/COLOR]',phimmobile,2,logos+'mobile.png')  
  addDir('[COLOR lightgreen]fptplay.net[/COLOR]',fptplay,2,logos+'fptplay.png')
  #addDir('[COLOR silver]zui.vn[/COLOR]',zui,2,logos+'zui.png')   
 
def megavn(url):
  content = makeRequest(url)
  if 'tvonline' in url:
    match = re.compile('<div class="infoC"> <a href="(.+?)" >\s*<h4>(.+?)<span>\((\d+)\)<\/span>').findall(content)
    for url, title, inum in match:
      if inum == '0':
        pass
      else:
        addDir('[COLOR yellow]' + title + '[/COLOR]', url, 13, logos + 'megabox.png')
  elif 'phim-le' in url:
    match = re.compile('<div class="infoC"> <a href="(.+?)" >\s*<h4>(.+?)<span>\((\d+)\)<\/span>').findall(content)[6:]
    for url, title, inum in match:
      if inum == '0':
        pass
      else:
        addDir('[COLOR lime]' + title + '[/COLOR]', url, 15, logos + 'megabox.png')  
  elif 'phim-bo' in url:
    match = re.compile('<div class="infoC"> <a href="(.+?)" >\s*<h4>(.+?)<span>\((\d+)\)<\/span>').findall(content)[5:]
    for url, title, inum in match:
      if inum == '0':
        pass
      else:
        addDir('[COLOR yellow]' + title + '[/COLOR]', url, 13, logos + 'megabox.png')  

def search():
  try:
    keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    if 'phim3s' in name:  
      url=phim3s+'search?keyword='+searchText
      index(url)
    elif 'dangcaphd' in name:
      url=dchd+'movie/search.html?key='+searchText+'&search_movie=0'
      index(url)
    elif 'Tìm Phim Lẻ' in name:
      url=pgt+'result.php?type=search&keywords='+searchText 
      index(url)
    elif 'FPTPLAY' in name:
      url=fptplay+'/Search/'+searchText      
      try:
        mediaList(url)  # Fast - no thumbs + 1 more click
      except:  
        fpt_img(url)    # Slow - thumbs + 1 less click
    elif 'zui' in name:
      url='http://zui.vn/tim-kiem-nc/'+searchText+'.html'  
      mediaList(url)
    elif 'hdcaphe' in name:		
      url=hd_caphe+'search-result.html?keywords='+searchText  
      mediaList(url)
    elif 'anhtrang' in name:		
      url=anhtrang+'tim-kiem='+searchText+'.html'  
      anhtrang_mediaList(url)
    elif 'megabox' in name:	
      url = megaboxvn + 'home/search/index/key/' + searchText.replace('+','%20')	
      megaListEps(url)
      otherMegaList(url)
    elif 'phimhayhd' in name:	
      url = hayhd + 'tim-kiem.html?query=' + searchText
      hayhd_bo(url)
    elif 'phimmobile' in name:	
      url = phimmobile + 'film/ajaxSearch?keyword=' + searchText 	
      mobile_search_result(url)
    elif 'dangcapmovie' in name:      
      url = dangcapmovie + 'movie/search.html?key=' + searchText
      dangcapmovie_search_result(url) 
    elif 'phim7' in name:      
      url = phim7+'/tim-kiem/tat-ca/'+searchText.replace('+','-')+'.html'
      mediaList(url)
    elif 'phimb' in name: 
      url=phimb+'/tim-kiem/'+searchText
      phimb_mediaList(url)	
    elif 'phim14' in name: 
      url=phim14+'search/'+searchText.replace('+','-')+'.html'
      mediaList(url)	
  except: pass

def episodes_phimb(url,name):
  content=phimbRequest(url)
  name=name.replace('[COLOR lime]','').replace('[/COLOR]','')  
  match=re.compile('<div class="svname">'+name+'</div><div class="svep"><div class="border">(.+?)</div>').findall(content)
  for vlinks in match:
    match=re.compile('href="(.+?)"  title="(.+?)">(.+?)<').findall(vlinks)
    for url,title,eps in match:
      add_Link('[COLOR cyan]'+eps+'[/COLOR]',url,iconimage)	
  
def hayhd_bo(url):
  content = makeRequest(url)
  match = re.compile('href="([^"]*)">\s*<img.+?data-src="([^"]+)" alt.+?title="([^"]*)"').findall(content)
  for url, thumbnail, name in match:
    link = makeRequest(url)
    eps = re.compile('href="(.+?)" class="episode.+?">(.+?)<').findall(link)
    for vlink, title in eps:
      add_Link('[COLOR cyan]' + title + '[COLOR lime] - ' + name + '[/COLOR]',vlink,thumbnail)  
    
def categories(url):
  content=makeRequest(url)
  if 'phim3s' in url:
    addDir('[COLOR yellow]phim3s[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',phim3s,1,logos+'phim3s.png')
    match=re.compile("<a href=\"the-loai([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',('%sthe-loai%s' % (phim3s, url)),3,logos+'phim3s.png')					
    match=re.compile("<a href=\"quoc-gia([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',('%squoc-gia%s' % (phim3s, url)),3,logos+'phim3s.png')					
    match=re.compile("<a href=\"danh-sach([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR lightblue]'+name+'[/COLOR]',('%sdanh-sach%s' % (phim3s, url)),3,logos+'phim3s.png')					
  elif 'dangcaphd' in url:
    addDir('[COLOR yellow]dangcaphd[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR lightgreen]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',dchd+'',1,logos+'dchd.png')
    match=re.compile("<a href=\"([^\"]*)\" class='menutop' title='([^']+)'>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',url,3,logos+'dchd.png')  
    match=re.compile("<li><a href=\"http:\/\/dangcaphd.com\/cat(.+?)\" title=\"([^\"]*)\">").findall(content)[0:22]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',dchd+'cat'+url,3,logos+'dchd.png')
    match=re.compile("<li><a href=\"http:\/\/dangcaphd.com\/country(.+?)\" title=\"([^\"]+)\">").findall(content)[0:12]
    for url,name in match:
      addDir('[COLOR orange]'+name+'[/COLOR]',dchd+'country'+url,3,logos+'dchd.png')
    match=re.compile("<a href=\"http:\/\/dangcaphd.com\/movie(.+?)\"><span>(.*?)<\/span><\/a>").findall(content)[0:3]
    for url,name in match:
      addDir('[COLOR lightgreen]'+name+'[/COLOR]',dchd+'movie'+url,3,logos+'dchd.png')					
  elif 'dangcapmovie' in url:
    addDir('[COLOR lime]dangcapmovie.com   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [COLOR lime]Movie Search[/COLOR]',dangcapmovie,1,logos + 'dcm.png')
    match = re.compile('href="http:\/\/dangcapmovie.com\/cat(.+?)" title="(.+?)">').findall(content)[0:23] 
    for url,name in match:
      addDir('[COLOR cyan]'+name.replace('Hàng động','Hành động')+'[/COLOR]',dangcapmovie+'cat'+url,7,logos+'dcm.png')      
    match = re.compile('href="http:\/\/dangcapmovie.com\/country(.+?)" title="(.+?)">').findall(content)[0:10]
    for url,name in match:  
      addDir('[COLOR yellow]'+name+'[/COLOR]',dangcapmovie+'country'+url,7,logos+'dcm.png') 
    match = re.compile('href="http:\/\/dangcapmovie.com\/movie\/(.+?)" title="(.+?)">').findall(content)
    for url,name in match:  
      addDir('[COLOR lime]'+name+'[/COLOR]',dangcapmovie+'movie/'+url,7,logos+'dcm.png') 
  elif 'phimgiaitri' in url:
    addDir('[COLOR lime]phimgiaitri[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR lime]Tìm Phim Lẻ[/COLOR]',pgt,1,logos+'pgt.png')
    match=re.compile('<a href=\'result.php\?type=Phim Lẻ(.+?)\'><span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',pgt+'result.php?type=Phim%20L%E1%BA%BB'+url.replace(' ','%20'),3,logos+'pgt.png')
  elif 'fptplay' in url:
    addDir('[COLOR lime]Nhấn vô đây, [COLOR yellow]chọn cách bắt links [COLOR cyan]nhanh [COLOR yellow]hay [COLOR cyan]chậm[/COLOR]',url,17,logos+'fptplay.png')
    addDir('[COLOR blue]FPTPLAY[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR blue]Tìm Video[/COLOR]',fptplay,1,logos+'fptplaysearch.png')    
    match=re.compile("<li ><a href=\"(.+?)\" class=\".+?\">(.+?)<\/a><\/li>").findall(content)
    for url,name in match:
		  if 'livetv' in url:
			  pass
		  else:
			  addDir('[COLOR magenta]'+name+'[/COLOR]',fptplay+url,6,logos+'fptplay.png')				
  elif 'zui' in url:
    addDir('[COLOR magenta]zui[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR magenta]Tìm Phim[/COLOR]',zui,1,logos+'zui.png') 
    match=re.compile("<li><a title=\".+?\" href=\"([^\"]*)\">([^>]+)<\/a><\/li>").findall(content)[0:3]
    for url,name in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',url,7,logos+'zui.png')	  
    match=re.compile("<li><a href='([^']*)'><b class=\"larrow\"><\/b>(.+?)<\/a><\/li>").findall(content)[0:17]
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',url,7,logos+'zui.png')
    match=re.compile('<li><a href=\'([^\']*)\'><b class="larrow"><\/b>([^>]*)<\/a><\/li>').findall(content)[17:28]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',url,7,logos+'zui.png')
    match=re.compile('<li><a href=\'([^\']*)\' style=.+?<\/b>(\d+)<\/a><\/li>').findall(content)
    for url,name in match:
      addDir('[COLOR lightgreen]'+name+'[/COLOR]',url,7,logos+'zui.png')	
  elif 'hdcaphe' in url:
    addDir('[COLOR yellow]hdcaphe[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',hd_caphe,1,logos+'hdcaphe.png')
    match = re.compile("<li class=\"sibling\"><a href=\"([^\"]*)\"   title=\"([^\"]+)\"").findall(content)[3:7]
    for url,name in match:	
      addDir('[COLOR lime]'+name+'[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    match = re.compile("<li class=\"first\"><a href=\"(.+?)\"   title=\"(.+?)\"").findall(content)[0:4]
    for url,name in match:	
      addDir('[COLOR orange]'+name+'[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    match = re.compile("<li class=\"last\"><a href=\"(.+?)\"   title=\"(.+?)\"").findall(content)[0:-1]
    for url,name in match:	
      addDir('[COLOR cyan]'+name+'[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    addDir('[COLOR violet]PHIM HOẠT HÌNH[/COLOR]',hd_caphe+'PHIM_HD_IPHONE_MAY_TINH_BANG_TABLET.html',7,logos+'hdcaphe.png')  	
  elif 'anhtrang' in url:  
    addDir('[COLOR yellow]anhtrang[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',anhtrang,1,logos+'anhtrang.png')
    #content=makeRequest(anhtrang)
    match=re.compile("<a class=\"link\" href=\"http:\/\/.+?\/([^\"]*)\" >\s*<span>(.+?)<\/span>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png')  
    match=re.compile("<a class=\"link\" href=\"http:\/\/.+?\/([^\"]+)\">\s*<span>(.+?)<\/span>").findall(content)[0:7]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png')
    match=re.compile("<a class=\"link\" href=\"http:\/\/.+?\/([^\"]+)\">\s*<span>(.+?)<\/span>").findall(content)[7:19]
    for url,name in match:
      addDir('[COLOR orange]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png')	
    match=re.compile('<li class="item27">\s*<a class="topdaddy link" href="http:\/\/.+?\/([^"]*)">\s*<span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR magenta]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png') 
    match=re.compile('<li class="item28">\s*<a class="topdaddy link" href="http:\/\/.+?\/(.+?)">\s*<span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR lightblue]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png') 
  elif 'megabox' in url:  
    addDir('[COLOR cyan]megabox[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR cyan]Tìm Phim[/COLOR]',megaboxvn,1,logos+'megabox.png')
    match = re.compile("href=\"tvonline\/(.+?)\">([^>]*)<").findall(content)[:3]  
    for url, name in match: 
      if 'the-loai' in url:  
        addDir('[COLOR yellow]TV - ' + name + '[/COLOR]', ('%stvonline/%s' % (megaboxvn, url)), 11, logos + 'megabox.png')
      else:	  
        addDir('[COLOR yellow]TV - ' + name + '[/COLOR]', ('%stvonline/%s' % (megaboxvn, url)), 13, logos + 'megabox.png')
    addDir('[COLOR lime]Phim Lẻ - Mới Nhất[/COLOR]', megaboxvn + 'phim-le/moi-nhat.html', 15, logos + 'megabox.png')	  
    match = re.compile("href=\"phim-le\/(.+?)\">([^>]*)<").findall(content)[:3] 
    for url, name in match: 
      if 'the-loai' in url:  
        addDir('[COLOR lime]Phim Lẻ - ' + name + '[/COLOR]', megaboxvn + 'phim-le/' + url, 11, logos + 'megabox.png')
      else:
        addDir('[COLOR lime]Phim Lẻ - ' + name.replace('Phim ', '') + '[/COLOR]', megaboxvn + 'phim-le/' + url, 15, logos + 'megabox.png')	  
    addDir('[COLOR lime]Phim Lẻ - Dành Cho Bạn[/COLOR]', megaboxvn + 'for_you_movies.html', 15, logos + 'megabox.png')
    addDir('[COLOR yellow]Phim Bộ - Mới Nhất[/COLOR]', megaboxvn + 'phim-bo/moi-nhat.html', 13, logos + 'megabox.png')  
    match = re.compile("href=\"phim-bo\/(.+?)\">([^>]*)<").findall(content)[:4] 
    for url, name in match:
      if 'the-loai' in url:  
        addDir('[COLOR yellow]Phim Bộ - ' + name + '[/COLOR]', ('%sphim-bo/%s' % (megaboxvn, url)), 11, logos + 'megabox.png')	
      else:
        addDir('[COLOR yellow]Phim Bộ - ' + name + '[/COLOR]', ('%sphim-bo/%s' % (megaboxvn, url)), 13, logos + 'megabox.png')		
    match = re.compile("href=\"video-clip\/(.+?)\">([^>]*)<").findall(content)[1:5]
    for url, name in match:  
      addDir('[COLOR lime]Videos - ' + name + '[/COLOR]', megaboxvn + 'video-clip/' + url, 15, logos + 'megabox.png')	
  elif 'phimhayhd' in url:
    addDir('[COLOR yellow]phimhayhd[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim Lẻ[/COLOR]', hayhd, 9, logos + 'hayhd.png')
    addDir('[COLOR lime]phimhayhd[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR lime]Tìm Phim Bộ[/COLOR]', hayhd, 1, logos + 'hayhd.png')  
    content = makeRequest(hayhd) 
    match = re.compile('href=".+?the-loai([^"]*)">([^>]+)<').findall(content)[0:16]  
    for url, name in match:  
      addDir('[COLOR cyan]Phim Lẻ - [COLOR yellow]' + name.replace('Phim ','') + '[/COLOR]', ('%sthe-loai%s' % (hayhd, url)), 3, logos + 'hayhd.png')
    match = re.compile('href=".+?phim-bo([^"]*)">([^>]+)<').findall(content)[0:4] 
    for url, name in match: 
      addDir('[COLOR orange]Phim Bộ - [COLOR lime]' + name + '[/COLOR]', ('%sphim-bo%s' % (hayhd, url)), 7, logos + 'hayhd.png')	
  elif 'phimmobile' in url:
    addDir('[COLOR yellow]phimmobile[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',phimmobile,1,logos+'mobile.png')
    match=re.compile('href="\/(.+?)" class="icon-BXH">(.+?)<').findall(content)
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',phimmobile + url,18,logos+'mobile.png')  
    match=re.compile('title="phim(.+?)" href="\/(.+?)">').findall(content)
    for name,url in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',phimmobile + url,18,logos+'mobile.png')
  elif 'phim7' in url:
    addDir('[COLOR lime]phim7.com[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',phim7,1,logos+'phim7.png')
    match=re.compile("href='(.+?)' title='(.+?)'>").findall(content)[0:25]
    for url,name in match:	
      addDir('[COLOR cyan]'+name+'[/COLOR]',phim7+url,7,logos+'phim7.png')	
    addDir('[COLOR lime]Video mới[/COLOR]','http://phim7.com/video-moi.html',30,logos+'phim7.png')
    addDir('[COLOR lime]Video clip hay[/COLOR]','http://phim7.com/video.html',30,logos+'phim7.png')  
    match=re.compile('href="(.+?)" title="(.+?)">').findall(content)[1:27]
    for url,name in match:
      if 'video clip hay' in name:
        pass	
      else:  
        addDir('[COLOR yellow]'+name+'[/COLOR]',phim7+url,7,logos+'phim7.png')
  elif 'phim14' in url:
    addDir('[COLOR lime]phim14.net[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR lime]Tìm Phim[/COLOR]',phim14,1,logos+'phim14.png')
    match=re.compile('href="http://phim14.net/the-loai([^"]*)">(.+?)<').findall(content)[0:15]
    for url,name in match:	
      addDir('[COLOR yellow]'+name+'[/COLOR]',phim14+'the-loai'+url,7,logos+'phim14.png')
    match=re.compile('href="http://phim14.net/quoc-gia(.+?)">(.+?)<').findall(content)[0:11]
    for url,name in match:  
      addDir('[COLOR cyan]'+name+'[/COLOR]',phim14+'quoc-gia'+url,7,logos+'phim14.png')	
    match=re.compile('href="http://phim14.net/danh-sach([^"]*)".*>(.+?)<').findall(content)[0:5]
    for url,name in match:  
      addDir('[COLOR violet]'+name+'[/COLOR]',phim14+'danh-sach'+url,7,logos+'phim14.png')	

def phimbRequest(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    response=urllib2.urlopen(req, timeout=60)
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

def phimb_cat(url):
  content=phimbRequest(url)
  addDir('[COLOR lime]phimb.net[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR lime]Tìm Phim[/COLOR]',phimb,1,logos+'phimb.png')
  match=re.compile('class="add" href="(.+?)" title="(.+?)"').findall(content)
  for url,name in match:  
    addDir('[COLOR yellow]'+name+'[/COLOR]',phimb+url,41,logos+'phimb.png')
  match=re.compile('title="Phim(.+?)" href="(.+?)"').findall(content)
  for name,url in match:	
    addDir('[COLOR cyan]'+name+'[/COLOR]',url,41,logos+'phimb.png')	
	  	  
def filmmobile(url):
  content=makeRequest(url)
  match=re.compile('title="(.+?)" class.+? href="\/(.+?)">\s*<img height.+?src="(.+?)"').findall(content)		
  for name,url,thumbnail in match:
    if 'jpg' in thumbnail:
      addDir('[COLOR yellow]'+name+'[/COLOR]',phimmobile+url,19,phimmobile+thumbnail)
    else:
      addDir('[COLOR yellow]'+name+'[/COLOR]',phimmobile+url,19,phimmobile+'images/movies.jpg')          
  match=re.compile('href="\/(.+?)\?.+?">(\d+)<').findall(content)
  for url,name in match:
    url=url.replace('=','/')	
    addDir('[COLOR lime]Trang '+name+'[COLOR cyan] >>>>[/COLOR]',phimmobile+url,18,logos+'mobile.png')

def mobile_video_link(url,name):
  content=makeRequest(url)
  thumbnail=re.compile('src="\/u(.+?)"').findall(content)[0]
  content=makeRequest(url.replace('/phim/','/xem-phim-online/'))
  match=re.compile('value="\/(.+?)".*>(.+?)<').findall(content)		
  for url,inum in match:
    if 'jpg' in thumbnail:
      add_Link('[COLOR lime]Tập '+inum+'[COLOR magenta] - '+name+'[/COLOR]',phimmobile+url,phimmobile+'u'+thumbnail)   
    else:
      add_Link('[COLOR lime]Tập '+inum+'[COLOR magenta] - '+name+'[/COLOR]',phimmobile+url,phimmobile+'images/movies.jpg') 
        
def mobile_search_result(url):
  content=makeRequest(url)
  match=re.compile('href="\/(.+?)">(.+?)-.+?<').findall(content)  
  for url,name in match:
    addDir('[COLOR yellow]'+name+'[/COLOR]',phimmobile+url,20,logos+'mobile.png')
  
def megaListEps(url):	
  content = makeRequest(url)
  if 'phim-bo' in url:
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s.*\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      addDir('[COLOR yellow]' + title + '[/COLOR]',url,8,thumbnail + '?.jpg')  
  else:	  
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s*\s.+\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      if 'victorias-secret-fashion-show' in url:
        add_Link('[COLOR lime]' + title + '[/COLOR]',url.replace('/phim-', '/xem-phim-'),thumbnail + '?.jpg')
      else:		
        addDir('[COLOR yellow]' + title + '[/COLOR]',url,8,thumbnail + '?.jpg')

def dangcapmovie_search_result(url):
  content = makeRequest(url)
  match = re.compile('href="(.+?)" title="(.+?)" data-tooltip=".+?">\s*<img src="(.+?)"').findall(content)
  for url,name,thumbnail in match:
    url=url.replace('/movie-','/watch-')
    addDir('[COLOR lime]' + name  + '[/COLOR]',url.replace('/movie-','/watch-'),8,thumbnail)
        
def index(url):
  content=makeRequest(url)
  if 'phim3s' in url:
    match=re.compile("<div class=\"inner\"><a href=\"(.*?)\" title=\"([^\"]*)\"><img src=\"(.+?)\"").findall(content)
    for url,name,thumbnail in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',('%s%sxem-phim' % (phim3s, url)),4,thumbnail)					
    match=re.compile("<span class=\"item\"><a href=\"([^\"]*)\">(\d+)<\/a><\/span>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',('%s%s' % (phim3s, url)),3,logos+'phim3s.png')					
  elif 'dangcaphd' in url:
    match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(content)
    for url,name,thumbnail in match:
      if 'Trailer' in name:
        pass
      else:      
        add_Link('[COLOR yellow]'+name+'[/COLOR]',(url.replace('movie','watch')),thumbnail) 
    match=re.compile("<a href=\"([^\"]+)\">&lt;&lt;<\/a>").findall(content)
    for url in match:
      addDir('[COLOR cyan]Trang Đầu[/COLOR]',url.replace('amp;',''),3,logos+'dchd.png')
    #match=re.compile("<a href=\"([^\"]*)\">&lt;<\/a>").findall(content)
    #for url in match:
      #addDir('[COLOR cyan]Trang Kế Trước[/COLOR]',url.replace('amp;',''),3,logos+'dchd.png')	
    match=re.compile("<a href=\"([^>]*)\">(\d+)<\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',url.replace('amp;',''),3,logos+'dchd.png')
    #match=re.compile("<a href=\"(.+?)\">&gt;<\/a>").findall(content)
    #for url in match:
      #addDir('[COLOR blue]Trang Kế Tiếp[/COLOR]',url.replace('amp;',''),3,logos+'dchd.png')
    match=re.compile("<a href=\"([^\"]*)\">&gt;&gt;<\/a>").findall(content)
    for url in match:
      addDir('[COLOR red]Trang Cuối[/COLOR]',url.replace('amp;',''),3,logos+'dchd.png')
  elif 'phimgiaitri' in url:
    match=re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)\s*<\/font>').findall(content)
    for url,thumbnail,name in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',pgt+url+'/Tap-1.html',pgt+thumbnail)					
    match=re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),3,logos+'pgt.png')					
  elif 'phimhayhd' in url:
    match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=".+?">(.+?)</span>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
    for thumbnail, cat, url, name in match:
      add_Link('[COLOR cyan]' + name + ' - [COLOR magenta]' + cat + '[/COLOR]', url, thumbnail)   
    match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
    for thumbnail, url, name in match:
      add_Link('[COLOR yellow]' + name + '[/COLOR]', url,thumbnail)
    match = re.compile('href="(.+?)">Trang đầu<').findall(content)
    for url in match:
      addDir('[COLOR cyan]Trang đầu[/COLOR]', url, 2, logos + 'hayhd.png')
    match = re.compile("href='(.+?)'>(\d+)<").findall(content)
    for url, inum in match:
      if url=='#':
        pass
      else:  
        addDir('[COLOR lightgreen]Trang ' + inum + '[/COLOR]', url, 2, logos + 'hayhd.png')
    match = re.compile('href="([^"]*)">Trang cuối<').findall(content)
    for url in match:
      addDir('[COLOR red]Trang cuối[/COLOR]', url, 2, logos + 'hayhd.png')

def episodes_714(url,name):
  content=makeRequest(url)
  name=name.replace('[COLOR lime]','').replace('[/COLOR]','')
  if 'phim7' in url:    
    match=re.compile('<p class=".+?"><b>'+name+'</b>((?s).+?)</p>').findall(content)
    for vlinks in match:
      match=re.compile('href="(.+?)" title="(.+?)" class=".+?">(.+?)<').findall(vlinks)
      for url,title,eps in match:
        add_Link('[COLOR cyan]'+eps+'[/COLOR]',phim7+url,iconimage)	
  elif 'phim14' in url:
    match=re.compile('<strong><img src=".+?"/>'+name+'</strong>\s*<ul((?s).+?)</ul>').findall(content)  
    for vlinks in match:
      match=re.compile('href="(.+?)" episode-type=".+?" title="(.+?)">(.+?)<').findall(vlinks)
      for url,title,eps in match:
        add_Link('[COLOR cyan]'+title+'[/COLOR]',url,iconimage)	
  
	  
def videoLinks(url,name):
  content=makeRequest(url)
  thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(content)[0]		
  match=re.compile("data-type=\"watch\" data-episode-id.+?href=\"([^\"]*)\" title=\"(.*?)\"").findall(content)
  for url,title in match:
    addLink(('%s   -   %s' % ('[COLOR lime]'+title+'[/COLOR]',name )),('%s%svideo.mp4' % (phim3s, url)),thumbnail)
	
def pgtri():
  #addDir('[COLOR cyan]Phimgiaitri[/COLOR]',pgt,5,logos+'pgt.png')
  content=makeRequest(url)
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[0]  
  addDir('[COLOR yellow]'+match+'[/COLOR]',pgt,2,logos+'pgt.png')			
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[1]		
  addDir('[COLOR lime]'+match+'[/COLOR]',pgt,6,logos+'pgt.png')	
 
def dirs(url):
  content=makeRequest(url) 
  if 'phimgiaitri' in url:
    addDir('[COLOR yellow]phimgiaitri[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim Bộ[/COLOR]',pgt,9,logos+'pgt.png')
    match=re.compile('<a href=\'result.php\?type=Phim Bộ(.+?)\'><span>(.+?)<\/span>').findall(content) 
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',pgt+'result.php?type=Phim%20B%E1%BB%99'+url.replace(' ','%20'),7,logos+'pgt.png')
  elif 'fptplay' in url:
    match=re.compile("<h3><a href=\"(.+?)\">(.+?)<\/a><\/h3>").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,mode_opt,logos+'fptplay.png')

def phimb_mediaList(url):
  content=phimbRequest(url)	
  match=re.compile('href="(.+?)" title="(.+?)"><img.+?src="(.+?)"').findall(content)
  for url,name,iconimage in match:
    addDir('[COLOR yellow]'+name+'[/COLOR]',url.replace('/phim/','/xem-phim/'),42,iconimage)
  match=re.compile("title='Trang(.+?)' href='(.+?)'").findall(content)
  for page,url in match:
    if 'đầu' in page:
	  addDir('[COLOR cyan]Trang '+page+'[/COLOR]',phimb+url,41,logos+'phimb.png')	
    elif 'cuối' in page:
	  addDir('[COLOR red]Trang '+page+'[/COLOR]',phimb+url,41,logos+'phimb.png')	
    else:
	  addDir('[COLOR lime]Trang '+page+'[/COLOR]',phimb+url,41,logos+'phimb.png')  

def serverlist_phimb(url):
  content=phimbRequest(url)
  match=re.compile('<div class="svname">(.+?)<\/div>').findall(content)
  for sname in match:
    addDir('[COLOR lime]'+sname+'[/COLOR]',url,43,iconimage)
	  
def mediaList(url):
  content=makeRequest(url)
  if 'phimgiaitri' in url:  
    match=re.compile('href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><div class=\'text\'>\s*<p>.+?<\/p>\s*<\/div>.+?>([^<]*)\s*<\/').findall(content)
    for url,thumbnail,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',pgt+url+'/Tap-1.html',8,pgt+thumbnail)				
    match=re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR yellow]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),7,logos+'pgt.png')
  elif 'fptplay' in url:
    match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(content)
    for url,iconimage,name in match: 
      addDir('[COLOR lime]'+name.replace('amp;','')+'[/COLOR]',fptplay+url,8,iconimage)
    match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]Trang '+name+'[/COLOR]',fptplay+url,7,logos+'fptplay.png')
  elif 'zui' in url:
    match=re.compile('<a data-tooltip=".+?" href="(.+?)" title="(.+?)".+?>\s*<img src="(.+?)"').findall(content)
    if 'phim-bo' in url:
      for url,name,thumbnail in match:
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,8,thumbnail)
      match=re.compile("<a href=\"([^\"]*)\" title='.+?'>([^>]*)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name.replace('&laquo;','[COLOR cyan]Kế Trước').replace(' &raquo;','[COLOR magenta]Kế Tiếp')+'[/COLOR]',url,7,logos+'zui.png')	  
    else:
      for url,name,thumbnail in match:
        add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)
      match=re.compile("<a href=\"([^\"]+)\" title='.+?'>([^>]*)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name.replace('&laquo;','[COLOR cyan]Kế Trước').replace(' &raquo;','[COLOR magenta]Kế Tiếp')+'[/COLOR]',url,7,logos+'zui.png')
  elif 'hdcaphe' in url:
    match=re.compile("a style=\"position: relative;display: block;\" href=\"(.+?)\">\s*<img class=\"imgborder\" width=\"165\" src=\"(.+?)\"").findall(content)		
    for url,thumbnail in match:
      addDir('[COLOR lime][UPPERCASE]'+url.replace('detail/movies/','').replace('-',' ').replace('.html','')+'[/UPPERCASE][/COLOR]',hd_caphe+url.replace('detail','video').replace('.html','/play/clip_1.html'),8,hd_caphe+thumbnail)
    match=re.compile("<span class=\"next\"><a href=\"(.+?)\" class=\"next\" title=\"(.+?)\">").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name.replace('Go to page','Trang')+' >>>>[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    match=re.compile("<span class=\"last\"><a href=\"(.+?)\" class=\"last\" title=\"(.+?)\">").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name.replace('Go to page','Trang')+'[COLOR cyan][B] = [/B][COLOR red]Trang cuối cùng >>>>[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
  elif 'phimhayhd' in url:
    match = re.compile('data-src="(.+?)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=.+?>(.+?)</span>\s*<span class=".+?"></span>\s*\s*<span class=".+?">\s*(.+?)</span>\s*</div>\s*<div class=".+?">\s*<a href="(.+?)" class="title">(.+?)<').findall(content)
    for thumbnail, cat, temp, url, name in match:
      addDir('[COLOR orange]' + name + ' - [COLOR magenta]' + cat + '[/COLOR]', url, 8, thumbnail)      
    match = re.compile('data-src="(.+?)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=".+?"></span>\s*\s*<span class=".+?">\s*(.+?)</span>\s*</div>\s*<div class=".+?">\s*<a href="(.+?)" class="title">(.+?)<').findall(content)
    for thumbnail, temp, url, name in match:
      addDir('[COLOR lime]' + name + '[/COLOR]', url, 8, thumbnail)
    match = re.compile('href="(.+?)">Trang đầu<').findall(content)
    for url in match:
      addDir('[COLOR cyan]Trang đầu[/COLOR]', url, 7, logos + 'hayhd.png')
    match = re.compile("href='(.+?)'>(\d+)<").findall(content)
    for url, inum in match:
      if url=='#':
        pass
      else:
        addDir('[COLOR lightgreen]Trang ' + inum + '[/COLOR]', url, 7, logos + 'hayhd.png')
    match = re.compile('href="([^"]*)">Trang cuối<').findall(content)
    for url in match:
      addDir('[COLOR red]Trang cuối[/COLOR]', url, 7, logos + 'hayhd.png')
  elif 'dangcapmovie' in url:
    match = re.compile('href="(.+?)" title="(.+?)" data-tooltip=".+?">\s*<img src="(.+?)"').findall(content)
    for url,name,thumbnail in match:
      url=url.replace('/movie-','/watch-')
      addDir('[COLOR cyan]' + name  + '[/COLOR]',url.replace('/movie-','/watch-'),8,thumbnail)
    match = re.compile('href="([^"]*)">(\d+|&gt;&gt;|&lt;&lt;)<').findall(content)
    for url,name in match:
      url=url.replace('&amp;','&')
      if '&lt;&lt;' in name:
        name=name.replace('&lt;&lt;','First')
        addDir('[COLOR yellow]' + name + ' Page[/COLOR]',url,7,logos + 'dcm.png')
      elif '&gt;&gt;' in name:
        name=name.replace('&gt;&gt;','Last')
        addDir('[COLOR red]' + name + ' Page[/COLOR]',url,7,logos + 'dcm.png')      
      else:
        addDir('[COLOR lime]Page ' + name + '[/COLOR]',url,7,logos + 'dcm.png')
  elif 'phim7' in url:
    match=re.compile('href="(.+?)" title="(.+?)"><span class="poster">\s*<img src=".+?" alt="" />\s*<img class=".+?" src=".+?" data-original="(.+?)"').findall(content)
    for url,name,iconimage in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',phim7+url.replace('/phim/','/xem-phim/'),31,iconimage)
    match=re.compile("href='(.+?)' >(\d+)<").findall(content)
    for url,page in match:
      addDir('[COLOR lime]Page '+page+'[/COLOR]',phim7+url,7,logos+'phim7.png')
  elif 'phim14' in url:	  
    match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)"').findall(content)
    for url,name,iconimage in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',url.replace('/phim/','/xem-phim/'),31,iconimage)
    match=re.compile('<span class="item"><a href="(.+?)">(\d+)<').findall(content)
    for url,pageNum in match:
	  addDir('[COLOR lime]Trang '+pageNum+'[/COLOR]',url,7,logos+'phim14.png')
	  
def serverlist_714(url):
  content=makeRequest(url)
  if 'phim7' in url:
    match=re.compile('<p class=".+?"><b>(.+?)</b>').findall(content)
    for sname in match:
      addDir('[COLOR lime]'+sname+'[/COLOR]',url,32,iconimage)
  elif 'phim14' in url:	 
    match=re.compile('<strong><img src="http://phim14.net/res//images/flag/vn.png"/>(.+?)</strong>').findall(content) #duplicate servers' name
    for sname in match:
      if 'Download' in sname:
	    pass
      else:
        addDir('[COLOR lime]'+sname+'[/COLOR]',url,32,iconimage)
  
def videoclip_7(url):
  content=makeRequest(url)
  match=re.compile('href="(.+?)" title="(.+?)"><span class="poster">\s*<img src=".+?" alt="" />\s*<img class=".+?" src=".+?" data-original="(.+?)"').findall(content)
  for url,name,iconimage in match:
    add_Link('[COLOR lime]'+name+'[/COLOR]',phim7+url.replace('/phim/','/xem-phim/'),iconimage)
  match=re.compile("href='(.+?)' >(\d+)<").findall(content)
  for url,page in match:
    addDir('[COLOR yellow]Page '+page+'[/COLOR]',phim7+url,22,logos+'phim7.png')
	  	    
def anhtrang_mediaList(url):
  content=makeRequest(url)
  match=re.compile("<a href=\"([^\"]*)\" title=\"([^\"]+)\"><img src=\"(.+?)\"").findall(content)		
  for url,name,thumbnail in match:
    addDir('[COLOR yellow]'+name+'[/COLOR]',url,14,thumbnail)
  match=re.compile("<a class=\"pagelink\" href=\"(.+?)\">(.+?)<\/a>").findall(content)
  for url,name in match:	
    addDir('[COLOR lime]Trang '+name+'[COLOR cyan] >>>>[/COLOR]',url,12,logos+'anhtrang.png')
  match=re.compile("<a class=\"pagelast\" href=\"([^\"]*)\">(.+?)<\/a>").findall(content)
  for url,name in match:	
    addDir('[COLOR red]Trang '+name.replace('Cuối','[COLOR red]Cuối[COLOR magenta] >>>>')+'[/COLOR]',url,12,logos+'anhtrang.png')

def fpt_img(url):
  content=makeRequest(url)
  match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(content)
  for url1,thumbnail,name in match:	
    name=name.replace('amp;','')
    content1=makeRequest(fptplay+url1)	
    match1=re.compile('data="([^"]*)" href.*?onclick.+?<a>(\d+)<').findall(content1)
    for url2,inum in match1:
      #add_Link('%s - %s' % ('[COLOR cyan]Tập '+inum,'[COLOR lime]'+name+'[/COLOR]'),'%s%s' % (fptplay,url2),thumbnail)
      add_Link(('%s - %s' % ('[COLOR cyan]Tập '+inum,'[COLOR lime]'+name+'[/COLOR]')).replace('Tập 1 - ',''),'%s%s' % (fptplay,url2),thumbnail)          
  match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
  for url,name in match:	
    addDir('[COLOR yellow]Trang '+name+'[/COLOR]',fptplay+url,16,logos+'fptplay.png')         
    
def episodes(url,name):
  content=makeRequest(url)
  if 'phimgiaitri' in url:    
    thumbnail=re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)
    add_Link('[COLOR yellow]Tập 1  -  [/COLOR]'+name,url,thumbnail[0])
    match=re.compile("<a href=\"(.+?)\" page=(\d+)>").findall(content)
    for url,title in match:
      add_Link('[COLOR yellow]Tập '+title+'  -  '+name+'[/COLOR]',url,thumbnail[0])
  elif 'fptplay' in url:
    title=re.compile('<title>([^\']+)</title>').findall(content)[-1].replace('amp;','')		
    match=re.compile('data="([^"]*)" href.*?onclick.+?<a>(\d+)<').findall(content)
    for url,inum in match:
      add_Link(('%s - %s' % ('[COLOR lime]Tập '+inum,'[COLOR yellow]'+title+'[/COLOR]')).replace('Tập 1 - ',''),('%s%s' % (fptplay, url)),iconimage)
  elif 'zui' in url:
    thumbnail=re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)[0]		
    match=re.compile('<a id=\'.+?\' href=\'(.+?)\'  >(.+?)<\/a><\/li>').findall(content)
    for url,episode in match:
      add_Link(('%s   -   %s' % ('[COLOR lime]Tập '+episode+'[/COLOR]',name )),zui+url,'http://vncdn.zui.vn'+thumbnail)					
  elif 'hdcaphe' in url:
    add_Link(name,url,logos+'hdcaphe.png')  
    match=re.compile("<a style=\"margin-left:10px\" href=\"(.+?)\"  >(\d+)<\/a>").findall(content)
    for url,title in match:
      add_Link('[COLOR yellow]Tập '+title+'[/COLOR]',hd_caphe+url,logos+'hdcaphe.png')  
  elif 'megabox' in url:
    thumbnail = re.compile ('<link rel="image_src" href="(.+?)"').findall(content)[-1]
    match = re.compile('<option selected="selected"  value="(.+?)">(.+?)<\/option>').findall(content)
    for url, title in match:
      add_Link('[COLOR cyan]' + title + '[COLOR magenta] - ' + name + '[/COLOR]',megaboxvn + url,thumbnail + '?.jpg')     
    match = re.compile('<option  value="(.+?)">(.+?)<\/option>').findall(content)
    for url, title in match:
      add_Link('[COLOR cyan]' + title + '[COLOR magenta] - ' + name + '[/COLOR]',megaboxvn + url,thumbnail + '?.jpg') 
  elif 'phimhayhd' in url:
    thumbnail = re.compile('img class="thumbnail" src="(.+?)"').findall(content)[0]
    match = re.compile('href="(.+?)" class="episode.+?">(.+?)<').findall(content)
    for url, title in match:
      add_Link('[COLOR cyan]' + title + '[COLOR lime] - ' + name + '[/COLOR]',url,thumbnail) 
  elif 'dangcapmovie' in url:
    thumbnail=re.compile('rel="image_src" href="(.+?)"').findall(content)[0]
    match = re.compile('episode="(.+?)" _link="(.+?)" _sub=".+?"').findall(content)
    for eps,url1 in match:
      content1 = makeRequest(url1)
      match1 = re.compile('{"url":"https://redirector(.+?)","height".+?"video.+?"}').findall(content1)
      if eps=='1':
        add_Link(name,'https://redirector'+match1[-1],thumbnail)    
      else:
        add_Link('[COLOR yellow]Tập ' + eps+ '[/COLOR]','https://redirector'+match1[-1],thumbnail)
        
def otherMegaList(url):	
  content = makeRequest(url)
  if 'video-clip' in url:
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s*\s.+\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      add_Link('[COLOR lime]' + title + '[/COLOR]',url.replace('/phim-', '/xem-phim-'),thumbnail + '?.jpg')  
  else:
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s.*\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      add_Link('[COLOR lime]' + title + '[/COLOR]',url.replace('/phim-', '/xem-phim-'),thumbnail + '?.jpg')
   
def anhtrang_eps(url,name):
  thumb=makeRequest(url)
  thumbnail=re.compile('meta property="og:image" content="(.+?)"').findall(thumb)[0]
  newurl=url.replace(anhtrang,m_anhtrang)
  content=makeRequest(newurl)  
  add_Link('[COLOR lime]Tập 1'+'[COLOR cyan][B]  -  [/B][/COLOR]'+name,newurl,thumbnail)
  match=re.compile('<a href="(.+?)" class="ep">(.+?)<\/a>').findall(content)
  for url,title in match:
    add_Link('[COLOR lime]Tập '+title+'[COLOR cyan][B]  -  [/B][/COLOR]'+name,url,thumbnail)   
  
def inquiry():
  try:
    keyb=xbmc.Keyboard('', '[COLOR lime]Enter search text[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    if 'Tìm Phim Bộ' in name:  
      url=pgt+'result.php?type=search&keywords='+searchText  
      mediaList(url)
    elif 'phimhayhd' in name:
      url = hayhd + 'tim-kiem.html?query=' + searchText  
      hayhd_le(url)
  except: pass

def hayhd_le(url):	
  content = makeRequest(url)
  match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=".+?">(.+?)</span>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
  for thumbnail, cat, url, name in match:
    add_Link('[COLOR cyan]' + name + ' - [COLOR magenta]' + cat + '[/COLOR]', url, thumbnail)   
  match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
  for thumbnail, url, name in match:
    add_Link('[COLOR yellow]' + name + '[/COLOR]', url,thumbnail)
  
def resolveUrl(url):
  if 'fptplay' in url:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    req.add_header('Referer', fptplay)
    response=urllib2.urlopen(req, timeout=120)
    link=response.read()
    response.close()    
    mediaUrl=link 
  elif 'dangcaphd' in url:
    content=makeRequest(url)
    try:	
	    mediaUrl=re.compile('<a _episode="1" _link="(.+?)_\d_\d+.mp4"').findall(content)[0].replace('demophimle','phimle2112')+'.mp4'	  
    except:
      mediaUrl=re.compile('<a _episode="1" _link="(.+?)"').findall(content)[0].replace(' ','%20')
  elif 'phimgiaitri' in url:
    content=makeRequest(url)	
    match = re.compile('file: "rtmpe:\/\/5318b6e71a98f.streamlock.net(.+?)"').findall(content)[0]  
    if '/media1/' in match:
      mediaUrl = 'http://phimgiaitri.vn/phimtxn/' + match.replace('/media1/mp4:','')
    else:
      mediaUrl = 'http://phimgiaitri.vn:81/phimtxn/' + match.replace('/media2/mp4:','') 
  elif 'zui' in url:
    content=makeRequest(url)
    mediaUrl='rtmp'+re.compile("'rtmp(.+?)'").findall(content)[0]#+'/playlist.m3u8'
  elif 'hdcaphe' in url:
    content=makeRequest(url)	
    mediaUrl=re.compile('\'http.startparam\':\'start\',\s*file: \'(.+?)\'').findall(content)[0].replace(' ','%20')	
  elif 'anhtrang' in url:
    content=makeRequest(url)
    try:
      mediaUrl=re.compile("<source src=\"([^\"]*)\"").findall(content)[0]
    except: 
      mediaUrl=re.compile("var video_src_mv=\"(.+?)\"").findall(content)[0]
  elif 'megabox' in url:
    content=makeRequest(url)
    videoUrl = re.compile('file: "(.+?)"').findall(content)[0]
    if 'youtube' in videoUrl:
      mediaUrl = videoUrl.replace('https://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/?action=play_video&videoid=')
    else:
      mediaUrl = videoUrl 
  elif 'phimhayhd' in url:
    content=makeRequest(url)
    mediaUrl = re.compile('"film":{"url":"(.+?)m3u8"').findall(content)[0].replace('\\','')+'m3u8' 
  elif 'phimmobile' in url:
    content=makeRequest(url)
    try:
      mediaUrl=phimmobile+re.compile('src="\/(.+?)"><\/source>').findall(content)[0]
    except:
      mediaUrl='plugin://plugin.video.youtube/play/?video_id='+re.compile('file: "https://www.youtube.com/watch\?v=(.+?)"').findall(content)[-1]        
  elif 'phim7' in url:
    content=makeRequest(url)  
    try:
      mediaUrl='https://redirector'+re.compile('file: "https://redirector(.+?)", label:".+?", type: "video/mp4"').findall(content)[-1]
    except:
      mediaUrl='plugin://plugin.video.youtube/?action=play_video&videoid='+re.compile('file : "http://www.youtube.com/watch\?v=(.+?)&amp').findall(content)[0]
  elif 'phimb' in url:
    url=url.replace('http://www.phimb.net','http://m.phimb.net')
    req=urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16')
    response=urllib2.urlopen(req, timeout=60)
    content=response.read()
    response.close()
    try:  
      mediaUrl=re.compile('source src="(.+?)"').findall(content)[0]
    except:
      mediaUrl='plugin://plugin.video.youtube/?action=play_video&videoid='+re.compile('src="http://www.youtube.com/embed/(.+?)\?.+?"').findall(content)[0]    
  elif 'phim14' in url:
    url=url.replace('http://phim14.net','http://m.phim14.net')
    req=urllib2.Request(url)
    req.add_header('User-Agent' , 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3')
    req.add_header('Cookie' , 'window.location.href')
    response=urllib2.urlopen(req)
    content=response.read()
    response.close()  
    try:  
      mediaUrl=re.compile('source src="(.+?)"').findall(content)[0]
    except:
      try:
        mediaUrl='plugin://plugin.video.youtube/?action=play_video&videoid='+re.compile('src="http://www.youtube.com/embed/(.+?)\?.+?"').findall(content)[0]  
      except:
	    mediaUrl='plugin://plugin.video.dailymotion_com/?mode=playVideo&url='+re.compile('<iframe src="http://www.dailymotion.com/embed/video/(.+?)" width.+?</iframe>').findall(content)[0]	
  else:
    mediaUrl = url  
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
    
def add_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=10"+"&iconimage="+urllib.quote_plus(iconimage)  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  
  
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
  search()
		
elif mode==2:
  categories(url)
				
elif mode==3:
  index(url)
        
elif mode==4:
  videoLinks(url,name)

elif mode==5:
  pgtri()
  
elif mode==6:
  dirs(url)
  
elif mode==7:
  mediaList(url)
  
elif mode==8:
  episodes(url,name)
  
elif mode==9:
  inquiry()
 
elif mode==10:
  resolveUrl(url)

elif mode==11:
  megavn(url)
  
elif mode==12:
  anhtrang_mediaList(url) 

elif mode==13:
  megaListEps(url) 
  
elif mode==14:
  anhtrang_eps(url,name)  

elif mode==15:
  otherMegaList(url)

elif mode==16:
  fpt_img(url)
  
elif mode==17:
  mysettings.openSettings()
 
elif mode==18:
  filmmobile(url)

elif mode==19:
  mobile_video_link(url,name)

elif mode==30:
  videoclip_7(url) 
  
elif mode==31:
  serverlist_714(url)  

elif mode==32:
  episodes_714(url,name) 

elif mode==40:
  phimb_cat(url) 

elif mode==41:
  phimb_mediaList(url) 

elif mode==42:
  serverlist_phimb(url)

elif mode==43:
  episodes_phimb(url,name)
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))