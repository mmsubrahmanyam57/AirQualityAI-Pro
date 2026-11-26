import math, random
SOURCES=[('Industrial zone',180,220),('Road traffic',480,350),('Construction site',730,150)]
SENSORS=[(x,y) for y in (110,260,410) for x in (150,350,550,750)]
def simulate(speed=14,direction=0,emission=70,source=0):
    rng=random.Random(42); speed=max(2,min(30,float(speed))); emission=max(10,min(100,float(emission)))
    angle=math.radians(float(direction)); ux,uy=math.cos(angle),math.sin(angle)
    _,sx,sy=SOURCES[int(source)]; sensors=[]; scores=[0.0]*len(SOURCES); paths=[]
    for i,(x,y) in enumerate(SENSORS):
        dx,dy=x-sx,y-sy; along=dx*ux+dy*uy; cross=-dx*uy+dy*ux
        spread=45+max(0,along)*.25
        excess=emission*2.5*math.exp(-cross**2/(2*spread**2))*math.exp(-max(0,along)/(150+speed*22))* (1 if along>=0 else math.exp(along/35))
        pm=round(15+excess,1); sensors.append(dict(id=i+1,x=x,y=y,pm25=pm,pm10=round(pm*1.6,1),co=round(.3+pm*.009,2),no2=round(12+pm*.4,1)))
        for p in range(80):
            px,py=x,y; path=[[x,y]]; best=[float('inf')]*len(SOURCES)
            for step in range(45):
                px-=ux*speed*.7+rng.gauss(0,5); py-=uy*speed*.7+rng.gauss(0,5)
                for j,(_,a,b) in enumerate(SOURCES): best[j]=min(best[j],(px-a)**2+(py-b)**2)
                if step%5==0:path.append([round(px,1),round(py,1)])
            for j,d in enumerate(best): scores[j]+=excess*math.exp(-d/(2*55**2))
            if p==0 and excess>10:paths.append(path)
    total=sum(scores); ranks=[dict(name=n,x=x,y=y,score=round(100*s/total,1) if total else 0) for (n,x,y),s in zip(SOURCES,scores)]
    return dict(sensors=sensors,sources=sorted(ranks,key=lambda r:-r['score']),paths=paths,wind=speed,direction=direction,emission=emission,actual_source=SOURCES[int(source)][0])
