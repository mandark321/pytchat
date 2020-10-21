
import queue


class Buffer(queue.Queue):
    '''
    A FIFO queue that acts as a buffer to store chat data

    Parameter
    ---------
    max_size : int
        Maximum number of chat blocks to store. Infinite if 0. 
        If the maximum value is exceeded, the old chat block will be discarded.
    '''

    def __init__(self, maxsize=0):
        super().__init__(maxsize=maxsize)

    def put(self, item):
        if item is None:
            return
        if super().full():
            super().get_nowait()
        else:
            super().put(item)

    def put_nowait(self, item):
        if item is None:
            return
        if super().full():
            super().get_nowait()
        else:
            super().put_nowait(item)

    def get(self):
        ret = []
        ret.append(super().get())
        while not super().empty():
            ret.append(super().get())
        return ret
