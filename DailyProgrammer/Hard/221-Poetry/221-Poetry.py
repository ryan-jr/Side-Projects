# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:14:25 2018

@author: rjr
"""

# Iterate over the lines of the file checking each of the words and seeing 
# if they contain the most common words in the dictionary, if they do, add that line 
# to a list

words = []
ngrams = ["bk",  "fq",  "jc",  "jt",  "mj",  "qh",  "qx",  "vj",  "wz",  "zh",
"bq",  "fv",  "jd",  "jv",  "mq",  "qj",  "qy",  "vk",  "xb",  "zj", "bx",  "fx",
"jf",  "jw",  "mx",  "qk",  "qz",  "vm",  "xg",  "zn", "cb",  "fz",  "jg",  "jx",
"mz",  "ql",  "sx",  "vn",  "xj",  "zq", "cf", "gq",  "jh",  "jy",  "pq",  "qm",
"sz",  "vp",  "xk",  "zr", "cg",  "gv",  "jk",  "jz",  "pv",  "qn",  "tq",  "vq",
"xv",  "zs", "cj",  "gx",  "jl",  "kq",  "px",  "qo",  "tx",  "vt",  "xz",  "zx",
"cp",  "hk",  "jm",  "kv",  "qb",  "qp",  "vb",  "vw",  "yq", "cv",  "hv",  "jn",
"kx",  "qc",  "qr",  "vc",  "vx",  "yv", "cw",  "hx",  "jp",  "kz",  "qd",  "qs",
"vd",  "vz",  "yz", "cx",  "hz",  "jq",  "lq",  "qe",  "qt",  "vf",  "wq",  "zb",
"dx",  "iy",  "jr",  "lx",  "qf",  "qv",  "vg",  "wv",  "zc", "fk",  "jb",  "js",
"mg",  "qg",  "qw",  "vh",  "wx",  "zg"]

poetryWords = ["time", "light", "night", "long", "love", "man", "yes", "white", "world", "face", "air", "left", "black", "water", "head", "life", "day", "hand", "people", "wind",
"inside", "sea" "red", "things", "lost"]

with open("belowSeventy.txt", "r") as f:
    x = f.readlines()
    
ctr = 0  
x = list(map(lambda s: s.strip(), x))


with open("poetry.txt", "r") as f:
    for line in f:
        if len(line) > 100:
            pass
        else:
            for word in line.split():
                if len(word) >= 15 or len(word) == 1:
                    pass
                else:
                   \
                    words.append(word)
    
with open("words.txt", "w") as f:
    for i in words:
        if i in x:
            f.write(i)
            f.write(" ")
    


"""
# appending the line if if one of the words from poetry matches 
                if word in poetryWords:
                    lines.append(line)
                    
# Trying to add/find words that are the average length in english:
    # (i in x and len(i) >= 3) or 
    
    
    
"""