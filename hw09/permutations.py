def permutations(array):
    vysledek = []
    def generate(current, remaining):
        if not remaining:
            vysledek.append(current)
            return
 
        for i in range(len(remaining)):
            new = current + [remaining[i]]
            new_remaining = remaining[:i] + remaining[i+1:]
            generate(new, new_remaining)
 
    generate([], array)
    return vysledek