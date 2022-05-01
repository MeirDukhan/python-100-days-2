# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
T_times_n1 = (name1.lower()).count('t')
R_times_n1 = (name1.lower()).count('r')
U_times_n1 = (name1.lower()).count('u')
E_times_n1 = (name1.lower()).count('e')
#print("T occurs f'{(name1.lower()).count('t')}' times")
print(f"T occurs {T_times_n1} times")
print(f"R occurs {R_times_n1} times")
print(f"U occurs {U_times_n1} times")
print(f"E occurs {E_times_n1} times")

L_times_n2 = (name2.lower()).count('l')
O_times_n2 = (name2.lower()).count('o')
V_times_n2 = (name2.lower()).count('v')
E_times_n2 = (name2.lower()).count('e')
#print("T occurs f'{(name1.lower()).count('t')}' times")
print(f"L occurs {L_times_n2} times")
print(f"O occurs {O_times_n2} times")
print(f"V occurs {V_times_n2} times")
print(f"E occurs {E_times_n2} times")
true_total = T_times_n1 + R_times_n1 + U_times_n1 + E_times_n1
love_total = L_times_n2 + O_times_n2 + V_times_n2 + E_times_n2
print(f"Score: {true_total}{love_total}%")
score = true_total * 10 + love_total
if score <= 10 or score >= 90:
  print(f"Your score is **{score} %**, you go together like coke and mentos.")

if score >= 40 and score <= 50:
  print(f"Your score is **{score} %**, you are alright together.")
  
