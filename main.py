from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

print("Ethereum Vanity Address Generator :")
print("Please Enter Your Prefix or Suffix")
print("0 - Prefix")
print("1- Suffix")
check = int(input())
print("Please Enter Desered Vanity Input : Wihtout 0X")
usrInput= str(input())
if(check == 0):
  print("You Have Selected Suffix Option With Custom Vanity",usrInput)
  for i in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    private_key = str(private_key.hex())
    if((addr.lower()).startswith(usrInput)):
      print("Address Generated With Prefix: ",usrInput)
      print('eth addr: 0x' + addr)
      print('private_key:', private_key)
    else:
      continue
elif(check== 1):
  print("You Have Selected Prefix Option With Custom Vanity",usrInput)
  for j in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    private_key = str(private_key.hex())
    if((addr.lower()).endswith(usrInput)):
      print("Address Generated With Sufix: ",usrInput)
      print('eth addr: 0x' + addr)
      print('private_key:', private_key)
    else:
      continue
