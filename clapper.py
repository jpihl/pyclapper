import time
import array
import pyaudio

CHUNK_SIZE = 1024
MIN_VOLUME = 10000


def clapper(stopped, clap_callback):
    stream = pyaudio.PyAudio().open(
        format=pyaudio.paInt16,
        channels=2,
        rate=44100,
        input=True,
        frames_per_buffer=1024)

    last = 0
    while True:
        if stopped.wait(timeout=0):
            break
        chunk = array.array('h', stream.read(CHUNK_SIZE))
        volume = max(chunk)
        if volume >= MIN_VOLUME:
            now = time.time()
            diff = now - last
            if diff > 0.2 and diff < 1.0:
                clap_callback()
            last = now
