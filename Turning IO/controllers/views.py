#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import *
import json
import base64

"""
Elaborado por: Fredy Flores Merodio
"""

winMatrix = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def tictactoe(request):
    context = {}
    return render(request, 'gameTictactoe.html', context)

def sendPlay(request, index, player, board, shoot):
    data = dict()
    data = set(index, player, board, shoot)
    return HttpResponse('response = ' + json.dumps(data), mimetype="application/json")

def set(index, player, board, shoot):
    index = int(index)
    player = True if player == 'true' else False
    shoot = int(shoot)
    board = board + '=='
    board = json.loads(base64.b64decode(board).decode('utf-8'))
    res = dict()

    if player == True:
        board[index] = shoot
    else:
        indexAI = turno_ai(board, shoot)
        board[indexAI] = shoot
        res['indexAI'] = indexAI
    game    = True
    ganador = shoot if player == True else 'Computer'
    msg     = 'Following !'
    nextTurno = 2 if shoot == 1 else 1
    nextTurno = 'Player turn ' + str(nextTurno) + '.'
    isWin = checkWin(board, shoot)
    if isWin or checkFull(board):
        game    = False
        nextTurno   = 'Game Over !'
        msg = 'Player ' + str(ganador) + ', is the Winner !' if isWin else 'Game without a Winner !'
    res['state_game']          = game
    res['msg_game']            = msg
    res['next_turn_player']    = nextTurno
    return res
    
def checkWin(board, shoot):
    for x in range(0, 8):
        win = True
        for y in range(0, 3):
            if board[winMatrix[x][y]] != shoot:
                win = False
                break
        if win: return True
    return False
  
def checkFull(board):
    for x in range(0, 8):
        if board[x] == 0:
            return False
    return True

def turno_ai(board, shoot):
    newboard = board
    # Verifica algun tiro ganador
    for x in range(0, 9):
        if newboard[x] == 0:
            newboard[x] = shoot
            if checkWin(newboard, shoot):
                return x
            else:
                newboard[x] = 0
    # Tira una opcion
    for y in range(0, 9):
        if board[y] == 0:
            return y

