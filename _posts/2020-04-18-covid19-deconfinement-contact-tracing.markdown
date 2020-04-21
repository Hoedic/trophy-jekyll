---
layout: post
title: "COVID19 - Comment le déconfinement et le 'contact tracing' pourraient se faire"
date: 2020-04-08 20:15
description: "Le suivi de contact est un outil à notre dispositions. Comment évaluer s'il est utile?"
comments: true
categories: ["Politique"]
image: "2020-04-trace-together.jpg" 
---

Alors que le gros de la première vague de l'épidémie semble être derrière nous, tout le monde veut savoir **quand** aura lieu le déconfinement. Toutefois, la principale question devrait surtout être **comment**.

Je vais me concentrer sur un exemple, les outils numériques de suivi de contact (aka *contact tracing*) pour mettre de l'avant le genre de cheminement que je juge nécessaire à cette étape-ci et les conséquences sociales qu'on peut envisager. Si vous voulez des réponses, passez votre chemin, vous n'en aurez pas. Vous aurez surtout des questions et des possibilités de réponses.

### La fin de la première vague

Dans la plupart des pays occidentaux, la courbe s'aplanit; le confinement, version épidémiologique du bouton nucléaire a des conséquences qui sont plus désastreuses chaque jour qui passe. La souffrance et les impacts cumulés liés à l'arrêt de notre économie vont vite être mis dans la balance des mesures confinement qui a priori ne font que repousser à plus tard la vraie question: comment vivre avec une maladie comme la COVID-19.

La premier acte de la pièce fut dur, mais assez simple: renvoyer tout le monde à la maison, le scénario était déjà écrit par d'autres. Le deuxième acte risque de s'avérer nettement plus complexe: aucune approche miracle pour, cette fois, trouver un équilibre entre fonctionnement de notre société et maladie. L'histoire est à écrire et chacun l'abordera à sa manière.

Je vais parler d'un outil en particulier, le suivi de contact, mais la première chose que nos gouvernements devraient partager, c'est la stratégie visée pour ce deuxième acte. Pour revenir à ma [classification](./2020/03/30/covid19-strategie-quebec-1/): vise-t-on une stratégie de ralentissement, dans laquelle on conserve un nombre de nouveaux cas quotidien assez élevé au long cours avec comme objectif une immunité de troupeau mais sans déborder les urgences et en protégeant les plus faibles, ou vise-t-on un étouffement ciblé qui vise vraiment à avoir un nombre de cas très faible, contrôlé de très près et de tenir le fort jusqu'à une immunité obtenue par vaccin. Cette différence est majeure parce que les outils qui seront mis au service de la stratégie choisie seront déployés différemment. Sachant qu'on parle toujours de stratégie *visée*: on peut partir sur une stratégie et évaluer en cours de route que ça ne marche pas, on n'est pas au pays des certitudes ici.

L'OMS nous donne une [série de critères](https://www.npr.org/sections/goatsandsoda/2020/04/15/834021103/who-sets-6-conditions-for-ending-a-coronavirus-lockdown
) pour relancer la machine et par la bande des pistes de comment le faire. Plusieurs de ces critères sont transitoires: valider que les autorités ont repris le contrôle. Les autres éléments sont opérationnels: comment on maintient ce contrôle.

La plupart des éléments opérationnels étaient disponibles avant le début de la crise et ce ne fut pas suffisant pour maitriser l'explosion de cas. Une hypothèse en partant: à défaut d'avoir un outil qui à lui seul, une fois renforcé, permettrait d'enrayer la maladie, tous les outils disponibles doivent être bonifiés. Le suivi de contact fait partie de ces outils et il est d'ores et déjà clair que cet outil ne sera pas la [solution à lui seul](https://www.wired.com/story/apple-google-contact-tracing-wont-stop-covid-alone/). Mais il peut jouer un rôle important.

### Pourquoi le suivi de contact

La nature furtive du SARS-CoV-2 fait qu'il est vraiment primordial de remonter dans le temps pour aller chercher les opportunités de contamination d'une personne testée positive. En effet, certaines [études](https://science.sciencemag.org/content/early/2020/04/09/science.abb6936) laissent penser que la contagiosité pré-symptomatique ou faiblement symptomatique est suffisante pour maintenir à R0 (ou un [R<inf>t</inf>](http://systrom.com/blog/the-metric-we-need-to-manage-covid-19/)) supérieur à 1, il faut donc intervenir sur la période avant les symptômes.

C'est la raison d'être du suivi de contact. En temps normal, le suivi de contact est fait par des personnes de la santé publique: une fois une personne testée positive, on lui demande, formulaire à l'appui, les lieux fréquentés et les personnes rencontrées pour la durée supposée de contagion (en général 14 jours pour la COVID-19). Cette méthode a plusieurs limites:

- La mémoire humaine est faillible, une personne peut oublier des éléments majeurs dans ses contacts
- Les personnes disponibles pour faire du suivi de contact peuvent se trouver dépassées par la charge de travail, rendant le mécanisme plus ou moins opérationnel
- C'est long (surtout quand le système est dépassé), plusieurs journées critiques peuvent s'écouler avant que les personnes à risque soient contactées
- Enfin il ne sera pas possible de contacter tous les personnes souhaitées: on ne connait pas le nom de nombreuses personnes avec qui on interagit quotidiennement.

Bref, beaucoup de limitations pour un mécanisme qui peut jouer un rôle central. En théorie, si on pouvait mettre en isolement préventif toutes les personnes potentiellement malades rapidement après une exposition, on arrêterait la propagation aussi efficacement qu'avec un confinement généralisé.

Comme souvent dans ce genre de situation, on se dit que la technologie numérique peut nous venir en aide. Si un outil numérique pouvait mémoriser pour nous tous nos "contacts" (même ceux que nous ne connaissons pas) et, le cas échéant, signaler à ces personnes qu'elles ont été proches d'une personne malade, ça rendrait soudainement la vie bien plus facile. C'est l'idée derrière les outils numériques de suivi de contact: maximiser le nombre de personnes averties, minimiser le délais entre l'information d'une personne malade et la notification des personnes susceptibles. 

Il existe plusieurs variantes de ces outils, pour être dans le concret, je vais en prendre un en particulier qui est bien documenté: l'application développée par le National Health Service (NHS) au Royaume-Uni et qui reprend la formule de Singapour pour [TraceTogether](https://www.tracetogether.gov.sg/). Le mode de fonctionnement est expliqué ci-dessous (une version plus [longue](https://ncase.me/contact-tracing/) existe aussi).


![Explication graphique de l'application de contact tracing]({{ root_url }}/images/2020-04-21_contact-tracing.png)
<div class="photoattrib">Explication sommaire du fonctionnement du protocole DP3T par <a href="https://ncase.me/contact-tracing/">Nicky Case</a></div>

D'un point de vue vie privée, les avantages de cette solutions sont nombreux, notamment en évitant de collecter des informations personnelles et des traces de déplacement (pas d'utilisation du GPS). Comme les identifiants diffusés changent, il faudrait vraiment mettre en place un stratagème complexe pour être en mesure de remonter des contacts entre différentes personnes. Enfin, l'application conserve le statut médical secret: une personne notifiée n'a pas connaissance de la personne dont la présence a déclenché l'alerte. En bout de ligne, ça limite grandement les risques de dérive dans l'utilisation des données. D'autres variantes existent, certaines ajoutent les données GPS, mais ça change assez peu le propos de ce qui suit.

### Alors, on l'utilise ou pas cette solution?

Pour commencer, faisons le parallèle avec le développement d'un vaccin: le processus de mise en place est long, mais les gains et les risques sont bien documentés: en sortant du processus d'approbation, on connait généralement le pourcentage de couverture et l'incidence des effets adverses. C'est l'idéal.

Doit-on attendre 12-18 mois pour faire des tests sérieux sur l'impact d'une application de suivi de contact? Ce serait surement souhaitable, mais autant les gains que les risques seraient de toutes manières très difficiles à apprécier. Dans le cas d'un vaccin comme d'une application, le bénéfice est fonction d'un effet de réseau: une personne vaccinée change relativement peu le cours des choses, de la même manière qu'une application de suivi utilisé par une unique personne n'a pas d'intérêt. La différence, c'est que l'impact d'un vaccin est plus binaire et surtout plus connu. Pour une application de suivi, les bénéfices sont plus difficiles à modéliser d'avance, le nombre d'hypothèses à faire pour un tel modèle, énorme. Les conséquences négatives sont aussi plus difficiles à évaluer. Par exemple comme évaluer l'impact d'une surveillance continue sur la qualité de vie générale? Surtout dans un contexte où cette surveillance est déjà omniprésente, qu'ajoute-t-on avec une telle application?

Il faut aussi évaluer l'impact de cet outil sur les autres outils mis en place. Par exemple, une telle application sera très peu spécifique sur l'intensité du risque. Malgré les tentatives de filtrer les cas les plus à risque, il est envisageable que l'application déclenche beaucoup de notifications, donc un nombre élevé de personnes qui souhaiteront se faire tester. Même si on augmente le volume d'analyse, est-ce qu'il sera possible de traiter toutes les personnes qui se déclarent à risque? Très difficile à dire mais on peut supposer que ça pourrait augmenter très vite malgré tout. Pour faire un calcul rapide: mettons que nous avons 200 cas/jour, et chaque cas déclenche une cinquantaine de personnes, on parle 10 000 tests/j, soit plus que la capacité actuelle de 5000-6000 analyses/j. Bref, dans les risques à prendre en considération, un outil de ce type doit non seulement avoir une efficacité, mais il ne doit pas avoir d'effet adverse sur le déploiement des autres outils.

Enfin, il faut être conscient qu'une telle application ne pourrait pas remplacer le suivi de contact "classique": à cause de la non utilisation de l'application par une partie de la population. Il sera toujours nécessaire de faire appel à une armée de personnes pour faire ce travail, partiellement en doublon avec l'application. Bref, faut-il investir un effort important à faire adopter un tel outil alors que la bonne vieille méthode manuelle devra continuer d'exister?

Supposons que l'on juge que le gain mérite l'investissement...

### Maturité technologique, standardisation et logiciel libre.

Comme l'explique assez bien ce [billet](https://www.cigionline.org/articles/digital-response-outbreak-covid-19) de Sean McDonald, une solution technologique ne vaut que par la maturité et les protocoles institutionnels qui l'encadrent. Le risque du syndrome *There's an app for that* c'est d'évaluer une application en dehors de son cadre de fonctionnement. Dans le cadre d'une application de traçage, on parle d'un système complexe, le système de santé. C'est un système, au Québec, qui n'est pas réputé pour sa simplicité organisationnelle et sa maturité technologique. Par maturité j'entends trois choses:

- La capacité individuelle d'utiliser ces outils. C'est surement la moins problématique, la majorité des gens se sont adaptés à des outils technologiques dans leur vie personnelle.
- Les routines opérationnelles. Ce sujet est plus complexe car la majorité de ces routines n'ont pas de propriétaire de bout en bout; en d'autres termes, elles sont difficiles à faire changer. Le risque de la mise en oeuvre d'un outil comme celui-ci est qu'il soit adopté de manière asymétrique à différentes étapes, résultant en des tensions et des erreurs.
- Enfin, la maturité dans les décisions stratégiques: quelle solution déploie-t-on et comment. Là encore, la maturité générale n'est pas très bonne. Notre cadre légal est flou et peu adapté à répondre aux questions soulevées par des outils comme du suivi de contact. Des organisations comme la FIPA a proposé des [lignes directrices](https://fipa.bc.ca/wordpress/wp-content/uploads/2020/04/joint_statement_digital_surveillance_technologies_and_covid-19_in_canada.pdf), de même pour l'[Electronic Frontier Foundation](https://www.eff.org/deeplinks/2020/04/challenge-proximity-apps-covid-19-contact-tracing), mais ça reste assez haut niveau. C'est un effort considérable de traduire ces orientations en outils de prise de décision. Exemple de maturité: L'Ontario avait commencé à y réfléchir [avant le crise](https://www.publichealthontario.ca/-/media/documents/eb-internet-contact-tracing.pdf?la=en) alors qu'au Québec la Commission d'accès à l'information a été plus [réactive](https://www.cai.gouv.qc.ca/documents/CAI_reflexionPRP-COVID-19_V2_2020-04-16.pdf).

Pour le dire plus simplement: le risque d'embourber le système ou de prendre de mauvaises décisions est plus élevé dans un système qui n'a pas la maturité pour gérer ce type d'outil. Ce n'est pas une raison pour ne pas le faire, ça fait partie des éléments à prendre en considération.

Un élément pouvant faciliter l'adoption est la standardisation. Toujours à titre d'exemple, la solution développée par le NHS se base sur un protocole standardisé et ouvert le DP3T pour [Decentralized Privacy-Preserving Proximity Tracing](https://github.com/DP-3T/documents).

La standardisation permet de nombreuses choses: d'abord, elle ouvre la porte à une approche inter-juridictionnelle. Par exemple, ce serait très dommage que le Québec parte avec son approche et l'Ontario la sienne considérant les liens entre les deux provinces. Pareil entre le Canada et les États-Unis. Considérant que les voyages vont demeurer un élément difficile à gérer à l'avenir, la standardisation est une question importante. Par ailleurs, la standardisation augmente la capacité à échanger des informations et des bonnes pratiques entre juridiction, ce qui peut suppléer partiellement à un manque de maturité. 

La standardisation, c'est la partie théorie. Dans la pratique, une application pourrait chercher à collecter et utiliser d'autres données. Par exemple, si le GPS est activé, on pourrait craindre l'utilisation de la position GPS pour essayer d'obtenir d'autres informations. C'est là qu'il est important de faire le développement en logiciel libre comme le fait NHS. Ça augmente le niveau de transparence et donc de confiance.

L'avantage du logiciel libre est également de faciliter la réplicabilité ou le transfert. Ainsi le travail réalisé peut servir à d'autres.

### Internationalisation et gouvernance des données

Cette approche de standardisation et de logiciel libre ouvre même des portes interessantes (là je me mets à rêver en couleur): une application comme celle développée par NHS pourrait être transférée à l'OMS. En effet, même s'il n'y a pas de données personnelles, les données de contact stockées dans la base de correspondance entre identifiant révèle tout de même des patrons relationnels importants. Il pourrait être tentant pour un pays ou une entreprise d'utiliser ces données pour étudier les comportements relationnels des habitants. L'OMS a, a priori, moins de motifs de se lancer dans ce genre de démarche. Le fait d'impliquer l'OMS permettrait aussi de déployer l'outil à moindre coût dans les pays ayant moins la capacité de le faire. 

Ça pourrait aussi limiter les velléités de certains pays de profiter de la crise COVID-19 pour augmenter le niveau de surveillance d'état. Évidemment, je ne m'attends pas à ce que la Chine cesse ses pratiques orwelliennes pour adoptées les meilleures pratiques, mais des pays plus démocratiques qui auraient la tentation de la surveillance devraient expliquer en détail pourquoi une application à portée internationale ne ferait pas l'affaire; on peut par exemple penser à [Israël](https://www.nytimes.com/2020/04/12/world/middleeast/coronavirus-israel-mossad.html) et à d'autres qui semblent fortement tentées d'utiliser la crise pour contrôler encore plus leur population.


> Si on choisit de faire du suivi de contact numérique, je veux savoir pourquoi.<br/> Et si on décide de ne pas en faire je veux également savoir pourquoi.

Toutefois qu'un tel outil soit géré par l'OMS ou au niveau local, de nombreuses questions se posent sur la gouvernance des données collectées. Pour éviter certaines dérives, quelques gardes-fous devraient être mis en place. La gestion de l'infrastructure et surtout des données pourrait être déléguée à un organisme, que je vais nommer ici [fiducie](https://hello.elementai.com/les-fiducies-de-donnees.html) (même si ce n'est pas le seul modèle) dont le seul et unique rôle serait d'être responsable de l'utilisation des données: s'assurer de la sécurité, de la non-diffusion et de la suppression des données adéquatement. Mettons que l'application vienne avec un consentement pour un partage des données à des fins de recherche, la fiducie pourrait avoir la responsabilité d'administrer ce partage en lien avec les termes du consentement.

Cette fiducie devrait elle-même rendre publique l'ensemble de ses décisions et être soumise à des audits ponctuels commandés par le fiduciaire, l'OMS ou le gouvernement. Sans dire qu'une telle structure serait parfaite (et mes amis en gouvernance des données auraient surement d'autres recommandations), on s'assure d'un respect maximum des données collectées.

### La gestion locale

Même si l'application est gérée à l'échelle internationale, les juridictions doivent s'organiser en fonction. Premièrement, tel que recommandé par la FIPA, l'utilisation d'une telle application doit être encadrée légalement. Même si, mettons, l'OMS gère l'application, les juridictions locales doivent définir le cadre légal supportant l'utilisation de cet outil et sa délégation à une entité externe ainsi que les motifs d'utilisation, la portée et la durée de cette démarche, etc.

Ensuite, cela prend une organisation locale en mesure de supporter l'utilisation de cette application. Même avec un fonctionnement décentralisé, les autorités locales doivent avoir les infrastructures et procédure pour émettre les codes de validation des cas positifs qui enclenchent le mécanisme de diffusion d'une alerte.

Enfin et surtout, les autorités auraient pour mandat de soutenir l'adoption. Selon des [simulations](https://www.research.ox.ac.uk/Article/2020-04-16-digital-contact-tracing-can-slow-or-even-stop-coronavirus-transmission-and-ease-us-out-of-lockdown) faites par Oxford pour le NHS, avec 80% des possesseurs de téléphone intelligents utilisant cette application, il serait possible de passer à un R0 inférieur à 1 sans avoir beaucoup d'autres mesures hormis d'isoler les personnes de moins de 70 ans. Ce type de simulation est à prendre avec des grosses pincettes, ce qui est important c'est le taux d'adoption de 80%. C'est énorme! A contrario, avec un taux inférieur à 50%, l'application ne couvrirait qu'un taux très faible de contacts. Pour référence, Singapour est difficilement arrivé à un [quart de la population en un mois](https://www.wired.com/story/apple-google-contact-tracing-wont-stop-covid-alone/). 

Pour arriver à un taux d'adoption utile, considérant que ça devrait rester sur une base volontaire, les gouvernements devraient mettre en place une stratégie très complète. Et (et c'est là tout le coeur de la réflexion) bénéficier de la confiance de leur population. L'adoption massive de ce genre d'outil ne peut marcher que parce que la population a confiance en ses institutions. Tous les éléments que je viens de citer (standardisation ouvertes, logiciel libre, déploiement international neutre, etc.) servent notamment à générer de la confiance, mais si le niveau de départ est ras les pâquerettes, les chances que ça fonctionne sont quasi-nulles. 

### Public vs privé

Ce billet est déjà plus lourd que je souhaitais, mais il faut aborder le cas du duo Google/Apple qui a [annoncé](https://medium.com/@TamarSharon/when-google-and-apple-get-privacy-right-is-there-still-something-wrong-a7be4166c295) la mise en oeuvre d'une approche de traçage, d'abord sous forme d'une application et à terme intégrée dans le noyau de leurs systèmes d'exploitation (donc nécessitant juste une activation, mais pas d'installation d'application). Ce duopole utilise une approche très similaire à DP3T, alors pourquoi ne pas simplement laisser ces deux géants servir la population?

Considérant que l'utilisation d'une telle application repose sur la confiance, où souhaite-t-on bâtir du capital de confiance? Auprès des autorités gouvernementales et internationales en charge de la santé publique ou auprès d'entreprises dominantes largement impliquées dans des démarches de surveillance de masse?

Personnellement, il me semble important que les pilotes soient les entités publiques: sur un sujet de santé publique, c'est là que le capital de confiance doit se développer et déléguer une telle démarche à des joueurs comme ces deux-là serait, là encore, une légitimation de leur rôle dans la sphère publique ainsi qu'un gros "à charge de revanche" envers les gouvernements. Que "Gapple" [supportent](https://techcrunch.com/2020/04/17/europes-pepp-pt-covid-19-contacts-tracing-standard-push-could-be-squaring-up-for-a-fight-with-apple-and-google/) l'adoption massive, pourquoi pas, mais le message doit être très clair que c'est au service des démarches pilotées par les organes de santé publique.

### Les "bons" choix opérationnels

Dans mon billet sur les [bifurcations](./2020/04/08/covid19-avenir/) liées à la crise actuelle, je soulignais qu'à défaut de m'attendre à une révolution, nous aurions à faire quantité de choix de nature opérationnelle mais avec un impact possiblement profond sur les trajectoires de l'avenir.

Les décisions en matière de traçage de contact entrent dans cette catégorie.

Ne vous méprenez pas: je ne dis pas ici qu'il est nécessaire de faire appel à des applications de suivi de contact. C'est juste que si on choisit de faire du suivi de contact numérique, je veux savoir pourquoi. Et si on décide de ne pas en faire, alors que d'autres pays le font, je veux également savoir pourquoi.

Si les autorités décident (et convainquent le public) d'aller dans cette direction, c'est un choix important, à expliquer et à valoriser. Si ces choix se font, il faut souligner la décision de ne pas aller vers des approches plus invasives (e.g impliquant un suivi GPS), de promouvoir une souveraineté publique par rapport à la proposition de Google et Apple, de travailler avec l'OMS et d'ainsi promouvoir une coopération internationale volontariste, bref aller à contre-sens de beaucoup de tendances actuelles.

Ces réflexions doivent se faire maintenant et avec une certaine transparence. Les autorités qui préparent le terrain, qui prennent le temps, même en situation de crise, d'expliquer leur choix, les valeurs supportant ce choix, iront chercher la confiance. Ma crainte actuelle, c'est que là où cette réflexion n'est pas entamé en amont (et en l'absence probable d'un leadership de l'OMS), des autorités vont se retrouver à développer dans l'urgence quelque chose de mal fait ou d'adopter une solution toute faite, peut-être celle que GApple, non standardisée, moins testée et de se retrouver pied et poing lié avec une approche difficilement défendable... ce qui aurait pour effet de reproduire ce que nous avons déjà trop vu en matière d'improvisation technologiques. On ne ferait que continuer une trajectoire dont pas grand monde ne veut.


Enfin, et c'est un peu le fond de ce billet: reconnaitre ce qu'on ne sait pas. Bien franchement, je serais bien mal pris de devoir décider si on met en oeuvre une telle approche. Au-delà des enjeux de surveillance, la situation est terriblement complexe et les conséquences énormes. Comme beaucoup de décisions de politiques publiques, malgré les meilleures données disponibles, les meilleures évaluations et modélisations, il n'y a qu'en rétrospective qu'il sera possible de juger des décisions. Toutefois, en partageant les réflexions et les enjeux, il est possible décider au mieux de nos connaissance. Cette transparence permet aussi de mobiliser les infrastructures sociales pouvant supporter, par exemple, la décision d'aller de l'avant avec une solution de suivi. Quand on voit le faible taux d'adoption à Singapour, on peut légitimement se demander si les citoyens ont réellement confiance dans leur gouvernement ou si le gouvernement a mis tous les efforts possibles sur le déploiement. Considérant que l'application est d'utilisation volontaire, c'est notamment par le relais d'acteurs de terrain que l'adoption se ferait et donc son succès. 

Ça ne changera pas le monde, pas directement. Mais si de telles décisions se prennent, ce sera des précédents importants, des signaux importants pour les décisions similaires à venir. Ce sera une bifurcation.

