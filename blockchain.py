import hashlib
import glob
from hashlib import md5
import os
import re

def blockchain(blocks_dir, IV):
    ph=IV
    md5_str = ''
    blocks=glob.glob(blocks_dir+'/*',recursive=True)
    con = lambda text: int(text) if text.isdigit() else text 
    alphanum = lambda key: [ con(c) for c in re.split('([0-9]+)', key) ]
    BLOCKS= sorted(blocks, key = alphanum)
    for i in BLOCKS:
        Hleaf=[]
        T=[]
        tran=glob.glob(i+'/*',recursive=True)
        convert = lambda text: int(text) if text.isdigit() else text 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        SORtranz=sorted(tran, key = alphanum_key)
        for e in SORtranz:
            p=open(e)
            file=p.read()
            T.append(file)
        for row in T:
            currentItem=str(row)
            Hleaf.append(hashlib.md5(currentItem.encode()).hexdigest())
        if(len(Hleaf)%2 !=0):
            Hleaf.append( Hleaf[-1])
        x=[]
        x=i.split("-")
        Height=x[1].split("_")
        Sons=x[2].split("_")
        H=int(Height[1])
        Son=int(Sons[1])         
        for k in range(H):
            parentArr = []
            i = 0
            SORtranz= ''
            for x in Hleaf:
                if i == Son:
                    hashedFile  = hashlib.md5(SORtranz.encode()).hexdigest()
                    parentArr.append(hashedFile)
                    i = 1
                    SORtranz = str(x)
                else:
                    SORtranz += str(x)
                    i += 1
            last = hashlib.md5(SORtranz.encode()).hexdigest()
            parentArr.append(last)
            Hleaf = parentArr
    
        hashedTxTree = Hleaf[0]
        SORtranz = ph + hashedTxTree
        ph = str(hashlib.md5(SORtranz.encode()).hexdigest())
        print(ph)
    
    md5_str = ph
    return md5_str

