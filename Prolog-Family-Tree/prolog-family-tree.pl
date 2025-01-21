male(karamSingh).
male(arun).
male(rakesh).
male(gautam).
female(kamladevi).
female(abha).
female(anu).
female(saroj).
female(leena).

parent_of(karamSingh,arun).
parent_of(karamSingh,leena).
parent_of(karamSingh,rakesh).

parent_of(kamladevi,arun).
parent_of(kamladevi,rakesh).
parent_of(kamladevi, leena).
parent_of(arun,abha).
parent_of(saroj,abha).
parent_of(rakesh,gautam).
parent_of(leena,anu).



/* Rules */
parents(X,Y):- parent_of(X,Y).

child(X, Y) :-
    parent_of(Y, X).

grandparent(X, Y) :-
    parent_of(X, Z),
    parent_of(Z, Y).

sibling(X, Y) :-
    parent_of(Z, X),
    parent_of(Z, Y),
    X \= Y.

sister(X, Y) :-
    sibling(X, Y),
    female(X),
    X \= Y.

brother(X, Y) :-
    sibling(X, Y),
    male(X),
    X \= Y.

uncle(X, Y) :-
    brother(X, Z),
    child(Y, Z).

aunt(X, Y) :-
    sister(X, Z),
    child(Y, Z).

cousin(X, Y) :-
    grandparent(Z, X),
    grandparent(Z, Y),
    \+sibling(X, Y),
    X \= Y.

