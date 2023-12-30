---
layout: post
title: "Qui paie la Ville? Densité, fiscalité & équité"
date: 2022-05-30 20:00
description: "La fiscalité municipale et la faible densité nous vouent-ils aux gémonies?"
comments: true
categories: ["Politique", "Données & visualisation"]
image: "2022-05-30_accueil_3d_montreal.jpg" 
---

D’où vient l’argent des villes? Qui paie quoi? Combien? Pourquoi les villes [demandent des changements](https://www.lapresse.ca/affaires/economie/quebec/201805/16/01-5182131-impot-foncier-lunion-des-municipalites-du-quebec-sonne-lalarme.php) dans ce qui est leur principale source de revenu? Des questions a priori ennuyeuses et pourtant fondamentales pour la qualité de vie d’une majorité de Québécois (et de l’humanité) puisque désormais l’urbanité est le statut du plus grand nombre; à nous de décider si c'est pour le meilleur ou pour le pire.


## Version courte et manquant sérieusement de subtilité 

### (à sauter si vous comptez lire la version longue)

À partir des données de [taxes foncières](https://donnees.montreal.ca/ville-de-montreal/taxes-municipales) récemment publiées par la Ville de Montréal, il devient possible de calculer la contribution financière des différents quartiers de Montréal et d'analyser l'impact de la densité et de facteurs socio-économiques. Cette démarche se rapproche d’une [analyse](https://www.urbanthree.com/case-study/lafayette-la/) réalisée par la firme [Urban3](https://www.urbanthree.com/) qui compare les revenus et les dépenses municipales dans différents secteurs de la ville de Lafayette et Louisiane, et concluant que les zones centrales et souvent plus modestes subventionnent les zones périphériques et aisées.

Dans le cas de Montréal, nous manquons d’information sur les dépenses pour faire l’analyse complète; toutefois il est possible de réaliser une analyse des revenus par unité d’infrastructure (la rue). Les résultats obtenus pour Montréal s’approchent de ceux de Lafayette, à savoir que les quartiers centraux produisent significativement plus de revenus que les quartiers périphériques.

Pour ce qui est de la contribution en fonction des revenus de la population, on arrive également à la conclusion que dans l’ensemble, les ménages à revenus faibles contribuent collectivement plus que les ménages à revenus élevés, sachant que cette réalité varie selon la distance par rapport au centre de Montréal. Plus précisément, les quartiers riches *et* centraux ont une contribution financière significative alors que les quartiers riches *et* périphériques sont parmi ceux contribunant le moins. Toutefois, rien n'est aussi tranché, nuances et réserves sont détaillées dans la version complète…

Cette analyse souligne la nécessité de réfléchir à l'aménagement urbain aussi en fonction des revenus municipaux et des paramètres influançant la taxe foncière selon le type d'environnement urbain que l'on souhaite créer. Ainsi des développements peu denses présagent de difficultés à maintenir les infrastructures dans le temps alors que les développement plus denses sont plus viables financièrement. En même temps, la question fiscale ne peut être le seul paramètre à prendre en compte tant il serait facile de construire une forêt de tours d’habitation générant beaucoup de revenus mais nuisant à la qualité de vie d’ensemble.

Pour pousser la réflexion plus loin, il serait évidemment utile d’avoir les données permettant de modéliser plus finement les dépenses et surtout d’avoir les données pour l’ensemble du Grand Montréal. Il n'en reste pas moins que cette première analyse souligne que l’imposition que les villes doivent légalement appliquer tend à nous éloigner de milieux de vie soutenables et justes.


## Version complète (et plus nuancée)

En 2017, un article de StrongTowns, brutalement titré [The reason your city has no money](https://www.strongtowns.org/journal/2017/1/9/the-real-reason-your-city-has-no-money), m'a frappé comme il a frappé l'esprit de plusieurs: une [analyse](https://www.urbanthree.com/case-study/lafayette-la/) de la ville de Lafayette en Louisiane, réalisée par la firme [Urban3](https://www.urbanthree.com/), soulignait combien les quartiers centraux, denses et souvent relativement modestes génèrent plus de revenus fonciers que de dépenses tandis que les quartiers périphériques et plus aisés étaient des gouffres d'argent public. Leur conclusion était sans appel: en poursuivant le modèle dominant de développement urbain depuis l'après-guerre, les villes américaines s'enlisent financièrement.

Depuis cette époque, j'espérais voir une analyse similaire pour Montréal en me demandant quel serait le résultat considérant le contexte de Montréal avec une mixité possiblement supérieure mais aussi des formes urbaines très variées: de très dense au centre à clairsemé dans ses arrondissements le plus éloignés.

En tant que responsable des données ouvertes de la Ville de Montréal, j’ai bien essayé de prioriser la publication des données nécessaires à une telle analyse, mais bon, je ne pouvais pas non plus mettre de l'avant mes intérêts personnels dans la priorisation. Quand j'ai quitté la Ville, les terrains d'unité d'évaluation foncières avaient été publiés mais il manquait encore le montant de taxes. Heureusement, l'équipe des données ouvertes a poursuivi son travail acharné -et je leur lève mon chapeau trois fois. Ceci a permis de sortir les données tant espérées

Cet article présente donc le résultat d'une première analyse spatiale de la contribution au budget de la ville. Le modèle ne peut pas être aussi poussé que celui d'Urban3 fautes d’avoir les données de dépenses assez détaillées. Enfin ceci est le travail d’un amateur de la chose urbaine et je partage ces analyses ici pour ouvrir la discussion sur le sujet. Les conclusions ressemblent à celles de Urban3, avec plusieurs bémols toutefois.

Avant de me lancer dans le contenu, j’ajoute qu’en cours d’analyse, l’équipe d’[Anagraph](https://anagraph.io/), spécialisée en méthodes d’analyse géospatiale, a bien voulu contribuer en temps et en outils. Cela a permis d’assurer une certaine qualité dans le traitement tout en ajoutant certains outils d’analyse que je vais pointer par moment.


## Une vue à 30 000 pieds d’altitude
En l’absence de données de dépenses géolocalisées, j’ai utilisé un proxy pour évaluer les revenus par “unité de dépense d'infrastructure", à savoir des kilomètres linéaires de rue. Pour le dire plus concrètement: pour l'analyse principale, je vais évaluer le nombre de dollars générés par mètre linéaire de rue dans différents secteurs. Dans une section de discussion des résultats, je vais élaborer un peu plus en détail ce choix mais pour l'expliquer le plus simplement possible, un mètre de rue représente une approximation facile pour les dépenses les plus liées à la forme de la ville, notamment voirie et réseaux d’eaux qui représentent 55% du budget d’investissement de la ville. Ceci va donner des dollars de revenu foncier par mètre linéaire de rue qui seront regroupés par quartiers, en l’occurrence les aires de dissémination de Statistique Canada. 

Avant d'entrer dans la présentation des résultats, il est important de préciser que cette analyse n'est pas une critique ou une reconnaissance du mode de vie en fonction d'où vivent  les gens, ce n'est pas une critique sociale. C'est une contribution à la réflexion sur les politiques publiques, plus précisément quels sont les incitatifs et les contradictions créés par les politiques en place et l'impôt foncier en particulier. 

### Quelques statistiques d'ensemble

Les données d'unité d'évaluation foncière permettent de catégoriser chaque unité en fonction de son usage: résidentiel, commercial, industriel, etc. Le gros de la discussion sur les villes se concentre sur le résidentiel; c'est effectivement ce qui a le plus d'impact sur tout un chacun. Toutefois, le résidentiel n'est qu'une partie de l'histoire puisque que seulement la moitié des revenus viennent du résidentiel (1.8G$ pour le résidentiel et le même chiffre pour le non résidentiel). Le non-résidentiel a donc une part non négligeable qui mériterait aussi d’être analysé.

Pour donner une idée du volume, nous avons 499 784 unités foncières, d’une valeur de 226G$ et rapportant 3.6G$ pour 2021. Petite précision ici: on parle bien de la Ville de Montréal, ce qui exclut donc les villes dites liées: Ville Mont-Royal, Westmount, Baie d'Urfé et une douzaine d'autres.


![Répartition des revenus fonciers par type d'usage]({{ root_url }}/images/2022-05-30_Repartition_par_usage.png)
<div class="photoattrib">Répartition des revenus fonciers par type d'usage pour la Ville de Montréal</div>


### Dans le vif du sujet

J’explique dans la section méthodologie comment j’obtiens les résultats ci-dessous pour ceux que cela intéresse. À partir de là, le plus simple est de sauter directement les résultats avec des représentations graphiques. 


![Revenus fonciers par km de rue]({{ root_url }}/images/2022-05-30_taxe_tot_ratio.jpg)
<div class="photoattrib">Tous revenus fonciers par kilomètre de rue</div>

Pour comprendre carte: autant la couleur que la hauteur des blocs sont fonction des revenus fonciers par mètre de rue linéaire. En d’autres termes, ce qui est haut et blanc-jaune génère beaucoup de revenu par mètre de rue, en l’occurrence plus de 25 000$/m pour les zone les plus élevées, tandis que les zones rouge-ocre sont celles qui en génèrent le moins. Le rouge le plus sombre s’applique à des revenus de moins de 300$/m de rue. Chaque zone correspond à une aire de dissémination de Statistique Canada. Les aires de dissémination sont définies pour représenter à la fois une fourchette de population (entre 300 et 1500) et avoir une certaine cohérences socio-démographique. Le premier critère explique pourquoi certaines aires sont très étendues géographiquement: elles représentent relativement peu de monde, soit du fait que ce sont des zones industrielles, des parcs ou toute autre raison.

La première chose qui saute aux yeux: la contribution sans commune mesure du Centre-Ville dans les revenus municipaux. Cette première visualisation comprend tous les types de revenus fonciers et clairement les tours à bureaux et les commerces sont une source importante de revenus fonciers. On comprendra, à juste titre, les préoccupations de nombreux acteurs concernant la santé du Centre-ville dans un contexte (post-)pandémique. Évidemment, il y a du résidentiel au centre-ville, mais c'est avant tout le commercial qui pèse lourd dans la balance. L'aire de dissémination qui rapporte le plus par mètre de rue comprend plusieurs des principales tours à bureau de Montréal, dont la tour Ville-Marie. En fait le Centre-Ville génère tellement de revenu, qu'il "écrase" tout le reste et ça rend difficilement intelligible le reste des résultats.

On notera aussi la contribution notable des secteurs industriels de Saint-Laurent, le port de Montréal, et le secteur de l’intersection entre le 40 et la 25, des zones assez étendues car industrielles et qui vont "disparaître" quand on va se concentrer sur les revenus résidentiels.

Étant donné qu’une large partie de la discussion publique entoure le résidentiel, il est possible de sortir les revenus de bâtiments non-résidentiels de la représentation.

Donc si on retire le non résidentiel de l’équation, nous obtenons ceci:


<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap" style="margin-bottom: 10px">
  <iframe src="https://kepler.gl/demo/map/carto?mapId=a0672617-9f1c-a9c6-0f0a-74d0cf4613b7&owner=sguidoin&privateMap=false" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>
<div class="photoattrib"><br/>Visualisation 3D interactive des revenus fonciers résidentiels par kilomètre linéaire de rue selon les aires dissémination. Pour changer la perspective 3D, appuyez sur la touche *Ctlr* en même temps que vous déplacez la souris. Accès en <a href="https://kepler.gl/demo/map/carto?mapId=a0672617-9f1c-a9c6-0f0a-74d0cf4613b7&owner=sguidoin&privateMap=false">plein écran</a></div>


Ici, on peut se permettre de comparer des pommes avec des pommes: les revenus générés par des gens qui ont besoin de se loger. Commençons par quelques constats avant de discuter de la conséquence de ce qu’on voit:

Le Centre-ville demeure un centre de revenu important. Toutefois, ici nous avons un Centre-ville plus étendu qui s’étire aux arrondissements adjacents: Le Plateau—Mont-Royal, Rosemont—La-petite-Patrie, Le Sud-Ouest, Outremont, Cote-des-neiges, ou encore l’Île-des-soeurs.

Les quartiers périphériques rapportent généralement moins de revenu par mètre de rue, à quelques exceptions près. Comme on va le voir après, ces exceptions dans les quartiers périphériques sont parfois des artéfacts de données mais sont souvent liés à des espaces plus denses, par exemple des blocs appartements.
Globalement on ne peut qu’être frappé par l’ampleur des différences entre les aires le plus « productives » et celles qui le sont moins, allant de 8000$/m à parfois moins de 100$/m.

Le portrait d’ensemble est tout de même semblable à celui obtenu par Urban3: les quartiers centraux et denses génèrent nettement plus de revenus par unité d’infrastructure urbaine que les quartiers moins denses. Toutefois, cette similitude vient avec un certain nombre de bémols que je couvre plus bas.

[Anagraph](https://anagraph.io/) a développé une méthode permettant de découper le territoire selon des hexagones de taille fixe et d’y projeter des valeurs comme les revenus fonciers. Cette approche permet d’avoir une visualisation plus cohérente, évitant d’avoir des aires de tailles très variées; cela évite aussi certains artefacts de données liés au découpage des aires de dissémination. Toutefois, cela introduit aussi des effets de bords et peut amener à perdre, par exemple, l’uniformité socio-démographique qu’amènent les aires de dissémination. Bref, aucune approche n’est parfaite. La visualisation ci-dessous montre les données de revenus de taxe foncière brutes (*sans* ratio par kilomètre de rue) pour tous les usages et pour le résidentiel seulement; la même échelle est utilisée dans les deux cas, ce qui permet de constater l'impact du non-résidentiel.

<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap" style="margin-bottom: 10px">
  <iframe src="https://urban-dev-29e2f.web.app/" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>
<div class="photoattrib"><br/>Visualisation 3D interactive des revenus fonciers développée par Anagraph. Maintenir la touche <i>Ctrl</i> en déplaçant la souris pour changer le point de vue. Accès en <a href="https://urban.anagraph.io/">plein écran</a></div>

### Les revenus fonciers et les revenus familiaux

L’argumentaire de Urban3 repose en partie sur le fait que les quartiers centraux sont plus modestes et pourtant génèrent plus de revenus. Toutefois, Urban3 ne fournit pas vraiment de démonstration en se contentant d’une analyse géospatiale sans coupler avec des données socio-démographiques. Considérant que Montréal présente possiblement une plus grande mixité sociale dans ses quartiers (du moins c’est une hypothèse plausible), on ne peut pas se contenter de dire que les quartiers centraux sont généralement plus modestes, L’avantage d’utiliser les aires de dissémination de Statistique Canada comme découpage, c’est qu’il est possible de conjuguer les données foncières avec des indicateurs socio-démographiques. 

L’équipe d’Anagraph a eu la gentillesse de me partager un ensemble de données qu’ils ont monté permettant de mettre les revenus fonciers en rapport avec le revenu médian après impôt des ménages dans chaque aires de dissémination .

Si on fait une régression linéaire, à l’échelle des aires de dissémination entre ces deux variables, on obtient un nuage de point sans tendance visibles. En calculant le facteur de corrélation on obtient -0.17, ce qui est une absence de corrélation (ou si corrélation il y a, c’est très faible). L’absence de corrélation signifie que peu importe le revenu des ménages, chacun paie *en moyenne* une part à peu près égale. La majorité des politiques publiques essaient d’avoir un effet progressif, c’est-à-dire que les personnes aisées contribuent plus que celles qui le sont moins. Avec cette première régression, il apparaît assez clairement que la taxe foncière n’est pas progressive.

Pour pousser l’investigation un peu plus loin, j’ai essayé de faire des regroupements par fourchettes de salaire médian et ici on obtient un portrait plus intéressant qu’une régression linéaire ne peut effectivement pas capter:


![Contribution foncière en fonction du salaire]({{ root_url }}/images/2022-05-30_contribution_salaire-1.png)
<div class="photoattrib">Contribution foncière en fonction du salaire médian des ménages après impôts</div>


Pour comprendre le graphique: chaque point (bleu) correspond aux revenus fonciers moyens des aires de dissémination correspondant à une fourchette de revenus médians de ménage après impôt. Par exemple, les aires de dissémination où les ménages ont un revenu médian entre 75k$ et 80k$ génèrent un revenu foncier moyen de 500$ par mètre de rue. 

Les barres verticales jaunes fournissent une indication du nombre d’aires de dissémination pour chaque fourchette de revenus familiaux; par exemple il y a plus de 500 aires de dissémination où le revenu familiale est compris entre 40k$ et 45k$. Les revenus au-dessus de 100k$ sont groupés en une seule catégorie. Comme on peut le voir, dans la moyenne, les tranches de revenus faibles ont une surcontribution et globalement, chaque tranche de revenu contribue moins que celle qui la précède. Il y a seulement dans la tranche au-dessus de 90k$ que la tendance remonte un peu. De manière générale, la tranche à moins de 40k$ contribue 30% plus que la tranche 55k$ - 90k$. Je rappelle qu’on parle d’un ratio de contribution par mètre linéaire de rue, donc individuellement les foyers à revenus élevés plus d'impôts fonciers, mais collectivement ils ont moins d’impact dans le financement des infrastructures municipales (des exemples concrets plus bas vont venir expliquer cela).

Comme on a pu le voir dans les visualisations précédentes, on note une forte disparité géographique entre un centre-ville étendu et les zones plus périphériques. Il est possible d’essayer de représenter celle-ci de manière statistique. De manière visuelle, il m’a semblé que ce centre-ville étendu s’étire de manière concentrique à partir du Mont-Royal à peu près. J’ai donc divisé les aires de dissémination, de manière quelque peu arbitraire, entre celles à moins de 7km du Mont-Royal et celles à plus de 7km, ce qui donne ceci:

![Contribution foncière en fonction du salaire]({{ root_url }}/images/2022-05-30_contribution_salaire-2.png)
<div class="photoattrib">Contribution foncière en fonction du salaire médian des ménages après impôts selon la proximité au centre de la ville</div>



Beaucoup à dire sur ce graphique. D’abord, on confirme la contribution des quartiers plus centraux, mais ce n’est pas vraiment une surprise. Ce qui est plus intéressant, c’est la forme des courbes: pour les zones plus centrales, nous avons encore une contribution forte des foyers avec des revenus faibles (moins de 35k$); toutefois nous observons une contribution forte des salaires de plus de 60k$. Il faut prendre les chiffres entre 80k$ et 95k$ avec des pincettes car le nombre d’aires de dissémination considéré est très faible. Toutefois, pour les aires de dissémination où les foyers ont des revenus supérieurs à 60k$, la contribution foncière moyenne est de 1242$/m, alors que pour la tranche 25k$-60k$, c'est moins de 1000$/m

Portrait très différent dans les zones périphériques où la courbe de contribution est constamment à la baisse, avec une régularité très claire. Seuls les revenus de plus 100k$ arrivent, de peu, à renverser cette tendance.

Dans la section discussion, je vais amener certains bémols liés à mes hypothèses mais dans l’ensemble, on peut tirer deux grandes conclusions:
- Premièrement, on confirme de manière plus statistique la surcontribution des quartiers centraux;
- Deuxièmement, on note, à la grandeur du territoire, une certaine regressivité de la contribution foncière, c’est-à-dire une plus grande contribution des revenus les plus faibles. Toutefois, cette tendance à la regressivité a une variable géographique et se manifeste surtout dans les quartiers périphériques.

En d’autres termes, pour reprendre un peu le vocabulaire de l’article de StrongTown, les infrastructures des quartiers riches *et* périphériques sont subventionnées par le reste de la population.

### Digression sur l’impôt foncier et les finances municipales

Avant d’entrer plus dans la discussion des résultats, il convient de parler de l’impôt foncier. Il est calculé sur base de la valeur du terrain et des bâtiments qui sont dessus. Des calculs complexes sont appliqués; par exemple pour chaque unité d’évaluation il y a en fait entre 5 et 10 taxes et taux qui s’appliquent: taxe de base, taxe de l’ARTM, taxe de l’eau, taxe spéciale, etc. À travers le temps, les édiles montréalais ont fait des tentatives pour moduler la taxation, et la rendre progressive. Par exemple, il y a un taux plus élevé pour les résidences d’une valeur supérieure à 750k$. 

Clairement cette taxe n’a pas été faite pour avantager ou désavantager certaines populations, pour être progressive ou régressive, c’est « juste » un mécanisme pour générer des revenus, un mécanisme par ailleurs assez vieux: Jules César avait créé l’Ostiarum, un impôt basé sur le nombre de portes et la France révolutionnaire l'Impôt sur les portes et fenêtres; des proxys intéressants pour évaluer la richesse des propriétaires.

Toutefois, beaucoup d'experts en finance municipale [critiquent](https://vivreenville.org/nos-positions/chroniques/2019/au-dela-de-la-dependance-des-municipalites-a-l-impot-foncier-mettre-fin-a-la-chaine-de-ponzi.aspx) la [dépendance](https://ici.radio-canada.ca/nouvelle/1797911/financement-immobilier-municipalites-etude-eve-lyne-couturier) des finances municipales à l'impôt foncier, notamment au Québec, ainsi que ses impacts sur le développement des villes. Tel que mentionné dans une série [d’articles](https://www.lapresse.ca/actualites/politique/2022-05-09/etalement-urbain/choc-entre-les-maires-et-la-caq.php) de presse récemment, l’impôt foncier crée toutes sortes de problèmes dont un incitatif fort au développement et à l'étalement urbain plutôt qu’au redéveloppement et à la densification. Comme on peut le voir dans la présente analyse, cet impôt ne tient pas compte de la forme urbaine et encore moins de la capacité de payer des résidents. Enfin, il est très peu paramétrable: pour garantir une impartialité (compréhensible), les facteurs pouvant être intégrés dans le calcul de l’impôt foncier sont très limités; par exemple, à ma connaissance, on ne peut pas faire varier le taux d’impôt foncier selon les revenus ou la nature locative d’un bâtiment. Bref, l’impôt foncier est l’ami (qui génère des revenus) que tout le monde aime détester.

Pour avoir une meilleure compréhension des besoins en revenus, il est utile d’avoir une petite perspective sur les dépenses. Et ces dépenses varient sur des échelles de temps très importantes. Des infrastructures comme les réseaux d’eaux (et par extension ce qui va « dessus », les routes) ont des cycles de vie qui s’étendent sur plusieurs décennies, souvent une bonne cinquantaine d’années quand ce n’est pas plus (il arrivait encore récemment de refaire des conduites d’eau centenaires faites en briques). Pour les parties plus centrales de Montréal, on est souvent au deuxième cycle de vie. Par contre, pour plusieurs quartiers, surtout au format banlieue, on n’est pas toujours rendu au terme du premier cycle. Ainsi la prise en compte du renouvellement de certaines des infrastructures les plus coûteuses n’est pas encore évidente pour les zones qui datent, mettons, des années 70 et postérieures. En d’autres termes, il semble souvent facile de développer de nouveaux quartiers qui vont rapporter des revenus rapidement… jusqu’au jour où il faut payer la dette d’infrastructure.

Enfin pour Montréal en particulier, l’allocation des revenus et des dépenses est en partie décorrélée. Plus spécifiquement, si tout le monde paie uniformément ses taxes à « la ville-centre », le budget est lui scindé, selon des paramètres, entre les arrondissements et certaines services centraux. Comme je [l’expliquais](/2014/09/24/proto-ville-intelligente/) dans un billet de blogue il y a déjà 8 ans, les paramètres d’allocation des budgets des arrondissements soulèvent déjà quelques questions, notamment dans sa répartition entre les quartiers centraux et les quartiers périphériques.


## Quelques nuances utiles

La présente section souligne que, malgré tous mes efforts, les résultats ci-dessus sont à prendre avec un grain de sel.


### Les bémols de l’analyse géospatiale

Le ratio revenu foncier / mètre de rue est intéressant mais a évidemment des limites. Outre qu'on pourrait me critiquer pour l'invention d'indicateurs étranges, tous les coûts d’opération et d’infrastructure de la ville ne sont pas liés à des kilomètres de rue: les coûts de sécurités publiques (plus gros poste de dépense), la culture ou encore la gestion des parcs ne sont pas nécessairement liés au nombre de kilomètres de rue. Donc le ratio utilisé ici permet d’analyser la contribution au financement de *certaines dépenses* municipales mais pas à l’ensemble du budget d’une ville. L’analyse de Urban3 était capable d’être plus globale. En prenant en compte ce bémol, la présente analyse donne toutefois une idée de la capacité de financement des infrastructures les plus coûteuses: routes, réseau d’eaux potables et usées. 

Cependant, même pour l’analyse de Urban3, il faut bien être conscient qu’il y a une limite à ce genre d’approche: comment bien intégrer l’usage (et la dégradation accélérée) des rues par les navetteurs? Comment modéliser et affecter les coûts de parcs utilisés par des personnes venant de partout? La présente analyse bénéficierait évidemment d’être approfondie avec une modélisation juste des dépenses et en même temps aucune modélisation ne pourra refléter la richesse de la vie urbaine et des coûts d’opération et de maintenance qui s’y rattachent.

J’ajoute qu’à ces limites méthodologiques, l’analyse présente des incohérences liées au découpage de Statistique Canada qui n’a pas été fait pour s’attarder au réseau routier. Ainsi, surtout dans les aires de petite taille (donc très denses), il arrive parfois que les rues adjacentes ne soient pas incluses, ce qui sort des ratios exagérément élevés du fait d’un dénominateur ridiculement petit. Pour deux aires de dissémination assez petites, j’ai même dû modifier manuellement le résultat du calcul car générant des résultats hors norme. Le découpage en hexagone d’Anagraph permet de contourner ce problème et, montrant un profil de résultat similaire, permet de conclure que l’analyse avec les aires des dissémination n’est pas aberrante non plus.

### Les bémols de l’analyse socio-démographique

Les données de Statistique Canada sont intéressantes, mais très agrégées aussi. Le revenu médian après impôt est une indication utile mais qui a ses limites (et pareil pour tous les indicateurs disponibles). Il faudrait beaucoup de temps pour être capable de faire une analyse plus poussée. Le revenu médian permet d’avoir une idée d’où se situe l’individu moyen d’un quartier même s’il y a une très grande hétérogénéité, ce qui est mieux que rien et permet d’avoir une tendance. 

### Sur l’utilisation des infrastructures en milieu dense

Un des principaux facteurs que je ne peux pas évaluer est de savoir si les infrastructures en milieu denses sont plus couteuses car plus complexes ou s’usent plus vite. Les rues en milieu dense sont effectivement plus utilisées, ça nécessite aussi plus d’artères; toutefois cet usage est autant si ce n’est plus un usage de transit qu’un usage local. Certes, les infrastructures d’eau nécessaires pour connecter une tour d’habitation sont sûrement plus coûteuses que celles pour un bungalow, mais dans quel ordre de grandeur?

Il m’est difficile de le dire, et c’est la principale faiblesse de la présente analyse. Une indication qu’on ne parle pas de différences significatives toutefois: les paramètres d’allocation de budget des arrondissements se basent surtout sur la quantité d’actifs et non sur le nombre de personnes desservies, par exemple. Comme vous pourrez le voir dans les exemples spécifiques ci-dessous, les ordres de grandeurs sont tels qu’il faudrait vraiment que les infrastructures en milieu denses coûtent incroyablement plus cher pour compenser les effets du manque de densité. 

## Quelques exemples concrets

Histoire de valider la solidité de l’approche et juste voir à quoi correspondent ces données, il est possible de prendre quelques secteurs représentatifs pour se faire une idée plus… visuelle! Encore une fois: le but n’est pas de pointer du doigt le style de vie d’untel ou unetelle, le but est de regarder ce que produit une politique publique particulière qu’est l’impôt foncier. Ces exemples concrets visent à incarner les statistiques ci-dessus.

En plus des indicateurs utilisés jusqu’ici, j’ajoute quelques autres données qui permettent de comprendre un peu mieux le mode d’habitation d’un quartier:

- Le nombre moyen d’habitants par logement
- L’empreinte au sol de chaque habitant, obtenu en prenant la somme des surfaces des terrains résidentiel divisée par le nombre d’habitant
- La valeur moyenne du compte de taxe par logement.

Pour commencer, si on regarde du coté de Saint-Laurent, à un jet de pierre d’un de l’autre, nous avons deux situations très différentes:



<table style="font-size: 85%; background: #fff;">
  <tr>
    <td>
      <img src="{{ root_url }}/images/2022-05-30_StLaurent_bungalow.jpg"/>
    </td>
    <td>
      <img src="{{ root_url }}/images/2022-05-30_StLaurent_bloc.jpg"/>
    </td>
  </tr>
  <tr>
    <td>
      Saint-Laurent - Bungalows
      <ul>
        <li>Revenu foncier par km: 261$/m</li>
        <li>Revenu médian après taxe des foyers: 56 576$</li>
        <li>Habitant par logement: 2.71</li>
        <li>Empreinte au sol par habitant: 117m<sup>2</sup></li>
        <li>Taxe par logement: 2626$/an</li>
      </ul> 
    </td>
    <td>
      Saint-Laurent - Blocs appartements
        <ul>
        <li>Revenu foncier par km: 2241$/m</li>
        <li>Revenu médian après taxe des foyers: 41 600$</li>
        <li>Habitant par logement: 1.99</li>
        <li>Empreinte au sol par habitant: 18.4m<sup>2</sup></li>
        <li>Taxe par logement: 959$/an</li>
      </ul>
    </td>
  </tr>
</table>
<br/>


D’un coté, une zone peu dense, avec des bungalows et des terrains assez généreux; de l’autre des “barres” d’immeubles assez denses et pas nécessairement très attirantes. Les bungalows génèrent un revenu foncier de 261$/mètre de rue tandis que le revenu médian après impôt des foyers est de 56 576$/an. Dans les tours, on obtient un revenu foncier de 2241$/mètre de rue, pour un revenu médian de 41600$. Dix fois plus de revenus par mètre de rue! Quant aux revenus des ménages, on se trouve dans le segment assez central de la fourchette, bien que la zone de bungalow jouisse de revenus 36% plus élevés.

Dans la visualisation 3D des revenus fonciers par mètre de rue, une bonne partie des “pics” (les zones plus hautes et plus claires) dans les secteurs hors du centre-ville étendu sont des zones à forte densité comme ici: tours d’habitation, blocs appartements et autres au milieu de zones généralement caractérisées par une densité moindre comme c’est le cas avec les bungalows.

---

<table style="font-size: 85%; background: #fff;">
  <tr>
    <td>
      <img src="{{ root_url }}/images/2022-05-30_Outremont Revenus_eleves.jpg"/>
    </td>
    <td>
      <img src="{{ root_url }}/images/2022-05-30_CDN_faibles_revenus.jpg"/>
    </td>
  </tr>
  <tr>
    <td>
      Outremont - Quartier à hauts revenus
      <ul>
        <li>Revenu foncier par km: 1543$/m</li>
        <li>Revenu médian après taxe des foyers: 105 856$</li>
        <li>Habitant par logement: 2.48</li>
        <li>Empreinte au sol par habitant: 91m<sup>2</sup></li>
        <li>Taxe par logement: 4934$/an</li>
      </ul> 
    </td>
    <td>
      Cote-des-Neiges - Quartier à faibles revenus
        <ul>
        <li>Revenu foncier par km: 618$/m</li>
        <li>Revenu médian après taxe des foyers: 34 355$</li>
        <li>Habitant par logement: 1.94</li>
        <li>Empreinte au sol par habitant: 26.7m<sup>2</sup></li>
        <li>Taxe par logement: 930$/an</li>
      </ul>
    </td>
  </tr>
</table>
<br/>

Si on se tourne vers un quartier un peu plus central: Outremont et Cote-des-neiges. Là aussi à un jet de pierre l’un de l’autre, deux réalités très différentes: un quartier riche, avec un revenu médian par foyer de 105 856$ mais aussi une certaine densité, relativement peu de terrain, générant 1543$/m de rue; significativement plus que les bungalows de Saint-Laurent. Non loin de là, un secteur avec des revenus de ménage significativement plus faibles à 34 355$/an, des habitations en appartement moins serrées que des barres d’immeuble, avec une élévation assez limitée (3-4 étages) et produisant des revenus fonciers de 618$/mètre de rue, un chiffre plus faible que le quartier voisin mieux nanti à côté, mais toujours significativement plus élevé que les bungalows.

---

<table style="font-size: 85%; background: #fff;">
  <tr>
    <td>
      <img src="{{ root_url }}/images/2022-05-30_ile-bizard.jpg"/>
    </td>
    <td>
      <img src="{{ root_url }}/images/2022-05-30_parc-ex.jpg"/>
    </td>
  </tr>
  <tr>
    <td>
      Île-Bizard - Quartier à hauts revenus excentré
      <ul>
        <li>Revenu foncier par km: 284$/m</li>
        <li>Revenu médian après taxe des foyers: 112 640$</li>
        <li>Habitant par logement: 3.21</li>
        <li>Empreinte au sol par habitant: 261m<sup>2</sup></li>
        <li>Taxe par logement: 4384$/an</li>
      </ul> 
    </td>
    <td>
      Parc-Extension - Quartier à faibles revenus plus central
        <ul>
        <li>Revenu foncier par km: 918$/m</li>
        <li>Revenu médian après taxe des foyers: 25 232$</li>
        <li>Habitant par logement: 1.66</li>
        <li>Empreinte au sol par habitant: 23.8m<sup>2</sup></li>
        <li>Taxe par logement: 967$/an</li>
      </ul>
    </td>
  </tr>
</table>
<br/>


Maintenant, allons dans le secteur le plus éloigné de Montréal: L’île-Bizard. Je me permets d’aller dans ce coin car pour y être allé marché, je n’avais pu que constater les développements type McMansion, des maisons dont l’évaluation foncière dépasse souvent allègrement le million. C’est d’ailleurs cohérent avec les revenus moyens, de l’ordre de 112 640$/an. Et si les revenus fonciers sont supérieurs au secteur des bungalows de Saint-Laurent, c’est de peu, soit 284$/m.

Comme le montre cet exemple, en matière de revenu foncier, la valeur élevée d’une maison ne peut pas compenser une forme urbaine peu dense. Même si les propriétaires de ces maisons trouvent qu’individuellement ils payent beaucoup d'impôt foncier, 4384$ annuellement en moyenne, collectivement ils représentent des quartiers qui ont plus de difficultés à couvrir les dépenses d’infrastructures communes. À noter que la valeur de compte de taxe ici est similaire au quartier aisé d'Outremont ci-dessus, mais avec un niveau d'"étalement" nettement plus important: tandis que l'empreinte au sol par habitant est de 91m<sup>2</sup> pour Outremont contre 261m<sup>2</sup> pour L'Île-Bizard.

À l’autre bout du spectre des revenus, le secteur Acadie de Parc-Extension. Des logements compacts mais avec une élévation limitée (3 niveaux). Des revenus des ménages très modestes à 25 232$/an, parmi les plus bas de Montréal, et une contribution financière de l’ordre de 918$/mètre de rue, soit nettement plus que les deux quartiers à faible densité de Saint-Laurent ou L’Île-Bizard

---

<table style="width:50%; font-size: 85%; background: #fff; margin:auto;">
  <tr>
    <td>
      <img src="{{ root_url }}/images/2022-05-30_centre-ville.jpg"/>
    </td>
  </tr>
  <tr>
    <td>
      Centre-Ville
      <ul>
        <li>Revenu foncier par km: 3323$/m</li>
        <li>Revenu médian après taxe des foyers: 24 256$</li>
        <li>Habitant par logement: 1.3</li>
        <li>Empreinte au sol par habitant: 12.3m<sup>2</sup></li>
        <li>Taxe par logement: 1446$/an</li>
      </ul> 
    </td>
  </tr>
</table>
<br/>


Enfin on ne peut faire l’impasse sur le Centre-ville produit beaucoup de revenus fonciers avec des revenus médians passablement bas. Ici, une secteur représentatif autour de l’Université Concordia avec des revenus de 24 256$ pour une contribution record de 3323$/mètre de rue. La logique est un peu similaire au secteur Acadie, mais encore plus exagérée qui, comparé à l’Île-Bizard, pour un revenu de foyer 4 fois inférieur contribue presque 12 fois plus aux revenus municipaux! Pour mémoire, bien que nous soyons dans le centre-ville, avec une forte présence de commerces, les chiffres ici se limitent aux revenus résidentiels!

J’ai volontairement pris quelques exemples extrêmes tout en me limitant à creuser certains secteurs que je connais un peu pour m’y être rendu et parce que sur l'analyse cartographique ils étaient représentatifs de certaines tendances.

### Propriétaires, locataires, étudiants et ménages

Je profite de ces cas concrets pour faire un petit détour sur un autre bémol: propriétaires et locataires. Il n’existe, à ma connaissance, aucune information sur le statut de location d’une unité. On peut toutefois parier que les blocs appartements comme ceux dans les “barres” de Saint-Laurent ou encore dans les exemples de Côte-des-neiges, Acadie et du Centre-Ville sont occupés par des locataires. 

On pourrait ainsi rétorquer que ce n’est pas la personne qui réside (et dont on a le revenu médian) qui paie la taxe foncière mais bien le propriétaire, qui lui ne figure pas dans les indicateurs de Statistiques Canada. Ceci est juste, mais je fais ici l’hypothèse que le propriétaire n’est pas dans une démarche altruiste: il paie des taxes foncières parce qu’il a des locataires qui lui permettent de financer sa propriété. En d’autres termes, les locataires paient l'impôt foncier bien qu'indirectement.

Autre élément qui mélange sûrement les choses: les étudiants. L’exemple dans le Centre-Ville, proche de Concordia, n’est pas évident. Il y a dans le secteur des blocs clairement dédiés aux étudiants qui ont évidemment des revenus faibles. Ont-ils des bourses? Ont-ils des jobs étudiantes? Sont-ils aidés par leurs parents? S’endettent-ils? Impossible à dire évidemment. Mettons qu' ici, on peut s’arrêter au fait qu’a priori ce n’est pas la population qui a le plus de revenus discrétionnaires. Malgré tout, là encore, ils contribuent (indirectement) de manière significative aux revenus de la ville.

Enfin, la statistique de revenu utilisé, le revenu *par ménage* soulève des questions sur le nombre de personnes par ménage. Une grande maison a plus de chances d’abriter une famille, potentiellement avec deux adultes à revenus alors qu’un logement au centre-ville peut ne contenir qu’un étudiant… à moins que ce soit 3 étudiants en colocation! Ainsi, dans les exemples au-dessus, le quartier de l'Île-Bizard avait une moyenne de 3.21 habitants par logement alors que pour Parc-Extension et le Centre-ville c'était respectivement 1.66 et 1.3.

Là aussi je vais fournir une rapide indication que le nombre d’habitants dans une maison est certes important mais ne reverse pas les conclusions. J’ai fait une analyse complémentaire en calculant les revenus par mètre carré habitable et *par habitant*. Mis sur une carte nous obtenons ceci: 

![Revenus fonciers par metre carré par habitant]({{ root_url }}/images/2022-05-30_empreinte_habitant.jpg)
<div class="photoattrib">Revenus fonciers par metre carré par habitant</div>

Les zones les plus claires représentent des revenus inférieurs à 2$/m<sup>2</sup>/habitant, tandis que les zones plus foncées sont autour de 20$/m<sup>2</sup>/habitant. Encore une fois, on note des différences très significatives, même en intégrant le fait que les quartiers périphériques ont généralement plus d’habitant par logement.


## Conséquence sur les politiques publiques

Après avoir couvert beaucoup de terrain, nous revenons aux conclusions d’Urban3 et StrongTowns qui voient dans les résultats obtenus des recommandations assez claires. Ici, je vais marcher sur des œufs car c’est vraiment un terrain glissant et complexe.

Leurs principales recommandations tournent autour de deux axes:

- Renforcer la qualité des infrastructures dans les quartiers modestes, ce qui aurait pour effet d’augmenter la valeur foncière et générer donc plus de revenu pour la ville.
- Densifier.

Le premier point vient d’une hypothèse: les infrastructures dans les centre-villes sont plus usées, ce qui nuit à la valeur foncière des immeubles et donc à la quantité de taxes générées. À contrario, les zones excentrées, souvent plus récentes, sont souvent en meilleur état. Ainsi le potentiel de gain en taxe foncière pour chaque dollar investi est plus élevé dans les quartier centraux. 

Évidemment d’un point de vue des finances de la ville, cela parait très logique… mais à quel coût pour les populations qui y vivent? À n’en pas douter, une augmentation de la valeur foncière serait repassée à ceux qui sont souvent des locataires et qui ont le moins de capacité à payer. En même temps est-ce juste de laisser ceux qui contribuent le plus aux finances publiques dans des infrastructures plus désuètes?

Donc en théorie, il semblerait intéressant de mettre plus d’effort dans les infrastructures des quartiers denses notamment parce qu’ils contribuent plus. Mais il semble difficile d’aller dans cette direction sans réfléchir aux impacts.

Quant à la densification, le sujet est chaudement discuté actuellement au Québec. Les endroits qui génèrent le plus de revenus dans les exemples ci-dessus sont des immeubles massifs, dépassant volontiers 10 étages. Or, lisez Jan Gehl ou Jane Jacob: la hauteur a un coût élevé sur la qualité de vie. Les discussions actuelles sur le sort du bassin Peel où les promoteurs immobiliers [demandent](https://journalmetro.com/actualites/montreal/2807024/bassin-peel-developpeurs-dont-devimco-disent-baillonnes/) de pouvoir construire plus haut sont parlantes. Bizarrement, les élus se retrouvent à défendre une position qui enlève, a priori, des revenus à la Ville; ce n’est probablement pas pour ruiner la ville mais plus lié à la connaissance de l’impact des constructions résidentielles élevées sur la dynamique locale que les élus agissent ainsi.

Bref, densifier, certes, mais en respectant un espace qui respire. Parmi les exemples exposés ci-dessus, celui qui semble le plus en ligne avec les principes urbanistiques et architecturaux est celui de Parc-Extension avec des constructions sur 3 niveaux et de l’espace pour des arbres et un peu de verdure. Évidemment, je ne juge pas l’intérieur de ces bâtiments, ni leur qualité de construction, mais vu de l’extérieur et en regardant les revenus générés, ça semble un équilibre intéressant. Cette notion d’équilibre est importante: le but n’est pas de générer le maximum de revenus, le but est de couvrir les coûts de fonctionnement de la Ville permettant de livrer des services de qualité et pour tous. La modélisation géospatiale des coûts apporterait sans nul doute une compréhension plus approfondie permettant de définir un niveau de revenu nécessaire pour couvrir les frais d’opération en fonction des différentes formes urbaines.

Enfin, il est important de souligne que le champ de bataille est beaucoup plus vaste que Montréal. Si Montréal offre une large variété de formes urbaines et donc la possibilité d’explorer l’effet de la fiscalité foncière sur ces différentes forment, il n’en reste pas moins que les zones à développer y sont rares et le prix des terrains incite déjà (trop?) à la densification pour les promoteurs. Le potentiel de réflexion est plus aigu pour les régions périphériques à Montréal et plus généralement à l’ensemble des villes en croissance: comment développer de manière responsable (financièrement) et humaine.

On voit plusieurs articles de presse soulignant d’un coté des maires conscients des enjeux, ne serait-ce que d’un point de vue environnemental, [volontaires pour densifier](https://www.lapresse.ca/actualites/grand-montreal/2022-05-31/saint-jerome/on-veut-densifier-notre-centre-ville.php) et de l’autre coté un [enjeu d’acceptabilité](https://www.lapresse.ca/actualites/grand-montreal/2022-05-18/saint-bruno-se-densifiera-loin-de-son-centre-ville.php) (sur lequel surfent d’autres élus) pour maintenir le statu quo d’une faible densité. Le présent article démontre, je l’espère, les conséquences d’une faible densité: ce n’est pas viable financièrement et ce n’est pas socialement juste en plus d'être un frein à un avenir sobre en carbone.

 La difficulté, c’est d’avoir des discussions informées et approfondies sur ces sujets complexes et… passablement ennuyeux. Il est possible d’avoir des quartiers vivants et assez denses. Ce n'est pas tout rien: la monster house avec garage triple *ou* un champ morne de tours anonymes de 20 étages. Montréal et d'autres villes à travers le monde regorgent d'équilibres intéressants, denses *et* agréables; des [articles](https://www.lapresse.ca/contexte/2022-05-29/urbanisme/pour-une-densification-heureuse.php) s'en font écho. Les données ressorties montrent que des quartiers avec des constructions à 3-4 étages, même dans des secteurs assez modestes peuvent générer des revenus significatifs. Ce type de construction, que certains comme Jan Gehl nomment « à échelle humaine », ont tout le potentiel pour créer de milieux de vie résilients et agréables à vivre. L'insertion de quelques tours peut se faire lorsque bien réfléchi et planifié. La difficulté est de ne pas se contenter de formules simplificatrices et de trouver le temps et les moyens pour impliquer la population, non pas pour savoir si la densification est opportune, mais plutôt comment *bien* la faire.


## Conclusion

Comment assurer la pérennité des finances des villes? Comment contribuer à une qualité de vie urbaine? Comment limiter et faire face aux changements climatiques? Pour bien des personnes (et j’en suis), la “forme” des villes est un facteur important pour toutes ces questions. Mais comme pour toute question complexe, les réponses simples sont souvent mauvaises.

La présente analyse a été réalisé en quelques (dizaines d’) heures par un amateur à l’intersection de différents champs de pratique: analyse de données, gestion des villes, urbanisme. Pour avoir une réelle clarté, il faudrait que des experts de chacun de ces champs (incluant aussi la fiscalité, la finance, etc.) y passent des centaines d’heures. Toutefois on voit ressortir quelques tendances.

En premier lieu, les analyses réalisées par Urban3 semblent se confirmer à Montréal. En l’absence de données de coûts, on ne peut être certain de la balance finale, mais les quartiers denses génèrent significativement plus de revenus fonciers. La proximité au centre de Montréal joue un rôle, mais plus du fait de la forme que de la proximité à proprement parler: des résidences proches l’un de l’autre (donc également proche du centre) peuvent générer des revenus très différents selon leur forme. C’est donc plus la forme urbaine qui est le facteur déterminant.
 

Dans ce contexte, les personnes à revenu plus modestes, qui ont tendance à se loger dans des appartements, contribuent (indirectement) de manière disproportionnée aux revenus municipaux tandis que les personnes plus aisées et surtout lorsqu’elle décident de s’établir un peu plus loin, avec des terrains plus généreux, ne contribuent que très peu.

Est-il possible de renverser la tendance? Avant de chercher à renverser une tendance, il faudrait confirmer les conclusions. Advenant qu’elles se confirment? Deux avenues: l’existant et le nouveau.

Pour le nouveau, il est certain que c’est un signal à la densification. D’un point de vue financier en tous cas, l’avantage est évident. Toutefois, il faut aussi être attentif à conserver des quartiers agréables. C’est pour cela que le critère financier ne peut être le seul critère de réflexion. On notera que des quartiers récents, avec une élévation importante, comme Griffintown, génèrent beaucoup de revenus, mais pas de manière démesurée par rapport à des quartiers comme le Plateau–Mont-Royal (1600-3200$/m contre 1000-2200$/m), sachant que les données socio-démographique pointent vers des revenus familiaux médians significativement plus élevés dans Griffintown.

Pour l’existant? La recommandation d’Urban3 d’investir dans les infrastructures publiques dans les quartiers denses ou modestes est sans nulle doute intéressante du point de vue financier: d’abord il y aurait là une certaine logique considérant que ces quartiers contribuent largement (une forme d’utilisateur-payeur renversé), toutefois l’objectif visé (réhausser la valeur des logements) aurait un effet évident sur les résidents les plus vulnérables… surtout dans le contexte actuelle de flambée de prix. Une telle approche devrait donc se combiner avec une protection des résidents vulnérables: les locataires certes, mais aussi certains propriétaires pour qui une hausse de la valeur foncière serait difficile à absorber.

En complément, il serait possible de faire évoluer progressivement la taxe foncière pour prendre en compte des paramètres physiques: densité, taille, etc. Là aussi, ce n’est en aucun cas une solution magique, ça soulève le même genre d’enjeu que le point précédent mais permettrait de rétablir une logique à tout le moins dans les contributions. À cela s'ajoute les possibilités de diversification des revenus afin de réduire la représentation de la valeur foncière dans les budgets municipaux.

Toutes ces questions permettent d'ouvrir sur une multitdes d'enjeux connexes: transition écologique, résilience et entraide locale, crise du logement et même identité: qu'est-ce qui nous constitue? Qu'est-ce qui nous lie? Volontairement, je ne rentre pas dans ces considérations étant donné la longueur déjà exagérée de ce billet. Toutefois, la fiscalité municipale est un facteur sous-jacent de tous ces enjeux.

Pour finir, je vais redire que le but n’est pas de pointer du doigt telle personne ou la maison dans laquelle elle vit. La question fondamentale est de savoir comment créer des expériences de vie riches et agréables en ville et cela de manière durable, y compris financièrement. Je suis de ceux qui ont vécu péniblement la pandémie faute d’espace extérieur pour mes enfants. L’idée n’est donc pas de dire que tout le monde doit vivre dans des tours de 20 étages. 

L’idée est d’envisager la meilleure forme possible pour nos villes: offrir un confort de vie pour tous, notamment via des espaces partagés agréables, bien maintenus et donc fonctionnant dans un cadre financier viable. L’équilibre budgétaire ne doit pas dicter la forme de la ville, au risque d’en dénaturer l’essence, mais doit être un critère de design, un facteur de politique publique permettant d’atteindre un cadre de vie riche et attirant financé de manière juste et cohérente. La présente analyse haut niveau montre que la situation actuelle ne répond pas à ces critères et va plutôt dans le sens inverse.


## Un peu de méthodologie

### Ensembles de données utilisés

- [Données de taxes foncières](https://donnees.montreal.ca/ville-de-montreal/taxes-municipales)
- [Unités d’évaluation foncière](https://donnees.montreal.ca/ville-de-montreal/unites-evaluation-fonciere)
- [Réseau routier de la ville de Montréal](https://donnees.montreal.ca/ville-de-montreal/geobase)
- [Aires de distribution de Statistique Canada](https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-fra.cfm)
- Données socio-démographiques de Statistique Canada selon le recensement de 2015, assignées aux aires de distribution (monté et fourni par Anagraph)

### Version simplifiée des étapes de traitement des données

Le point de départ sont les données de taxes disponible qui doivent être sélectionnées pour seulement une année (en l’occurrence 2021) puis de faire la somme des différentes taxes appliquée à un même unité. Ensuite cette sommation des taxes pour une année peut être combinées avec les unités d’évaluation foncière par la clé qui est l’identifiant d’unité foncière qui est présent dans les deux ensembles. Avec cela il est possible d’avoir pour chaque unité: le territoire géographique couvert par l’unité, l’usage et les taxes.

Comme il peut y avoir plusieurs unités sur un même terrain (condos, etc.), il faut ensuite regrouper et donc sommer les valeurs de taxe foncière par polygone au sol. Ainsi nous obtenons une somme de taxes pour différents polygones. Comme cette somme cumule des données résidentielles et non résidentielle (par exemple un même bâtiment ayant au rez-de-chaussée un commerce et à l’étage au-dessus un appartement), il faut, pour chaque enregistrement, un champ pour les taxes résidentielles et un champ pour les taxes non-résidentielles.

En parallèle, en partant des données du réseau de voirie, j’ai exclu les voies hors budget municipal: autoroutes et voies privées. À cause du découpage de Statistique Canada qui ne suit pas toujours le contours des rues, il faut aussi redécouper le réseau de voirie à ses intersections avec les aires de dissémination pour optimiser l’allocation des rues aux bonnes aires de dissémination. 

Avec cela, il devient possible de faire un traitement géospatial pour faire la sommes des taxes (résidentielles et non résidentielles) pour une aires de dissémination, de la même manière, les longueurs totales de rue. Reste ensuite à diviser le taxes par les longueurs de rue pour obtenir le ratio de revenus par mètre de rue.

Une jointure avec les données socio-démographiques permettent ensuite de mettre toutes ces valeurs ensemble.

### Les choix de visualisation

La présentation contient plusieurs modes de visualisation différents, surtout pour la cartographie: 3D avec découpage sur les aires de dissémination, 3D avec découpage hexagonal, carte 2D type "choropleth" (gradient de couleur). Lorsque j'ai vu la visualisation d'Urban3 qui utilise de la 3D, je me suis demandé la pertinence d'un tel choix qui alourdi et rend plus difficile la compréhension. En faisant moi-même le travail, j'ai compris que l'usage de la 3D ne tenait pas nécessairement du gadget. 

Les graduations avec des intervalles constants permettent de bien voir les valeurs extrêmes, mais on perd la finesse dans les intermédiaires. Les graduations en quantiles ou plus intelligentes (Jenks), permettent de mieux catégoriser mais perdent les écarts parfois significatifs au sein d'une même catégorie. En 3D, la hauteur permet de représenter linéairement les écarts tandis que le code couleur, en utilisant des quantiles, permet d'avoir une catégorisation rapide. Bref, la 3D, bien qu'un peu lourde, présente un intérêt non négligeable ici.

### Code et données

- Une version simplifiée des requêtes SQL utilisées pour faire le traitement de données est [disponible](https://gist.github.com/Hoedic/700eb03a91eaafb1804d8488b63c3a43) sur Gist.
- [Extraction des données traitées]({{ root_url }}/images/2022-05-31_Donnees-analyse.zip) en GeoJSON


### Outils utilisés

- [PostgreSQL](https://www.postgresql.org/) avec l’extension géospatial [PostGIS](https://postgis.net/)
- [QGIS](https://www.qgis.org/fr/site/) connecté à PostgreSQL pour visualiser sur des cartes
- Le [Studio Plot.ly](https://chart-studio.plotly.com/) pour les graphiques
- [Kepler.gl](https://kepler.gl/) pour la visualisation 3D, connecté sur [Carto](https://carto.com/)
- La suite [GDAL](https://gdal.org/) (ogr2ogr et shp2psql) pour le traitement et l’import des données
- [Google Street View](https://www.google.ca/maps) pour illustrer les quartiers utilisés comme référence
- Les outils (et cerveaux) d'[Anagraph](https://anagraph.io/)



