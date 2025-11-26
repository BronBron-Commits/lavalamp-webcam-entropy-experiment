import time
from modules.camera_capture import CameraEntropySource
from modules.entropy_pool import EntropyPool

camera = CameraEntropySource(device_index=2)
pool = EntropyPool()

print("Entropy appliance started. Press Ctrl+C to stop.")

while True:
    chunk = camera.get_entropy_chunk()
    pool.mix(chunk)
    print("Mixed chunk:", chunk.hex())
    time.sleep(0.5)
