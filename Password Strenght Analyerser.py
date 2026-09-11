def check(Passw):
    length_ok = len(Passw) >= 8
    uppercase_ok = False
    lowercase_ok = False
    number_ok = False
    special_ok = False
    satisfied=0
    for i in Passw:
        if i.isupper():
            uppercase_ok = True
        if i.islower():
            lowercase_ok=True
        if i.isdigit():
            number_ok=True
        if not i.isalnum():
            special_ok=True
    if length_ok:
        satisfied+=1
    if uppercase_ok:
        satisfied+=1
    if lowercase_ok:
        satisfied+=1
    if special_ok:
        satisfied+=1
    if number_ok:
        satisfied+=1
    if satisfied<=2:
        strenght="Weak"
    elif satisfied<=4:
        strenght="Medium"
    else:
        strenght="Strong"
    print("\n===== PASSWORD ANALYSIS =====")

    print("At least 8 characters:", length_ok)
    print("Contains uppercase letter:", uppercase_ok)
    print("Contains lowercase letter:", lowercase_ok)
    print("Contains a number:", number_ok)
    print("Contains special character:", special_ok)
    print("\nStrength:", strenght)
print("=======PASSWORD ANALYSER=======")
password=input("Enter the password here ")
print("Analysing the password 🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️")
check(password)

        
            