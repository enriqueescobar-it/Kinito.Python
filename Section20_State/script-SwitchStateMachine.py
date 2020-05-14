from Section20_State.SwitchStateMachine.StateEnum import StateEnum

if __name__ == '__main__':
    code = '1234'
    state = StateEnum.LOCKED
    entry = ''

    while True:
        if state == StateEnum.LOCKED:
            entry += input(entry)

            if entry == code:
                state = StateEnum.UNLOCKED

            if not code.startswith(entry):
                # the code is wrong
                state = StateEnum.FAILED
        elif state == StateEnum.FAILED:
            print('\nFAILED')
            entry = ''
            state = StateEnum.LOCKED
        elif state == StateEnum.UNLOCKED:
            print('\nUNLOCKED')
            break
