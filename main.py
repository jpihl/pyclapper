import threading
import clapper
import light


def main():

    my_light = light.Light()

    stopped = threading.Event()

    clapper_thread = threading.Thread(
        target=clapper, args=(stopped, lambda: my_light.toggle()))
    clapper_thread.start()

    my_light.run()

    stopped.set()
    clapper_thread.join()

if __name__ == '__main__':
    main()
