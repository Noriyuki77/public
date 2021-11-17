import random
players = []

GOO = 0
CHK = 1
PAA = 2
player_number = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = None

def create_player():
    global player_number
    player_number = 5
    for i in range(0,player_number):
        players.append(Player(f"PLAYER{i+1}"))

def select_hand():
    for i in range(0,player_number):
        players[i].hand = random.randint(0,2)

def show_hand():
    janken = ['グー', 'チョキ', 'パー']
    for i in range(0,player_number):
        print(f"{players[i].name}の選んだ手：{janken[players[i].hand]}")

def jadgement():
    global player_number
    jadge_list = []

    for i in range(0,player_number):
        jadge_list.append(players[i].hand)

    jadge = set(jadge_list)
    print(f"選んだ手の種類（SET）:{jadge}")
    print(f"プレーヤーの選んだ手（LIST）:{jadge_list}")
    
    if len(jadge) == 1 or len(jadge) == 3:
        print("あいこ")
        play_game()
    else:
        if GOO in jadge and CHK in jadge:
            if jadge_list.count(GOO) == 1:
                #return jadge_list.index(GOO)
                print(f"勝ったプレーヤー：{players[jadge_list.index(GOO)].name}")
            else:
                for i in reversed(range(0,player_number)):
                    if jadge_list[i] == CHK:
                        print(f"負けたプレーヤー:{players[i].name}")
                        del players[i]
                        player_number -= 1
                play_game()
        elif CHK in jadge and PAA in jadge:
            if jadge_list.count(CHK) == 1:
                #return jadge_list.index(CHK)
                print(f"勝ったプレーヤー：{players[jadge_list.index(CHK)].name}")
            else:
                for i in reversed(range(0,player_number)):
                    if jadge_list[i] == PAA:
                        print(f"負けたプレーヤー:{players[i].name}")
                        del players[i]
                        player_number -= 1
                play_game()
        elif PAA in jadge and GOO in jadge:
            if jadge_list.count(PAA) == 1:
                #return jadge_list.index(PAA)
                print(f"勝ったプレーヤー：{players[jadge_list.index(PAA)].name}")
            else:
                for i in reversed(range(0,player_number)):
                    if jadge_list[i] == GOO:
                        print(f"負けたプレーヤー:{players[i].name}")
                        del players[i]
                        player_number -= 1
                play_game()

def play_game():
    print("---------------------------")
    print(f"{player_number}人じゃんけん")
    select_hand()
    show_hand()
    jadgement()
 
create_player()
play_game()