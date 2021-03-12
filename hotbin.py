import random
import secrets
import string
import stringplusplus

def mkBin(bl):
    bits = []

    for i in range(int(bl)):
        bits.append(str(random.randint(0, 1)))
        binary = "".join(bits)

    return(binary)

def mkBinStatement(bl, sl, d = " "):
    statements = []

    for i in range(int(sl)):
        statements.append(str(mkBin(int(bl))))
        binarystatements = d.join(statements)

    return(binarystatements)

def mkArc(al):
    arc = []

    for i in range(al):
        arc.append(random.choice(str(string.ascii_lowercase)) + random.choice(str(string.digits)) + random.choice(str(string.ascii_uppercase)))
        arcstatements = " ".join(arc)

    return(arcstatements)
    
def mkCode(cl):
    code = []
    
    for i in range(int(cl)):
        code.append(secrets.choice(secrets.choice(string.ascii_lowercase) + secrets.choice(string.ascii_uppercase) + secrets.choice(string.digits)))
        codes = "".join(code)
        
    return(codes)