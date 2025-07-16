import hashlib
import base64

def urlHasher(url: str) -> str:
    sha256 = hashlib.sha256(url.encode('utf-8')).digest()
    b64_encoded = base64.urlsafe_b64encode(sha256)  
    return b64_encoded.decode('utf-8')[:16]  
