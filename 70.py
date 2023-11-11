# declare an empty dictionary in python
result = {}

def climbStairs(num_of_stairs):
    if num_of_stairs <= 1:
        return 1
    elif num_of_stairs == 2:
        return 2
    else:
        # check if the key is already in the dictionary
        result_previous_stairs_by_one = 0
        result_previous_stairs_by_two = 0
        if num_of_stairs-1 in result:
            result_previous_stairs_by_one = result[num_of_stairs-1]
        else:
            result_previous_stairs_by_one = climbStairs(num_of_stairs-1)
            result[num_of_stairs-1] = result_previous_stairs_by_one
        
        if num_of_stairs-2 in result:
            result_previous_stairs_by_two = result[num_of_stairs-2]
        else:
            result_previous_stairs_by_two = climbStairs(num_of_stairs-2)
            result[num_of_stairs-2] = result_previous_stairs_by_two
        
        return result_previous_stairs_by_one + result_previous_stairs_by_two


if __name__ == '__main__':
    # read user input
    n = int(input())
    how_many_ways_in_total = climbStairs(n)
    print(how_many_ways_in_total)