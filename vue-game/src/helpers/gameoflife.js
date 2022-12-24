export default {
  listaDeVizinhosDeUmaCelula(celula) {
    let x = celula[0], y = celula[1]
    let celulasVizinhas = [
    [x - 1, y - 1],
    [x - 1, y],
    [ x - 1, y + 1],
    [x , y - 1],
    [ x , y + 1],
    [ x + 1, y - 1],
    [ x + 1, y],
    [ x + 1, y + 1]
    ]
    return celulasVizinhas
  },
  listaDeVizinhosDeVariasCelulas(celulas) {
    let celulasAtivas = this.retiraDuplicatas(celulas)
    let vizinhos = []
    for (let celula of celulasAtivas) {
      vizinhos.push(...this.listaDeVizinhosDeUmaCelula(celula))
    }
    return vizinhos
  },
  contaOcorrenciaDeLista(listaDeListas, lista) {
    let ocorrencia = 0
    for (let array_ of listaDeListas) {
      if (array_[0] === lista[0] && array_[1] === lista[1]) {
        ocorrencia ++
      }
    }
    return ocorrencia
  },
  listaExisteEmUmaArrayDeListas(listaDeListas, lista) {
    for (let array_ of listaDeListas) {
      if (array_[0] == lista[0] && array_[1] == lista[1]) return true
    }
    return false
  },
  listasComXOcorrencias(listaDeCelulasVizinhas, x) {
    let _listasComXOcorrencias = []
    for (let lista of listaDeCelulasVizinhas) {
      let ocorrencia = this.contaOcorrenciaDeLista(listaDeCelulasVizinhas, lista)
      if (ocorrencia === x) _listasComXOcorrencias.push(lista)
    }
    return this.retiraDuplicatas(_listasComXOcorrencias)
  },
  retiraDuplicatas(listas) {
    let copiaLista = JSON.parse(JSON.stringify(listas))
    let novaLista = []
    for (let lista of copiaLista) {
      if (!this.listaExisteEmUmaArrayDeListas(novaLista, lista)) {
        novaLista.push(lista)
      }
    }
    return novaLista
  },
  geraNovaListaDeCelulasAtivas(celulasAtivasAnteriores) {
    let celulasVizinhas = this.listaDeVizinhosDeVariasCelulas(celulasAtivasAnteriores)
    let celulasComDuasVizinhasAtivas = this.listasComXOcorrencias(celulasVizinhas, 2)
    let celulasComTresVizinhasAtivas = this.listasComXOcorrencias(celulasVizinhas, 3)
    let celulasAtivasComDuasVizinhasAtivas = []
    for (let celula of celulasComDuasVizinhasAtivas) {
      if (this.listaExisteEmUmaArrayDeListas(celulasAtivasAnteriores, celula)) {
        celulasAtivasComDuasVizinhasAtivas.push(celula)
      }
    }
    return [...celulasAtivasComDuasVizinhasAtivas, ...celulasComTresVizinhasAtivas]
  }
  }
