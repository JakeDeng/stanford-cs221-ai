def computeEditDistance(s, t):
    #use cache to avoid calculating the same problem again
    cache = {} # (m,n) => result
    def recurse(m,n):
        """
        Return the minimum edit distance between:
        first m letters of s
        first n letters of t
        """
        if(m,n) in cache:
            return cache[(m,n)]
        if m == 0:
            result = n #base case
        elif n == 0:
            result = m #base case
        elif s[m-1] == t[n-1]: #last case matches
            #reduce to a sub problem
            result = recurse(m-1, n-1)
        else:
            #loop through all possibilities
            #substitution
            subCost = 1 + recurse(m-1, n-1)
            #delete
            delCost = 1 + recurse(m-1, n)
            #insertion into s is delete from t
            insCost = 1 + recurse(m, n-1)
            result = min(subCost, delCost, insCost)
        cache[(m,n)] = result 
        return result
    return recurse(len(s), len(t))

#run function will be called in main.py
def run():
    print(computeEditDistance('a cat!'*10, 'the cats!'*10))