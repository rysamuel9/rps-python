import random

print("================")
print(
"""0 = Batu
1 = Kertas
2 = Gunting""")


batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameIcon = [batu, kertas, gunting]

userPilih = int(input("Pilihan user: "))
print(gameIcon[userPilih])

comPilih = random.randint(0, 2)
print("Pilihan komputer: {}".format(comPilih))
print(gameIcon[comPilih])


if userPilih >= 3 or userPilih < 0:
    print("Invalid nomor, kamu kalah!")
elif userPilih == 0 and comPilih == 2:
    print("Kamu menang!")
elif comPilih == 0 and userPilih == 2:
    print("Kamu kalah!")
elif comPilih > userPilih:
    print("Kamu kalah!")
elif userPilih > comPilih:
    print("Kamu menang!")
elif comPilih == comPilih:
    print("Draw!")
