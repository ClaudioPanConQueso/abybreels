import re
base=open('host.py').read()
iS=base.index("S=[(");iN=base.index("N=len(S)")
iF=base.index("def frame(i,t,gt):");iSub=base.index("    sub(d,i,t)\n    return im")
head=base[:iS];mid=base[iN:iF];tail=base[iSub:]
frame_head=base[iF:base.index("    if i==0:",iF)]
EXTRA='''
def link(d,x1,y1,x2,y2,t,sp,col,a=1):
    d.line((x1,y1,x2,y2),fill=M((60,95,140),a),width=4)
    p=(t*sp)%2;p=p if p<1 else 2-p;qx=x1+(x2-x1)*p;qy=y1+(y2-y1)*p
    d.ellipse((qx-12,qy-12,qx+12,qy+12),fill=M(col,a))
def bar(d,x,y,w,h,fr,col,a=1):
    d.rounded_rectangle((x,y,x+w,y+h),h//2,fill=M((40,55,95),a))
    if fr>0.01:d.rounded_rectangle((x,y,x+max(h,int(w*fr)),y+h),h//2,fill=M(col,a))
def vbar(d,cx,y0,y1,w,fr,col,a=1):
    d.rounded_rectangle((cx-w//2,y0,cx+w//2,y1),24,fill=M((40,55,95),a))
    if fr>0.01:d.rounded_rectangle((cx-w//2,y1-max(30,int((y1-y0)*fr)),cx+w//2,y1),24,fill=M(col,a))
def stopwatch(d,cx,cy,r,t,a=1):
    d.rectangle((cx-22,cy-r-34,cx+22,cy-r),fill=M(OL,a));d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=M(CARD,a),outline=M(GREEN,a),width=10)
    for k in range(12):
        an=k*math.pi/6;d.line((cx+(r-30)*math.sin(an),cy-(r-30)*math.cos(an),cx+(r-14)*math.sin(an),cy-(r-14)*math.cos(an)),fill=M(GRAY,a),width=5)
    an=t*2.6;d.line((cx,cy,cx+int(r*.68*math.sin(an)),cy-int(r*.68*math.cos(an))),fill=M(WHITE,a),width=9);d.ellipse((cx-14,cy-14,cx+14,cy+14),fill=M(GREEN,a))
def plug(d,x,y,a=1,col=GREEN):
    d.rounded_rectangle((x,y+30,x+60,y+90),14,fill=M(col,a));d.rectangle((x+12,y,x+22,y+30),fill=M((200,210,230),a));d.rectangle((x+38,y,x+48,y+30),fill=M((200,210,230),a));d.line((x+30,y+90,x+30,y+125),fill=M(col,a),width=8)
def cross(d,cx,cy,r,a=1):
    r=int(r*a)
    if r<4:return
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=SAL);d.line((cx-r*.4,cy-r*.4,cx+r*.4,cy+r*.4),fill=BG0,width=max(3,int(r*.22)));d.line((cx-r*.4,cy+r*.4,cx+r*.4,cy-r*.4),fill=BG0,width=max(3,int(r*.22)))
def cal(d,y,cols,a=1):
    for k,c in enumerate(cols):
        x=66+k*138;d.rounded_rectangle((x,y,x+120,y+170),26,fill=M(c,a),outline=M(OL,a),width=3);d.text((x+60,y+85),'LMMJVSD'[k],font=F(56),fill=M(WHITE,a),anchor='mm')
def ram(d,cx,cy,t,a=1):
    d.rounded_rectangle((cx-230,cy-70,cx+230,cy+70),14,fill=M((30,100,80),a),outline=M(GREEN,a),width=3)
    for k in range(6):d.rounded_rectangle((cx-205+k*72,cy-42,cx-205+k*72+56,cy+18),8,fill=M((14,24,52),a),outline=M((70,170,120),a),width=2)
    for k in range(16):d.rectangle((cx-215+k*27,cy+70,cx-215+k*27+16,cy+92),fill=M((230,190,80),a))
def gscene(d,t,s_,bcol=SAL):
    e=E(t,0.5,0.6);gamer(d,330,1250,t,e);monitor(d,560,880,360,230,t,e);ee=EB(t,1.6,0.35)
    if ee>0.05:
        w_=int(F(40).getlength(s_))+60;x0=980-w_;d.rounded_rectangle((x0,690,980,770),40,fill=M(bcol,min(1,ee)),outline=M(OL),width=2);d.text((x0+30,730),s_,font=F(40),fill=M(WHITE,min(1,ee)),anchor='lm')
    pill(d,540,1480,'EJEMPLO ILUSTRATIVO',26,GRAY,(14,21,48),(45,65,105),E(t,1.2),c=True)
def ej(d,t,t0=1.5,y=1490):pill(d,540,y,'EJEMPLO ILUSTRATIVO',26,GRAY,(14,21,48),(45,65,105),E(t,t0),c=True)
def features(d,t,lines,items,size=88):
    title(d,lines,t,size);n0=250+len(lines)*int(size*1.18)+40
    for k,s_ in enumerate(items):
        t0=0.8+k*0.7;e=E(t,t0);y=n0+k*200;ox=int((1-e)*500);card(d,(80+ox,y,1000+ox,y+170),e)
        TX(d,130+ox,y+85,s_,44 if len(s_)<20 else 36,WHITE,e,'lm')
        if t>t0+0.5:ck(d,940+ox,y+85,34,EB(t,t0+0.5,0.3))
def cta(d,t):
    title(d,[('ARGENTINO,',WHITE),('BUENO Y',WHITE),('BARATO.',GREEN)],t,100)
    e=E(t,0.9,0.5);card(d,(80,700,1000,960),e)
    TX(d,130,745,'DESDE',38,GRAY,e);TX(d,125,775,'$600',150,GREEN,e);TX(d,640,800,'POR SEMANA',40,WHITE,e);TX(d,640,860,'O POR MES',40,WHITE,e)
    e2=E(t,1.6,0.45);p=1+0.025*math.sin(t*7);bx=int(460*p);d.rounded_rectangle((540-bx,1030,540+bx,1190),80,fill=M(GREEN,e2));TX(d,540,1110,'abybhost.online',64,BG0,e2,'mm')
def chip(d,cx,cy,s,t,a=1,label='CPU'):
    h=s//2
    for k in range(5):
        o=-h+24+k*(s-48)//4
        d.rectangle((cx+o-6,cy-h-28,cx+o+6,cy-h),fill=M(OL,a));d.rectangle((cx+o-6,cy+h,cx+o+6,cy+h+28),fill=M(OL,a));d.rectangle((cx-h-28,cy+o-6,cx-h,cy+o+6),fill=M(OL,a));d.rectangle((cx+h,cy+o-6,cx+h+28,cy+o+6),fill=M(OL,a))
    d.rounded_rectangle((cx-h,cy-h,cx+h,cy+h),24,fill=M((28,40,78),a),outline=M(GREEN,a),width=4)
    g=0.5+0.5*math.sin(t*3);d.rounded_rectangle((cx-h+24,cy-h+24,cx+h-24,cy+h-24),16,outline=M(GREEN,a*(0.35+0.65*g)),width=3)
    d.text((cx,cy),label,font=F(max(24,s//4)),fill=M(GREEN,a),anchor='mm')
def cta2(d,t):
    title(d,[('ARGENTINO,',WHITE),('BUENO Y',WHITE),('BARATO.',GREEN)],t,100)
    e=E(t,0.9,0.5);card(d,(80,700,1000,960),e)
    TX(d,130,745,'DESDE',38,GRAY,e);TX(d,125,775,'$600',150,GREEN,e);TX(d,640,800,'POR MES',44,WHITE,e);TX(d,640,865,'EN PESOS',36,GRAY,e)
    e2=E(t,1.6,0.45);p=1+0.025*math.sin(t*7);bx=int(460*p);d.rounded_rectangle((540-bx,1030,540+bx,1190),80,fill=M(GREEN,e2));TX(d,540,1110,'abybhost.online',64,BG0,e2,'mm')
def bubble(d,x,y,w,s_,right,col,a=1):
    x0=1000-w-20 if right else 80+20
    d.rounded_rectangle((x0,y,x0+w,y+90),45,fill=M(col,a));d.text((x0+w//2,y+45),s_,font=F(34),fill=M(WHITE,a),anchor='mm')
'''
CTA_S=("Argentino, bueno y barato. Desde 600 pesos. Entrá a abybhost.online","Argentino, bueno y barato. Desde seiscientos pesos. Entrá a a b y b host punto online.")
V={}
V['ping']=dict(h='QUÉ ES EL PING',f='PING / LATENCIA / LAG',tags=['EL PROBLEMA','DEFINICIÓN','MEDIDA','COMPARACIÓN','DISTANCIA','ABYB HOST','EMPEZÁ HOY'],
S=[("¿Tenés buen internet y igual hay lag? Puede ser el ping.",)*2,("El ping es el tiempo que tarda un mensaje en ir de tu PC al server, y volver.","El ping es el tiempo que tarda un mensaje en ir de tu Pe Ce al server, y volver."),
("Se mide en milisegundos. Menos milisegundos, respuesta más rápida.",)*2,("Con ping bajo, tus acciones se ven al instante. Con ping alto, tardan en llegar.",)*2,
("Y ojo: cuanto más cerca está el server, menos ping tenés.",)*2,("En AByB Host tu server está online 24/7 y sin lag.","En Abyb Host tu server está online veinticuatro siete y sin lag."),CTA_S],
SC='''    if i==0:
        title(d,[('¿BUEN INTERNET',WHITE),('Y IGUAL',GREEN),('HAY LAG?',GREEN)],t,88);gscene(d,t,'¡SE TILDÓ!')
    elif i==1:
        title(d,[('PING =',WHITE),('TIEMPO DE IDA',GREEN),('Y VUELTA',GREEN)],t,84)
        e=E(t,0.6,0.5);monitor(d,140,900,220,140,t,e);rack(d,820,880,240,3,t,e)
        TX(d,250,1150,'JUGADOR',30,GRAY,e,'ma');TX(d,820,1200,'SERVER',30,GRAY,e,'ma')
        if t>1.2:link(d,390,980,700,980,t-1.2,1.4,GREEN,E(t,1.2));TX(d,545,925,'IDA',28,GRAY,E(t,1.2),'ma');TX(d,545,1010,'VUELTA',28,GRAY,E(t,1.2),'ma')
        ej(d,t)
    elif i==2:
        title(d,[('SE MIDE EN',WHITE),('MILISEGUNDOS',GREEN)],t,96)
        e=E(t,0.6,0.5);stopwatch(d,540,1020,190,t,e);TX(d,540,1130,'ms',60,GREEN,e,'mm')
        e2=E(t,1.6);card(d,(160,1290,920,1410),e2);TX(d,540,1350,'1 SEGUNDO = 1000 ms',44,WHITE,e2,'mm')
    elif i==3:
        title(d,[('PING BAJO',WHITE),('VS PING ALTO',GREEN)],t,96)
        for k,(ms,lab,col,sp) in enumerate([('30 ms','RESPUESTA RÁPIDA',GREEN,1.8),('300 ms','RESPUESTA LENTA',SAL,0.35)]):
            e=E(t,0.5+k*0.7);y=640+k*320;card(d,(80,y,1000,y+280),e)
            monitor(d,120,y+40,150,100,t,e);rack(d,885,y+40,120,2,t,e)
            if e>0.9:link(d,300,y+110,820,y+110,t,sp,col,1)
            TX(d,560,y+50,ms,46,col,e,'ma');TX(d,560,y+215,lab,34,col,e,'ma')
        ej(d,t,2.0)
    elif i==4:
        title(d,[('MÁS CERCA,',WHITE),('MENOS PING',GREEN)],t,100)
        e=E(t,0.5);avatar(d,190,1090,BLUE,e);TX(d,190,1200,'VOS',28,GRAY,e,'ma')
        e1=E(t,1.0);rack(d,620,840,140,1,t,e1);TX(d,620,945,'CERCA · 30 ms',28,GREEN,e1,'ma')
        if e1>0.5:link(d,260,1090,550,882,t,1.8,GREEN,e1)
        e2=E(t,2.0);rack(d,890,1230,140,1,t,e2);TX(d,890,1335,'LEJOS · 300 ms',28,SAL,e2,'ma')
        if e2>0.5:link(d,260,1110,820,1272,t,0.5,SAL,e2)
        ej(d,t,2.4)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('TU SERVER VA',GREEN),('SIN LAG',GREEN)],['SERVER ONLINE 24/7','SIN LAG','SOPORTE POR WHATSAPP Y DISCORD'])
    else:
        cta(d,t)
''')
V['ram']=dict(h='QUÉ ES LA RAM',f='RAM / MEMORIA / SERVER',tags=['EL PROBLEMA','DEFINICIÓN','CONSUMO','COMPARACIÓN','REGLA','ABYB HOST','EMPEZÁ HOY'],
S=[("¿Tu server se traba cuando entran muchos jugadores? Puede faltar RAM.",)*2,("La RAM es la memoria de trabajo del server: guarda lo que usa en el momento.",)*2,
("Cada jugador, cada mapa y cada plugin consumen un poco de RAM.",)*2,("Con poca RAM se llena rápido y el server se pone lento. Con más RAM, todo fluye.",)*2,
("Cuantos más jugadores y plugins, más RAM necesitás.",)*2,("En AByB Host elegís tu plan según tu juego, y si tenés dudas te ayudamos por WhatsApp o Discord.","En Abyb Host elegís tu plan según tu juego, y si tenés dudas te ayudamos por Guasap o Discord."),CTA_S],
SC='''    if i==0:
        title(d,[('¿SE TRABA',WHITE),('CUANDO ENTRAN',GREEN),('MUCHOS?',GREEN)],t,88)
        e=E(t,0.5,0.6);rack(d,540,860,440,4,t,e)
        for k in range(6):
            ee=E(t,1.0+k*0.25);avatar(d,160+k*152,1390,[BLUE,(200,90,120),(230,150,60),(90,180,120),BLUE,(200,90,120)][k],ee,0.7)
        ee=EB(t,2.4,0.35)
        if ee>0.05:d.rounded_rectangle((640,720,980,800),40,fill=M(SAL,min(1,ee)));d.text((810,760),'LAG...',font=F(40),fill=M(WHITE,min(1,ee)),anchor='mm')
    elif i==1:
        title(d,[('RAM =',WHITE),('MEMORIA DE',GREEN),('TRABAJO',GREEN)],t,92)
        e=E(t,0.6,0.6);ram(d,540,930+int(40*(1-e)),t,e)
        pill(d,540,1130,'GUARDA LO QUE USA AHORA',30,WHITE,(18,28,60),OL,E(t,1.6),c=True);ej(d,t,2.0,1300)
    elif i==2:
        title(d,[('TODO USA RAM',WHITE),('EN EL SERVER',GREEN)],t,96)
        TX(d,100,740,'RAM DEL SERVER',30,GRAY,E(t,0.5));e=E(t,0.5);d.rounded_rectangle((100,800,980,900),24,fill=M((40,55,95),e),outline=M(OL,e),width=3)
        x=100;segs=[('JUGADORES',(55,95,190),0.3,0.9),('MAPA',(90,200,130),0.25,1.9),('PLUGINS',(240,180,70),0.2,2.9)]
        for k,(nm,c,fr,t0) in enumerate(segs):
            w_=int(880*fr*E(t,t0,0.7));d.rectangle((x,806,x+w_,894),fill=M(c));x+=int(880*fr)
            ee=E(t,t0);d.ellipse((130,985+k*95-14,158,985+k*95+14),fill=M(c,ee));TX(d,180,985+k*95,nm,40,WHITE,ee,'lm')
        ej(d,t,3.2)
    elif i==3:
        title(d,[('POCA RAM',WHITE),('VS MÁS RAM',GREEN)],t,96)
        for k,(gb,fr,col,l1,l2) in enumerate([('1 GB',0.97,SAL,'LLENA','SE TRABA'),('4 GB',0.3,GREEN,'CON ESPACIO','FLUYE')]):
            x0=80+k*480;e=E(t,0.5+k*0.6);card(d,(x0,640,x0+440,1330),e);pill(d,x0+220,680,gb,34,WHITE,(14,21,48),OL,e,c=True)
            vbar(d,x0+220,790,1130,130,fr*E(t,1.0+k*0.6,0.9),col,e);TX(d,x0+220,1180,l1,40,col,e,'ma');TX(d,x0+220,1250,l2,36,GRAY,E(t,2.0+k*0.5),'ma')
        ej(d,t,2.6,1450)
    elif i==4:
        title(d,[('MÁS JUGADORES',WHITE),('Y PLUGINS =',GREEN),('MÁS RAM',GREEN)],t,84)
        for k,(h,gb,lab) in enumerate([(160,'1 GB','POCOS'),(270,'2 GB','MÁS'),(380,'4 GB','MUCHOS')]):
            e=E(t,0.6+k*0.7,0.6);cx=200+k*340;top=1380-int(h*e)
            d.rounded_rectangle((cx-110,top,cx+110,1380),24,fill=M((60,170,110),e),outline=M(GREEN,e),width=3)
            TX(d,cx,1350,gb,50,BG0,e,'mb') if e>0.6 else None
            TX(d,cx,top-70,lab,36,WHITE,e,'ma');TX(d,cx,top-28,'JUGADORES',24,GRAY,e,'ma')
        ej(d,t,2.8)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('ELEGÍS TU PLAN',GREEN)],['ELEGÍS TU JUEGO','PAGÁS SEMANAL O MENSUAL','SOPORTE POR WHATSAPP Y DISCORD'])
    else:
        cta(d,t)
''')
V['mods']=dict(h='MODS VS PLUGINS',f='MODS / PLUGINS / MINECRAFT',tags=['MINECRAFT','PLUGINS','EJEMPLOS','MODS','DIFERENCIA','ABYB HOST','EMPEZÁ HOY'],
S=[("¿Mods o plugins? En Minecraft no son lo mismo.",)*2,("Los plugins se instalan solo en el server. Los jugadores entran con el juego normal.",)*2,
("Sirven para agregar reglas y funciones: tiendas, protección, rangos o minijuegos.",)*2,("Los mods, en cambio, cambian el juego en sí: agregan bloques, objetos y criaturas nuevas.",)*2,
("Y los jugadores normalmente tienen que instalar los mismos mods para entrar.",)*2,("En AByB Host tenés servers de Minecraft online 24/7, sin lag, y con soporte por WhatsApp y Discord.","En Abyb Host tenés servers de Minecraft online veinticuatro siete, sin lag, y con soporte por Guasap y Discord."),CTA_S],
SC='''    if i==0:
        title(d,[('¿MODS O',WHITE),('PLUGINS?',GREEN)],t,120)
        for k,(nm,x0) in enumerate([('MODS',80),('PLUGINS',560)]):
            e=E(t,0.5+k*0.5);card(d,(x0,680,x0+440,1140),e);TX(d,x0+220,1070,nm,48,WHITE,e,'ma')
            if k==0:
                for r_ in range(3):
                    for c_ in range(3):d.rounded_rectangle((x0+100+c_*84,760+r_*84,x0+100+c_*84+72,760+r_*84+72),10,fill=M((90,200,130) if (r_+c_)!=2 else (150,90,220),e))
            else:plug(d,x0+160,780,e);d.rounded_rectangle((x0+110,900,x0+330,960),14,fill=M((28,40,78),e),outline=M(OL,e),width=3)
        pill(d,540,1250,'NO SON LO MISMO',38,WHITE,(18,28,60),OL,E(t,1.8),c=True)
    elif i==1:
        title(d,[('PLUGINS',WHITE),('VIVEN EN',GREEN),('EL SERVER',GREEN)],t,96)
        e=E(t,0.5,0.6);rack(d,330,880,300,3,t,e)
        for k in range(3):plug(d,505,900+k*100-30,E(t,1.2+k*0.3)*e,GREEN)
        e2=E(t,1.8);avatar(d,860,1000,BLUE,e2);TX(d,860,1115,'JUGADOR',28,GRAY,e2,'ma')
        if e2>0.5:link(d,560,1010,780,1010,t,1.2,GREEN,e2)
        pill(d,540,1300,'JUGADORES: SIN INSTALAR NADA',32,GREEN,(14,50,45),(40,120,90),E(t,2.4),c=True);ej(d,t,2.8)
    elif i==2:
        title(d,[('PLUGINS',WHITE),('AGREGAN',GREEN),('FUNCIONES',GREEN)],t,96)
        for k,(s_,t0) in enumerate([('TIENDA',0.8),('PROTECCIÓN',1.6),('RANGOS',2.4),('MINIJUEGOS',3.2)]):
            e=E(t,t0);x0=80+(k%2)*480;y0=700+(k//2)*210;oy=int((1-e)*40);card(d,(x0,y0+oy,x0+440,y0+170+oy),e)
            d.ellipse((x0+30,y0+oy+45,x0+110,y0+oy+125),fill=M(GREEN,e));TX(d,x0+70,y0+oy+85,s_[0],44,BG0,e,'mm');TX(d,x0+135,y0+oy+85,s_,34,WHITE,e,'lm')
        ej(d,t,3.6,1190)
    elif i==3:
        title(d,[('MODS',WHITE),('CAMBIAN EL',GREEN),('JUEGO',GREEN)],t,96)
        for r_ in range(3):
            for c_ in range(6):
                x=150+c_*130;y=780+r_*130;sp={(1,0):(150,90,220),(4,1):(240,170,60),(2,2):(230,100,120)}.get((c_,r_))
                if sp:
                    t0={(1,0):1.0,(4,1):2.0,(2,2):3.0}[(c_,r_)];s=EB(t,t0,0.4);ww=int(118*max(0,min(1.15,s)))
                    if ww>4:d.rounded_rectangle((x+59-ww//2,y+59-ww//2,x+59+ww//2,y+59+ww//2),14,fill=M(sp),outline=M(WHITE),width=3)
                else:
                    d.rounded_rectangle((x,y,x+118,y+118),14,fill=M((60,150,100),E(t,0.4+0.03*(r_*6+c_))));d.rectangle((x+8,y+8,x+110,y+30),fill=M((100,190,140),E(t,0.4+0.03*(r_*6+c_))))
        for k,(s_,t0) in enumerate([('BLOQUES NUEVOS',1.2),('OBJETOS NUEVOS',2.2),('CRIATURAS NUEVAS',3.2)]):pill(d,540,1250+k*90,s_,32,WHITE,(18,28,60),OL,E(t,t0),c=True)
    elif i==4:
        title(d,[('PLUGINS',WHITE),('VS MODS',GREEN)],t,104)
        rows=[('DÓNDE SE INSTALAN',['SOLO EN EL SERVER','SERVER Y JUGADORES']),('LOS JUGADORES',['NO INSTALAN NADA','INSTALAN LOS MISMOS']),('QUÉ CAMBIAN',['REGLAS Y FUNCIONES','EL JUEGO EN SÍ'])]
        for k in range(2):
            x0=80+k*480;e=E(t,0.5+k*0.5);card(d,(x0,640,x0+440,1380),e);pill(d,x0+220,680,['PLUGINS','MODS'][k],34,WHITE,(14,21,48),OL,e,c=True)
            for j,(lab,vals) in enumerate(rows):
                ee=E(t,1.2+j*0.6+k*0.3);y=820+j*180;TX(d,x0+220,y,lab,26,GRAY,ee,'ma');TX(d,x0+220,y+55,vals[k],32,GREEN if (k==0 or j!=1) else SAL if False else GREEN,ee,'ma')
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('TU SERVER DE',GREEN),('MINECRAFT',GREEN)],['SERVER ONLINE 24/7','SIN LAG','SOPORTE POR WHATSAPP Y DISCORD'])
    else:
        cta(d,t)
''')
V['comunidad']=dict(h='COMUNIDAD',f='EMPEZAR / CRECER / SERVER',tags=['EL INICIO','EMPEZÁ CHICO','SIN ATADURAS','CRECIMIENTO','EXIGENCIA','ABYB HOST','EMPEZÁ HOY'],
S=[("Toda gran comunidad empieza con tres amigos y un server.",)*2,("Al principio no necesitás algo enorme. Podés probar una semana.",)*2,
("Si les gusta, siguen. Si no, paran, sin deudas.",)*2,("Con el tiempo, la comunidad crece.",)*2,
("Y cuando hay más jugadores, esperan un server siempre online y sin lag.",)*2,("En AByB Host empezás desde 600 pesos, por semana o por mes.","En Abyb Host empezás desde seiscientos pesos, por semana o por mes."),CTA_S],
SC='''    if i==0:
        title(d,[('TODO EMPIEZA',WHITE),('CON 3 AMIGOS',GREEN)],t,96)
        e=E(t,0.5,0.6);rack(d,540,880,260,2,t,e)
        for k,(px,py,c) in enumerate([(240,1090,BLUE),(840,1090,(200,90,120)),(540,1330,(230,150,60))]):
            ee=E(t,1.0+k*0.4);link(d,px,py+20,540,1010,t+k*0.3,1.2,GREEN,ee) if ee>0.5 else None;avatar(d,px,py,c,ee)
        ej(d,t,2.4)
    elif i==1:
        title(d,[('EMPEZÁ',WHITE),('CHICO',GREEN)],t,130)
        cal(d,760,[(60,200,90) if t>0.7+k*0.2 else (80,80,100) for k in range(7)])
        pill(d,540,1000,'PAGÁS POR SEMANA',44,BG0,GREEN,GREEN,E(t,2.2),c=True);pill(d,540,1130,'SIN DEUDAS',36,GREEN,(14,50,45),(40,120,90),E(t,2.8),c=True)
    elif i==2:
        title(d,[('SIN',WHITE),('ATADURAS',GREEN)],t,130)
        for k,(q,a_) in enumerate([('¿LES GUSTA?','SEGUÍS'),('¿NO?','PARÁS, SIN DEUDAS')]):
            e=E(t,0.8+k*1.1);y=700+k*230;ox=int((1-e)*500);card(d,(80+ox,y,1000+ox,y+190),e);TX(d,130+ox,y+95,q,44,WHITE,e,'lm')
            pill(d,960-int(F(34).getlength(a_))-52+ox,y+48,a_,34,BG0,GREEN,GREEN,e)
        ej(d,t,3.0,1260)
    elif i==3:
        title(d,[('LA COMUNIDAD',WHITE),('CRECE',GREEN)],t,96)
        cnt=3 if t<2.0 else (10 if t<3.4 else 30);TX(d,540,690,str(cnt),130,GREEN,E(t,0.6),'mm');TX(d,540,790,'JUGADORES',34,GRAY,E(t,0.6),'mm')
        cols=[BLUE,(200,90,120),(230,150,60),(90,180,120)]
        for k in range(30):
            t0=0.7+k*0.0 if k<3 else (2.0+(k-3)*0.04 if k<10 else 3.4+(k-10)*0.04)
            e=EB(t,t0,0.3)
            if e>0.05:avatar(d,150+(k%10)*86,920+(k//10)*125,cols[k%4],min(1,e),0.45)
        ej(d,t,3.6,1330)
    elif i==4:
        title(d,[('MÁS JUGADORES,',WHITE),('MÁS EXIGENCIA',GREEN)],t,84)
        e=E(t,0.5,0.6);rack(d,540,720,440,3,t,e)
        for k,s_ in enumerate(['SERVER ONLINE 24/7','SIN LAG']):
            ee=E(t,1.4+k*0.8);pill(d,540,1130+k*130,s_,44,WHITE,(18,28,60),OL,ee,c=True,pad=50);ck(d,150,1130+k*130+42,34,ee) if False else None
        ej(d,t,2.8,1450)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('EMPEZÁS',GREEN),('DESDE $600',GREEN)],['PAGÁS POR SEMANA O POR MES','SIN DEUDAS','ACTIVACIÓN EN MINUTOS'])
    else:
        cta(d,t)
''')

V['cpu']=dict(h='CPU COMPARTIDA',f='CPU / COMPARTIDA / DEDICADA',tags=['PREGUNTA','DEFINICIÓN','COMPARTIDA','DEDICADA','COMPARACIÓN','ANTES DE PAGAR','ABYB HOST'],
S=[("¿Por qué hay planes con CPU compartida? Te lo explico.",)*2,("La CPU es el cerebro del server: hace los cálculos del juego o del bot.","La Ce Pe U es el cerebro del server: hace los cálculos del juego o del bot."),
("En una CPU compartida, varios servicios usan el mismo procesador.","En una Ce Pe U compartida, varios servicios usan el mismo procesador."),("En una dedicada, el procesador es solo para vos, pero cuesta bastante más.",)*2,
("Compartida permite precios más bajos, y la mayoría de estos juegos y bots consumen poco.",)*2,("Eso sí: revisá los límites del plan, y si usás muchos plugins, consultanos.",)*2,(("Argentino, Bueno y Barato. Desde 600 pesos por mes. Mirá todo en abybhost.online","Argentino, Bueno y Barato. Desde seiscientos pesos por mes. Mirá todo en a b y b host punto online."))],
SC='''    if i==0:
        title(d,[('¿QUÉ ES LA',WHITE),('CPU COMPARTIDA?',GREEN)],t,88);e=E(t,0.5,0.6);chip(d,540,1050,300,t,e);ej(d,t,2.0)
    elif i==1:
        title(d,[('CPU =',WHITE),('EL CEREBRO',GREEN),('DEL SERVER',GREEN)],t,92);e=E(t,0.5,0.6);chip(d,540,1030,260,t,e)
        pill(d,540,1280,'HACE LOS CÁLCULOS',34,WHITE,(18,28,60),OL,E(t,1.6),c=True)
    elif i==2:
        title(d,[('CPU',WHITE),('COMPARTIDA',GREEN)],t,110);e=E(t,0.5,0.6);chip(d,540,1010,200,t,e)
        for k,(px,py,s_) in enumerate([(190,820,'SERVER 1'),(890,820,'SERVER 2'),(190,1230,'BOT'),(890,1230,'SERVER 3')]):
            ee=E(t,1.0+k*0.4)
            if ee>0.5:link(d,px,py,540,1010,t+k*0.3,0.9,GREEN,ee)
            pill(d,px,py-36,s_,30,WHITE,(18,28,60),OL,ee,c=True)
        ej(d,t,2.8,1420)
    elif i==3:
        title(d,[('CPU',WHITE),('DEDICADA',GREEN)],t,110);e=E(t,0.5,0.6);chip(d,540,900,200,t,e)
        e2=E(t,1.2);avatar(d,540,1200,BLUE,e2);pill(d,540,1330,'SOLO PARA VOS',34,GREEN,(14,50,45),(40,120,90),E(t,1.8),c=True);pill(d,540,1430,'COSTO MÁS ALTO',34,SAL,(40,22,28),SAL,E(t,2.4),c=True)
    elif i==4:
        title(d,[('COMPARTIDA',WHITE),('VS DEDICADA',GREEN)],t,96)
        rows=[('PRECIO',['MÁS BAJO','MÁS ALTO']),('PROCESADOR',['SE COMPARTE','SOLO PARA VOS']),('ALCANZA PARA',['JUEGOS Y BOTS LIVIANOS','USOS EXIGENTES'])]
        for k in range(2):
            x0=80+k*480;e=E(t,0.5+k*0.5);card(d,(x0,640,x0+440,1380),e);pill(d,x0+220,680,['COMPARTIDA','DEDICADA'][k],30,WHITE,(14,21,48),OL,e,c=True)
            for j,(lab,vals) in enumerate(rows):
                ee=E(t,1.2+j*0.6+k*0.3);y=820+j*180;TX(d,x0+220,y,lab,26,GRAY,ee,'ma');TX(d,x0+220,y+55,vals[k],28,(GREEN if (k==0 or j==1) else SAL) if j==0 else GREEN,ee,'ma')
    elif i==5:
        features(d,t,[('ANTES DE',WHITE),('CONTRATAR',GREEN)],['REVISÁ LOS LÍMITES DEL PLAN','MUCHOS PLUGINS? CONSULTANOS','TE AYUDAMOS A ELEGIR'],104)
    else:
        cta2(d,t)
''')
V['checklist']=dict(h='ANTES DE CONTRATAR',f='PREGUNTÁ / CONFIRMÁ / ELEGÍ',tags=['CHECKLIST','PREGUNTA 1','PREGUNTA 2','PREGUNTA 3','POR ESCRITO','ABYB HOST','EMPEZÁ HOY'],
S=[("Antes de pagar un hosting, hacé estas preguntas.",)*2,("Uno: ¿cuánta RAM, CPU y slots incluye el plan?","Uno: ¿cuánta RAM, Ce Pe U y slots incluye el plan?"),
("Dos: ¿la CPU es compartida o dedicada, y cuáles son los límites reales?","Dos: ¿la Ce Pe U es compartida o dedicada, y cuáles son los límites reales?"),("Tres: ¿cuál es el precio total, la moneda y el plazo de activación?",)*2,
("Y pedí todo por escrito antes de pagar.",)*2,("En AByB Host te respondemos por WhatsApp o Discord, y te ayudamos a elegir.","En Abyb Host te respondemos por Guasap o Discord, y te ayudamos a elegir."),(("Argentino, Bueno y Barato. Desde 600 pesos por mes. Mirá todo en abybhost.online","Argentino, Bueno y Barato. Desde seiscientos pesos por mes. Mirá todo en a b y b host punto online."))],
SC='''    if i==0:
        title(d,[('ANTES DE',WHITE),('PAGAR UN',GREEN),('HOSTING',GREEN)],t,92)
        e=E(t,0.5,0.6);d.rounded_rectangle((340,820,740,1330),30,fill=M(CARD,e),outline=M(OL,e),width=3);d.rounded_rectangle((440,790,640,850),16,fill=M(OL,e))
        for k in range(3):
            ee=E(t,1.0+k*0.6);y=950+k*120;ck(d,410,y,34,ee);bar(d,470,y-14,230,28,1,(70,95,150),ee)
    elif i==1:
        title(d,[('1.',WHITE),('RECURSOS',GREEN)],t,120)
        for k,s_ in enumerate(['RAM','CPU','SLOTS']):
            t0=0.8+k*0.7;e=E(t,t0);y=700+k*200;ox=int((1-e)*500);card(d,(80+ox,y,1000+ox,y+170),e);TX(d,130+ox,y+85,s_,56,GREEN,e,'lm');TX(d,420+ox,y+85,'¿CUÁNTA INCLUYE?',38,WHITE,e,'lm')
    elif i==2:
        title(d,[('2.',WHITE),('LÍMITES DE CPU',GREEN)],t,92);e=E(t,0.5,0.6);chip(d,540,930,220,t,e)
        pill(d,540,1160,'¿COMPARTIDA O DEDICADA?',34,WHITE,(18,28,60),OL,E(t,1.4),c=True);pill(d,540,1280,'¿QUÉ LÍMITES REALES TIENE?',34,GREEN,(14,50,45),(40,120,90),E(t,2.2),c=True)
    elif i==3:
        features(d,t,[('3.',WHITE),('PRECIO, MONEDA',GREEN),('Y PLAZO',GREEN)],['PRECIO TOTAL','MONEDA DE PAGO','PLAZO DE ACTIVACIÓN'])
    elif i==4:
        title(d,[('TODO',WHITE),('POR ESCRITO',GREEN)],t,104)
        pill(d,540,540,'EJEMPLO',30,BG0,GREEN,GREEN,E(t,0.3),c=True);e=E(t,0.4);d.rounded_rectangle((60,650,1020,1250),40,fill=M((49,51,56),e),outline=M(OL,e),width=3)
        for k,(s_,right,w_) in enumerate([('Hola, ¿qué incluye el plan?',True,620),('Te paso los detalles del plan',False,620),('Perfecto, confirmo por acá',True,560)]):
            ee=E(t,0.9+k*1.0);bubble(d,0,700+k*160+int((1-ee)*30),w_,s_,right,BLUE if right else (70,80,110),ee)
        pill(d,540,1330,'CONFIRMÁ ANTES DE PAGAR',34,GREEN,(14,50,45),(40,120,90),E(t,3.8),c=True)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('PREGUNTÁ',GREEN),('SIN PROBLEMA',GREEN)],['CONSULTÁS POR WHATSAPP O DISCORD','TE AYUDAMOS A ELEGIR','CONDICIONES CLARAS EN LA WEB'])
    else:
        cta2(d,t)
''')
for k,v in V.items():
    s=head+"S="+repr(v['S'])+"\n"+mid
    s=s.replace("'QUÉ ES UN HOST'",repr(v['h'])).replace("'HOST / SERVER / ONLINE'",repr(v['f']))
    s=re.sub(r"TAGS=\[.*?\]\n","TAGS="+repr(v['tags'])+"\n",s,count=1,flags=re.S)
    s+=EXTRA+'\n'+frame_head
    s+=v['SC']+tail
    open(f'v_{k}.py','w').write(s)
print('ok')
