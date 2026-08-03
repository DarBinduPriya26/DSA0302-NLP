transition = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}

initial_state = 'q0'
final_states = ['q2']

def simulate_dfa(input_string):
    current_state = initial_state
    path = [current_state]

    for symbol in input_string:
        if symbol not in ['a', 'b']:
            print("Invalid Input Symbol")
            return

        current_state = transition[(current_state, symbol)]
        path.append(current_state)

    print("\nTransition Path:")
    print(" → ".join(path))

    if current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")

string = input("Enter Input String: ")
simulate_dfa(string)
