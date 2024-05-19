from permutationsHandler import ListPermutations


if __name__ == '__main__':

    permutation = ListPermutations(list_data=list("ABC"))

    perm_itr = permutation.permutation_iterator()

    for perm in perm_itr:
        print(perm)
    permutation.tree_display()

