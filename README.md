La topologie est une branche des mathématiques qui étudie les propriétés des espaces qui sont préservées sous les transformations continues. Nous allons couvrir les concepts fondamentaux de la topologie, puis nous progresserons vers des concepts plus avancés comme les espaces localement convexes métrisables nucléaires. Voici le plan de cours que nous allons suivre :

1. **Notions de base de la topologie**
    - Ensembles ouverts et fermés
    - Topologies et bases
    - Intérieur, adhérence et frontière
    - Continuité et homéomorphismes

2. **Topologies usuelles et exemples**
    - Topologie triviale et topologie discrète
    - Topologie de la droite réelle \( \mathbb{R} \)
    - Topologie produit et topologie quotient

3. **Propriétés topologiques importantes**
    - Compacité
    - Connexité
    - Compacité séquentielle
    - Séparabilité et axiomes de séparation (T0, T1, T2, etc.)

4. **Espaces métriques et métrisabilité**
    - Définitions et exemples
    - Espaces métrisables
    - Théorème d'Urysohn
    - Théorème de Nagata-Smirnov

5. **Espaces vectoriels topologiques**
    - Définition et exemples
    - Topologies sur les espaces vectoriels
    - Espaces de Banach et de Hilbert

6. **Espaces localement convexes**
    - Définitions et propriétés
    - Systèmes de semi-normes
    - Espaces de Fréchet

7. **Espaces localement convexes métrisables nucléaires**
    - Définitions et propriétés
    - Critères de nucléarité
    - Exemples et applications

### 1. Notions de base de la topologie

#### Ensembles ouverts et fermés

Un **espace topologique** est un ensemble \( X \) muni d'une collection \( \mathcal{T} \) de sous-ensembles de \( X \) vérifiant les conditions suivantes :
1. \( X \in \mathcal{T} \) et \( \emptyset \in \mathcal{T} \).
2. Toute union de membres de \( \mathcal{T} \) appartient à \( \mathcal{T} \).
3. Toute intersection finie de membres de \( \mathcal{T} \) appartient à \( \mathcal{T} \).

Les éléments de \( \mathcal{T} \) sont appelés **ensembles ouverts**. Un ensemble est dit **fermé** s'il est le complémentaire d'un ensemble ouvert.

#### Exercice 1:
Soit \( X = \{a, b, c\} \). Quels sont les possibles topologies sur \( X \) ?

#### Topologies et bases

Une **base** pour une topologie sur \( X \) est une collection \( \mathcal{B} \) de sous-ensembles ouverts de \( X \) telle que chaque ensemble ouvert de \( X \) peut être exprimé comme une union d'éléments de \( \mathcal{B} \).

#### Exercice 2:
Montrer que la collection \( \mathcal{B} = \{(a, b) : a, b \in \mathbb{Q}, a < b\} \) est une base pour la topologie usuelle sur \( \mathbb{R} \).

#### Intérieur, adhérence et frontière

- **Intérieur** d'un ensemble \( A \), noté \( \text{int}(A) \), est le plus grand ensemble ouvert contenu dans \( A \).
- **Adhérence** d'un ensemble \( A \), notée \( \overline{A} \), est le plus petit ensemble fermé contenant \( A \).
- **Frontière** d'un ensemble \( A \), notée \( \partial A \), est l'ensemble des points qui sont dans l'adhérence de \( A \) mais pas dans son intérieur.

#### Exercice 3:
Soit \( A = (0, 1) \cup (1, 2) \) dans \( \mathbb{R} \) avec la topologie usuelle. Trouvez \( \text{int}(A) \), \( \overline{A} \), et \( \partial A \).

#### Continuité et homéomorphismes

Une fonction \( f: (X, \mathcal{T}_X) \rightarrow (Y, \mathcal{T}_Y) \) est **continue** si pour tout ouvert \( V \) de \( Y \), \( f^{-1}(V) \) est un ouvert de \( X \).

Un **homéomorphisme** est une bijection continue dont l'inverse est aussi continue.

#### Exercice 4:
Soit \( f: \mathbb{R} \rightarrow \mathbb{R} \) définie par \( f(x) = 2x + 3 \). Montrer que \( f \) est un homéomorphisme.

### 2. Topologies usuelles et exemples

#### Topologie triviale et topologie discrète

- **Topologie triviale** : \( \mathcal{T} = \{ \emptyset, X \} \)
- **Topologie discrète** : \( \mathcal{T} = \mathcal{P}(X) \) (l'ensemble de toutes les parties de \( X \))

#### Topologie de la droite réelle \( \mathbb{R} \)

La **topologie usuelle** sur \( \mathbb{R} \) est générée par la base des intervalles ouverts \( (a, b) \).

#### Exercice 5:
Décrire les ouverts de la topologie triviale et de la topologie discrète sur un ensemble \( X \).

#### Topologie produit et topologie quotient

- **Topologie produit** : Pour deux espaces topologiques \( (X, \mathcal{T}_X) \) et \( (Y, \mathcal{T}_Y) \), la topologie produit sur \( X \times Y \) est la topologie la plus fine telle que les projections sont continues.
- **Topologie quotient** : Si \( X \) est un espace topologique et \( \sim \) est une relation d'équivalence sur \( X \), alors l'ensemble quotient \( X/\sim \) hérite d'une topologie où les ensembles ouverts sont les images réciproques des ensembles ouverts de \( X \).

#### Exercice 6:
Décrire la topologie produit sur \( \mathbb{R} \times \mathbb{R} \).

### 3. Propriétés topologiques importantes

#### Compacité

Un espace \( X \) est **compact** si de toute couverture ouverte de \( X \), on peut extraire une sous-couverture finie.

#### Exercice 7:
Montrer que l'intervalle \([0, 1]\) est compact.

#### Connexité

Un espace \( X \) est **connexe** s'il ne peut pas être écrit comme l'union disjointe de deux ouverts non vides.

#### Exercice 8:
Montrer que \( \mathbb{R} \) est connexe.

#### Compacité séquentielle

Un espace \( X \) est **compact séquentiellement** si toute suite a une sous-suite convergente.

#### Séparabilité et axiomes de séparation

- **Séparabilité** : Un espace est **séparable** s'il contient un sous-ensemble dense dénombrable.
- **Axiomes de séparation** : Différents niveaux de séparation des points dans un espace topologique (T0, T1, T2, etc.).

#### Exercice 9:
Déterminer si \( \mathbb{R} \) est séparable.

### 4. Espaces métriques et métrisabilité

#### Définitions et exemples

Un **espace métrique** est un ensemble \( X \) muni d'une fonction \( d: X \times X \rightarrow \mathbb{R} \) (appelée **métrique**) satisfaisant les propriétés de non-négativité, de symétrie, et d'inégalité triangulaire.

#### Espaces métrisables

Un espace topologique est **métrisable** s'il existe une métrique qui induit sa topologie.

#### Théorème d'Urysohn

Un espace topologique est normal si et seulement s'il est métrisable.

#### Théorème de Nagata-Smirnov

Un espace est métrisable si et seulement s'il est régulier et possède une base dénombrable.

#### Exercice 10:
Montrer que tout espace métrisable est normal.

### 5. Espaces vectoriels topologiques

#### Définition et exemples

Un **espace vectoriel topologique** est un espace vectoriel \( E \) sur un corps \( K \) muni d'une topologie telle que les opérations de l'addition et de la multiplication par un scalaire sont continues.

#### Topologies sur les espaces vectoriels

Les topologies les plus courantes sur les espaces vectoriels sont définies par des normes, semi-normes ou des systèmes de semi-normes.

#### Espaces de Banach et de Hilbert

- **Espace de Banach** : Un espace vectoriel normé complet.
- **Espace de Hilbert** : Un espace de Banach où la norme est induite par un produit scalaire.

#### Ex

ercice 11:
Donner un exemple d'espace de Banach et d'espace de Hilbert.

### 6. Espaces localement convexes

#### Définitions et propriétés

Un **espace localement convexe** est un espace vectoriel topologique où la topologie peut être définie par une famille de semi-normes.

#### Systèmes de semi-normes

Un système de semi-normes \( \{p_i\}_{i \in I} \) définit une topologie sur un espace vectoriel \( E \) où une base des ouverts est donnée par les ensembles de la forme \( \{ x \in E : p_i(x) < \epsilon \} \).

#### Espaces de Fréchet

Un espace de Fréchet est un espace vectoriel topologique complet et métrisable dont la topologie provient d'une famille dénombrable de semi-normes.

#### Exercice 12:
Montrer que tout espace de Banach est un espace de Fréchet.

### 7. Espaces localement convexes métrisables nucléaires

#### Définitions et propriétés

Un **espace localement convexe nucléaire** est un espace vectoriel topologique localement convexe qui a la propriété que toute application linéaire continue d'un espace vectoriel topologique vers un espace localement convexe est nucléaire.

#### Critères de nucléarité

Un espace localement convexe est nucléaire si et seulement si pour toute base de la topologie, il existe une base plus fine telle que les inclusions sont des applications compactes.

#### Exemples et applications

Exemples typiques incluent les espaces de distributions et certains espaces de fonctions analytiques.

#### Exercice 13:
Vérifier si l'espace de Schwartz \( \mathcal{S}(\mathbb{R}^n) \) est un espace nucléaire.

Avec ces concepts et exercices, vous devriez avoir une bonne compréhension des bases de la topologie jusqu'aux espaces localement convexes métrisables nucléaires. N'hésitez pas à poser des questions ou demander des clarifications sur des points spécifiques.
