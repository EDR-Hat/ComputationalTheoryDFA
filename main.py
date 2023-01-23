from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def makeNFA():
    # NFA which matches strings beginning with 'a', ending with 'a', and containing
    # no consecutive 'b's
    nfa = NFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15'},
        input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
        transitions={
            # '1': {'q7'}, '1': {'q1'},
            'q0': {'0': {'q0', 'q7'}, '1': {'q1', 'q7'}, '2': {'q2', 'q7'}, '3': {'q3', 'q7'}, '4': {'q4', 'q7'},
                   '5': {'q5', 'q7'}, '6': {'q6', 'q7'}, '7': {'q0', 'q7'}, '8': {'q1', 'q7'}, '9': {'q2', 'q7'}},
            'q1': {'0': {'q3', 'q8'}, '1': {'q4', 'q8'}, '2': {'q5', 'q8'}, '3': {'q6', 'q8'}, '4': {'q0', 'q8'},
                   '5': {'q1', 'q8'}, '6': {'q2', 'q8'}, '7': {'q3', 'q8'}, '8': {'q4', 'q8'}, '9': {'q5', 'q8'}},
            'q2': {'0': {'q6', 'q9'}, '1': {'q0', 'q9'}, '2': {'q1', 'q9'}, '3': {'q2', 'q9'}, '4': {'q3', 'q9'},
                   '5': {'q4', 'q9'}, '6': {'q5', 'q9'}, '7': {'q6', 'q9'}, '8': {'q0', 'q9'}, '9': {'q1', 'q9'}},
            'q3': {'0': {'q2', 'q10'}, '1': {'q3', 'q10'}, '2': {'q4', 'q10'}, '3': {'q5', 'q10'}, '4': {'q6', 'q10'},
                   '5': {'q0', 'q10'}, '6': {'q1', 'q10'}, '7': {'q2', 'q10'}, '8': {'q3', 'q10'}, '9': {'q4', 'q10'}},
            'q4': {'0': {'q5', 'q11'}, '1': {'q6', 'q11'}, '2': {'q0', 'q11'}, '3': {'q1', 'q11'}, '4': {'q2', 'q11'},
                   '5': {'q3', 'q11'}, '6': {'q4', 'q11'}, '7': {'q5', 'q11'}, '8': {'q6', 'q11'}, '9': {'q0', 'q11'}},
            'q5': {'0': {'q1', 'q12'}, '1': {'q2', 'q12'}, '2': {'q3', 'q12'}, '3': {'q4', 'q12'}, '4': {'q5', 'q12'},
                   '5': {'q6', 'q12'}, '6': {'q0', 'q12'}, '7': {'q1', 'q12'}, '8': {'q2', 'q12'}, '9': {'q3', 'q12'}},
            'q6': {'0': {'q4', 'q13'}, '1': {'q5', 'q13'}, '2': {'q6', 'q13'}, '3': {'q0', 'q13'}, '4': {'q1', 'q13'},
                   '5': {'q2', 'q13'}, '6': {'q3', 'q13'}, '7': {'q4', 'q13'}, '8': {'q5', 'q13'}, '9': {'q6', 'q13'}},
            'q7': {'0': {'q7'}, '1': {'q8'}, '2': {'q9'}, '3': {'q10'}, '4': {'q11'}, '5': {'q12'}, '6': {'q13'},
                   '7': {'q7'}, '8': {'q8'}, '9': {'q9'}},
            'q8': {'0': {'q10'}, '1': {'q11'}, '2': {'q12'}, '3': {'q13'}, '4': {'q7'}, '5': {'q8'}, '6': {'q9'},
                   '7': {'q10'}, '8': {'q11'}, '9': {'q12'}},
            'q9': {'0': {'q13'}, '1': {'q7'}, '2': {'q8'}, '3': {'q9'}, '4': {'q10'}, '5': {'q11'}, '6': {'q12'},
                   '7': {'q13'}, '8': {'q7'}, '9': {'q8'}},
            'q10': {'0': {'q9'}, '1': {'q10'}, '2': {'q11'}, '3': {'q12'}, '4': {'q13'}, '5': {'q7'}, '6': {'q8'},
                    '7': {'q9'}, '8': {'q10'}, '9': {'q11'}},
            'q11': {'0': {'q12'}, '1': {'q13'}, '2': {'q7'}, '3': {'q8'}, '4': {'q9'}, '5': {'q10'}, '6': {'q11'},
                    '7': {'q12'}, '8': {'q13'}, '9': {'q7'}},
            'q12': {'0': {'q8'}, '1': {'q9'}, '2': {'q10'}, '3': {'q11'}, '4': {'q12'}, '5': {'q13'}, '6': {'q7'},
                    '7': {'q8'}, '8': {'q9'}, '9': {'q10'}},
            'q13': {'0': {'q11'}, '1': {'q12'}, '2': {'q13'}, '3': {'q7'}, '4': {'q8'}, '5': {'q9'}, '6': {'q10'},
                    '7': {'q11'}, '8': {'q12'}, '9': {'q13'}},
            'q14': {'1': {'q1', 'q15'}, '2': {'q2', 'q15'}, '3': {'q3', 'q15'}, '4': {'q4', 'q15'}, '5': {'q5', 'q15'},
                    '6': {'q6', 'q15'}, '7': {'q0', 'q15'}, '8': {'q1', 'q15'}, '9': {'q2', 'q15'}},
            'q15': {'0': {'q7'}, '1': {'q8'}, '2': {'q9'}, '3': {'q10'}, '4': {'q11'}, '5': {'q12'}, '6': {'q13'},
                    '7': {'q7'}, '8': {'q8'}, '9': {'q9'}},

        },
        initial_state='q14',
        final_states={'q0', 'q7'}
    )

    return nfa

def calcRelate(dfa, n):
  max_state = len(dfa.states)
  curr = [0] * max_state
  dfa_states = list(dfa.states)

  #Setting the values of curr, or the base case column in our transition table
  for (i, state) in enumerate(dfa_states):
    if str(state) in list(dfa.final_states):
      curr[i] = 1

  nex = [0] * len(dfa.states)

  #Same concept as our project1 part1, creating a transition table of length n 2 columns at a time
  while (n > 0):
    for (i, state) in enumerate(dfa.states):
      for j in range(10):
        nex[i] += curr[dfa_states.index(dfa.transitions[state][str(j)])]
    curr = nex
    nex = [0] * max_state
    n -= 1
  return curr[dfa_states.index(dfa.initial_state)]  # use nex since both were flipped

def main():
    userInput = input("Please enter a string length or quit to exit: ")
    while userInput != "quit":
        dfa = DFA.from_nfa(makeNFA())
        dfa = dfa.minify()
        print(calcRelate(dfa, int(userInput)))
        userInput = input("Please enter a string length: ")

    print("Exiting!...")


main()



def transitionsWithKleen(q, k, off):
    """Creates the  original copy of the DFA, in which we have to clean star from state i of the original copy to state i to the second DFA
      Args:
          q (int): The state we to get the transitions for
          k (k): The state we want to klean star over into. Add klean star transitions from State i of the original
                 to state i of the second copy.
          off (bool):  (Offset) is False if we we are in the first DFA (i.e because states are 0-7),
                       and True if were in the second DFA (i.e because states are 7-15).
      Returns:
          delta (dict): Returns a dictionary of transitions we will use to make our NFA in
                        automata lib.
      """
    for e in range(10):
        n = int(q) % 7
        n = str(n) + str(e)
        n = int(n) % 7
        if bool(off):
            n += 7
        print(f"'{e}': ", end='')
        print("{", end='')
        print(f"'q{n}', 'q{k}'", end='')
        print("}", end='')
        if e != 9:
            print(", ", end='')

def transitionsWithoutKleen(q, off):
    for e in range(10):
        n = int(q) % 7
        n = str(n) + str(e)
        n = int(n) % 7
        if bool(off):
            n += 7
        print(f"'{e}': ", end='')
        print("{", end='')
        print(f"'q{n}'", end='')
        print("}", end='')
        if e != 9:
            print(", ", end='')

def calcTransitions():
    kleen = True
    for i in range(14):
        if i > 6:
            kleen = False
        print(f"'q{i}': ", end='')
        print("{", end='')
        if bool(kleen):
            transitionsWithKleen(i, i + 7, False)
        else:
            transitionsWithoutKleen(i, True)
        print("},")






