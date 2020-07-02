import cppyy
cppyy.include('./main.hpp')
cppyy.load_library('libstockfish.so')

from cppyy.gbl import engine_info, UCI, Tune, PSQT, Bitboards, \
    Position, Bitbases, Endgames, Threads, Search, Options


class Stockfish(object):

    def __init__(self):
        UCI.init(Options)
        Tune.init()
        PSQT.init()
        Bitboards.init()
        Position.init()
        Bitbases.init()
        Endgames.init()
        Threads.set(int(Options['Threads']).__float__())
        Search.clear()


    def __del__(self):
        Threads.set(0)
