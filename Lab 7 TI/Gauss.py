import Euqlid

def Gauss(M,q):
    i_begin,j_begin=0,0
    while(True):
        if i_begin>=len(M) or j_begin>=len(M[0]): return
        i_lead,j_lead,check=0,0,0
        for j in range(j_begin,len(M[0])):
            for i in range(i_begin,len(M)):
                if (M[i][j]!=0):
                    i_lead,j_lead=i,j
                    check=1
                    break
            if (check==1): break
            if (j==len(M[0])-1): return
            j_begin+=1

        if (i_lead!=i_begin):
            M[i_lead],M[i_begin]=M[i_begin],M[i_lead]
            i_lead=i_begin
        
        lead_elem=M[i_lead][j_lead]
        if (M[i_lead][j_lead]!=1):
            for j in range(j_lead,len(M[0])):
                M[i_lead][j]=(M[i_lead][j]*Euqlid.extended_Euqlid(lead_elem,q))%q
                #M[i_lead][j]//=lead_elem

        if (i_lead<len(M)-1):
            for i in range(i_lead+1,len(M)):
                if (M[i][j_lead]==0):
                    continue
                #k=(-1)*M[i][j_lead]//M[i_lead][j_lead]
                k=q-M[i][j_lead]
                for j in range(j_lead,len(M[0])):
                    M[i][j]=(M[i][j]+(M[i_lead][j]*k)%q)%q
                    #M[i][j]+=M[i_lead][j]*k

        #for j in range(j_lead+1,len(M[0])):
         #   k=q-M[i_lead][j]
            #k=(-1)*M[i_lead][j]//lead_elem
         #   M[i_lead][j]=(M[i_lead][j]+(M[i_lead][j_lead]*k)%q)%q
        #i_begin+=1
        #j_begin+=1

