import subprocess, re, array, wave, glob, os, sys
FF='/tmp/mv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v9.0.2'
SR=44100
def decode(f):
    raw=subprocess.run([FF,'-v','error','-i',f,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True,check=True).stdout
    a=array.array('h'); a.frombytes(raw); return a
def silences(f,th=0.42):
    err=subprocess.run([FF,'-hide_banner','-i',f,'-af','silencedetect=noise=-38dB:d=0.25','-f','null','-'],capture_output=True,text=True).stderr
    out=[]
    for m in re.finditer(r'silence_end: ([\d.]+) \| silence_duration: ([\d.]+)',err):
        e,d=float(m.group(1)),float(m.group(2))
        if d>=th: out.append(e-d/2)
    return out
def sil(sec): return array.array('h',[0]*int(SR*sec))
def encode(a,out,br='128k'):
    subprocess.run([FF,'-v','error','-y','-f','s16le','-ac','1','-ar',str(SR),'-i','-','-c:a','libmp3lame','-b:a',br,out],input=a.tobytes(),check=True)
def stretch(f,extra=0.4):
    a=decode(f); dur=len(a)/SR
    pts=[p for p in silences(f) if p<dur-0.8]  # skip trailing silence
    res=array.array('h'); last=0
    for p in pts:
        i=int(p*SR); res.extend(a[last:i]); res.extend(sil(extra)); last=i
    res.extend(a[last:]); return res,len(pts)
mode=sys.argv[1]
if mode=='join08':
    a=decode('parts/DUN003_VO_08a.mp3'); b=decode('parts/DUN003_VO_08b.mp3')
    # trim trailing/leading digital silence roughly then join with 0.55 s pause
    def trim(x):
        s=0
        while s<len(x) and abs(x[s])<60: s+=1
        e=len(x)
        while e>s and abs(x[e-1])<60: e-=1
        return x[s:e]
    j=trim(a); j.extend(sil(0.55)); j.extend(trim(b)); j.extend(sil(0.4))
    j=sil(0.15)+j
    encode(j,'DUN003_VO_08_chani_and_the_twins.mp3','64k')
    print('08',round(len(j)/SR,1))
else:
    files=sorted(glob.glob('DUN003_VO_[0-9]*.mp3'))
    full=array.array('h'); log=[]
    for k,f in enumerate(files):
        s,n=stretch(f); full.extend(s)
        if k<len(files)-1: full.extend(sil(2.5))
        log.append((f,n,round(len(s)/SR,1)))
    encode(full,sys.argv[2] if len(sys.argv)>2 else 'DUN003_VO_FULL_paced.mp3')
    for l in log: print(*l)
    print('TOTAL',round(len(full)/SR,1))
