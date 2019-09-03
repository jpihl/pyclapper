#!/usr/bin/env python

# Copyright (c) 2019 Jeppe Pihl
# All Rights Reserved
#
# Distributed under the "BSD License". See the accompanying LICENSE file.
import threading
import clapper
import light


def main():

    my_light = light.Light()

    stopped = threading.Event()

    clapper_thread = threading.Thread(
        target=clapper.clapper, args=(stopped, lambda: my_light.toggle()))
    clapper_thread.start()

    my_light.run()

    stopped.set()
    clapper_thread.join()

if __name__ == '__main__':
    main()
