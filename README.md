# Lavalamp Webcam Entropy Experiment

This project collects entropy from a webcam feed and outputs one byte at a time through a named pipe.  
Other programs (like U-ai) can read from this pipe to add external randomness.

## Purpose

The goal is to create a simple, real-world entropy source using pixel values from a live webcam.  
This allows any application to incorporate a small amount of real-world noise.

## How It Works

1. A Python script opens the webcam.
2. Each frame is sampled using a basic intensity calculation.
3. One byte of entropy is produced from each frame.
4. The byte is written to a named pipe at:

    /tmp/unhidra_entropy.pipe

5. Any external program can read from this pipe.

## Running

Create the pipe:

    rm -f /tmp/unhidra_entropy.pipe
    mkfifo /tmp/unhidra_entropy.pipe

Start the entropy script:

    python3 src/entropy_pipe.py

The script will continually write single bytes into the pipe.

## Requirements

- Python 3
- OpenCV (opencv-python)
- NumPy
- A functional webcam

## Project Structure

- src/entropy_pipe.py – main entropy generator.
- src/modules/camera_capture.py – webcam helpers.
- src/modules/entropy_pool.py – entropy byte processing.

## Notes

The entropy method used here is very simple and meant only for experimentation.  
It is not a cryptographic-quality random number generator.

## License
