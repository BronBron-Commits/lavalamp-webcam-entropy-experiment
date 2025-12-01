import os, time

pipe_path = "/tmp/unhidra_entropy.pipe"

# Ensure pipe exists
if not os.path.exists(pipe_path):
    os.mkfifo(pipe_path)

print("[🧠] Starting entropy feeder ->", pipe_path)

while True:
    entropy = os.urandom(32)
    try:
        with open(pipe_path, "wb", buffering=0) as pipe:
            pipe.write(entropy)
    except BrokenPipeError:
        pass
    time.sleep(0.05)  # adjustable frequency
