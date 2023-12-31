


t = int(input())
if t in range (0,513):

    val = []
    for i in range(0,t):
        d ,m ,c = input().split()
        
        d = str(d)
        d = list(d)
        
        m = str(m)
        m = list(m)
        
        c = str(c)
        c = list(c)

        if ((c[0] or c[1])not in (d[0] or d[1] or m[0] or m[1])):
            if c[0] == "O" :
                val.append("valid")

            elif d[0] == c[0] or m[0] == c[0] or d[0] == c[1] or m[0] == c[1] or d[1] == c[0] or d[1] == c[1] or m[1] == c[0] or m[1] == c[1]:
                if c[1] == "+" or c[1] == "-":
                    val.append("invalid")
                else: 
                    val.append("valid")
                
            else:
                val.append("invalid")

                
        else:
            val.append("valid")
        
        
    for p in range(0,len(val)):
        print(val[p])
