import hashlib
print(hashlib.sha256(b"Nobody inspects the spammish repetition1712912126").hexdigest())
string = "Nobody inspects the spammish repetition"
zeros = int(input('how many zeros'))
nonce = 876
print(hashlib.sha256(b"Nobody inspects the spammish repetition1712912126").hexdigest())
nhash = '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
while nhash[:zeros]!='0'*zeros:
    nhash = hashlib.sha256(bytes(string+str(nonce), 'utf-8')).hexdigest()
    nonce += 10
print(nhash)
print(string+str(nonce))
