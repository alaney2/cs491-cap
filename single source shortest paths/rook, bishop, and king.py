r1, c1, r2, c2 = map(int, input().split())

rook_moves = 0
bishop_moves = 0
king_moves = 0

if r1 == r2 and c1 == c2:
  print(rook_moves, bishop_moves, king_moves)
  
if r1 == r2 or c1 == c2:
  rook_moves = 1
else:
  rook_moves = 2
  
if (r1 + c1) % 2 != (r2 + c2) % 2:
  bishop_moves = 0
else:
  if abs(r1 - r2) == abs(c1 - c2):
    bishop_moves = 1
  else:
    bishop_moves = 2
    
king_moves = max(abs(r1 - r2), abs(c1 - c2))

print(rook_moves, bishop_moves, king_moves)