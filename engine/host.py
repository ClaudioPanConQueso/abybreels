import numpy as np, subprocess, wave, math, sys
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro
W,H,FPS,SR=1080,1920,30,22050
FP='/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
fc={}
def F(s):
    if s not in fc: fc[s]=ImageFont.truetype(FP,s)
    return fc[s]
BG0=(8,13,38);GREEN=(110,230,150);WHITE=(255,255,255);GRAY=(125,140,175);SAL=(240,135,115);CARD=(18,28,60);OL=(60,95,140);BLUE=(55,95,190);SKIN=(240,196,160)
def M(c,a=1):return tuple(int(BG0[k]+(c[k]-BG0[k])*a) for k in range(3))
def E(t,t0,d=0.4):
    x=min(max((t-t0)/d,0),1);return 1-(1-x)**3
def EB(t,t0,d=0.45):
    x=min(max((t-t0)/d,0),1);c=1.4;return 1+(c+1)*(x-1)**3+c*(x-1)**2
S=[("¿Querés tu propio server? Primero entendé qué es un host.",)*2,
("Un host es una computadora siempre prendida, conectada a internet, que mantiene tu server online.",)*2,
("En tu PC se apaga y puede lagear. En un host, está online 24/7.","En tu Pe Ce se apaga y puede lagear. En un host, está online veinticuatro siete."),
("Tus amigos se conectan desde cualquier lugar y juegan en el mismo server.",)*2,
("Elegís el juego, pagás por semana o por mes, y lo activamos en minutos.",)*2,
("En AByB Host: online 24/7, sin lag, y soporte por WhatsApp y Discord.","En Abyb Host: online veinticuatro siete, sin lag, y soporte por Guasap y Discord."),
("Argentino, bueno y barato. Desde 600 pesos. Entrá a abybhost.online","Argentino, bueno y barato. Desde seiscientos pesos. Entrá a a b y b host punto online.")]
N=len(S);LEAD=0.3
K=Kokoro('k.onnx','v.bin');durs=[]
for i,(d_,sp) in enumerate(S):
    a,sr0=K.create(sp,voice='em_alex',speed=1.1,lang='es');a=np.asarray(a,dtype=np.float32)
    nn=int(len(a)*SR/sr0);a=np.interp(np.linspace(0,len(a)-1,nn),np.arange(len(a)),a);a=a/max(1e-6,np.abs(a).max())*0.95
    np.save(f'v{i}.npy',a);durs.append(len(a)/SR)
sd=[max(3.6,d+LEAD+0.6) for d in durs];st=np.cumsum([0]+sd);T=st[-1]
A=np.zeros(int(T*SR)+SR)
for i in range(N):
    x=np.load(f'v{i}.npy');s0=int((st[i]+LEAD)*SR);A[s0:s0+len(x)]+=x
t_=np.arange(len(A))/SR;rng=np.random.default_rng(1)
def lp(x,n):
    c=np.cumsum(np.insert(x,0,0));y=np.zeros_like(x);h=n//2
    y[:]=(c[np.clip(np.arange(len(x))+h+1,0,len(x))]-c[np.clip(np.arange(len(x))-h,0,len(x))])/n;return y
def saw(f,t):return 2*((f*t)%1)-1
bt=60/120;bar=bt*4
root=np.array([110.0,98.0,87.31,82.41])[((t_//(bar*2)).astype(int))%4]
eb=bt/2;pe=(t_%eb)/eb
g=lp(np.tanh((saw(root,t_)+saw(root*1.4983,t_)+saw(root*2,t_))*2.5)*np.exp(-pe*3),9)*0.2
bs=np.sin(2*np.pi*root/2*t_)*np.exp(-pe*1.5)*0.28
pb=t_%bt;bi=((t_//bt).astype(int))%4
kick=np.sin(2*np.pi*55*t_)*np.exp(-pb*14)*((bi==0)|(bi==2))*0.4
sn=lp(rng.standard_normal(len(t_)),12)*np.exp(-pb*16)*((bi==1)|(bi==3))*0.5
m=g+bs+kick+sn
ve=lp(np.abs(A),3000);duck=1-0.65*np.clip(ve*12,0,1)
A=np.clip(A+m*0.45*duck,-1,1)
wr=wave.open('a.wav','wb');wr.setnchannels(1);wr.setsampwidth(2);wr.setframerate(SR);wr.writeframes((A*32767).astype(np.int16).tobytes());wr.close()
# ---- drawing helpers
yy=np.linspace(0,1,H)[:,None,None]
BASE=Image.fromarray(np.repeat(np.array((11,18,50))*(1-yy)+np.array((5,8,26))*yy,W,1).astype(np.uint8))
def TX(d,x,y,s,size,col,a=1,anchor='la'):d.text((x,y),s,font=F(size),fill=M(col,a),anchor=anchor)
def pill(d,x,y,s,size,fg,bg,ol,a=1,c=False,pad=26):
    f=F(size);w=f.getlength(s);hh=int(size*1.9);x0=x-(w+2*pad)/2 if c else x
    d.rounded_rectangle((x0,y,x0+w+2*pad,y+hh),hh//2,fill=M(bg,a),outline=M(ol,a),width=2)
    d.text((x0+pad,y+hh/2),s,font=f,fill=M(fg,a),anchor='lm')
def card(d,box,a=1,r=30):d.rounded_rectangle(box,r,fill=M(CARD,a),outline=M(OL,a),width=3)
def ck(d,cx,cy,r,a=1,col=GREEN):
    r=int(r*a)
    if r<4:return
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=col);d.line((cx-r*.45,cy,cx-r*.1,cy+r*.4,cx+r*.5,cy-r*.35),fill=BG0,width=max(3,int(r*.2)),joint='curve')
def title(d,lines,t,size,t0=0.3):
    for k,(s,c) in enumerate(lines):
        e=E(t,t0+k*0.18);TX(d,80,250+k*int(size*1.18)+int(30*(1-e)),s,size,c,e)
def rack(d,cx,top,w,n,t,a=1):
    for k in range(n):
        y=top+k*100;x=cx-w//2
        d.rounded_rectangle((x,y,x+w,y+84),16,fill=M((28,40,78),a),outline=M(OL,a),width=3)
        on=math.sin(t*6+k*1.7)>-0.3
        d.ellipse((x+26,y+34,x+42,y+50),fill=M(GREEN if on else (30,70,60),a));d.ellipse((x+54,y+34,x+70,y+50),fill=M((240,190,80) if math.sin(t*4+k)>0.2 else (70,60,40),a))
        for j in range(4):d.line((x+w-150+j*28,y+22,x+w-150+j*28,y+62),fill=M((70,95,150),a),width=5)
def monitor(d,x,y,w,h,t,a=1):
    d.rounded_rectangle((x,y,x+w,y+h),18,fill=M((30,42,80),a),outline=M(OL,a),width=3)
    d.rounded_rectangle((x+12,y+12,x+w-12,y+h-12),10,fill=M((14,24,52),a))
    for k in range(5):
        bh=30+int(25*math.sin(t*3+k));d.rectangle((x+30+k*(w//6),y+h-12-bh-10,x+30+k*(w//6)+int(w/9),y+h-22),fill=M(GREEN if k%2==0 else (70,170,120),a))
    d.rectangle((x+w//2-14,y+h,x+w//2+14,y+h+36),fill=M((40,55,105),a));d.rounded_rectangle((x+w//2-60,y+h+34,x+w//2+60,y+h+48),6,fill=M((40,55,105),a))
def avatar(d,cx,cy,col,a=1,s=1.0):
    r=int(36*s);d.rounded_rectangle((cx-int(58*s),cy+int(8*s),cx+int(58*s),cy+int(90*s)),int(34*s),fill=M(col,a))
    d.ellipse((cx-r,cy-int(44*s),cx+r,cy+int(28*s)),fill=M(SKIN,a))
def gamer(d,cx,cy,t,a=1):
    bob=int(4*math.sin(t*3))
    d.rounded_rectangle((cx-130,cy-330,cx-70,cy+20),24,fill=M((40,55,105),a))
    d.rounded_rectangle((cx-70,cy-70,cx+190,cy-20),22,fill=M((32,44,90),a));d.rounded_rectangle((cx+150,cy-40,cx+200,cy+190),22,fill=M((32,44,90),a));d.rounded_rectangle((cx+140,cy+170,cx+250,cy+205),16,fill=M((20,28,60),a))
    d.rounded_rectangle((cx-200,cy-6,cx+640,cy+22),8,fill=M((60,75,130),a));d.rectangle((cx-160,cy+22,cx-144,cy+230),fill=M((60,75,130),a));d.rectangle((cx+580,cy+22,cx+596,cy+230),fill=M((60,75,130),a))
    d.rounded_rectangle((cx-90,cy-300,cx+50,cy-40),40,fill=M(BLUE,a))
    hy=int(3*math.sin(t*8));d.line((cx+20,cy-240,cx+170,cy-72+hy),fill=M(BLUE,a),width=44);d.ellipse((cx+150,cy-94+hy,cx+194,cy-50+hy),fill=M(SKIN,a))
    d.ellipse((cx-45,cy-420+bob,cx+55,cy-320+bob),fill=M(SKIN,a));d.pieslice((cx-48,cy-428+bob,cx+58,cy-330+bob),180,360,fill=M((40,40,70),a))
    d.arc((cx-55,cy-435+bob,cx+65,cy-315+bob),180,360,fill=M(GREEN,a),width=10);d.ellipse((cx-60,cy-385+bob,cx-30,cy-345+bob),fill=M(GREEN,a));d.line((cx-52,cy-350+bob,cx+10,cy-330+bob),fill=M(GREEN,a),width=6)
def sub(d,i,t):
    tt=t-LEAD
    if tt<0 or tt>durs[i]+0.4:return
    ws=S[i][0].split();ln=np.array([len(w)+2 for w in ws],float);cum=np.cumsum(ln)/ln.sum()*durs[i]
    idx=min(len(ws)-1,int(np.searchsorted(cum,tt)));c0=idx
    while c0>0 and F(44).getlength(' '.join(ws[c0-1:idx+1]))<780 and (idx-c0)<3: c0-=1
    # chunk by fixed groups for stability
    g=[];cur=[]
    for k,w in enumerate(ws):
        if cur and F(44).getlength(' '.join([ws[j] for j in cur]+[w]))>800:g.append(cur);cur=[]
        cur.append(k)
    g.append(cur);ch=[c for c in g if idx in c][0]
    line=' '.join(ws[k] for k in ch);tw=F(44).getlength(line)
    d.rounded_rectangle((W//2-tw/2-40,1555,W//2+tw/2+40,1655),50,fill=(14,21,48),outline=(45,65,105),width=2)
    x=W//2-tw/2
    for k in ch:
        d.text((x,1605),ws[k],font=F(44),fill=GREEN if k==idx else WHITE,anchor='lm');x+=F(44).getlength(ws[k]+' ')
TAGS=['EL PROBLEMA','DEFINICIÓN','COMPARACIÓN','CONEXIÓN','TU SERVER','ABYB HOST','EMPEZÁ HOY']
def chrome(d,i,gt):
    TX(d,80,70,'QUÉ ES UN HOST',28,GRAY);TX(d,1000,70,'%02d / %02d'%(i+1,N),28,GRAY,anchor='ra');d.line((80,125,1000,125),fill=(35,50,90),width=2)
    pill(d,80,160,TAGS[i],30,GREEN,(14,50,45),(40,120,90),pad=24)
    d.line((80,1760,1000,1760),fill=(35,50,90),width=4);d.line((80,1760,80+int(920*gt/T),1760),fill=GREEN,width=4)
    TX(d,80,1805,'HOST / SERVER / ONLINE',26,GRAY);TX(d,1000,1805,'GUÍA VISUAL',26,GRAY,anchor='ra')
def frame(i,t,gt):
    im=BASE.copy();d=ImageDraw.Draw(im,'RGBA');o=int(gt*10)%90
    for x in range(-90,W+90,90):d.line((x+o,0,x+o,H),fill=(255,255,255,8),width=2)
    for y in range(-90,H+90,90):d.line((0,y+o,W,y+o),fill=(255,255,255,8),width=2)
    d=ImageDraw.Draw(im);chrome(d,i,gt)
    if i==0:
        title(d,[('¿QUERÉS TU',WHITE),('PROPIO SERVER?',GREEN)],t,96)
        e=E(t,0.5,0.6);gamer(d,330,1250,t,e);monitor(d,560,880,360,230,t,e)
        for k,(s_,t0,y0) in enumerate([('¿Jugamos?',1.6,690),('¿Hay server?',2.6,790)]):
            ee=EB(t,t0,0.35)
            if ee>0.05:
                w_=int(F(40).getlength(s_))+60;x0=980-w_;d.rounded_rectangle((x0,y0,980,y0+80),40,fill=M((55,95,190),min(1,ee)),outline=M(OL,1),width=2);d.text((x0+30,y0+40),s_,font=F(40),fill=M(WHITE,min(1,ee)),anchor='lm')
        pill(d,540,1480,'AMIGOS LISTOS · FALTA EL SERVER',30,WHITE,(18,28,60),OL,E(t,1.2),c=True)
    elif i==1:
        title(d,[('HOST =',WHITE),('UNA COMPUTADORA',GREEN),('SIEMPRE ONLINE',GREEN)],t,84)
        for r_,ph in [(40,0),(85,0.5),(130,1.0)]:
            a=0.25+0.75*max(0,math.sin(t*4-ph*3))*E(t,0.8);d.arc((540-r_,840-r_,540+r_,840+r_),225,315,fill=M(GREEN,a),width=12)
        d.ellipse((530,850,550,870),fill=M(GREEN,E(t,0.8)))
        e=E(t,0.6,0.6);rack(d,540,930+int(40*(1-e)),440,4,t,e)
        for k,s_ in enumerate(['POTENTE','24/7','INTERNET']):pill(d,[250,540,830][k],1400,s_,30,WHITE,(18,28,60),OL,E(t,1.6+k*0.3),c=True)
        pill(d,540,1490,'EJEMPLO ILUSTRATIVO',26,GRAY,(14,21,48),(45,65,105),E(t,2.0),c=True)
    elif i==2:
        title(d,[('TU PC',WHITE),('VS HOST',GREEN)],t,104)
        for side in (0,1):
            x0=80+side*480;a=E(t,0.5+side*0.5);box=(x0,640,x0+440,1380);card(d,box,a)
            pill(d,x0+220,680,['TU PC','HOST'][side],34,WHITE,(14,21,48),OL,a,c=True)
            if side==0:monitor(d,x0+130,800,180,120,t,a)
            else:rack(d,x0+220,790,180,2,t,a)
            col=SAL if side==0 else GREEN
            TX(d,x0+220,1010,['SE APAGA','ONLINE 24/7'][side],40,col,a,'ma')
            for k in range(14):
                on=(k%4==0) if side==0 else True
                d.rounded_rectangle((x0+36+k*27,1090,x0+36+k*27+19,1150),5,fill=M(col if on else (40,55,95),a))
            TX(d,x0+220,1190,['A VECES','SIEMPRE'][side],34,GRAY,a,'ma')
            TX(d,x0+220,1270,['PUEDE LAGEAR','SIN LAG'][side],36,col,E(t,1.8+side*0.5),'ma')
        pill(d,540,1450,'EJEMPLO ILUSTRATIVO',26,GRAY,(14,21,48),(45,65,105),E(t,2.2),c=True)
    elif i==3:
        title(d,[('TODOS JUEGAN',WHITE),('EN EL MISMO',GREEN),('SERVER',GREEN)],t,92)
        hc=(540,1080);pl=[(200,820),(880,820),(200,1320),(880,1320)];cols=[(55,95,190),(200,90,120),(230,150,60),(90,180,120)]
        for k,(px,py) in enumerate(pl):
            a=E(t,0.5+k*0.25)
            d.line((px,py+30,hc[0],hc[1]),fill=M((60,95,140),a),width=4)
            p=((t*0.7+k*0.25)%1)*E(t,1.6);qx=px+(hc[0]-px)*p;qy=py+30+(hc[1]-py-30)*p
            if E(t,1.6)>0:d.ellipse((qx-12,qy-12,qx+12,qy+12),fill=M(GREEN))
            avatar(d,px,py,cols[k],a);TX(d,px,py+110,'JUGADOR %d'%(k+1),26,GRAY,a,'ma')
        e=E(t,0.4,0.5);rack(d,hc[0],hc[1]-90,220,2,t,e)
        pill(d,540,1480,'EJEMPLO · CONEXIÓN AL HOST',26,GRAY,(14,21,48),(45,65,105),E(t,2.0),c=True)
    elif i==4:
        title(d,[('VOS ELEGÍS,',WHITE),('NOSOTROS',GREEN),('LO ACTIVAMOS',GREEN)],t,92)
        for k,(s_,t0) in enumerate([('ELEGÍS EL JUEGO',0.8),('PAGÁS POR SEMANA O MES',1.9),('ACTIVAMOS EN MINUTOS',3.0)]):
            e=E(t,t0,0.45);y=700+k*210;ox=int((1-e)*500)
            card(d,(80+ox,y,1000+ox,y+170),e)
            d.ellipse((120+ox,y+41,208+ox,y+129),fill=M(GREEN,e));TX(d,164+ox,y+85,str(k+1),50,BG0,e,'mm')
            TX(d,240+ox,y+85,s_,40,WHITE,e,'lm')
            if t>t0+0.6:ck(d,940+ox,y+85,34,EB(t,t0+0.6,0.3))
    elif i==5:
        title(d,[('EN ABYB HOST',WHITE),('TENÉS TODO ESTO:',GREEN)],t,84)
        items=[((80,680,520,900),'24/7','ONLINE',0.7),((560,680,1000,900),'SIN LAG','',1.3),((80,940,1000,1160),'SOPORTE','POR WHATSAPP Y DISCORD',1.9),((80,1200,1000,1420),'PAGÁS','SEMANAL O MENSUAL',2.5)]
        for (bx,t0) in [(b[0],b[3]) for b in items]:pass
        for box,big,small,t0 in items:
            e=E(t,t0,0.45);oy=int((1-e)*40);b=(box[0],box[1]+oy,box[2],box[3]+oy);card(d,b,e)
            cx=(b[0]+b[2])//2 if small=='' or box[2]-box[0]<500 else b[0]+60
            if box[2]-box[0]<500:
                TX(d,cx,b[1]+110,big,80 if big=='24/7' else 64,GREEN,e,'mm');TX(d,cx,b[1]+175,small,34,GRAY,e,'mm') if small else None
            else:
                TX(d,b[0]+50,b[1]+80,big,64,GREEN,e,'lm');TX(d,b[0]+50,b[1]+155,small,38,WHITE,e,'lm')
            if t>t0+0.4:ck(d,b[2]-50,b[1]+50,28,EB(t,t0+0.4,0.3))
    else:
        title(d,[('ARGENTINO,',WHITE),('BUENO Y',WHITE),('BARATO.',GREEN)],t,100)
        e=E(t,0.9,0.5);card(d,(80,700,1000,960),e)
        TX(d,130,745,'DESDE',38,GRAY,e);TX(d,125,775,'$600',150,GREEN,e);TX(d,640,800,'POR SEMANA',40,WHITE,e);TX(d,640,860,'O POR MES',40,WHITE,e)
        e2=E(t,1.6,0.45);p=1+0.025*math.sin(t*7)
        bx=int(460*p);d.rounded_rectangle((540-bx,1030,540+bx,1190),80,fill=M(GREEN,e2))
        TX(d,540,1110,'abybhost.online',64,BG0,e2,'mm')
    sub(d,i,t)
    return im
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i','a.wav','-c:v','libx264','-pix_fmt','yuv420p','-preset','fast','-crf','21','-c:a','aac','-b:a','160k','-shortest',sys.argv[1] if len(sys.argv)>1 else 'out.mp4'],stdin=subprocess.PIPE)
only=int(sys.argv[2]) if len(sys.argv)>2 else None
for i in range(N):
    for f in range(int(sd[i]*FPS)):
        p.stdin.write(frame(i,f/FPS,st[i]+f/FPS).tobytes())
p.stdin.close();p.wait();print(T)
