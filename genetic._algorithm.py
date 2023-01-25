from numpy.random import randint
from numpy.random import rand

def selection(pop, scores):
    first = randint(len(pop))
    opponents = randint(0, len(pop), 2)
    for o in opponents:
        if scores[o] < scores[first]:
            first = o
    return pop[first]

def mutation(c, mutation_rate):
    for i in range(len(c)):
        if rand() < mutation_rate:
            c[i] = 1 - c[i]
    

def crossover(p1, p2, crossover_rate):
    c1 = p1.copy()
    c2 = p2.copy()
    if rand() < crossover_rate:
        cross_point = randint(0, len(p1) - 2)
        c1 = p1[:cross_point] + p2[cross_point:]
        c2 = p2[:cross_point] + p1[cross_point:]
    return [c1, c2]

def genetic(objective, n_pop, n_bits, n_iter, mutation_rate, crossover_rate):
    pop = []
    for _ in range(n_pop):
        p = []
        for _ in range(n_bits):
            p.append(randint(0, 2))
        pop.append(p)

    best = pop[0]
    best_eval = objective(pop[0])

    for gen in range(n_iter):

        scores = []
        for p in pop:
            scores.append(objective(p))

        #print('pop:', pop)
        #print('scores:', scores)
        
        for i in range(len(scores)):
            if scores[i] < best_eval:
                best_eval = scores[i]
                best = pop[i]
                print(gen, '->', best, 'con punteggio:', scores[i])
        
        selected = []

        for _ in range(n_pop):
            selected.append(selection(pop, scores))

        children = []

        for i in range(0, n_pop, 2):
            p1 = selected[i]
            p2 = selected[i + 1]
            for c in crossover(p1, p2, crossover_rate):
                mutation(c, mutation_rate)
                children.append(c)

        pop = children

    return [best, best_eval]

def onemax(lst):
    return - sum(lst)

if __name__ == "__main__":
    n_iter = 100
    n_bits = 100
    n_pop = 100
    crossover_rate = 0.9
    mutation_rate = 1.0 / float(n_bits)
    best, score = genetic(onemax, n_pop, n_bits, n_iter, mutation_rate, crossover_rate)
    print('Done!')
    print('f(%s) = %d' % (best, score))


