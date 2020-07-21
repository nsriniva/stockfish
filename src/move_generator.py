from stockfish import UCI, Stockfish

s = Stockfish()

for i in range(1000000):
    print(f'Iteration {i}')
    s.position('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

    for m in s.legal_moves():
        print(UCI.move(m.move, s.is_chess960()), end=' ')

    print(s.legal_moves_str(), end=' ')

