with open('6-input.txt', 'r') as fp:
    parents = dict(reversed(orbit.split(')'))
                   for orbit in fp.read().splitlines())


def dist_to_root(n): return 1+dist_to_root(parents[n]) if n in parents else 0


print(sum(dist_to_root(n) for n in parents))


def ancestors(n): return ancestors(parents[n]).union(
    [parents[n]]) if n in parents else set()


print(len(ancestors('YOU') ^ ancestors('SAN')))
