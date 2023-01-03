# Runge-Kutta

# Euler explicite

La méthode de Newmark et la méthode d'Euler explicite sont deux méthodes de résolution numérique de problèmes de dynamique des structures qui permettent de calculer les déplacements, les vitesses et les accélérations d'un système de masse, de raideur et de damping à un pas de temps donné, en utilisant les valeurs de ces grandeurs aux pas de temps précédents.

La méthode de Newmark utilise une approche itérative qui consiste à combiner les valeurs de la fonction et de ses dérivées aux pas de temps précédents pour prédire les valeurs aux pas de temps suivants. Elle est stable pour des pas de temps assez petits et converge plus rapidement que la méthode de Verlet, mais elle peut être moins stable que la méthode d'Euler explicite pour des pas de temps trop grands. La méthode de Newmark est particulièrement adaptée pour résoudre des problèmes de dynamique non linéaire, car elle permet de prendre en compte les effets de damping et de calculer les déplacements, les vitesses et les accélérations à chaque pas de temps.

La méthode d'Euler explicite est une méthode itérative qui consiste à approximer les dérivées d'une fonction en utilisant les valeurs de la fonction aux pas de temps précédents. Elle est simple à implémenter et converge rapidement, mais elle est sensible aux erreurs d'arrondi et peut donner des résultats instables pour des pas de temps trop grands. Elle est souvent utilisée comme méthode de référence pour comparer les performances et la précision de méthodes de résolution numérique de problèmes de dynamique des structures.

En résumé, la méthode de Newmark et la méthode d'Euler explicite sont deux méthodes de résolution numérique de problèmes de dynamique des structures qui présentent des avantages et inconvénients différents. La méthode de Newmark est stable pour des pas de temps assez petits et converge plus rapidement que la méthode de Verlet, mais elle peut être moins stable que la méthode d'Euler explicite pour des pas de temps trop grands. La méthode d'Euler explicite est simple à implémenter et converge rapidement, mais elle est sensible aux erreurs d'arrondi.

Il est important de choisir la méthode de résolution numérique de problèmes de dynamique des structures la plus adaptée en fonction du problème à résoudre. Dans certains cas, la méthode de Newmark peut être préférable à la méthode d'Euler explicite, notamment lorsque l'on souhaite prendre en compte les effets de damping ou lorsque l'on étudie des problèmes de dynamique non linéaire. Dans d'autres cas, la méthode d'Euler explicite peut être préférable, notamment lorsque l'on cherche à obtenir des résultats rapidement ou lorsque l'on étudie des problèmes de dynamique linéaire simples.

Il est également possible de combiner les avantages de ces deux méthodes en utilisant des schémas de Newmark améliorés, qui utilisent des combinaisons non linéaires des valeurs de la fonction et de ses dérivées aux pas de temps précédents pour prédire les valeurs aux pas de temps suivants. Ces schémas permettent d'obtenir une meilleure précision que la méthode de Newmark classique et une meilleure stabilité que la méthode d'Euler explicite, mais ils sont plus complexes à implémenter et peuvent nécessiter l'utilisation de techniques de continuation et de bifurcation pour étudier les comportements non linéaires des systèmes.

En conclusion, la méthode de Newmark et la méthode d'Euler explicite sont deux méthodes de résolution numérique de problèmes de dynamique des structures qui présentent des avantages et inconvénients différents et qui peuvent être utilisées en fonction du problème à résoudre et des objectifs de l'étude. Il est important de choisir la méthode la plus adaptée et de la paramétrer correctement pour obtenir des résultats précis et stables.



# Verlet
