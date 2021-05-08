print("Hello Adventurer")
name = input('How should I call you?:')
print("Welcome to the dungeon, " + name)
race = input("What is your race? 1)elf 2)human 3)orc 4)wiz:")
print(f"Thanks for that, {name} of race {race}")

rupees = 0
force = 0
magic  = 0 
weapon_type =  int(input("0)Mallet or 1)Sword?"))
rupees = 15 + 5*weapon_type
weapon_type = 1 - weapon_type 
force = 10 + weapon_type*10

magic_type =  int(input("0)water or 1)fire?"))
rupees = rupees + 20 + 15*magic_type
magic = 10 + magic_type*10

cooldown_type =  int(input("0)short or 1)long?"))
rupees =  rupees +  15 + 10*cooldown_type
force = force +  5 + 15*cooldown_type


print(f"fz {force} mg {magic}  pr {rupees} ")

"""
Comentario largo
Config. arma
                            -> FZ, MG, PR
1)fz espada   2) mazo  -> espada 10 fz, mazo 20 fz , espada 20Rps , mazo 15Rps
2)mg fuego   2) agua  -> fuego 20 mg, agua 10 mg , fuego 35Rps , agua 20Rps
3)cd long   2) short  -> long +15fz, short +5 fz , long 20Rps , short 10Rps

"""