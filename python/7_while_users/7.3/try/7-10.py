# 加input才能获取用户输入，不要想当然的认为能获取用户输入，要加input！！！

resort = {}

mark = True

while mark:
    name = input("What is your name? ") # 加input才能获取用户输入
    resort_0 = input("If you could visit one place in the would,where would you go? ")

    resort[name] = resort_0

    repeat =input("Any more users to questionnaire(yes/no)? ") # 加input才能获取用户输入
    if repeat == 'no':
        mark = False
    
print("\n--- Findings ---")
for name,resonse in resort.items():
    print(name + " would go to the " + resonse + ".")