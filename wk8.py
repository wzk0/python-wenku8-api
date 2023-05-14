import requests
from bs4 import BeautifulSoup

cookies={'jieqiUserInfo':''}
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}

def back_space(num):
    num=int(num)
    if 0 < num < 1000:
        return 0
    elif 999 < num < 2000:
        return 1
    elif 1999 < num < 3000:
        return 2
    elif 2999 < num < 3456:
        return 3

def req(link):
	r=requests.get(link,cookies=cookies,headers=headers)
	soup=BeautifulSoup(r.text,features='html5lib')
	return soup

def get_bookcase():
	soup=req('https://www.wenku8.net/modules/article/bookcase.php')
	book=[]
	status=[]
	author=[]
	aid=[]
	for a in soup.select('span.hottext'):
		status.append(a.text)
	for b in soup.find_all('a'):
		if 'cid' in str(b):
			pass
		elif 'aid' in str(b):
			book.append(b.text)
			ls=str(b['href']).split('aid=')[-1].split('&bid')[0]
			aid.append(ls)
		elif 'authorarticle' in str(b):
			author.append(b.text)
	all_info=[]
	for b,a,s,d in zip(book,author,status,aid):
		dic={'name':b,'author':a,'status':s,'aid':d}
		all_info.append(dic)
	return all_info

def get_userdetail():
	soup=req('https://www.wenku8.net/userdetail.php')
	odd=soup.select('td.odd')
	even=soup.select('td.even')
	all_info=[]
	for i in range(len(odd)):
		all_info.append({str(odd[i].text).replace('：',''):str(even[i+1].text)})
	return all_info

'''
list_type:
总排行榜-allvisit
总推荐榜-allvote
月排行榜-monthvisit
月推荐榜-monthvote
周排行榜-weekvisit
周推荐榜-weekvote
日排行榜-dayvisit
日推荐榜-dayvote
最新入库-postdate
最近更新-lastupdate
总收藏榜-goodnum
字数排行-size
完结全本-done
'''
def get_toplist(list_type,page):
	if list_type!='done':
		soup=req('https://www.wenku8.net/modules/article/toplist.php?sort=%s&page=%s'%(list_type,page))
	else:
		soup=req('https://www.wenku8.net/modules/article/articlelist.php?fullflag=1&page=%s'%page)
	book=[]
	author=[]
	info=[]
	tag=[]
	note=[]
	td=soup.find_all('td')
	ls=str(td).split('\n')
	for l in ls:
		if '<b><a href=\"https://www.wenku8.net/book/' in l:
			book.append(l)
			position=ls.index(l)
			author.append(ls[position+1])
			info.append(ls[position+2])
			tag.append(ls[position+3])
			note.append(ls[position+4])
	all_info=[]
	for b,a,i,t,n in zip(book,author,info,tag,note):
		b=BeautifulSoup(b,features='html5lib')
		a=BeautifulSoup(a,features='html5lib')
		i=BeautifulSoup(i,features='html5lib')
		t=BeautifulSoup(t,features='html5lib')
		n=BeautifulSoup(n,features='html5lib')
		all_info.append({'name':b.find('a')['title'],'author':a.find('p').text,'info':i.find('p').text,'tag':t.find('p').text.replace('Tags:',''),'note':n.find('p').text})
	return all_info

def get_review(page):
	soup=req('https://www.wenku8.net/modules/article/reviewslist.php?page=%s'%page)
	tr=soup.find_all('tr')
	alll=[]
	all_info=[]
	for t in tr:
		if 'odd' in str(t):
			alll.append(t)
	for al in alll:
		td=al.find_all('td')
		all_info.append({'theme':td[0].text,'source':td[1].text,'num':td[2].text,'user':td[3].text,'time':td[4].text,'rid':td[0].find('a')['href'].split('rid=')[-1],'uid':td[3].find('a')['href'].split('uid=')[-1]})
	return all_info

'''
还没做好...
def get_reviewshow(rid,page):
	soup=req('https://www.wenku8.net/modules/article/reviewshow.php?rid=%s&page=%s'%(rid,page))
	alll=[]
	td=soup.find_all('td')
	for d in td:
		if 'avatar' in str(d):
			alll.append(d)
		if 'even' in str(d):
			alll.append(d)
	all_info=[]
	for al in alll:
		st=al.find_all('strong')
		uinfo=al.find_all('div')[0].text.split('\n')[5:-3]
		#uinfo=list(filter(None,div[0].text.replace('\t','').replace('\n',' ').replace('：','').split(' ')))[1:-3]
		#print(uinfo)
		user=st[0].find('a').text
		uid=st[0].find('a')['href'].split('uid=')[-1]
		identity=[uinfo[0].replace('\t\t\t\t',''),uinfo[1].replace('\t\t\t\t','')]
		jointime=uinfo[3].split('：')[-1]
		exp=uinfo[4].split('：')[-1]
		point=uinfo[-1].split('：')[-1]
'''

def req_book(fmt,num):
    r=requests.get('https://dl1.wenku8.com/down/txt%s/%s/%s.txt'%(fmt,back_space(num),num),headers=headers)
    r.encoding='utf-8'
    return r.text

'''
简体-utf8
繁体-big5
'''
def get_book(aid,fmt='utf8'):
    print(fmt)
    data=req_book(fmt,aid)
    title=data.split('\n')[2].replace('<','').replace('>','')
    with open('%s.txt'%title,'w')as f:
        f.write(data)
