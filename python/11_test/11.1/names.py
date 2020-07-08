from name_function import get_formatted_name

print("enter 'q' at any time to quit.")
while True:
    first = input("\nfirst name is:")
    if first == 'q':
        break

    last = input("\nlast name is:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last) # return full_name.title()
    print("\tNeatly formatted name: " + formatted_name + '.')

    