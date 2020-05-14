from Section20_State.StateMachine.StateEnum import StateEnum
from Section20_State.StateMachine.TriggerEnum import TriggerEnum

if __name__ == '__main__':
    rules = {
        StateEnum.OFF_HOOK: [
            (TriggerEnum.CALL_DIALED, StateEnum.CONNECTING)
        ],
        StateEnum.CONNECTING: [
            (TriggerEnum.HUNG_UP, StateEnum.ON_HOOK),
            (TriggerEnum.CALL_CONNECTED, StateEnum.CONNECTED)
        ],
        StateEnum.CONNECTED: [
            (TriggerEnum.LEFT_MESSAGE, StateEnum.ON_HOOK),
            (TriggerEnum.HUNG_UP, StateEnum.ON_HOOK),
            (TriggerEnum.PLACED_ON_HOLD, StateEnum.ON_HOLD)
        ],
        StateEnum.ON_HOLD: [
            (TriggerEnum.TAKEN_OFF_HOLD, StateEnum.CONNECTED),
            (TriggerEnum.HUNG_UP, StateEnum.ON_HOOK)
        ]
    }

    state = StateEnum.OFF_HOOK
    exit_state = StateEnum.ON_HOOK

    while state != exit_state:
        print(f'The phone is currently {state}')

        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f'{i}: {t}')

        idx = int(input('Select a trigger:'))
        s = rules[state][idx][1]
        state = s

    print('We are done using the phone.')
