---
layout: post
title: "Le vélo d'hiver progresse-t-il vraiment?"
date: 2017-02-12 00:00
description: "La pratique du vélo d'hiver au milieu de l'échantillonage sélectif, des 'petites' données et de l'interprétation qualitative"
comments: true
categories: ["Données"]
image: "2017-02-12-photo-velo-graph.jpg" 
credit: ""
---

Y a pas juste le *big data* qui mérite notre attention. Les "petites" données, bien plus fréquentes sont tout aussi importantes et fréquemment sujettes à des simplifications et des mauvaises interprétations. Visite guidée au pays des données de vélo d'hiver et des différentes conclusions qu'il est possible de tirer selon différents angles d'analyse.

Dans un [billet récent](http://mon-ile.net/carnet/2017/02/05/10-ans-velo-hiver/), je souhaitais écrire *"Tant que la courbe d’utilisation du vélo d’hiver continuera de progresser d’année en année ..."*. Sauf qu'une analyse rapide des données montrait... une stagnation. La semaine passée, dans le cadre du [Congrès international de vélo d'hiver](http://www.velo.qc.ca/wcc/), qui se déroulait à Montréal, j'entendais le chiffre magique de 100% d'augmentation de la pratique du vélo d'hiver entre 2014-2015 et 2015-2016. De visu, une stagnation long terme semblait surprenante mais un doublement d'une année sur l'autre semble encore moins plausible. Il n'en fallait pas plus pour me pousser à creuser un peu plus les données. Et comme souvent, c'est plus compliqué que cela en a l'air.

---

## Analyse naïve - le premier niveau

Première étape, reproduire les résultats de base. C'est relativement simple en prenant les [données](http://donnees.ville.montreal.qc.ca/dataset/velos-comptage) de boucles de comptage qui donnent des valeurs quotidiennes, certaines remontants à 2009.

Variation entre 2014-2015 et 2015-2016: pour la période d'hiver étendu (du 1<sup>er</sup> dec. au 31 mars), la somme des six boucles<sup>**</sup> étudiées passe de 117604 passages à 263511; 124% d'augmentation! Prises individuellement, chaque boucle montre une augmentation de cet ordre. Yeah!

Variation sur le long terme: En prenant le même échantillonnage (du 1<sup>er</sup> dec. au 31 mars, six boucles) sur plusieurs années, le portrait est nettement moins rose: une courbe sans réelle tendance. L'année de la hausse de 124% est certes la plus haute mais dépasse difficilement un autre sommet de 2011-2012 qui fut suivi de 3 années de baisse consécutives. On peut difficile tirer de ce graphique que la pratique du vélo d'hiver progresse sur le long terme.

![Évolution du vélo 2010-2016]({{ root_url }}/images/2017-02-12-graph-velo-1.png)
<div class="photoattrib">Nombre total de passages annuels de vélos sur six boucles entre le 1<sup>er</sup> dec. et le 31 mars<sup>***</sup> </div>

---

## Correlation météorologique - le deuxième niveau

Évidemment, quiconque a vécu au Québec quelques années sait que les hivers des années 2013-2014 et 2014-2015 furent particulièrement rigoureux. Tentons donc l'hypothèse suivante: Le creux des années précédant 2015-2016 était principalement le fait de la météo et non d'une désaffection temporaire du vélo d'hiver. Pour ce faire, nous allons chercher les [données](http://climat.meteo.gc.ca/historical_data/search_historic_data_f.html) d'Environnement Canada qui nous donnent, parmi d'autres choses, la température moyenne et les précipitations de chaque jour depuis 1840. Celles depuis 2009 suffiront. Maintenant regardons rapidement l'évolution de la fréquentation des pistes avec la température moyenne pour chaque hiver.

![Évolution du vélo 2010-2016 comparé à la température moyenne]({{ root_url }}/images/2017-02-12-graph-velo-2.png)
<div class="photoattrib">Nombre total de passages annuels de vélos (1<sup>er</sup> dec. et le 31 mars) comparé à la température moyenne pendant la même période</div>

Le lien semble assez convainquant. Un rapide calcul de corrélation donne un beau 0.92 (1 = corrélation parfaite)! En plusiers années d'analyse de données, je n'ai jamais vu un tel résultat. Les corrélations, c'est comme les scores d'élection, quand c'est trop haut, ça en devient louche. Même si on nous met tout le temps en garde à ne pas confondre [correlation et causalité](http://www.tylervigen.com/spurious-correlations), le lien, ici, semble assez clair. En fait, avec une température moyenne de -2.7°C en 2015-2016 contre -8.7°C en 2014-2015, j'aurais pu prévoir à quelques dizaines près le nombre de cyclistes pendant la saison 2015-2016 juste avec la température moyenne.

La signification de cette correction est que la température est le paramètre déterminant de la pratique du vélo et donc, de manière implicite, que les années qui passent n'ont pas d'impact. Il n'y aurait donc pas de progression significative. Est-ce si simple?

---

## Segmentation - le troisième (et dernier) niveau

Pour analyser une donnée, il est important de se demander ce qu'elle représente. Il est tentant de voir dans les données de comptage une indication du nombre de cyclistes faisant du vélo. Toutefois, nous avons ici des *cyclistes.jours* que l'on agrège ensuite par période de temps. 

Même si cela enlève la vision d'ensemble, il est nécessaire de regarder les données à leur plus fine résolution: la journée.

![Comptages par boucle quotidiens vs la météo]({{ root_url }}/images/2017-02-12-graph-velo-3.png)
<div class="photoattrib">Nombre total de passages quotidiens durant la saison 2015-2016 comparé à la température moyenne et aux précipitations</div>

À ce niveau, on constate que la forte corrélation avec la température moyenne semble disparaitre, passant de 0.92 à 0.58 (ce n'est pas zéro, mais c'est loin d'être impressionant. Pour la forme j'ajoute les précipitations qui ont aussi un impact. On note une certains cyclicité de la fréquentation, lié aux fins de semaines qui peut avoir un impact négatif sur la corrélation. Surtout, dans le cas présent, on voit que l'activité demeure assez élevée pendant tout le mois de décembre grâce aux températures clémentes. Les hautes fréquentations annuelles de 2015-2016 semblent surtout le fait d'un hiver tardif.

Serait-il possible d'évaluer, à température controlée, l'évolution de la fréquentation au fil des années? Segmentons les journées de janvier et février des différentes années en fonction de la température quotidienne moyenne par bloc de 5°C, ajoutons des courbes de tendance, nous obtenons ceci: 

![Évolution annuelles en fonction de segments de températures]({{ root_url }}/images/2017-02-12-graph-velo-4.png)
<div class="photoattrib">Évolution du nombre total de passages annuels (janvier et février) segmentés selon la température moyenne du jour</div>


Avant de commenter les résultats, il est important de comprendre que dans la majorité des cas, on a entre une dizaine et une vingtaine de journées par année pour chaque segment de température, ce qui est peu faible pour faire une moyenne mais n'est pas non plus dénué de valeur. Dans des cas extrêmes, comme le segment 0°C à -5°C en 2015, il y a juste deux mesures, ce qui est très nettement insuffisant.

Malgré cette relative faiblesse statistique, on note toutefois que toutes les courbes sont à la hausse. Une hausse pas très importante d'une année sur l'autre, mais significative sur le long terme, un peu plus qu'un doublement des valeurs sur la période de 7 ans étudiée. On note qu'en 2015, toutes les courbes prennent un coup à la baisse, signe que l'hiver très rigoureux a coupé les jambes à beaucoup de personnes, même quand le thermomètre acceptait de remonter un peu. Évidemment, le rebond de 2016 est par la suite flagrant.

---

## Est-ce valide?

J'ai du mal à évaluer la validité des résultats. Si on calcule quelques indicateurs comme l'erreur type ou la validité des corrélations, les chiffres obtenus ne sont pas très beaux. Beaucoup de variables influencent le résultat; j'ai ici travaillé sur la température qui a l'avantage d'être un facteur continu et clairement identifiable. On voit clairement sur les données journalières que les précipitations ont un impact, mais c'est loin d'être homogène: d'expérience une faible plus verglaçante va plus rebuter le monde qu'une petite bordée de neige. Pour faire bonne mesure, j'aurais également dû essayer de corriger l'effet des fins de semaines, quitte à simplement les enlever.

L'état de la chaussée est également réputé être un élément important. Si ma mémoire est bonne, le vénéré [François Démontagne](http://www.francoisdemontagne.com/) avait noté l'état de la chaussée pendant une saison ou plus et conclut que c'était un facteur important. Les données quotidiennes montrent que certains jours après des précipitations, l'affluence reste anormalement faible. On peut supposer que l'état de la chaussée demeurait difficile: soit les cyclistes sortaient juste moins, soit ils ne passaient pas sur les boucles. En effet, il faut bien comprendre que les boucles, aussi utiles soient-elles sont imparfaites: il faut que les cyclistes passent dessus. Lorsque la rue est insuffisamment déblayée, surtout après des épisodes verglaçants, les cyclistes évitent les pistes cyclables et roulent plus au milieu de la chaussées, hors des boucles souvent situées sur des bandes cyclables. 

Ce faisant le travail d'entretien joue aussi un role important: en déneigeant les pistes, les cyclistes y passeront plus volontier. 2016 a vu une bonne amélioration de ce coté et 2017 semble encore mieux. Mais quoiqu'il en soit, la qualité de l'entretien est aussi une variable difficile à controler et pour lesquelles je ne vois pas de donnée fiable.

---

## Pourquoi c'est important 

C'est une lapalissade de nos jours, mais si on a la prétention de prendre des décisions sur base de données factuelles, il est important de faire l'effort de comprendre ces données; dans le cas contraire, ça risque de se retourner contre nous. L'année ayant vue une hausse de 100% pourrait être suivie par plusieurs années avec une faible fréquentation juste à cause de conditions climatiques adverses. Faudrait-il alors tirer la conclusion que le vélo d'hiver est en perte de vitesse? En analysant les données avec assez de profondeur, il est possible d'en tirer des analyses qui demeureront valides même si certains paramètres changent.

Ça prend aussi une certaine honnêteté intellectuelle: quand j'ai commencé à triturer les données, j'étais prêt à obtenir des résultats qui auraient pointé vers une stagnation de la pratique du vélo d'hiver, même si cela serait allé à l'encontre de mes intérêts. Est-ce qu'on continuant à raffiner l'analyse et la prise en compte d'autres paramètres, il serait possible d'arriver à la conclusion inverse (démontrant ainsi, comme le clament certains, qu'on peut faire dire n'importe quoi à des données)?

Ça semble peu probable, mais le point important n'est pas là de toutes manières: il est important de caractériser ce qu'on cherche, en l'occurence, ce qu'on considère comme du vélo d'hiver. Je suis d'un peu mauvaise fois en m'attanquant à ce +100%, ne sachant pas ce que ses auteurs voulaient démontrer (et le message a surement été simplifié par le biais par lequel il m'est parvenu: Twitter). Pour moi, du vélo d'hiver, c'est le fait de ne pas avoir d'interruption prolongée (e.g plusieurs mois) de sa pratique. Une personne qui reprend occasionnellement son vélo en janvier-février quand le temps le permet, mais ne roule pas qyand il fait moins que -5°C fait du vélo d'hiver. À contrario, une personne qui s'arrête dès qu'il fait zéro, à la première neige, et entrepose son vélo jusqu'au retour des conditions clémentes ne fait pas du vélo d'hiver... même si, comme en 2015-2016 cette personne a pu rouler jusqu'au 28 décembre.

Bref, en prenant une définition exagérée de l'hiver (du 1er dec. au 31 mars), on inclut des tas de passages sur les boucles qui font augmenter les statistiques mais ne sont pas du vélo d'hiver; mais qui par le volume peut noyer le reste de l'information. C'est pour cette raison que dans la dernière analyse, j'ai volontairement limité l'analyse aux mois de janvier et février plutôt que décembre à mars. 

En conclusion, cela m'a surtout permis de confronter une impression rapide que j'avais eu en regardant des statistiques annuelles qui montraient une stagnation; ainsi mon article sur mes 10 ans de vélo d'hiver n'est pas complètement dans le faux. Mais qui sait, mes impressions sur la progression de cette pratique auraient pu être erronées.

P.S.: Si par hasard vous réalisez une analyse plus approfondie des données et arrivez à d'autres résultats, il me fera plaisir d'en prendre connaissance et de les partager ici.

<sup>**</sup> par soucis de cohérence, j'utilise pour toutes les analyse la somme de six boucles de comptage actives de manière constante entre 2010 à 2016, à savoir la piste Berri, la piste Cote-Sainte-Catherine, la piste Maisonneuve, la piste Parc, la bande Pierre-Dupuy et la piste Rachel.

<sup>***</sup> Tous les graphiques ont été réalisé avec l'excellent [Plot.ly](https://plot.ly/)