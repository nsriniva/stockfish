import cppyy
cppyy.include('./main.hpp')
cppyy.load_library('libstockfish.so')

from cppyy.gbl import engine_info, UCI, Tune, PSQT, Bitboards, \
    Position, Bitbases, Endgames, Threads, Search, Options, std, \
    StateListPtr, StateInfo


class Stockfish(object):

    pos : Position
    states : StateListPtr
    token : str
    cmd : str

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

        for i in Options:
            print(i[0], i[1].__float__())

        self.pos = Position()
        self.states = StateListPtr(std.deque(StateInfo)(1))
        self.token = str()
        self.cmd = str()

        print(self.pos, self.states, self.token, self.cmd)
        
    def __del__(self):
        Threads.set(0)

    def position(self):
        pass


Stockfish()
