class Node:
    def __init__(self, num=0, l=None, r=None):
        self.num = num
        self.l = l
        self.r = r


def find_path(node, required_sum, path, res):
    if not node:
        return

    path.append(node.num)

    if sum(path) == required_sum:
        res.append(path.copy())

    find_path(node.l, required_sum, path, res)
    find_path(node.r, required_sum, path, res)

    path.pop()

def paths_search(root, required_sum):
    res = []
    find_path(root, required_sum, [], res)
    return res

def bin_tree(nodes, ind, none_moves):
    try:
        if ind >= len(nodes):
            return None
    except:
        return None
    # Индексация следующих непустых узлов
    # после пустых
    if nodes[ind] is None:
        none_moves[ind] = [None, None]
        for i in range(ind + 1, len(nodes)):
            none_moves[i] = [2 * (i - 1) + 1, 2 * (i - 1) + 2]
        return None
    else:
        try:
            if (len(none_moves[ind]) == 2):
                pass
        except:
            none_moves[ind] = [2 * ind + 1, 2 * ind + 2]

    root = Node(nodes[ind])

    root.l = bin_tree(nodes, none_moves[ind][0], none_moves)
    root.r = bin_tree(nodes, none_moves[ind][1], none_moves)
    return root

def main():
    nodes = input('Введите значения для узлов: ')
    nodes = nodes.split(',')
    try:
        for i in range(len(nodes)):
            if nodes[i] == '':
                nodes[i] = None
            else:
                nodes[i] = int(nodes[i])
        root = bin_tree(nodes, 0, {})

        required_sum = input('Введите искомую сумму: ')
        try:
            required_sum = int(required_sum)
        except:
            print('(!!!) Искомая сумма должна быть целым числом')

        paths = paths_search(root, required_sum)
        if paths:
            letter = 'ь'
            if len(paths) > 1:
                letter = 'и'
            print(f'Пут{letter} до суммы "{required_sum}":')
            for path in paths:
                print('->'.join(map(str, path)))
        else:
            print('Искомую сумму составить невозможно!')
    except:
        print('(!!!) Неверный ввод узлов. Верный формат ввода: "3,5,,,11,,4"')

if __name__ == '__main__':
    main()