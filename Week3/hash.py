keys = [34874, 340985, 20687, 39587908, 
842086, 93927768, 49285, 349070, 20395, 939, 20687, 4810059, 2030678, 2049689, 204569795, 206873, 3946]
hash_map = [False]*256
collisions = 0
h1 = lambda k: k % 19
h2 = lambda k, i: (h1(k) + i) % 256
for k in keys:
    if not hash_map[h1(k)]:
        hash_map[h1(k)] = True
    else:
        i = 1
        while hash_map[h2(k, i)]:
            i += 1
        hash_map[h2(k, i)] = True
        collisions += i
print(collisions)