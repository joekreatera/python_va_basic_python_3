# BattleForMiddleEarth
 battle for middle earth with orcs and elves

 Battle for middle earth: In this program, Orcs and Elves will have to fight. Orcs and Elves are CREATURES of the Middle Earth, and they should be modeled as such. Trolls are around and can EAT any CREATURE in Middle Earth.

 Orcs and Elves start around a 100x100 unit grid (logically) in which they can  get together and start walking as a horde.  Two Creatures cannot be occupying the same place at the same time, so, when moving, be careful that the position the creature is heading to, does not have another creature already.

 To determine if orcs or Elves can make a horde, the distance between them must be 5. Once they are a horde, advancing is slower (average of all speeds) and the future position must be in function of the centroid (average of their X's and Y's separately).  

 If an Orc and an Elf meet in Middle Earth, they will start a fight. If two hordes meet each other, one orc will stand against one elf. If there are more creatures on one side, one of the guys on the other side will die. If the struggle is 3 against 1, the 1 will die. Any other case is left to interpretation by developer.

 To fight, each creature has a combination of strength and magic. Elves have multiply-by-2 on magic and orcs have a multiply-by-3 on strength. These specs are determined upon creature birth (instantiation) and are random according to the following table:

 Orc: Strength[50-140] Magic[1-10] [ready]
 
 Elf: Strength[20-50] Magic[60-120] [ready]

 These can be modified if anything of the next events happen:
 
 Orc finds Weapon : strength +30 [ready]
 
 Orc finds Amulet: destroys Amulet [ready]
 
 Elf finds Weapon: strength + 10 [ready]
  
 Elf finds Amulet : magic +40 [ready]

 There are at least 4 Weapons and 4 Amulets randomly put on the grid.
 
 In the fights is possible that both creatures die. The damage they receive is according to the following formula:
 
 DamageDoneByOrc = Strength*0.7+Magic*0.3 (considering any updates of amulets and weapons)
 
 DamageDoneByElfs = Strength*0.2+Magic*0.8 (considering any updates of amulets and weapons)
 

 The max life of each creature is according to:
 
 ORC: 1000-2500
 
 ELF: 1500-2000
 

 There are some special HEALERS: items that will recover 50% of life.
 
 The damage done by a creature to the other creature, unless they find a HEALER, will not recover.

 The game will end when there's no more creatures of one side.

 Is important to note that when there is a horde, the move is going to be towards the nearest single enemy. When a creature is not in a horde, it moves randomly changing its direction vector each 5 days or when it has found the world's end. If there are just hordes missing, they will follow the nearest one.



Project extra for Honors:

- Las hordas deben perseguir otras hordas y creaturas, prefiriendo estas ultimas. 
- El juego debe durar mientras haya vivos de los dos lados

o

- Hacerlo gráfico (console) utilizando *(elfos) °(orcos) %(trolls) @(items) 
 
