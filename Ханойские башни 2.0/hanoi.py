

def move(states, stacks, number, stack_from, stack_to):

    if number == 1:
        stacks[stack_to].append(stacks[stack_from].pop())
        states.append([[j for j in stacks[i]] for i in range(3)])


    else:
        aux_stack = 3 - stack_from - stack_to
        move(states, stacks, number - 1, stack_from, aux_stack)
        move(states, stacks, 1, stack_from, stack_to)
        move(states, stacks, number - 1, aux_stack, stack_to)

def hanoi(size):
    # генерация
    stacks = [[] for i in range(3)]
    stacks[0] = [size - i for i in range(size)]

    # сохранение исходного состояния
    states = [[[j for j in stacks[i]] for i in range(3)]]


    move(states, stacks, size, 0, 2)
    return states

if __name__ == '__main__':
    size = int(input('Задайте размер: '))

    for state in hanoi(size):
        print(state)

