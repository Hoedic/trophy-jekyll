---
layout: post
title: "Considérations de visualisation de données"
date: 2013-11-03 13:52
comments: true
categories: ["Données & visualisation"]
image: "2013-11-03-cartodb.png"
---

Après plusieurs années, je vais finalement justifier le nom de domaine que j'utilise pour héberger ce blog: parlons données et plus précisément représentation de données géospatiales.

La Presse a sorti hier une représentation des dons de campagne pour les quatre principaux partis montréalais qui, dans un esprit de transparence, ont rendu disponible cette information (apparamment sous forme de PDF, ce qui a impliqué du travail inutile du coté de La Presse, mais c'est un autre problème.)

Nous arrivons donc avec la visualisation suivante:

![Dons]({{ root_url }}/images/2013-11-03-carte-lapresse.png)
<div class="photoattrib"><a href="http://www.lapresse.ca/multimedias/201311/01/01-4706410-carte-du-financement-politique-a-montreal.php">Carte des dons</a>. Source: La Presse</div>

Carte classique obtenue avec Google FusionTables (GFT)... et c'est là que le bât blesse. Le contrôle des marqueurs dans GFT est très limité, ce qui se traduit par des marqueurs trop superposés et sans transparence (donc se masquant mutuellement) et de taille unique -ce qui est bien dommage car des dons de 100$ ou de 1000$ apparaissent de la même manière.

La superposition est doublement problématique: outre que des marqueurs peuvent en cacher d'autres, cela peut créer un biais pour un parti. Google affiche "par-dessus" les derniers marqueurs qu'il traite. Si, pour une raison technique, les enregistrements d'un parti sont traités en dernier, ils apparaitront "dessus" et cela biaisera la perception du résultat.

Enfin, les couleurs disponibles pour les marqueurs de Google ne se valent pas. Sans entrer dans les détails du [choix des couleurs en visualisation](http://mkweb.bcgsc.ca/brewer/) de données, le rouge ressort ici plus que le vert, le bleu et encore plus le jaune.

Étant donné que La Presse avait rendu disponibles les données géocodées -merci!, j'ai réalisé une carte semblable essayant de corriger quelques éléments, notamment la superposition des dons et la prise en compte de la taille des dons.

![Dons]({{ root_url }}/images/2013-11-03-cartodb.png)
<div class="photoattrib"><a href="http://cdb.io/1alnktr">Carte des dons</a>.</div>

Les couleurs restent encore discutables (par manque de volonté pour faire mieux et pour respecter les couleurs des partis) mais à mon goût cela donne une meilleure idée de l'information.

Après discussion avec Cédric Sam qui a réalisé la carte, le choix de GFT était entre autre motivé par la nécessite de devoir agréger les dons situés au même endroit (ce qui corrige en partie le problème de superposition). C'est effectivement quelque chose que ma visualisation ne supporte pas et qui m'aurait pris beaucoup plus de temps à faire.

Il faut toutefois se poser une question: une majorité des gens vont s'arrêter à une impression de haut niveau: quelle couleur dominait la carte. En fonction de l'outil utilisé et du fait de contraintes technologiques propres à ce dernier, on peut se retrouver avec une représentation biaisée (et de manière générale difficile à juger d'un rapide coup d'oeil).

Quoiqu'il en soit, les représentations graphiques, et surtout en carto, ont toutes leus limitations. C'est pour cela qu'il faut autant que possible donner des éléments objectifs de compréhension des données. Dans ce cas, fournir un tableau avec le nombre de dons et le montant des dons par parti permettrait surement de mettre en perspective certains éléments:

<table style="margin: 20px auto;">
<tr><th style="width:200px">Parti</th>
	<th style="width:150px">Montant total</th>
	<th style="width:150px">Nombre de dons</th>
	<th style="width:150px">Moyenne par don</th></tr> 
<tr><td>Équipe Coderre</td><td>335 720$</td><td>1609</td><td>208$</td></tr> 
<tr><td>Projet Montréal</td><td>249 489$</td><td>1042</td><td>239$</td></tr>  
<tr><td>Coalition Montréal</td><td>212 870$</td><td>844</td><td>252$ </td></tr> 
<tr><td>Équipe Joly</td><td>71 975 $</td><td>241</td><td>298$ </td></tr> 
</table>


⁂

Profitant des données travaillées par La Presse, j'ai réalisé une autre carte qui nous donne le parti vainqueur en matière de dons par district électoral. Nous verrons si c'est un "proxy" intéressant pour déterminer les résultats!

![Dons]({{ root_url }}/images/2013-11-03-cartodb2.png)
<div class="photoattrib"><a href="http://cdb.io/1alnvFg">Vainqueur (en dons) par district électoral</a>.</div>

Les données ne sont pas tout à fait comparable car la période couverte pour les différents partis n'est pas la même. Ça vaut ce que ça vaut.