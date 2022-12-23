from time import sleep

def _generate_list_of_neighboring_cells_from_active_cells_list(active_cells: list = []):
  """ Gera uma lista contendo as coordenadas de todas as células vizinhas a partir das células ativas passadas """
  neighboring_cells = []
  for active_cell in active_cells:
    neighboring_cells += _generate_neighboring_cells(active_cell=active_cell)
  return neighboring_cells

def _generate_neighboring_cells(active_cell: tuple):
  """ Gera lista de vizinhos a partir de uma única célula ativa """
  x, y = active_cell
  neighboring_cells = [
    (x - 1, y - 1),
    (x - 1, y),
    ( x - 1, y + 1),
    (x , y - 1),
    ( x , y + 1),
    ( x + 1, y - 1),
    ( x + 1, y),
    ( x + 1, y + 1)
  ]
  return neighboring_cells

def _count_occurrence_neighboring_cells(cells_list: list = []):
  """ Retorna um dicionario com a chave como célula, e valor como o número de vezes em que ela aparece """
  neighboring_cells_counted = {}
  for cell in cells_list:
    neighboring_cells_counted[cell] = neighboring_cells_counted.get(cell, 0) + 1
  return neighboring_cells_counted

def _cells_with_x_occurence(cells_occurence: dict = {}, target_occurence : int =  0):
  """ Retorna todas as células que tem uma quantidade de ocorrência passada como parametro da funcao """
  neighboring_cells_with_x_occurence = []
  for cell, occurence in cells_occurence.items():
    occurence == target_occurence and neighboring_cells_with_x_occurence.append(cell)
  return neighboring_cells_with_x_occurence

def _active_cells_with_two_actives_neighboring(active_cells: list = [], neighboring_cells_with_two_occurence: list = []):
  """ Retorna uma lista de células que estejam no conjunto de celulas ativas e no conjunto de células com duas ocorrências(o que indica duas vizinhas activas) """
  active_cells_with_two_actives_neighboring = [ cell for cell in neighboring_cells_with_two_occurence if cell in active_cells]
  return active_cells_with_two_actives_neighboring


def _generate_new_list_of_active_cells(initial_cells_active_list):
  """ Gera a lista de células ativas da próxima etapa a partir de uma lista inicial de células ativas"""
  next_active_cells = []
  neighboring_cells = _generate_list_of_neighboring_cells_from_active_cells_list(initial_cells_active_list)
  neighboring_cells_occurence = _count_occurrence_neighboring_cells(neighboring_cells)
  cells_with_three_active_neighboring = _cells_with_x_occurence(neighboring_cells_occurence, 3)
  cells_with_two_active_neighboring = _cells_with_x_occurence(neighboring_cells_occurence, 2)
  next_active_cells += cells_with_three_active_neighboring
  next_active_cells += _active_cells_with_two_actives_neighboring(initial_cells_active_list, cells_with_two_active_neighboring)
  return next_active_cells

def _print_matrix(active_cells):
  """ Imprime a matriz na tela. Verifica a menor  e maior coordenada x na lista de células, e a maior, e com isso imprime um matriz bonitnha """
  min_x = min(active_cells, key = lambda k: k[0])[0]
  max_x = max(active_cells, key = lambda k: k[0])[0]
  min_y = min(active_cells, key = lambda k: k[1])[1]
  max_y = max(active_cells, key = lambda k: k[1])[1]
  for x in range(min_x, max_x+1):
    print(f"{x:03d}", end=' ')
    for y in range(min_y, max_y + 3):
      print("\U00002B1C" if (x,y) in active_cells else "\U00002B1B", end='')
    print('')

def game_of_life(initial_active_cells: list = []):
  print("\nMatriz inicial")
  _print_matrix(initial_active_cells)
  print('\n')
  active_cells = initial_active_cells
  while True:
    active_cells = _generate_new_list_of_active_cells(active_cells)
    _print_matrix(active_cells=active_cells)
    print('')
    sleep(1)
    if not active_cells:
      break


if __name__ == '__main__':
  default_cells = [(1, 1), (2, 2), (2, 3), (3, 2), (2, 5), (-3, 5), (4, 4), (9,9), (10,10)]
  user_input = input("Insira uma lista de coordenadas cartesianas para começar a jogar. Tem de ser no formato (1,2),(3, 4), sem espaço entre as vírgulas de cada tupla (faça isso, estou com preguiça de te ajudar, usuário.) \t")
  try:
    user_input = user_input.split("),")
    user_input = [tuple(item) for item in user_input]
  except:
    print("\n\n\nVocê é maluco, cara ")
    sleep(3)
    user_input = default_cells
  game_of_life(default_cells)
