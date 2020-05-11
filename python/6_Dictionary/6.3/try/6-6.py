favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
staff = ['jen','sarah']
for name in favorite_language.keys():
    if name in staff:
        print("Thanks " + name.title() + ".")
    else:
        print(name.title() + " We invite you to participate in our survey.")