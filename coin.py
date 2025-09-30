def how_many_coins(target: int, coins: list) -> int:
    coins.sort(reverse=True)
    available_coins = list(filter(lambda x: x <= target, coins))
    if len(available_coins) == 0:
        raise ValueError("No coins available for the target amount")
    else:
        new_target = target - available_coins[0]
        if new_target == 0:
            return 1
        else:
            return 1 + how_many_coins(new_target, coins)


def test():
    target = 14
    coins = [1, 2, 5]
    result = how_many_coins(target, coins)
    print(f"{result} coins needed")


if __name__ == '__main__':
    test()
