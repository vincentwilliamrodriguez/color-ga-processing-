#genetic algorithm slowly converges to a color

pol=[]

#target red
tr=0

#target green
tg=255

#target blue
tb=0

#mutation rate(from 1 to 100)
mr=1

def setup():
    size(500,500)
    
    #start
    
    for i in range(10):
        pol.append([])
        for j in range(10):
            pol[i].append([])
            r=floor(random(0,256))
            g=floor(random(0,256))
            b=floor(random(0,256))
            
            pol[i][j]=[r,g,b]
            
    #display
    for i in range(10):
        for j in range(10):
            dr=pol[i][j][0]
            dg=pol[i][j][1]
            db=pol[i][j][2]
            
            fill(dr,dg,db)
            rect(i*50,j*50,50,50)
            
    
def draw():
    # delay(500)
    
    global pol
    allowed=True

    #fitness
    totalscore=0
    for i in range(10):
        for j in range(10):
            # print(pol[i][j])
            cr=pol[i][j][0]
            cg=pol[i][j][1]
            cb=pol[i][j][2]
            
            fitness=765-(abs(tr-cr)+abs(tg-cg)+abs(tb-cb))
            pol[i][j].append(fitness)
            
            totalscore+=fitness
                
    #new pol
    newpol=[]
    
    for inp in range(10):
        newpol.append([])
        
        for jnp in range(10):
            newpol[inp].append([])
            
            #selection
            parent=[]
            
            minimum=0
            rs=floor(random(0,totalscore+1))
            
            for i in range(10):
                for j in range(10):
                    if minimum<rs and rs<minimum+pol[i][j][3]:
                        parent.append(pol[i][j][0:3])
                        
                    minimum+=pol[i][j][3]
                    
            #mutation
            for n in range(3):
                rand=floor(random(0,100))
                if rand<mr:
                    try:
                        parent[0][n]=abs(parent[0][n]+rand+1)
                    except:
                        allowed=False
            
            #acception
            try:
                newpol[inp][jnp]=[parent[0][0],parent[0][1],parent[0][2]]
            except:
                allowed=False
    if allowed:
        pol=newpol
    
        #display
        for i in range(10):
            for j in range(10):
                dr=pol[i][j][0]
                dg=pol[i][j][1]
                db=pol[i][j][2]
            
                fill(dr,dg,db)
                rect(i*50,j*50,50,50)
