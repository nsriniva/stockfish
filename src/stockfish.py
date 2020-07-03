from io import StringIO
import cppyy

def replace_getstr(klass, name):
    try:
        klass.__str__ = klass.__dict__['get_str']
    except KeyError:
        pass

cppyy.py.add_pythonization(replace_getstr, 'UCI')

cppyy.include('./main.hpp')
cppyy.load_library('libstockfish.so')

from cppyy.gbl import engine_info, UCI, Tune, PSQT, Bitboards, \
    Position, Bitbases, Endgames, Threads, Search, Options, std, \
    StateListPtr, StateInfo
from cppyy.gbl.UCI import Option


class Stockfish(object):

    def __init__(self):
        UCI.init(Options)
        Tune.init()
        PSQT.init()
        Bitboards.init()
        Position.init()
        Bitbases.init()
        Endgames.init()
        Threads.set(int(Options['Threads'].__float__()))
        Search.clear()

        UCI.loop_init()

        for name,val in Options:
            print(name, val)

        
    def __del__(self):
        Threads.set(0)

    def position(self, cmd):
        UCI.loop_next('position '+cmd)

    def go(self, cmd):
        UCI.loop_next('go '+cmd)

    def cmd(self, cmd__):
        UCI.loop_next(cmd__)


print('-----------Starting Stockfish--------------------')
s = Stockfish()
print('-----------Position Stockfish-----------------')
s.position('fen rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print('-----------Go Stockfish-----------------------')
s.go('perft 1')
print('-----------Terminate Stockfish----------------')
del s
print('-----------Stockfish Terminated---------------')

