import PySimpleGUI as sg
import requests
import pokeapi
from random import randint
index = 1
def setIndex(i):
    global index
    index = i
def getPrev():
    global index
    if index > 1:
        index = index-1
    else:
        setIndex(891)
    return index
def getNext():
    global index
    if index < 891:
        index = index+1
    else:
        setIndex(1)
    return index
def scan_nome():
    layout = [[sg.Text("Insira o nome ou Id do pokemon")],
            [sg.Input()],
            [sg.Button("OK")]
        ]
    window = sg.Window("pokedex", layout)

    event, values = window.read()
    window.close()
    return values[0]
def pop_up(info):
    sg.popup(f"Nome: {info['nome']}\nId: {info['id']}\nPeso: {info['peso']}\nAltura: {info['altura']}")
def saida(nome,id,url,ataque,vida,defesa): 
    response = requests.get(url, stream=True)
    response.raw.decode_content = True
    img = sg.Image(data=response.raw.read(), size=(300,150),pad=(10,0))
    layout = [
        [sg.Text("MyPokedex",justification='center',size=(100,1), font=("Roboto, 30"),text_color='#FFF',background_color='#FA0303')],
        [sg.Text(f"Nome: {nome}", justification=('left'), size=(20,1), font=("Roboto, 16"),text_color='#FFF',background_color='#FA0303'), sg.Text(f"ID: {id}", justification=('right'), size=(20,1), font=("Roboto, 16"),text_color='#FFF',background_color='#FA0303')],
        [img],
        [sg.Text("Buscar", size=(100,1),pad=(0,(10,0)), justification='center',font=("Roboto,16"),text_color='#FFF',background_color='#FA0303')],
        [sg.Input(size=(15,1),pad=((90,5),0),background_color=('#FFF')), sg.Button("OK", size=(3,1),button_color=('#000'), key='busca')],
        [sg.Text(f"Ataque: {ataque}",size=(15,2),justification='center', pad=(90,0),background_color=('#FFF'),text_color='#000',font='Roboto,16')],
        [sg.Text(f"HP: {vida}",size=(15,2),justification='center', pad=(90,0),background_color=('#FFF'),text_color='#000',font='Roboto,16')],
        [sg.Text(f"Defesa: {defesa}",size=(15,2), justification='center',pad=(90,0),background_color=('#FFF'),text_color='#000',font='Roboto,16')],
        [sg.Button('Anterior',pad=(30,20),button_color='Black', key='anterior'), sg.Button('Random',pad=(20,20),button_color='Black',key='random'), sg.Button('Próximo',pad=(30,20),button_color='Black',key='proximo')]
    ]
    window = sg.Window("MyPokedex", layout, size=(350, 500), background_color='#FA0303',grab_anywhere=True)
    sg.Image(size=(200,200))
    event, values = window.read()
    if event == "busca":
        setIndex(int(values[1]))
        window.close()
        pokeapi.buscar(values[1])
    if event == "anterior":
        window.close()
        pokeapi.buscar(getPrev())
    if event == "proximo":
        window.close()
        pokeapi.buscar(getNext())
    if event == "random":
        window.close()
        aux = randint(1,891)
        setIndex(aux)
        pokeapi.buscar(aux)
    window.close()
