import requests
url='https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text'
r=requests.get(url)
r.encoding='utf8'
data=str(r.text)


begin=data.find('One year ago, I stood before')
end=data.rfind('Thank you very much. Thank you. (Applause.)')


s=data[begin:end+43]
s=s.replace('\n','')

for k in range(999):
	if '</p>' in s:
		a=s.find('</p>')
		b=s.find('id="')
		c=s[a:b+12]
		s=s.replace(c,' ')
				
s=s.replace('.','')
s=s.replace(',','')
s=s.replace('(Applause)','')
s=s.replace('(Laughter)','')
s=s.replace('(Laughter and applause)','')
s=s.replace('—',' ')
s=s.replace('"',' ')
s=s.replace("'",' ')
s=s.replace(':','')
s=s.replace(';','')
s=s.replace('–',' ')
s=s.replace('“',' ')
s=s.replace('”',' ')
s=s.replace('’s',' ')

s=s.lower()
s=s.split()

mydict={}
for w in s:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1

print('<최다 빈도 단어 20개>')
print()

mydict1=sorted(mydict, key=mydict.__getitem__, reverse=True)
mydict2=mydict1[:20]

for k in mydict2:
    print('%s: %s'%(k, mydict[k]))
