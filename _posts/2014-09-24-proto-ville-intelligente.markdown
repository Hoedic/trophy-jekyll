---
categories:
- Données & visualisation
- Politique
comments: true
date: 2014-09-24 21:38
image: 2014-09-24-graph.webp
layout: post
title: La ville paramétrique, proto ville intelligente
---

Ce (long) billet va donner un sens au nom de domaine utilisé pour ce blogue: dataholic!

Le présent article vise à faire une analyse de la réforme du financement des arrondissements de la Ville de Montréal sous l'angle de la ville intelligente. Plus précisément, nous allons viser les points suivants:

- Démontrer que la paramétrisation de la ville, logique sous-jacente à la ville intelligente, est un outil puissant mais nécessitant un travail d'analyse approfondi et une compréhension détaillée du fonctionnement de la ville.
- Souligner comment les données ouvertes peuvent être utilisées pour mieux comprendre notre environnement et idéalement pour créer une base de discussion et d'engagement avec les citoyens.
- Montrer ce à quoi pourrait ressembler du journalisme de données de fond. Malheureusement le journalisme de données se contente trop souvent de quelques graphiques sans fournir d'analyse de fond.
- Suggérer une démarche dans laquelle les citoyens pourraient avoir leur mot à dire sans nécessairement avoir à rentrer en détail dans les données disponibles.

Ce billet est le résultat d'un travail dilétante pendant une partie de l'été où j'ai joué avec plusieurs jeux de données en essayant de faire le lien avec les paramètres utilisés pour définir le financement des arrondissements.

Si vous êtes vraiment pressés, vous pouvez passer directement à la [conclusion](#conclusion), mais vont manquerez comment j'arrive à ce résultat (au risque de mauvaises interprétations!)

## Mettons le couvert

D'abord pourquoi faire le lien entre un exercice de paramétrage budgétaire et le concept de ville intelligente? Parce que ce paramétrage se rapproche des formules d'optimisation utilisées pour la ville intelligente (voir cet [article](http://cllbr.com/post/montreal-l-intelligence-dans-l-engagement/400/)). La différence est que pour le budget on applique des paramètres à des constantes pour obtenir un budget alors que pour la ville intelligente on essaie de faire varier les paramètres pour les optimiser, mais la logique est la même.

Et je dois dire dès le début que cette logique est... logique! D'ailleurs les budgets étaient déjà paramétrés, mais avec d'autres critères. Il est tout à fait souhaitable de vouloir normaliser les budgets de manière à ce que les citoyens de différents arrondissements bénéficient de niveaux de services équivalents... pour des coûts équivalents. De ce point de vue, le budget paramétré est non seulement normal mais nécessaire et le bris d'un status quo existant n'est pas une raison valable pour refuser de nouveaux paramètres ou refuser la mise en oeuvre d'une approche paramétrique en générale.

Les paramètres en question (anciens et nouveaux) sont disponibles dans un document publié par la Ville et disponible [en ligne](http://ville.montreal.qc.ca/pls/portal/docs/page/Service_Fin_Fr/media/documents/RFA_structure_de_financement_2014.pdf). Bien que le document soit un peu long, je vous invite à regarder la section 2 présentant les paramètres adoptés. Le but de l'exercice est de définir des "proxy", des paramètres quantifiables qui varient de manière proportionnelle aux dépenses, et il faut souligner que les critères utilisés semblent tout à fait raisonnables: surface de voirie pondérée par la "pression" subie, nombre de transactions dans les librairies, etc. Selon une approche progressiste, on prend même en compte des éléments comme l'indice de défavorisation pour mobiliser plus de fonds dans les zones de la ville actuellement en difficulté.

Appliqué à l'année 2015, les nouveaux paramètres amènent les changements présentés ci-dessous en matière de budget (notes rapides: dans les faits, les changements seront appliqués progressivement, donc les arrondissements ne vont pas subir ces changements du jour au lendemain. Le graphique contient uniquement les principaux postes budgétaires; la cause étant que les données sont présentées sous forme de PDF et qu'il a donc fallu retranscrire les informations à la main.)

![Variation de budget]({{ root_url }}/images/2014-09-24-budget-absolu.webp)
<div class="photoattrib">Variation du budget par arrondissement pour les principaux postes de dépense (en milliers de dollars)</div>


Les variations sont importantes et mis en pourcentage, cela implique des variations de plus de 15% pour les extrêmes. D'ailleurs, il est important de noter que le tout se fait à somme nulle: la réforme ne change pas la quantité d'argent reversée à l'ensemble des arrondissements mais se contente simplement de réallouer entre arrondissements.

En mettant les changements sur une carte, il appert que les arrondissements périphériques semblent généralement plus dans le positif tandis que les arrondissements centraux souffrent d'une baisse de financement. Comme on peut le voir sous forme [graphique](https://plot.ly/6/~hoedic), on note assez nettement le lien entre variation du budget et éloignement des arrondissements.

<a href="http://cdb.io/1CiKuBv">
![Variation de budget]({{ root_url }}/images/2014-09-24-carte.webp)
</a>
<div class="photoattrib">Carte des variations de budget par arrondissement. <a href="http://cdb.io/1CiKuBv">Accès à la carte interactive</a></div>

Sans rentrer dans les détails, il est intéressant de noter que le budget par habitant est très variable d'un arrondissement à l'autre passant de 0.89$ pour Saint-Laurent et Ville-Marie à 0.45$ pour Cote-des-neiges--Notre-Dame-de-Grace ([données ici](https://plot.ly/7/~hoedic)). On ne trouvera pas de solution facile à se contentant de regarder le coût par habitant.

## L'exemple des bibliothèques

Évidemment, il est difficle d'arriver à une conclusion sur l'ensemble des paramètres à cause de la mulitiplicité des sujets. Si on regarde d'un peu plus près les bibliothèques, on voit qu'un des paramètres est le nombre de transactions. Ça semble un bon proxy: plus de transactions signifie plus d'activité à gérer, plus de ressources nécessaires, etc.

Pourtant, en allant chercher les données d'emprunt, le calcul de certains ratios (en l'occurrence le nombre de livre par habitant, le nombre d'emprunt par livre et le nombre d'emprunt par habitant -qui détermine en partie le budget alloué aux bibliothèques) donne des résultats assez surprenants.


<a href="https://plot.ly/~hoedic/9">
![Emprunts de livres]({{ root_url }}/images/2014-09-24-emprunts-livres.webp)
</a>
<div class="photoattrib">Emprunts par livres et nombre total d'emprunt par arrondissement. <a href="https://plot.ly/~hoedic/9">Accès au graph interactif</a></div>

Il est presque choquant de voir que certains arrondissements disposent uniquement de 1.4 livres par habitant (Lachine), alors que d'autres sont à 3.86 (Pierrefonds). Tendance générale: les arrondissements avec le plus faible taux de livre par habitant sont ceux avec le plus d'emprunt par livre. Spécifiquement Lachine et le Plateau ont un ratio emprunt/livre supérieur à livre/habitant.

La question que cela provoque: est-ce que dans ces arrondissements, le nombre d'emprunts (critère de financement) est limité par la disponibilité des livres. La réalité, c'est que les indicateurs obtenus ne sont pas suffisants pour conclure. Pour ce faire, il faudrait une meilleure compréhension du fonctionnement des bibliothèques et les facteurs limitants le nombre d'emprunts. Pour apprécier un peu plus ces chiffres, on pourra noter que selon l'[ASTED](https://milieuxdoc.ca/cm2s_content/_milieux-documentaire/document/milieux-documentaires-1323485319-Lignesdirectrices.atelier4.Roussel.pdf), pour une ville de 100 000 habitants (même si un arrondissement peut difficile être considéré comme une ville), un ratio de 2.2 livres/hab est considéré comme "de base" alors qu'à 3.2 est dans l'"excellent". 

*Si* le nombre de livres est effectivement un facteur limitant le nombre d'emprunt, cela veut dire que des arrondissements comme Lachine et le Plateau (et d'autres) ont besoin de plus de financement (et non de moins comme c'est le cas), pour se mettre à niveau. Pourquoi se retrouve-t-on avec de tels écarts de livres par habitant? Est-ce le résultat d'un sous-investissement dans l'achat de livres de la part de ces arrondissements? Est-ce à cause du manque d'espace dans les bibliothèques? Du nombre de bibliothèque? Difficile de savoir juste sur base des données. Ce qui est certain, c'est qu'un indicateur comme le nombre de transaction rend difficilement compte de ces complexités.

### Digression méthologique

Maintenant je vais me permettre de pointer une lacune dans les données que j'utilise (pourtant très riches): il n'est pas possible de voir les emprunts entre bibliothèque. Quand on réalise un emprunt par réservation, la bibliothèque essaie de répondre à la demande par son catalogue local. Si ce n'est pas possible, le livre peut être transféré d'une autre bibliothèque.

La logique voudrait que les arrondissements avec un taux d'emprunt élevé doivent plus souvent faire appel à la réservation, se traduisant par des emprunts hors bibliothèque voire hors arrondissement. Vivant dans un des arrondissements avec un faible ratio de livre, nous nous retrouvons effectivement à utiliser ce système de réservation. Durant les dernières semaines j'ai regardé la provenance des livres réservés (principalement pour les enfants): sur 52 livres, deux seulement viennent de mon arrondissement, la grande majorité vient d'arrondissements avec un taux d'emprunt modéré ou faible: Anjou, Montréal-Nord ou encore Verdun. Anecdotique, il va de soit, mais éclairant sur le fait que les réservations peuvent reposer en large partie sur l'emprunt hors bibliothèque.

En d'autres termes, le nombre de transactions comptabilisées est faussé par ce mécanisme. Quelle proportion des transactions cela représente? 50% ou 0.01%, impossible à dire. C'est là où l'adoption de paramètres nécesssite de bien comprendre le fonctionnement de l'entité analysée. Pour être bien franc les données me donnent l'impression que certains arrondissements manquent de livres et que leur budget ne va pas améliorer la situation, mais les données seules, vue de l'extérieur, ne permettent pas de pleinement saisir l'état des lieux.

## La bonne densité

L'analyse des emprunts de bibliothèque apporte une indication, mais ça représente seulement un de la dizaine de critères utilisés. Peut-on trouver un autre critère que l'éloignement au centre pour expliquer les résultats dans leur ensemble? Dans un premier temps j'ai regardé du coté de la densité... sans obtenir un résultat très intéressant. C'est que la densité dans son acceptation la plus classique (nombre d'habitant divisé par la superficie du territoire) est parfois fourbe: des arrondissements comme Ville-Marie, le Sud-Ouest et bien d'autres ont une densité finalement assez faible à cause des nombreuses zones commerciales et industrielles.

Pour arriver à une analyse intéressante, il faut regarder l'empreinte individuelle au sol: la surface *résidentielle* divisée par le nombre de personnes. On obtient alors une idée de l'espace que chaque résident utilise et ça donne une vision de la densité nettement plus réaliste. (à noter qu'à ce petit jeu, le Plateau perd son titre de champion de la densité au profit de Ville-Marie.)

En prenant ainsi l'empreinte par habitant, on note trouve une correlation assez forte: les augmentations de budgets sont une fonction croissante de l'empreinte. En d'autres termes, la nouvelle formulation du budget tend à favoriser les gens qui s'étalent.

<a href="https://plot.ly/~hoedic/5">
![Empreinte par habitant]({{ root_url }}/images/2014-09-24-emprunte-habitant.webp)
</a>
<div class="photoattrib">Variation du budget en fonction de l'empreinte au sol des résidents. <a href="https://plot.ly/~hoedic/5">Accès au graph interactif</a></div>

Certains diront qu'éloignement du centre et étalement sont synonymes. À mes yeux, ça ne l'est pas: l'empreinte par habitant est un attribut important du tissu urbain contrairement à l'éloignement. La densité détermine le type d'organisation urbaine (avec les coûts privés et publics qui s'y rattachent). Par exemple, avec des stratégies "transit oriented", on peut obtenir de bonnes densités dans des lieux éloignés. Je reviendrai sur ces considérations en conclusion mais le résultat de ce graphique n'en demeure pas moins important.

## Location, location, location

Ceci dit, la question de la distance au centre ne doit pas être écartée pour autant. Malgré sa forme de croissant au beurre et son réseau hippodamien, Montréal présente une structure concentrique comme toutes les villes du monde (ou presque). La conséquence c'est qu'une bonne partie des résidents de la périphérie oscillent quotidiennement vers le centre sous forme de bouchons de circulation.

On notera que les paramètres pour le budget de voirie prennent en compte la pression (sous forme de pondération). Ces facteurs de pondération représentent-il la réalité?

### Autre digression méthodologique

Dans le monde des études d'impact environnemental, il existe une approche nommée [analyse du cycle de vie](http://fr.wikipedia.org/wiki/Analyse_du_cycle_de_vie) visant à évaluer l'impact sur toute la vie d'un produit sur tous les domaines environnementaux (GES, déchets, ressource naturelles, etc). 

Souvent, les analyses du cycle de vie arrivent à une note globale. Pour passer d'impacts sur des domaines très variés à une note globale, il faut appliquer une pondération. Mais comment pondérer l'impact des GES avec l'impact sur les ressource aquifère? On pondère, on compare des pommes avec des navets.

On arrive à des situations désolantes où McDonald avait réussi à démontrer que d'aller manger chez eux avait moins d'impact environnemental que d'aller au restaurant... tout cela parce qu'ils avaient utilisés une pondération qui minimisait les catégories d'impacts où McDo était plus polluant. Fin de la digression.

### Comment pondérer
Concentration des flux
Dans le cas des routes, la situation est un peu moins complexe car au moins on compare des choses comparables: des routes. En revanche, comment sont pondérées les catégories dont le budget est fonction de plusieurs paramètres? Est-ce 50/50? Y a-t-il une autre pondération?

Tout ceci m'amène à une autre critique du budget paramétré: si les paramètres sont listés, il nous manque les facteurs de pondérations exacts et les données utilisées pour arriver à ces résultats. Pourquoi? Pour déconstuire *comment* des paramètres qui *a priori semblent bons* créent un biais vers l'étalement.

### Concentration des flux

Pour retourner à des considération plus concrètes, il faut noter que certaines infrastructures sont communes et bénéficient à tous. Plus précisément certains arrondissements font proportionnellement moins usage de leurs infrastructures que les autres. Je m'explique: le réseau routier des arrondissements centraux est très largement utilisé par les résidents des arrondissements (et villes) périphériques. L'enquête [origine-destination de 2008](http://www.amt.qc.ca/enquete-od/precedentes/) nous apprend que les résidents de Rosemont, du Plateau, du Sud-Ouest ou encore de Ville-Marie, utilisent leur voiture dans une proportion généralement inférieure à 40%. 

En revanche, environ 70-80% des résidents des arrondissements périphériques utilisent leur automobile et une large partie se rend au centre-ville (et, logiquement traversent plusieurs arrondissements proches bien que l'enquête ne donne pas ce niveau de détail). Bien que l'on parle de l'autonomisation des banlieues, Ville-Marie reçoit quotidiennement 275 000 personnes en voiture (de partout dans la CMM). Ce sont 275 000 personnes qui souvent sont bien plus intéressées par la qualité de voirie de l'arrondissement (et des arrondissements) traversé que les résidents des dits arrondissements qui préfèrent dans une large proportion les transports en commun et actifs.

En d'autres termes, il faudrait se poser la question suivante: les budgets devraient-ils essayer de prendre en compte l'usure d'infrastructure causée par les résidents d'autres arrondissements et viser à rebalancer une partie de la situation. Bon courage pour y arriver car c'est complexe, mais les choses sont-elles vraiment équitable sans cela?


## Prendre en compte l'existant

Un des refrains de la ville intelligente, c'est de prendre en compte les données pour améliorer le processus décision. "Evidence based", "data sensitive", etc.

Lors d'un récent événement, M. Harout Chitilian, élu en charge de la ville intelligente, soulignait à quel point Montréal était jusqu'à présent en retard sur les métriques que l'administration oeuvrait à en mettre en place. Toronto et bien d'autres villes ont mis en place dans la dernière décennie des indicateurs, avec des objectifs précis à atteindre. Edmonton a même mis en place un ["dashboard" citoyen](https://dashboard.edmonton.ca/).

Comment cette approche "data sensitive" pourrait se traduire dans un budget paramétré? Continuons sur le sujet de la voirie. C'est un des domaines avec le plus de variation de budget, c'est aussi un des sujets de plainte récurrent des usagers de la route.

Des indicateurs existent. La Ville réalise notamment à intervalle régulier un état des lieux des rues pour évaluer les besoins de réfection. Ces données ont été obtenues par Radio Canada et [utilisées](http://ici.radio-canada.ca/sujet/etat-rues-montreal) lors du hackathon geoHack l'année dernière (j'ai eu la chance de faire partie de l'équipe gagnante avec lesdites données.) Est-ce que les données d'état des rues ont été prises en compte pour la paramétrisation? Non, les paramètres ne les prennent pas en compte et je m'attendais à ne vois aucune corrélation entre variation de budget et état des rues.

<a href="https://plot.ly/~hoedic/4">
![État des rues]({{ root_url }}/images/2014-09-24-etat-rue.webp)
</a>
<div class="photoattrib">Variation du budget en fonction de l'état des rues <a href="https://plot.ly/~hoedic/4">Accès au graph interactif</a></div>

Le graphique donne une image surprenante. D'abord, on note des clusters: d'un coté les quartiers centraux qui subissent tous une baisse alors que les quartiers périphériques augmentent. Ensuite, on note une corrélation positive assez forte à l'intérieur des deux clusters principaux entre la variation de budget et l'état des rues. En d'autres termes plus votre qualité de rue est bonne, plus vous recevez de l'argent. 

Encore une fois, le budget n'est pas *fait* pour donner ce résultat et l'état actuel des rues est probablement le fait du paramétrage précédent.

En regardant les variations de budget seulement, on pourrait imaginer que les paramètres précédents favorisaient les quartiers centraux et que le nouveau rééquilibre les choses. Mais en mettant cela en relation avec l'état des rues, ça ne semble plus tenir. Pour s'aligner dans une vision de ville intelligente, l'état des infrastructure actuel devrait entrer en compte dans l'allocation des budgets.

Comment? A priori, les arrondissements ayant une plus mauvaise qualité de rue devraient bénéficier de plus d'argent pour se remettre à niveau. Une formule mathématique pourrait permettre de pondérer le budget par l'écart à la moyenne de la qualité des rues. 

Certains répondront qu'un arrondissement pourrait maintenir une piètre qualité de rue pour avoir plus de budget. Mais comme tout ville intelligence, l'allocation du budget suivant pourrait être conditionnelle à l'atteinte d'objectifs.

Cette approche ne règle pas toutefois le problème du mauvais paramétrage. Si les paramètres pris en compte ne reflètent pas la réalité, si pour une raison ou pour une autres la voirie se dégrade plus vite à certains endroits qu'à d'autres, alors même l'atteinte d'objectifs est compromise. C'est là que la définition de proxy proches de la réalité est une étape cruciale sinon l'ensemble de la démarche est biaisée.

Quoiqu'il en soit, une première étape, surtout lorsqu'on fait *tabula rasa*, serait de prendre en compte l'existant et de donner à coup de pouce à ceux qui sont en retard. Ensuite, les paramètres pourraient être modulés pour inciter à une bonne performance.


<a id="conclusion"></a>


## (Longue) Conclusion

Alors que dire de ce budget paramétrique? Est-ce que je vais publier un edito titrant "le nouveau budget favorise l'étalement urbain"? Non.

D'abord on ne part pas d'une situation neutre, mais d'un autre budget paramétré qui lui-même avait possiblement des biais que je n'ai pas étudié.

Il faut tout de même se poser la question: pourquoi ce budget sembler rebalancer le budget des arrondissements assez nettement en faveur des arrondissements éloignés où les résidents ont une empreinte supérieure.

### À prendre avec des pincettes

La première chose à comprendre avec ce billet, c'est que c'est un travail rapide. Il peut contenir des erreurs (bien que j'ai essayé de vérifier mes résultats). Par ailleurs les différents éléments que j'ai étudié sont sur base des données disponibles, données que j'ai essayé de mettre en rapport avec les variations de budget. Les ratios que j'ai invité viennent de mon esprit, peut être que j'ai oublié des réalités importantes. Ce qui m'importait c'était d'essayer de mettre en évidence certaines préconceptions venant avec l'approche paramétrée.

### Journalisme de données

C'est une petite taloche amicale pour les journalistes de données car je sais qu'ils manquent de temps et de ressources. Personnellement je trouve que les questions obscures comme la réforme du financement des arrondissements ne sont pas assez traitées en général. Quelques articles donnant 2-3 chiffres, des critiques plus ou moins informées et voilà. Pourtant, il est tout à fait possible de remonter la logique décisionnelle et de l'expliquer de manière accessible.


### Biais politique

Bien que le sujet soit peu couvert dans les médias, une partie des commentaires sur le sujet laissaient penser qu'il s'agissait d'un exercice partisan. Mon premier reflexe fut donc de regarder si les arrondissements ayant voté pour l'équipe du maire ont été remercié par leur appui. Comme le montre le [graphique](https://plot.ly/8/~hoedic), ce n'est pas vraiment le cas. Avec une corrélation inférieure à 0.1, on ne peut pas dire que cette réforme est le résultat d'un exercice partisan.


### Données ouvertes

Comme noté précédemment, il est dommage que les données ayant servi au calcul des budgets ne soient pas disponibles. Pour être utilisées, ces données doivent avoir été préparées et normalisées, donc assez faciles à publier. Cette demande n'est pas pour mettre en doute les résultats, c'est pour pouvoir déconstruire ce qui a permis d'obtenir le résultat. Dans ce même objectif, les formules pour arriver aux résultats devraient être publiées.

### De la qualité de proxy

Comme je le disais en introduction, la question centrale de l'approche paramétrique -et de la ville intelligente- c'est de savoir si les proxys utilisés reflètent la réalité. L'article montre combien il est difficile d'avoir ce genre de proxy. Même pour les données de bibliothéque, où le proxy semblait excellent, on finit par lui trouver de possibles failles.

Pour discuter spéficiquement du choix des proxy dans la réforme, on peut en arriver à la conclusion que les paramètres se concentrent trop sur la comptabilisation des actifs sans prendre en compte leur taux d'utilisation. Des livres empruntés plus fréquemment devront être changés plus souvent. Des mètres carrés de rue ou de parc nécessiteront plus ou moins d'entretien selon l'intensité avec laquelle ils seront utilisés. Les paramètres "statiques" peinent intégrer l'aspect dynamique.

Évidemment, les paramètres dynamiques sont nettement plus difficile à collecter. Comment quantifier l'usage d'un parc? En comptant le nombre de personne dans le parc? Pas facile. Peut-être en pondérant avec le nombre de personnes vivant dans un rayon donné du parc, mais dans ce cas il faut passer par l'exercice difficile de calibrer le facteur de pondération.

### Du tissu urbain

Les lignes qui suivent entrent suivent une perspective plus personnelle. C'est là où s'arrête l'objectivité des données pour entrer dans l'interprétation. Cette interprération se base sur le biais constaté en faveur des arrondissements éloignés, un biais qui est relatif, relatif au budget précédent. Mon approche est que considérant que les arrondissements centraux ne sont visiblement pas dans l'opulence comparativement aux arrondissements périphériques, il y a lieu de se demander si on ne créée pas un déséquilibre. Sans pouvoir trancher de manière certaine l'existence d'un biais (c'est tout le noeud du problème), le but est discuter l'impact d'un tel biais SI il existe.

Un corrolaire à la question des proxy, c'est la difficulté à prendre en compte la valeur relative de certains actifs en fonction de leur localisation. Un mètre carré de verdure n'a pas la même valeur dans certains secteurs fortement urbanisés et verdis qu'à Pierrefonds où la majorité dispose d'un cour gazonnée.

S'installer dans tel ou tel quartier est un choix important. Les personnes s'installant dans les quartiers centraux cherchent la vie de quartier, les services et la proximité avec leur travail. Ce faisant ils acceptent souvent de payer plus cher pour plus petit. Et bien que payant plus chers, ils sont aussi plus demandeurs de certains services publics comme les parcs et les loisirs. Cela entraine aussi des coûts; par exemple le déneigement est plus demandant.

A contrario, les personnes s'installant dans les quartiers plus périphériques choisissent l'espace au détriment du temps de tranports. Par ce choix, ils décident de "privatiser" une partie de leurs besoins: voiture au lieu des transports en commun, grande cour avec piscine plutôt que parcs et piscines publiques, etc. Ceci dit ce choix a évidemment un coût public sous forme notamment de besoin plus élevés de transport, notamment de routes et d'infrastructures routières. (évidemment, je parle ici de moyennes).

Les paramètres choisis dans la réforme ont tendance à être aveugles à cette réalité, un mètre carré de pelouse est un mètre carré de pelouse, peu importe le contexte. Et c'est là aussi un immense défi: prendre en compte ce que les économistes appellent la valeur d'usage d'un bien public. Le résultat: le modèle proposé tend à financer les actifs développés. Les paramètres ne visent rien, ils n'ont pas d'objectifs, de vision, ils visent à comptabiliser les besoins des structures existantes, passivement. 

Lors d'une conférence récente pour l'Association des Transports du Canada, M. Aref Salem expliquait qu'on ne pouvait plus développer les villes sur base du tout à l'auto et qu'il est nécessaire de densifier. Le plan métropolitain d'aménagement et de développement (PMAD) adopté par le CMM arrivait à la même conclusion. Mais comment mettre en oeuvre ces recommandations sur les flux budgets continuent de supporter un mode de développement étalé?

Certains argueront que ce qui oriente la ville, ce sont plus les budgets d'investissements et non les budgets d'opération. C'est vrai et ce n'est pas vrai: les investissements permettent de développer des nouvelles infrastructures. Mais si les budgets ne permettent pas de faire "vivre" les infrastructures, si l'opération tend à défavoriser une approche par rapport à une autre -et surtout celle qui repose sur des espaces et services publics- c'est certain que cela va créer un débalancement de la population d'un sens vers l'autre.

Ce qui m'amène donc au dernier point: la nécessité de discuter de ces enjeux.

### Créer une discussion autour de ces enjeux

Le choix des paramètres à optimiser dans une ville intelligente est loin d'être neutre. L'argent étant le nerf de la guerre, le choix des paramètres de financement joue un rôle clé dans le développement d'une ville. Les arrondissements centraux de Montréal sont parmi les seuls endroits où il est possible d'avoir une vie "urbaine" dans la région. Si Montréal désinvestit ces arrondissements, ceux qui ont fait le choix d'y vivre, faute des services qu'ils espéraient, vont revoir leur choix et s'installer dans un endroit où ils peuvent "privatiser" leurs besoins (du moins ceux qui peuvent se le payer). 

Mais à ce jeu, la Ville de Montréal sera perdante: pour un Pointe-aux-trembles, il y a 5 Brossard. Moralité, si les arrondissements centraux se mettent à se vider faute de financement (et donc de services), il est à parier que les déménagements iront plus hors Montréal que dans les arrondissements périphériques de Montréal, affaiblissant ainsi l'assiette budgétaire de Montréal.

Certains pourront arguer que c'est un choix individuel de s'installer au centre ou à la périphérie et qu'il n'y a pas de raison pour que le financement des arrondissements prenne en compte le fait que ceux habitant au centre souhaitent plus de services publics et communs. Sauf que comme expliqué précédemment, vivre en périphérie a également des coûts communs. Donc tout ceci en revient à faire des choix, non plus individuels mais de société. Ne plus regarder la question du financement comme un sujet administratif, mais comme un sujet politique, un sujet dont les citoyens doivent comprendre les implications.

### Comment discuter de ces enjeux?

Plusieurs fois, en lisant ou en écrivant sur les enjeux de ville intelligente, il est question d'impliquer les citoyens, on parle parfois d'intelligence collective et autres concepts du genre. Et pour avoir discuté certaines des personnes en charges des approches de ville intelligente, tout le monde est conscient de la nécessité d'impliquer les citoyens. Les deux grandes difficultés sont: 

- Comment s'assurer que cette approche intelligente et citoyenne est appliqué à l'ensemble des domaines d'activité (le budget et la fiscalité était les moins évidents)
- Comment le concept de participation doit être appliqué pour être efficace.

Habituellement je me pose la question de manière abstraite. Cette réforme de financement est une belle occasion d'essayer de réfléchir à ceci de manière plus concrète.

Il est difficile d'espérer que tout le monde va se mettre à manipuler ces données. Il est déjà difficile d'obtenir les niveaux d'engagement souhaitables pour des actions assez simples, rares sont ceux qui s'investiront dans de l'analyse de données. Il faut donc trouver un processus permettant de mettre en évidence les choix et leurs impacts sans avoir à traiter les données. 

Une démarche consultative devrait donc commencer par le processus classique: aller à la rencontre des gens et demander ce qu'ils veulent. Et c'est ce qui a été fait avec le PMAD. Et des recommandations assez claires, notamment en faveur de la densification en sont ressorties, des recommandations supportées par la majorité des gens qui s'y sont intéressés. Prochainement l'administration de Montréal va lancer une consultation sur le plan d'aménagement, ce qui démontre une ouverture et un désir de prendre en compte l'avis des citoyens.

L'étape suivante consiste donc s'assurer ce que ces recommandations sont mise en oeuvre dans les différentes actions, notamment le financement. Comment? En invitant pas nécessairement toute la population mais certains représentants à donner leur avis sur les paramètres de financement choisis. Ou plus précisément en faisant un travail d'évaluation des paramètres qui suivent la philosophie des recommandations.

Fait intéressant: d'après les discussions que j'ai pu avoir, à défaut d'inviter des représentants de la société civile, la démarche de réforme du financement s'est fait en collaboration avec des membres de l'opposition qui semblaient satisfaits des critères... mais qui furent très déçus du résultat.

C'est pour cela que l'étape suivante ne doit pas être d'adoption des critères mais plutôt une ou des simulations. Et pour le coup, ces résultats doivent être publics. Des outils comme un simulateur de budget peuvent même permettre d'explorer différents scenarios et leurs impacts, les gens peuvent voter, commenter sur les paramètres, sur les résultats. Après cela seulement, il est possible d'adopter les critères qui sont le plus en ligne avec les recommandations.

C'est par un mécanisme de boucle de rétroaction que les citoyens vont eux-mêmes mieux comprendre l'impact de leurs choix individuels, que ces choix viennent avec des coûts et des attentes.

### Pour un meilleur développement

Une telle démarche permettrait aussi de mieux guider le développement de la ville. En fait, ce n'est pas faute de connaitre des gens ayant déménagé dans des unifamiliales, en banlieue, parfois par dépit. Certains rêvaient d'une grande maison grand jardin et ils l'ont eu. D'autres rêvaient plus d'un quartier vivant, relativement dense, avec des services mais abordable. Ça n'existe plus à Montréal.

Faute d'une offre appropriée, notamment pour les familles, faute d'une capacité à développer des quartiers complets, agréables beaucoup s'en vont plus loin... et pas nécessairement heureux d'y aller. 

La ville intelligente promet de se régler en observant les gens: leurs déplacements, leurs usages, leur consommation. Mais s'est-on demandé si ce qu'on observait correspondait à leurs besoins. S'est-on demandé si les comportements que l'on observe et que l'on essaie d'optimiser representent ce que les gens veulent ou si c'est seulement un pis-aller que l'on cherche à rendre plus efficace?

C'est pour cette raison qu'on ne peut pas faire l'économie de débats, d'échanges, de mises en situation, de consultation. Sans quoi on va reproduire et optimiser *ad nauseam* des villes ne correspondant pas aux attentes.


***

## Un peu de méthodologie

### Des choix 

Analyser des données, c'est beaucoup une histoire de choix. Voici une brève discussion sur les choix dont je suis conscient:

- Pour le choix des jeux de données, j'y suis vraiment allé au nez, sur base de ce que je connaissais des différentes sources possibles, notamment la Ville de Montréal. Les jeux de données choisis ont tous en commun que je les avais déjà utilisés dans le passé et je me suis pas mal contenté de ça. Hormis les données de comptage des voitures, je pense avoir tout utilisé. Pourquoi ne pas utiliser les comptages? Je n'ai pas trouvé de ratio ou d'angle d'analyse intéressant.
- Les ratios que j'ai choisis sortent de mon imagintion. N'ayant pas accès aux données utilisées pour les paramètres, j'ai moi aussi cherché à constituer mes propres proxy. Les différents paramètres utilisés visant généralement à être mis en relation avec la variation de budget en pourcentage. L'utilisation du pourcentage permet de mieux quantifier l'impact sur les finances d'un arrondissement plutôt que la valeur absolue qui est uniquement utilisée dans le premier graphique pour montrer les échelles en jeu.
- Dans certains graphiques, j'ai volontairement homis l'Île-Bizard (et parfois Pierrefonds) à cause du fait que son éloignement et sa densité est complètement hors échelle, "écrasant" ainsi les autres valeurs. L'Île-Bizard (18 097 habitants) est de loin, avec Outremont (23 566), le plus petit arrondissement en population, les suivants font quasiment le double (Lachine et Anjou avec 41 000 habitants.)
- En allant un peu vite, j'ai oublié de prendre certaines échelles classiques, notamment pour tout ce qui est géospatial. Donc les distances et les superficies sont dans une unité de degré de radian, ça n'a pas d'impact si ce n'est que ça se traduit par des valeurs de distance et de superficie un peu étranges. Une fois les résultats produit, il est un peu difficile de refaire des conversions en kilomètre.


### Jeux de données utilisés 

- [Résultats détaillés des élections municipales de 2013](http://donnees.ville.montreal.qc.ca/dataset/elections-2013-resultats-detailles)
- [Postes électifs de la ville de montréal](http://donnees.ville.montreal.qc.ca/dataset/elections-2013-postes-electifs)
- [Affectation du sol de la CMM](http://cmm.qc.ca/geomatique/utilisation-du-sol/) (fichier nettement plus facile à traiter que [celui](http://donnees.ville.montreal.qc.ca/dataset/affectation-du-sol) de Montréal qui utilise des "multipolygon" complexes, bien pour l'affichage mais vraiment pénible à traiter dans postgis...)
- [Catalogue des livres](http://donnees.ville.montreal.qc.ca/dataset/catalogue-bibliotheques) des bibliothèques de Montréal
- États des rues de Montréal (obtenu par une demande d'accès à l'information de Radio-Canada)
- [Enquête origine destination de l'AMT](http://www.amt.qc.ca/enquete-od/precedentes/)
- [Intersections de Montréal avec des feux](http://donnees.ville.montreal.qc.ca/dataset/feux-tous)
- [Geobase](http://donnees.ville.montreal.qc.ca/dataset/geobase) de Montréal
- Rapport de la révision du financment des arrondissements (avec des tableaux PDF...)
- [Limites des arrondissements](http://donnees.ville.montreal.qc.ca/dataset/polygones-arrondissements) de Montréal
- Montréal en statistiques (population et revenus par arrondissements)


### Outils utilisées

- Postgresql avec PostGIS (calcul de distance, de superficie, etc.)
- Ogr2Ogr pour loader les fichiers bien formattés dans Postgres
- PgLoader pour loaders certaines données utilisant des formats exotiques
- Excel (et oui! Malgré son horrible bug sur l'encodage en UTF-8)
- Libre Office
- Plot.ly
- CartoDB
- Plusieurs commandes unix (cut, split, awk, etc.)