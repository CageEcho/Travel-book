import os; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import json, re, urllib.request, urllib.parse, sys, time
UA={'User-Agent':'FolioDemo/1.0 (travel brochure demo; contact local)'}
Q0={
 'cover':'Istanbul Suleymaniye Mosque Golden Horn skyline sunset',
 'bluemosque':'Sultan Ahmed Mosque exterior blue sky',
 'bosphorus':'Bosphorus Bridge panorama Istanbul',
 'dolma_gate':'Dolmabahce Palace gate Bosphorus',
 'dolma_in':'Dolmabahce Palace interior chandelier',
 'dolma_ext':'Dolmabahce Palace facade garden',
 'galata':'Galata Tower street Istanbul',
 'ferry':'Istanbul ferry Kadikoy',
 'cat':'Istanbul street cat',
 'breakfast':'Turkish breakfast table',
 'simit':'Simit Istanbul',
 'tea':'Turkish tea glass',
 'kunefe':'Kunefe dessert',
 'balik':'Balik ekmek Eminonu',
 'cap_balloons':'Cappadocia hot air balloons Goreme sunrise',
 'cap_pano':'Cappadocia balloons panorama valley',
 'goreme':'Goreme town view evening',
 'rosevalley':'Rose Valley Cappadocia',
 'redvalley':'Red Valley Cappadocia hiking',
 'avanos':'Avanos pottery',
 'cavehotel':'Cappadocia cave hotel terrace',
 'testi':'Testi kebab',
 'kaleici':'Antalya Kaleici harbour',
 'konyaalti':'Konyaalti beach Antalya',
 'suluada':'Suluada island',
 'hadrian':'Hadrian Gate Antalya',
 'market':'Turkish market fruit stall',
 'antalya_cliff':'Antalya cliffs sea',
}
ok_lic=re.compile(r'^(CC0|Public domain|CC BY(-SA)? [0-9.]+|CC BY(-SA)?)',re.I)
def strip(h): return re.sub(r'<[^>]+>','',h or '').strip()
out=json.load(open('images/credits.json'))

Q={
 'uchisar':'Uchisar castle Cappadocia',
 'boat':'Bosphorus cruise boat',
}
for key,q in Q.items():
    params={'action':'query','format':'json','generator':'search','gsrsearch':q+' filetype:bitmap','gsrnamespace':'6','gsrlimit':'15',
            'prop':'imageinfo','iiprop':'url|size|extmetadata|mime','iiurlwidth':'1200'}
    url='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(params)
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30))
    except Exception as e:
        print(key,'ERR',e); continue
    pages=sorted(d.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',99))
    pick=None
    for p in pages:
        ii=p['imageinfo'][0]; m=ii.get('extmetadata',{})
        lic=m.get('LicenseShortName',{}).get('value','')
        if ii.get('mime')!='image/jpeg' or not (0.5<ii['width']/ii['height']<2.2) or ii['width']<1400 or not ok_lic.match(lic): continue
        pick=(p,ii,m,lic);break
    if not pick: print(key,'NONE'); continue
    p,ii,m,lic=pick
    fn=f'images/{key}.jpg'
    try:
        urllib.request.urlretrieve if False else None
        data=urllib.request.urlopen(urllib.request.Request(ii['thumburl'],headers=UA),timeout=60).read()
        open(fn,'wb').write(data)
    except Exception as e:
        print(key,'DLERR',e); continue
    out[key]={'file':fn,'title':p['title'],'artist':strip(m.get('Artist',{}).get('value',''))[:80],'license':lic,'page':ii['descriptionurl'],'w':ii['width'],'h':ii['height']}
    print(key,'|',p['title'],'|',lic,'|',ii['width'],'x',ii['height'])
    time.sleep(4)
json.dump(out,open('images/credits.json','w'),ensure_ascii=False,indent=1)
