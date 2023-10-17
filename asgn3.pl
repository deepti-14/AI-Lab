criminal(X):- american(X), weapon(Y), sells(X,Y,Z), hostile(Z).
owns(Nono,m1).

missile(m1).
sells(west, X, Nono):- missile(X), owns(Nono,X).
weapon(X):- missile(X).
hostile(X) :- enemy(X,american).
american(west).
enemy(Nono, american).