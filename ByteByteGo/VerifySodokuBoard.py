from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                continue
            
            if num in rows[r]:
                return False
            rows[r].add(num)

            if num in cols[c]:
                return False
            cols[c].add(num)

            subgrid_r, subgrid_c = r // 3, c // 3
            if num in subgrids[subgrid_r][subgrid_c]:
                return False
            subgrids[subgrid_r][subgrid_c].add(num)

    return True
