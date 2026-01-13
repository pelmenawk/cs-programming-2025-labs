from racevse import *

def create_char():
    global char
    char = Character()
    char.char_stats()
    char.show_stats(lvl,exp,req_exp)

req_exp = 5
exp = 0
lvl = 1
stat_point = 0


create_char()     
