import requests
import pysimple_input as ps
def getStats(stats):
    aux = []
    for item in stats:
        if item['stat']['name'] == "hp" or item['stat']['name'] == "attack" or item['stat']['name'] == "defense":
            aux.append(item['base_stat'])
    retorno = {"hp": aux[0], "ataque":aux[1], "defesa": aux[2]}
    return retorno
def getMoves(moves):
    retorno = []
    for mov in moves:
        retorno.append(mov["move"]["name"])
    return retorno
def getTypes(types):
    return (types[0]['type']["name"])
def getAbilities(abilities):
    retorno = []
    for ab in abilities:
        retorno.append(ab["ability"]["name"])
    return retorno
def getImg(sprites):
    return sprites["front_default"] 
def getDados(pokemon):
    dados = {"nome":pokemon["name"], "tipo":getTypes(pokemon["types"]), "habilidades":getAbilities(pokemon["abilities"]), "movimentos":getMoves(pokemon["moves"]), "altura":pokemon["height"], "peso":pokemon["weight"], "id":pokemon["id"], "img":getImg(pokemon['sprites']), "stats": getStats(pokemon["stats"])}
    return dados
def weightInfo():
    x = input("quantos pokemons deseja ver?\n") 
    for i in range(1,x):
            api = f"https://pokeapi.co/api/v2/pokemon/{i}"
            pokemon = (requests.get(api)).json()
            info = getDados(pokemon)
            nome = info["nome"]
            peso = info["peso"]
            print(f"\npeso dos pokemon {i} de 20:\n{nome} : {peso}")
def buscar(poke): 
    api = f"https://pokeapi.co/api/v2/pokemon/{poke}"
    pokemon = (requests.get(api)).json()
    info = getDados(pokemon)
    ps.saida(info['nome'], info['id'], info["img"],info["stats"]["ataque"], info["stats"]["hp"],info["stats"]["defesa"])
def main():
    buscar(1)
if __name__ == "__main__":
    main()

   