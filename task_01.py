new_list = [(-2 + 0j), 1, 3.4, True, None, 'Text', [1, 2],
            (8, 9, 12), {19: 'nineteen', 20: 'twenty'}, {30, 55},
            frozenset(), range(24), b'twelve', bytearray(b'thirteen'),
            zip(*[(67, 69), (78, 79), ('a', 'b')]), TypeError]

for i, value in enumerate(new_list, 1):
    print(f"{i}) {value} - {type(value)}")
