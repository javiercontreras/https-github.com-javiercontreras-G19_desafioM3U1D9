from string import ascii_lowercase

password = str(input("Ingrese un password : ")).lower()



uncripted_pass = []
count = 0
for num in range(len(password)):
    for letter in ascii_lowercase:
        count += 1
        if password[num] == letter:
            uncripted_pass += letter
            break

print(f"La constrasena fue forzada {count} veces")
print(uncripted_pass)