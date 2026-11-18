import re
exec(open('build.py').read().split("V={}")[0])
EXTRA2=r"""
def stat(d,t,lines,small,big,tail,pills,size=100):
    title(d,lines,t,size);e=E(t,0.8,0.5);card(d,(80,640,1000,940),e)
    TX(d,130,685,small,38,GRAY,e);TX(d,125,725,big,150,GREEN,e);TX(d,640,760,tail[0],44,WHITE,e);TX(d,640,825,tail[1],32,GRAY,e)
    for k,s_ in enumerate(pills):pill(d,540,1040+k*110,s_,38,WHITE,(18,28,60),OL,E(t,1.6+k*0.6),c=True)
def cmp(d,t,lines,hdrs,rows,cols,size=96,note=None):
    title(d,lines,t,size)
    for k in range(2):
        x0=80+k*480;e=E(t,0.5+k*0.5);card(d,(x0,640,x0+440,1380),e);pill(d,x0+220,680,hdrs[k],30,WHITE,(14,21,48),OL,e,c=True)
        for j,(lab,vals) in enumerate(rows):
            ee=E(t,1.2+j*0.6+k*0.3);y=820+j*180;TX(d,x0+220,y,lab,26,GRAY,ee,'ma');TX(d,x0+220,y+55,vals[k],28,cols[k],ee,'ma')
    if note:pill(d,540,1430,note,26,GRAY,(14,21,48),(45,65,105),E(t,3.5),c=True)
def grid(d,t,lines,items,size=96):
    title(d,lines,t,size)
    for k,s_ in enumerate(items):
        e=E(t,0.8+k*0.5);x0=80+(k%2)*480;y0=700+(k//2)*210;oy=int((1-e)*40);card(d,(x0,y0+oy,x0+440,y0+170+oy),e)
        d.ellipse((x0+30,y0+oy+45,x0+110,y0+oy+125),fill=M(GREEN,e));TX(d,x0+70,y0+oy+85,s_[0],44,BG0,e,'mm');TX(d,x0+135,y0+oy+85,s_,32 if len(s_)<10 else 28,WHITE,e,'lm')
def chat(d,t,lines,msgs,size=104,note='EJEMPLO'):
    title(d,lines,t,size);yt=250+len(lines)*int(size*1.18)
    pill(d,540,yt+20,note,30,BG0,GREEN,GREEN,E(t,0.3),c=True);e=E(t,0.4)
    d.rounded_rectangle((60,yt+120,1020,yt+120+len(msgs)*170+80),40,fill=M((49,51,56),e),outline=M(OL,e),width=3)
    for k,(s_,right) in enumerate(msgs):
        ee=E(t,0.9+k*1.0);w_=int(F(34).getlength(s_))+60;bubble(d,0,yt+160+k*170+int((1-ee)*30),w_,s_,right,BLUE if right else (70,80,110),ee)
def panel(d,t,lines,size=104):
    title(d,lines,t,size);e=E(t,0.6,0.5);card(d,(80,640,1000,1280),e);d.rounded_rectangle((80,640,1000,720),30,fill=M((28,40,78),e))
    d.ellipse((120,668,148,696),fill=M(GREEN,e));TX(d,170,680,'EN LÍNEA',32,GREEN,e,'lm')
    for k,(s_,c) in enumerate([('INICIAR',GREEN),('REINICIAR',(240,190,80)),('DETENER',SAL)]):
        ee=E(t,1.2+k*0.4);x=210+k*330;d.rounded_rectangle((x-130,780,x+130,860),40,outline=M(c,ee),width=3,fill=M((14,24,52),ee));TX(d,x,820,s_,28,c,ee,'mm')
    for j,(lab,fr) in enumerate([('CPU',0.35),('RAM',0.5),('SLOTS',0.2)]):
        ee=E(t,2.0+j*0.4);y=930+j*90;TX(d,130,y,lab,30,GRAY,ee,'lm');bar(d,260,y-14,640,28,fr*E(t,2.2+j*0.4,0.8),GREEN,ee)
    ej(d,t,3.2,1330)
def botscene(d,t,lines,size=110):
    title(d,lines,t,size);e=E(t,0.6,0.5);cx,cy=540,980
    d.line((cx,cy-120,cx,cy-170),fill=M(GRAY,e),width=8);d.ellipse((cx-14,cy-196,cx+14,cy-168),fill=M(GREEN,e))
    d.rounded_rectangle((cx-110,cy-120,cx+110,cy+40),36,fill=M(BLUE,e),outline=M(OL,e),width=4)
    bl=int(t*2)%5==0
    for ex in(-45,45):d.ellipse((cx+ex-18,cy-60,cx+ex+18,cy-60+(6 if bl else 36)),fill=M(WHITE,e))
    d.rounded_rectangle((cx-70,cy+50,cx+70,cy+170),30,fill=M((40,70,150),e),outline=M(OL,e),width=4)
    pill(d,330,1230,'NODE.JS',36,WHITE,(18,28,60),OL,E(t,1.4),c=True);pill(d,750,1230,'PYTHON',36,WHITE,(18,28,60),OL,E(t,2.0),c=True)
def clip(d,t,e):
    d.rounded_rectangle((340,820,740,1330),30,fill=M(CARD,e),outline=M(OL,e),width=3);d.rounded_rectangle((440,790,640,850),16,fill=M(OL,e))
    for k in range(3):
        ee=E(t,1.0+k*0.6);y=950+k*120;ck(d,410,y,34,ee);bar(d,470,y-14,230,28,1,(70,95,150),ee)
def mate(d,cx,cy,t,e):
    r=int(150*e)
    if r<10:return
    d.line((cx+20,cy-r*0.5,cx+160*e,cy-r*1.9),fill=(200,200,210),width=16);d.ellipse((cx+140*e,cy-r*2.0,cx+180*e,cy-r*1.8),fill=(220,220,230))
    d.ellipse((cx-r,cy-r*0.9,cx+r,cy+r*1.2),fill=(70,160,80),outline=OL,width=6);d.ellipse((cx-r*0.6,cy-r*1.0,cx+r*0.6,cy-r*0.6),fill=(30,60,30),outline=OL,width=4)
    for k in range(3):d.line([(cx-70+k*70+12*math.sin(t*6+k+j*0.6),cy-r*1.2-j*28) for j in range(8)],fill=(255,255,255),width=8)
def cards3(d,t):
    for k,(n,c) in enumerate([('1',(40,90,200)),('7',(220,40,50)),('3',(40,160,70))]):
        e=EB(t,0.5+k*0.3,0.4);x=330+k*210;w=int(190*max(0,min(1.1,e)));h=int(290*max(0,min(1.1,e)))
        if w>6:
            d.rounded_rectangle((x-w//2,1000-h//2,x+w//2,1000+h//2),24,fill=WHITE,outline=OL,width=6)
            if e>0.7:d.text((x,1000),n,font=F(110),fill=c,anchor='mm')
def restart(d,cx,cy,r,t,a):
    s_=int(t*200)%360;d.arc((cx-r,cy-r,cx+r,cy+r),s_,s_+270,fill=M(GREEN,a),width=16)
    ang=math.radians(s_+270);px=cx+r*math.cos(ang);py=cy+r*math.sin(ang);d.ellipse((px-16,py-16,px+16,py+16),fill=M(GREEN,a))
def myth(d,t,my,r1,r2,num):
    title(d,[('MITO %d'%num,WHITE)],t,110);e=E(t,0.5);card(d,(80,480,1000,700),e);pill(d,110,500,'MITO',28,BG0,SAL,SAL,e)
    TX(d,540,615,my,56,WHITE,e,'mm')
    if t>2.0:
        pr=min(1,(t-2.0)/0.25);d.line((120,615,120+int(840*pr),615),fill=SAL,width=14)
    if t>2.6:
        e2=E(t,2.6);card(d,(80,780,1000,1180),e2);pill(d,110,800,'REALIDAD',28,BG0,GREEN,GREEN,e2);TX(d,540,975,r1,52,GREEN,e2,'mm');TX(d,540,1075,r2,44,WHITE,e2,'mm')
def stopw(d,t,lines,pills,size=110):
    title(d,lines,t,size);e=E(t,0.6,0.5);stopwatch(d,540,980,170,t,e)
    for k,s_ in enumerate(pills):pill(d,540,1250+k*100,s_,30,WHITE if k==0 else GREEN,(18,28,60) if k==0 else (14,50,45),OL if k==0 else (40,120,90),E(t,1.4+k*0.8),c=True)
def pillstack(d,t,lines,items,size=110,fs=46):
    title(d,lines,t,size)
    for k,s_ in enumerate(items):
        e=E(t,0.8+k*0.5);pill(d,540,780+k*125,s_,fs,WHITE,(18,28,60),OL,e,c=True,pad=50)
def threenums(d,t):
    d.line((240,950,840,950),fill=M(OL,E(t,0.6)),width=6)
    for k in range(3):
        e=EB(t,0.8+k*0.5,0.4);r=int(70*max(0,min(1.1,e)))
        if r>5:d.ellipse((240+k*300-r,950-r,240+k*300+r,950+r),fill=GREEN);d.text((240+k*300,950),str(k+1),font=F(70),fill=BG0,anchor='mm')
def halves(d,t):
    e=E(t,0.3);card(d,(60,330,1020,900),e);TX(d,540,420,'SIN SERVER',84,GRAY,e,'mm')
    for k,x in enumerate([300,540,780]):avatar(d,x,640,(70,80,110),E(t,0.6+k*0.2))
    TX(d,540,830,'...',60,GRAY,E(t,1.2),'mm')
    e2=E(t,1.6);card(d,(60,980,1020,1500),e2);TX(d,540,1070,'CON SERVER',84,GREEN,e2,'mm');rack(d,540,1150,320,2,t,e2)
    r=int(56*E(t,2.2))
    if r>5:d.ellipse((540-r,940-r,540+r,940+r),fill=GREEN);d.text((540,940),'VS',font=F(44),fill=BG0,anchor='mm')
"""
CTA2S=("Argentino, Bueno y Barato. Desde 600 pesos argentinos por mes. Mirá todo en abybhost.online","Argentino, Bueno y Barato. Desde seiscientos pesos argentinos por mes. Mirá todo en a b y b host punto online.")
def sv(a,b=None):return (a,b if b else a)
V2={}
V2['v4_barato']=dict(h='BARATO DE VERDAD',f='PRECIO / CLARO / SIMPLE',tags=['EL PROBLEMA','PRECIO','SIN EXTRAS','EJEMPLO','POR ESCRITO','ABYB HOST','EMPEZÁ HOY'],
S=[sv("¿Pagás por cosas que no usás en tu hosting?"),sv("Barato de verdad significa precios accesibles y claros."),sv("Sin agregar características que no necesitás para tu servidor."),
sv("Por ejemplo, hay planes con CPU compartida, que permiten bajar costos.","Por ejemplo, hay planes con Ce Pe U compartida, que permiten bajar costos."),sv("Y antes de pagar, confirmá el precio total por escrito."),
sv("En AByB Host: desde 600 pesos argentinos por mes, atención por WhatsApp o Discord, y hecho para Argentina.","En Abyb Host: desde seiscientos pesos argentinos por mes, atención por Guasap o Discord, y hecho para Argentina."),CTA2S],
SC="""    if i==0:
        title(d,[('¿PAGÁS POR',WHITE),('COSAS QUE',GREEN),('NO USÁS?',GREEN)],t,88);gscene(d,t,'$ $ $')
    elif i==1:
        stat(d,t,[('BARATO',WHITE),('DE VERDAD',GREEN)],'DESDE','$600',('ARS POR MES','PRECIOS CLAROS'),['ACCESIBLES','CLAROS'],110)
    elif i==2:
        features(d,t,[('SIN EXTRAS',WHITE),('QUE NO',GREEN),('NECESITÁS',GREEN)],['SOLO LO QUE NECESITÁS','PRECIO ACCESIBLE Y CLARO','SIN CARACTERÍSTICAS DE MÁS'],92)
    elif i==3:
        title(d,[('EJEMPLO:',WHITE),('CPU COMPARTIDA',GREEN)],t,92);e=E(t,0.5,0.6);chip(d,540,1000,240,t,e)
        pill(d,540,1260,'MENOS COSTO',36,GREEN,(14,50,45),(40,120,90),E(t,1.4),c=True);pill(d,540,1360,'REVISÁ SUS LÍMITES',36,WHITE,(18,28,60),OL,E(t,2.2),c=True)
    elif i==4:
        chat(d,t,[('CONFIRMÁ',WHITE),('EL PRECIO',GREEN),('POR ESCRITO',GREEN)],[('Hola, ¿cuál es el precio total?',True),('Te lo confirmo por acá',False)],88)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('TENÉS',GREEN)],['DESDE $600 ARS POR MES','ATENCIÓN POR WHATSAPP O DISCORD','HECHO PARA ARGENTINA'],96)
    else:
        cta2(d,t)
""")
V2['v5_incluye']=dict(h='QUÉ INCLUYE',f='BENEFICIOS / RECURSOS / SOPORTE',tags=['EL SERVICIO','BENEFICIOS','RECURSOS','SOPORTE','ACTIVACIÓN','CONDICIONES','ABYB HOST'],
S=[sv("¿Qué incluye tu hosting? Te lo mostramos claro."),sv("Beneficios: infraestructura en Argentina, panel Pterodactyl y reinicio automático ante fallos, según el plan.","Beneficios: infraestructura en Argentina, panel Terodáctil y reinicio automático ante fallos, según el plan."),
sv("Recursos: RAM, CPU y slots definidos en la ficha de cada servicio.","Recursos: Ram, Ce Pe U y eslots definidos en la ficha de cada servicio."),sv("Soporte: consultas y contratación por WhatsApp o Discord.","Soporte: consultas y contratación por Guasap o Discord."),
sv("La activación es manual, generalmente en menos de una hora hábil tras confirmar el pago."),sv("Y las condiciones reales están a la vista: no ofrecemos garantía de 99,9% de disponibilidad."),CTA2S],
SC="""    if i==0:
        title(d,[('¿QUÉ INCLUYE',WHITE),('TU HOSTING?',GREEN)],t,96);clip(d,t,E(t,0.5,0.6))
    elif i==1:
        features(d,t,[('BENEFICIOS',GREEN)],['INFRAESTRUCTURA EN ARGENTINA','PANEL PTERODACTYL','REINICIO AUTOMÁTICO (SEGÚN PLAN)'],120)
    elif i==2:
        title(d,[('RECURSOS',GREEN)],t,120)
        for k,s_ in enumerate(['RAM','CPU','SLOTS']):
            e=E(t,0.8+k*0.7);y=500+k*200;ox=int((1-e)*500);card(d,(80+ox,y,1000+ox,y+170),e);TX(d,130+ox,y+85,s_,56,GREEN,e,'lm');TX(d,420+ox,y+85,'SEGÚN LA FICHA',38,WHITE,e,'lm')
        ej(d,t,3.0,1190)
    elif i==3:
        features(d,t,[('SOPORTE',GREEN)],['CONSULTAS POR WHATSAPP','CONSULTAS POR DISCORD','TE AYUDAMOS A ELEGIR'],120)
    elif i==4:
        stopw(d,t,[('ACTIVACIÓN',WHITE),('MANUAL',GREEN)],['GENERALMENTE MENOS DE 1 HORA HÁBIL','TRAS CONFIRMAR EL PAGO'],110)
    elif i==5:
        features(d,t,[('CONDICIONES',WHITE),('REALES',GREEN)],['SIN GARANTÍA DE 99,9%','PAGO POR TRANSFERENCIA','COBERTURA COMERCIAL DE 48 HS'],104)
    else:
        cta2(d,t)
""")
V2['v6_mitos']=dict(h='MITOS DEL HOSTING',f='MITO / REALIDAD / TRANSPARENCIA',tags=['EL TEMA','MITO 1','MITO 2','MITO 3','GARANTÍA','ABYB HOST','EMPEZÁ HOY'],
S=[sv("Dicen cosas del hosting barato. Vamos a ver qué es cierto."),sv("Mito uno: la atención es lejana. Realidad: atención directa por WhatsApp o Discord.","Mito uno: la atención es lejana. Realidad: atención directa por Guasap o Discord."),
sv("Mito dos: te prometen disponibilidad perfecta. Realidad: no ofrecemos garantía de 99,9%, y te lo decimos."),sv("Mito tres: hay costos escondidos. Realidad: confirmás el precio total por escrito antes de pagar."),
sv("Y si algo falla por nuestra cuenta, hay cobertura comercial de 48 horas."),sv("En AByB Host, sin humo: atención directa, condiciones reales en la web y precios claros.","En Abyb Host, sin humo: atención directa, condiciones reales en la web y precios claros."),CTA2S],
SC="""    if i==0:
        title(d,[('¿HOSTING BARATO',WHITE),('ES MALO?',GREEN)],t,92);TX(d,540,1010,'?',520,GREEN,E(t,0.8),'mm')
    elif i==1:
        myth(d,t,'ATENCIÓN LEJANA','ATENCIÓN DIRECTA','POR WHATSAPP O DISCORD',1)
    elif i==2:
        myth(d,t,'PROMESAS EXAGERADAS','SIN GARANTÍA DE 99,9%','TE LO DECIMOS DE ENTRADA',2)
    elif i==3:
        myth(d,t,'COSTOS ESCONDIDOS','PRECIO TOTAL POR ESCRITO','ANTES DE PAGAR',3)
    elif i==4:
        stopw(d,t,[('COBERTURA',WHITE),('COMERCIAL DE 48 HS',GREEN)],['POR PROBLEMAS A NUESTRO CARGO'],92)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('SIN HUMO',GREEN)],['ATENCIÓN DIRECTA','CONDICIONES REALES EN LA WEB','PRECIOS CLAROS'],104)
    else:
        cta2(d,t)
""")
V2['v7_comunidad']=dict(h='TU COMUNIDAD DE DISCORD',f='COMUNIDAD / SERVER / BOTS',tags=['TU COMUNIDAD','EL PROBLEMA','JUEGOS','BOTS','PANEL','CONTRATÁ','EMPEZÁ HOY'],
S=[sv("¿Tenés una comunidad de Discord? Dale su propio server."),sv("Cuando todos quieren jugar y no hay dónde, la comunidad se frena."),
sv("En AByB Host podés alojar SCP: Secret Laboratory, Counter-Strike 1.6, Counter-Strike: Source y Minecraft.","En Abyb Host podés alojar Ese Ce Pe Secret Laboratory, Counter Strike uno punto seis, Counter Strike Source y Minecraft."),
sv("Y también bots de Discord, en Node.js y Python.","Y también bots de Discord, en Nod punto Yei Ese y Páiton."),sv("Con el panel Pterodactyl, administrás todo vos mismo.","Con el panel Terodáctil, administrás todo vos mismo."),
sv("Consultás y contratás por WhatsApp o Discord, y te ayudamos a elegir.","Consultás y contratás por Guasap o Discord, y te ayudamos a elegir."),CTA2S],
SC="""    if i==0:
        title(d,[('¿TENÉS UNA',WHITE),('COMUNIDAD',GREEN),('DE DISCORD?',WHITE)],t,96)
        for k in range(9):
            txt_=t;t0=0.5+k*0.22
            if t>t0:TX(d,180+(k*173)%760,950+(k*113)%420,'+1',100,GREEN,E(t,t0,0.3),'mm')
    elif i==1:
        chat(d,t,[('¿JUGAMOS',WHITE),('Y NO HAY',GREEN),('SERVER?',GREEN)],[('¿Jugamos CS?',True),('¿Alguien tiene server?',False),('Yo no...',True)],88)
    elif i==2:
        grid(d,t,[('TU SERVER',WHITE),('DE JUEGO',GREEN)],['SCP:SL','CS 1.6','CS:SOURCE','MINECRAFT'],110)
    elif i==3:
        botscene(d,t,[('BOTS DE',WHITE),('DISCORD',GREEN)],110)
    elif i==4:
        panel(d,t,[('PANEL',WHITE),('PTERODACTYL',GREEN)],104)
    elif i==5:
        features(d,t,[('CONTRATÁ',WHITE),('FÁCIL',GREEN)],['CONSULTÁ POR WHATSAPP','O UNITE AL DISCORD','TE AYUDAMOS A ELEGIR'],110)
    else:
        cta2(d,t)
""")
V2['v8_contratar']=dict(h='CÓMO CONTRATAR',f='CONSULTÁ / CONFIRMÁ / ACTIVÁ',tags=['LOS PASOS','PASO 1','PASO 2','PASO 3','ACTIVACIÓN','ABYB HOST','EMPEZÁ HOY'],
S=[sv("¿Cómo se contrata un server? Son tres pasos."),sv("Uno: consultanos por WhatsApp o Discord qué necesitás.","Uno: consultanos por Guasap o Discord qué necesitás."),
sv("Dos: confirmá por escrito el precio, los recursos y la forma de pago."),sv("Tres: pagás por transferencia y activamos tu servicio de forma manual."),
sv("Generalmente, en menos de una hora hábil, después de confirmar el pago."),sv("Si tenés dudas, te ayudamos a elegir el servicio adecuado."),CTA2S],
SC="""    if i==0:
        title(d,[('¿CÓMO SE',WHITE),('CONTRATA?',GREEN)],t,110);threenums(d,t)
    elif i==1:
        chat(d,t,[('1.',WHITE),('CONSULTÁ',GREEN)],[('Hola, quiero un server de Minecraft',True),('Te ayudamos a elegir',False)],110)
    elif i==2:
        features(d,t,[('2.',WHITE),('CONFIRMÁ',GREEN)],['PRECIO TOTAL','RECURSOS DEL PLAN','FORMA DE PAGO'],110)
    elif i==3:
        features(d,t,[('3.',WHITE),('ACTIVAMOS',GREEN)],['PAGO POR TRANSFERENCIA','ACTIVACIÓN MANUAL','TU SERVICIO EN MARCHA'],110)
    elif i==4:
        stopw(d,t,[('MENOS DE',WHITE),('1 HORA HÁBIL',GREEN)],['GENERALMENTE, TRAS CONFIRMAR EL PAGO','ACTIVACIÓN MANUAL'],96)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('TE AYUDAMOS',GREEN)],['ELEGÍS TU SERVICIO','CONSULTÁS POR WHATSAPP O DISCORD','CONFIRMÁS TODO POR ESCRITO'],96)
    else:
        cta2(d,t)
""")
V2['v9_pc_vs_host']=dict(h='TU PC VS UN HOST',f='PC / HOST / PANEL',tags=['EL PROBLEMA','COMPARACIÓN','PANEL','REINICIO','SIN PROMESAS','ABYB HOST','EMPEZÁ HOY'],
S=[sv("¿Hosteás tu server en tu PC? Mirá la diferencia.","¿Hosteás tu server en tu Pe Ce? Mirá la diferencia."),sv("Tu PC depende de que esté prendida y de tu internet. Un host tiene su infraestructura en Argentina, con panel y reinicio automático según el plan."),
sv("Con un host, administrás todo desde el panel Pterodactyl.","Con un host, administrás todo desde el panel Terodáctil."),sv("Y si el servicio falla, hay reinicio automático, según el plan elegido."),
sv("Eso sí: no prometemos una garantía de 99,9% de disponibilidad."),sv("En AByB Host: infraestructura en Argentina, panel Pterodactyl y soporte por WhatsApp o Discord.","En Abyb Host: infraestructura en Argentina, panel Terodáctil y soporte por Guasap o Discord."),CTA2S],
SC="""    if i==0:
        title(d,[('¿HOSTEÁS',WHITE),('EN TU PC?',GREEN)],t,100);gscene(d,t,'¡SE APAGÓ!')
    elif i==1:
        cmp(d,t,[('TU PC',WHITE),('VS HOST',GREEN)],['TU PC','HOST'],[('UBICACIÓN',['TU CASA','EN ARGENTINA']),('ADMINISTRACIÓN',['TODO A MANO','PANEL PTERODACTYL']),('ANTE FALLOS',['VOS REINICIÁS','REINICIO AUTOMÁTICO*'])],[SAL,GREEN],104,'*SEGÚN EL PLAN')
    elif i==2:
        panel(d,t,[('PANEL',WHITE),('PTERODACTYL',GREEN)],104)
    elif i==3:
        title(d,[('REINICIO',WHITE),('AUTOMÁTICO',GREEN)],t,104);e=E(t,0.5,0.6);rack(d,540,820,300,2,t,e);restart(d,540,1230,100,t,e)
        pill(d,540,1380,'SEGÚN EL PLAN',34,WHITE,(18,28,60),OL,E(t,1.6),c=True)
    elif i==4:
        title(d,[('SIN PROMESAS',WHITE),('EXAGERADAS',GREEN)],t,96);e=E(t,0.6);card(d,(80,640,1000,960),e);TX(d,540,800,'99,9%',170,GRAY,e,'mm')
        if t>1.4:d.line((200,860,880,740),fill=SAL,width=16)
        pill(d,540,1030,'NO LO GARANTIZAMOS',38,SAL,(40,22,28),SAL,E(t,1.8),c=True);pill(d,540,1150,'HACEMOS LO POSIBLE POR MANTENER TODO ARRIBA',26,WHITE,(18,28,60),OL,E(t,2.6),c=True)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('TENÉS',GREEN)],['INFRAESTRUCTURA EN ARGENTINA','PANEL PTERODACTYL','SOPORTE POR WHATSAPP Y DISCORD'],96)
    else:
        cta2(d,t)
""")
V2['v10_servicios']=dict(h='ELEGÍ TU SERVICIO',f='JUEGOS / MINECRAFT / BOTS',tags=['EL INICIO','JUEGOS','MINECRAFT','BOTS','A MEDIDA','ABYB HOST','EMPEZÁ HOY'],
S=[sv("¿Qué querés alojar? Elegí tu servicio."),sv("Para juegos, tenemos SCP: Secret Laboratory, Counter-Strike 1.6 y Counter-Strike: Source.","Para juegos, tenemos Ese Ce Pe Secret Laboratory, Counter Strike uno punto seis y Counter Strike Source."),
sv("En Minecraft: Vanilla, Paper o Forge.","En Minecraft: Vainila, Péiper o Forch."),sv("Y para tu comunidad de Discord, bots en Node.js y Python.","Y para tu comunidad de Discord, bots en Nod punto Yei Ese y Páiton."),
sv("¿Necesitás otra cosa? Hay servicio personalizado: contanos qué querés alojar."),sv("En AByB Host elegís entre servidores de juego, bots de Discord o un servicio personalizado.","En Abyb Host elegís entre servidores de juego, bots de Discord o un servicio personalizado."),CTA2S],
SC="""    if i==0:
        pillstack(d,t,[('¿QUÉ QUERÉS',WHITE),('ALOJAR?',GREEN)],['SCP:SL','CS 1.6','CS:SOURCE','MINECRAFT','BOTS DE DISCORD'],110)
    elif i==1:
        grid(d,t,[('SERVIDORES',WHITE),('DE JUEGO',GREEN)],['SCP:SL','CS 1.6','CS:SOURCE'],110)
    elif i==2:
        features(d,t,[('MINECRAFT',GREEN)],['VANILLA','PAPER','FORGE'],120)
    elif i==3:
        botscene(d,t,[('BOTS DE',WHITE),('DISCORD',GREEN)],110)
    elif i==4:
        title(d,[('SERVICIO',WHITE),('PERSONALIZADO',GREEN)],t,96);e=E(t,0.6);card(d,(80,700,1000,1000),e);TX(d,540,850,'¿NECESITÁS OTRA COSA?',48,WHITE,e,'mm')
        pill(d,540,1100,'CONTANOS QUÉ NECESITÁS',38,GREEN,(14,50,45),(40,120,90),E(t,1.4),c=True);pill(d,540,1220,'EVALUAMOS QUÉ ALTERNATIVA OFRECERTE',28,WHITE,(18,28,60),OL,E(t,2.2),c=True)
    elif i==5:
        features(d,t,[('EN ABYB HOST',WHITE),('ELEGÍS',GREEN)],['SERVIDORES DE JUEGO','BOTS DE DISCORD','SERVICIO PERSONALIZADO'],96)
    else:
        cta2(d,t)
""")
V2['v11_antes_despues']=dict(h='ANTES Y DESPUÉS',f='SIN SERVER / CON SERVER',tags=['LA DIFERENCIA','SIN SERVER','CON ABYB HOST','TU SERVICIO','ACTIVACIÓN','PRECIO','EMPEZÁ HOY'],
S=[sv("Mirá la diferencia."),sv("Sin server: tus amigos esperando y nadie juega."),sv("Con AByB Host: infraestructura en Argentina, panel Pterodactyl y soporte por WhatsApp o Discord.","Con Abyb Host: infraestructura en Argentina, panel Terodáctil y soporte por Guasap o Discord."),
sv("Elegís tu servicio y lo activamos."),sv("La activación es manual, generalmente en menos de una hora hábil tras confirmar el pago."),sv("Y los precios son accesibles: desde 600 pesos argentinos por mes."),CTA2S],
SC="""    if i==0:
        halves(d,t)
    elif i==1:
        chat(d,t,[('SIN SERVER',GREEN)],[('¿Y el server?',True),('Nada...',False),('Me aburro',True)],120)
    elif i==2:
        features(d,t,[('CON ABYB HOST',GREEN)],['INFRAESTRUCTURA EN ARGENTINA','PANEL PTERODACTYL','SOPORTE POR WHATSAPP O DISCORD'],100)
    elif i==3:
        grid(d,t,[('ELEGÍS',WHITE),('TU SERVICIO',GREEN)],['SCP:SL','CS 1.6','CS:SOURCE','MINECRAFT'],104)
    elif i==4:
        stopw(d,t,[('ACTIVACIÓN',WHITE),('MANUAL',GREEN)],['GENERALMENTE MENOS DE 1 HORA HÁBIL','TRAS CONFIRMAR EL PAGO'],110)
    elif i==5:
        stat(d,t,[('PRECIOS',WHITE),('ACCESIBLES',GREEN)],'DESDE','$600',('ARS POR MES','EN PESOS ARGENTINOS'),['ACCESIBLES','CLAROS'],110)
    else:
        cta2(d,t)
""")
V2['v12_argentino']=dict(h='ARGENTINO, BUENO Y BARATO',f='ARGENTINO / BUENO / BARATO',tags=['EL INICIO','MATE','TRUCO','TU SERVER','ARGENTINO','BUENO Y BARATO','EMPEZÁ HOY'],
S=[sv("Argentino que se respeta tiene tres cosas."),sv("Uno: mate caliente."),sv("Dos: truco con los pibes."),sv("Tres: tu propio server."),
sv("Argentino: hecho para comunidades argentinas y jugadores de Latam."),sv("Bueno para jugar: simple de gestionar. Y barato de verdad: desde 600 pesos.","Bueno para jugar: simple de gestionar. Y barato de verdad: desde seiscientos pesos."),CTA2S],
SC="""    if i==0:
        pillstack(d,t,[('ARGENTINO QUE',WHITE),('SE RESPETA',GREEN)],['MATE','TRUCO','SERVER'],88,64)
    elif i==1:
        title(d,[('1.',WHITE),('MATE',GREEN)],t,120);mate(d,540,1000,t,E(t,0.4,0.5))
    elif i==2:
        title(d,[('2.',WHITE),('TRUCO',GREEN)],t,120);cards3(d,t)
    elif i==3:
        title(d,[('3.',WHITE),('TU PROPIO',GREEN),('SERVER',GREEN)],t,96);rack(d,540,900,440,3,t,E(t,0.5,0.6))
    elif i==4:
        features(d,t,[('ARGENTINO',GREEN)],['HECHO PARA ARGENTINA','COMUNIDADES ARGENTINAS','JUGADORES DE LATAM'],120)
    elif i==5:
        features(d,t,[('BUENO',WHITE),('Y BARATO',GREEN)],['SIMPLE DE GESTIONAR','PRECIOS ACCESIBLES Y CLAROS','DESDE $600 ARS POR MES'],110)
    else:
        cta2(d,t)
""")
for k,v in V2.items():
    s=head+"S="+repr(v['S'])+"\n"+mid
    s=s.replace("'QUÉ ES UN HOST'",repr(v['h'])).replace("'HOST / SERVER / ONLINE'",repr(v['f']))
    s=re.sub(r"TAGS=\[.*?\]\n","TAGS="+repr(v['tags'])+"\n",s,count=1,flags=re.S)
    s+=EXTRA+"\n"+EXTRA2+"\n"+frame_head+v['SC']+tail
    open(f'w_{k}.py','w').write(s)
print('built',list(V2))
