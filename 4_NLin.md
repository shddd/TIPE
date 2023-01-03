La méthode de Newmark peut être appliquée à des problèmes de dynamique des structures non linéaires en utilisant des modèles constitutifs non linéaires pour la matrice de raideur et/ou la matrice de damping.

Pour résoudre un problème de dynamique des structures non linéaire avec la méthode de Newmark, il faut d'abord écrire les équations de mouvement du système sous forme matricielle. Ces équations sont données par :

M * a + C(u, v) * v + K(u) * u = f

où M est la matrice de masse, a est le vecteur des accélérations, C est la matrice de damping qui dépend de u et v, v est le vecteur des vitesses, K est la matrice de raideur qui dépend de u et f est le vecteur des forces appliquées sur le système.

Pour résoudre ce système d'équations à chaque pas de temps, on peut utiliser la méthode de Newmark avec des combinaisons linéaires des valeurs de u, v et a aux pas de temps précédents pour prédire les valeurs aux pas de temps suivants. Cependant, il faut être vigilant aux problèmes de stabilité qui peuvent survenir lorsque la matrice de raideur ou la matrice de damping sont non linéaires.
