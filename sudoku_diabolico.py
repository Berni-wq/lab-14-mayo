""" sudoku diabolico MVR """
class SudokuSolver:
    def __init__(self):
        self.backtracks = 0

    def is_valid(self, board, r, c, val):
        """Verifica la validez en Fila, Columna y Sub-cuadrícula"""
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == val:
                    return False
        return True

    def get_next_cell_mrv(self, board):
        """Heurística MRV: Celda con menos opciones disponibles"""
        min_options = 10
        best_cell = None
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    options = sum(1 for val in range(1, 10) if self.is_valid(board, r, c, val))
                    if options < min_options:
                        min_options = options
                        best_cell = (r, c)
                    if min_options == 0: return (r, c)
        return best_cell

    def solve(self, board):
        cell = self.get_next_cell_mrv(board)
        if not cell:
            return True

        r, c = cell
        for val in range(1, 10):
            if self.is_valid(board, r, c, val):
                board[r][c] = val
                if self.solve(board):
                    return True
                board[r][c] = 0
                self.backtracks += 1 # Registro de retrocesos
        return False

def print_board(board):
    """Imprime el tablero con formato de cuadrícula"""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

# Tablero Diabólico (Estado Inicial)
tablero_inicial = [
    [0, 0, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0]
]

# Crear una copia para resolver
tablero_para_resolver = [row[:] for row in tablero_inicial]

print("=== TABLERO INICIAL (Pistas) ===")
print_board(tablero_inicial)

solver = SudokuSolver()
if solver.solve(tablero_para_resolver):
    print("\n=== TABLERO FINAL (Resuelto) ===")
    print_board(tablero_para_resolver)
    print(f"\nResultados del análisis:")
    print(f"- Heurística utilizada: MRV (Minimum Remaining Values)")
    print(f"- Total de retrocesos (backtracks): {solver.backtracks}")
else:
    print("\nNo se pudo resolver el tablero.")
