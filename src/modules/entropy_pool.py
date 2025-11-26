import hashlib

class EntropyPool:
    def __init__(self):
        # 64-byte initial pool
        self.pool = b'\x00' * 64

    def mix(self, entropy_chunk):
        if entropy_chunk:
            self.pool = hashlib.sha512(self.pool + entropy_chunk).digest()

    def get(self, size=32):
        # derive random output
        out = hashlib.sha512(self.pool).digest()
        self.pool = hashlib.sha512(self.pool + out).digest()
        return out[:size]
