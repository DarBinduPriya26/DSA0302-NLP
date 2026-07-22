def check_string(text):
    state = "q0"

    for ch in text:
        if state == "q0":
            if ch == 'a':
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if ch == 'b':
                state = "q2"
            elif ch == 'a':
                state = "q1"
            else:
                state = "q0"

        elif state == "q2":
            if ch == 'a':
                state = "q1"
            else:
                state = "q0"

    if state == "q2":
        return True
    else:
        return False


string = input("Enter a string: ")

if check_string(string):
    print("Accepted: String ends with 'ab'")
else:
    print("Rejected: String does not end with 'ab'")