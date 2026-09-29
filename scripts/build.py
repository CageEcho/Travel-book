import base64, json, re, subprocess, os, shutil
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
PYFT=shutil.which('pyftsubset') or '/tmp/fvenv/bin/pyftsubset'
s=open('index.html',encoding='utf-8').read()
# 1) images + credits (same as bundle.py)
cred=json.load(open('images/credits.json'))
used=set(re.findall(r"images/(\w+)\.jpg",s))
cred={k:{kk:vv for kk,vv in v.items() if kk!='file'} for k,v in cred.items() if k in used}
os.makedirs('build/img',exist_ok=True)
for k in used:
    src,dst=f'images/{k}.jpg',f'build/img/{k}.jpg'
    if not os.path.exists(dst):
        if shutil.which('sips'): subprocess.run(['sips','-Z','900','-s','format','jpeg','-s','formatOptions','55',src,'--out',dst],check=True,capture_output=True)
        else: shutil.copy(src,dst)
s=s.replace('/*CREDITS*/{}', json.dumps(cred,ensure_ascii=False))
for k in used:
    b=base64.b64encode(open(f'build/img/{k}.jpg','rb').read()).decode()
    s=s.replace(f"images/{k}.jpg",'data:image/jpeg;base64,'+b)
# 2) fonts: subset to the characters this page uses, embed as woff2
os.makedirs('build',exist_ok=True)
chars=set(open('index.html',encoding='utf-8').read())|set(chr(c) for c in range(0x20,0x7F))|set('，。、：；！？（）“”‘’—…·～《》【】')
open('build/chars.txt','w',encoding='utf-8').write(''.join(sorted(ch for ch in chars if ch.isprintable())))
FONTS=[('Long Cang','LongCang-Regular.ttf','400'),('Noto Sans SC','NotoSansSC[wght].ttf','100 900'),
       ('Noto Serif SC','NotoSerifSC[wght].ttf','200 900'),('Caveat','Caveat[wght].ttf','400 700'),
       ('Pinyon Script','PinyonScript-Regular.ttf','400'),('IBM Plex Mono','IBMPlexMono-Regular.ttf','400'),
       ('IBM Plex Mono','IBMPlexMono-Medium.ttf','500')]
faces=[]
for fam,fn,w in FONTS:
    out=f"build/{fn.replace('[wght]','-var').replace('.ttf','.woff2')}"
    subprocess.run([PYFT,f'fonts/{fn}','--text-file=build/chars.txt','--flavor=woff2',f'--output-file={out}','--layout-features=*'],check=True)
    b=base64.b64encode(open(out,'rb').read()).decode()
    faces.append(f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b}) format('woff2');font-weight:{w};font-style:normal;font-display:block}}")
    print(fam,w,os.path.getsize(out)//1024,'KB')
s=re.sub(r'<link rel="preconnect"[^>]*>\n','',s)
s=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>\n','',s)
assert 'fonts.googleapis' not in s
s=s.replace('<style>','<style>\n'+'\n'.join(faces)+'\n',1)
os.makedirs('dist',exist_ok=True)
out='dist/土耳其12日-翻书旅行方案.html'
open(out,'w',encoding='utf-8').write(s)
open('docs/index.html','w',encoding='utf-8').write(s)  # GitHub Pages serves docs/
print(out, os.path.getsize(out)//1024,'KB')
