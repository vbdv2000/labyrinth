# Un movimiento es válido cuando la posición de la fila y columna es mayor o igual a 0 y menor que el número máximo
# en 3x3, serían válidas desde la 0,0 hasta la 2,2 siempre que haya un .
def is_valid_move(row, col, labyrinth):
    rows = len(labyrinth)
    cols = len(labyrinth[0])
    if 0 <= row < rows and 0 <= col < cols and labyrinth[row][col] == ".":
        return True
    return False

# Se puede rotar el rod, asumiendo derecha y abajo de posibles movimientos, 
# cuando el cuadro de 3x3 está libre desde el centro en el que estás,es decir,
# todas las posiciones son válidas
def can_rotate(row, col, direction, labyrinth):
    directions = [(0, 1), (1, 0)]  # Right, Down
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if not is_valid_move(i, j, labyrinth):
                return False
    return True

# Rota el rod si está horizontal y lo pasa a vertical o viceversa
def rotate(row, col, direction, labyrinth):
    if direction == 0:  # Horizontal
        if is_valid_move(row - 1, col, labyrinth) and is_valid_move(row + 1, col, labyrinth):
            return row, col, 1
    else:  # Vertical
        if is_valid_move(row, col - 1, labyrinth) and is_valid_move(row, col + 1, labyrinth):
            return row, col, 0
    return row, col, direction

def solution(labyrinth):
    rows = len(labyrinth)
    cols = len(labyrinth[0])
    directions = [(0, 1), (1, 0)]  # Right, Down
    queue = [(0, 1, 0, 0)]  # (row, col, direction, steps)
    visited = set([(0, 0, 0)])  # (row, col, direction)
    while queue:
        row, col, direction, steps = queue.pop(0)
        direction = 0
        print("Current position:", row, col)
        print("Current direction:", direction)
        print("Steps:", steps)

        if row == rows - 1 and col + 1 == cols - 1:
            return steps

        new_row = row + directions[direction][0]
        new_col = col + directions[direction][1]

        if new_col == cols - 1 and is_valid_move(row + 1, col, labyrinth): # baja cuando la siguiente columna sea la última
            direction = 1
            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]
            
        if is_valid_move(new_row, new_col, labyrinth) and (new_row, new_col, direction) not in visited:
            queue.append((new_row, new_col, direction, steps + 1))
            visited.add((new_row, new_col, direction))
            print("Move in current direction")

        if can_rotate(row, col, direction, labyrinth):
            print("Can rotate == true")
            new_row, new_col, new_direction = rotate(row, col, direction, labyrinth)
            if (new_row, new_col, new_direction) not in visited:
                queue.append((new_row, new_col, new_direction, steps + 2)) # Se le suman 2 pasos, uno de rotar y otro de mover
                visited.add((new_row, new_col, new_direction))
                print("Rotate the rod")

    return -1  # No se puede

def main():
    
    labyrinth1 = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["#", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", ".", ".", "#", "."],
        [".", "#", ".", ".", ".", ".", ".", "#", "."]
    ]
    result1 = solution(labyrinth1)
    print("Result 1:", result1)

    labyrinth2 = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["#", ".", ".", ".", "#", ".", ".", "#", "."],
        [".", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", ".", ".", "#", "."],
        [".", "#", ".", ".", ".", ".", ".", "#", "."]
    ]
    result2 = solution(labyrinth2)
    print("Result 2:", result2)

    labyrinth3 = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]
    result3 = solution(labyrinth3)
    print("Result 3:", result3)

    labyrinth4 = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
        [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    result4 = solution(labyrinth4)
    print("Result 4:", result4)

    

if __name__ == "__main__":
    main()
