a = [1,4,1,2,4,3,1,5,7,1,5,3]
track={} 

for e in a:
    if e in track.keys(): #jodi track dictionary te age item ta thake, taile item tar count barabo 
        track[e] += 1  
    else:
        track[e] = 1     #ar jodi na thake value tar count 1 dhore nibo, dictionary te insert korbo
mx, ans = 0,0            #apatoto max value(mx) 0, answer 0
for e in track.items():  #dictionary er kon item kotobar ache iterate 
    if e[1] > mx:        #ekhane e ekta tuple, 0 index a key thakbe, 1 index er value thakbe
        mx = e[1]        #jodi je value ta beshibar ache update kortesi, ans a oi item key ta rakhtesi  
        ans = e[0]
print(ans)
        
