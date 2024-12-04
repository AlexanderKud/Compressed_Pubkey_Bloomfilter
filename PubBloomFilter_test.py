from pubkey_bloomfilter import PubBloomFilter
import secp256k1 as ice
from datetime import datetime

print(f"[{datetime.now().strftime("%H:%M:%S")}] Creating PubBloomFilter")
a = PubBloomFilter(2**32)
for i in range(2**22):
    P = ice.scalar_multiplication(i)
    pub = ice.point_to_cpub(P)
    a.add(pub)
a.save('test.bin')
print(f'1 bit -> {a.count_one()}')
print(f'0 bit -> {a.count_zero()}')
print(f"[{datetime.now().strftime("%H:%M:%S")}] Done")

print(f"[{datetime.now().strftime("%H:%M:%S")}] Checking")
b = PubBloomFilter()
b.load('test.bin')
for i in range(2**22, 2**23):
    P = ice.scalar_multiplication(i)
    pub = ice.point_to_cpub(P)
    if b.check(pub):
        print(f'Pub: {pub}')
print(f"[{datetime.now().strftime("%H:%M:%S")}] Done") 
