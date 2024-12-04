from bitarray import bitarray

class PubBloomFilter:
    
    def __init__(self, size = 0):
        if size == 0:
            self.array = bitarray()
        else:
            self.array = bitarray(size)
        self.loop = 2 # 2 3 4  4 - max
        
    def size(self):
        return len(self.array)
    
    def save(self, filename):
        with open(filename, 'wb') as f:
            self.array.tofile(f)
    
    def load(self, filename):
        with open(filename, 'rb') as f:
            self.array.fromfile(f)

    def add(self, pubkey):
        pub_slice = pubkey[2:]
        for i in range(self.loop):
            num1 = int(pub_slice[i*14:i*14+8], 16)
            num2 = int(pub_slice[i*14+8:i*14+8+6], 16)
            if num1 > num2:
                index = num1 - num2
                self.array[index] = True
            else:
                index = num2 - num1
                self.array[index] = True
        num3 = int(pub_slice[56:60], 16)
        self.array[num3] = True
        num4 = int(pub_slice[60:64], 16)
        self.array[num4] = True
        num5 = int(pub_slice[56:64], 16)
        self.array[num5] = True
    
    def check(self, pubkey):
        pub_slice = pubkey[2:]
        for i in range(self.loop):
            num1 = int(pub_slice[i*14:i*14+8], 16)
            num2 = int(pub_slice[i*14+8:i*14+8+6], 16)
            if num1 > num2:
                index = num1 - num2
                if self.array[index] == False:
                    return False
            else:
                index = num2 - num1
                if self.array[index] == False:
                    return False
        num3 = int(pub_slice[56:60], 16)
        if self.array[num3] == False:
            return False
        num4 = int(pub_slice[60:64], 16)
        if self.array[num4] == False:
            return False
        num5 = int(pub_slice[56:64], 16)
        if self.array[num5] == False:
            return False
        return True
        
    def count_one(self):
        return self.array.count(1)
    
    def count_zero(self):
        return self.array.count(0)
