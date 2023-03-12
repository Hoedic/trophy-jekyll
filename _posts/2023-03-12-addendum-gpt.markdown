---
layout: post
title: "GPT et la sécurité routière, addendum"
date: 2023-03-11 00:00
description: "les chatbots rêvent-ils (encore) de vélos électriques et de réglementation?"
comments: true
categories: ["Donnees"]
image: "2023-03-12_pyramides.jpg" 
---

Le présent article est un ajout au [précédent](/2023/02/19/apprendre-a-gpt3/) billet où j'expliquais mes tentatives de rendre GPT-3 capable de répondre à des questions spécifiques sur le Code de sécurité routière du Québec. Je terminais l'article en mentionnant qu'il fallait encore voir ce que donneraient ces tests si ChatGPT devenait accessible via une API. Les choses n'ont pas tardé à se [réaliser](https://platform.openai.com/docs/guides/chat) et je n'ai pas tardé à réaliser quelques essais dont voici la synthèse.

## Bref récapitulatif

Si vous n'avez pas le courage de lire l'article précédent, le point de départ était que ChatGPT, tout en ayant une connaissance d'ensemble de la sécurité routière, était incapable de répondre correctement à des questions spécifiques et notamment lorsque le Québec se distingue ou présente des détails divergents de la moyenne. J'arrivais à améliorer sensiblement la qualité des réponses en utilisant la méthode de l'embedding sur GPT-3, le modèle sous-jacent de ChatGPT; toutefois la qualité des résultats demeurait insuffisante pour en fait une source fiable.

Mon intuition était que l'embedding serait surement très efficace combiné avec ChatGPT (plutôt que GPT-3). Mais pour cela, il fallait une API offrant la capacité d'utiliser ChatGPT de manière programmatique, c'est-à-dire qu'un programme de ma conception peut échanger directement avec le modèle de génération de texte. Cette API permet notamment de faire de l'embedding, une approche qui consiste à faire une analyse de proximité sémantique, dans notre cas entre une question et une source d'information textuelle de grande taille, mais segmentée. L'analyse de proximité sémantique permet de sélectionner quelques segments pertinents pour la question et d'envoyer au modèle la question *avec* les segments; ici une poignée d'articles du code vraisemblablement utiles pour répondre à la question.

Utilisée avec GPT-3, la méthode de l'embedding avait deux lacunes évidentes:
- L'embedding ne permettait pas toujours de sélectionner la bonne information à envoyer à GPT. Il n'a aucune chance d'amélioration avec mes nouveaux tests: que ce soit GPT-3 ou ChatGPT ne change rien à l'affaire si l'information utile n'est pas présente;
- GPT-3 avait fait plusieurs erreurs de compréhension, soit de la question, soit des articles fournis comme contexte. ChatGPT étant plus dégourdi de la compréhension, j'avais espoir de ce côté-ci.

## Les résultats

Mes espoirs n'ont pas été déçus: en combinant l'approche d'embedding avec l'API `gpt-3.5-turbo` (oui, c'est son nom), on arrive à des scores presque parfaits:

![Synthèse des résultats]({{ root_url }}/images/2023-03-12_resultats_chatgpt_API.png)
<div class="photoattrib">Performance des différents modèles</div>

Cette méthode obtient 3.81/4 de moyenne, ce qui implique en général 1 ou 2 erreurs pour chacun des types de question. Cette approche permet également d’éviter les situations de réponse complètement erronée. Le détail des résultats est disponible [ici](https://docs.google.com/spreadsheets/d/1M_lYCFBuZ6nJXIXMxIYprET7rPaYOCA1pfi5Fjk8VFY/edit#gid=460853519). Et comme nous allons le voir, par la suite j'ai même été en mesure d'améliorer les résultats. 

## Comment ça marche

La nouvelle API fonctionne de manière différente de la précédente. Dans la précédente, il était seulement possible d'envoyer un message pêle-mêle (contenant de manière semi-structurée toute l'information à fournir: question et articles du code) et de recevoir une unique réponse. Pour rendre les fonctionnalités de ChatGPT disponible par API, notamment l'aspect conversationnel avec mémoire du contexte, il est désormais possible et nécessaire d'envoyer des requêtes plus structurées selon trois personas: le système, l'assistant ou l'utilisateur.

- Le système définit un peu les règles du jeu. Dans mon cas, le message système ressemblait à ceci: `Tu es un assistant qui répond clairement et de manière aussi fiable que possible à des questions sur le code de sécurité routière du Québec en te basant principalement sur des extraits du Code de sécurité routière du Québec qui te seront fournis. Il est important de fournir le ou les numéros d'articles appuyant la réponse.`
- L'utilisateur est, dans mon cas, celui qui pose des questions. Dans mon approche initiale d'embedding, j'envoyais un message séparé avec les articles du code pertinent, puis un message de question.
- L'assistant représente évidemment les réponses de ChatGPT... ceci dit, il est possible de lui mettre des mots dans la bouche. Par exemple, dans mon cas, entre mon message utilisateur contenant les articles pertinents et celui de la question, j'insérais une réponse de ChatGPT que j'avais décidé. C'est une manière de créer la dynamique d'échange que l'on souhaite.

Ainsi, j'envoyais *d'un coup*, dans une unique requête d'API au format JSON contenant les quatre messages suivants:
- `système` : Tu es  un gentil assistant
- `utilisateur` : Voici quelques articles du code de sécurité routière que je te demande d'utiliser pour répondre à des questions à venir: Art 241. blablabla
- `assistant`: Merci, je vais faire de mon mieux pour répondre à vos questions grâce à ces articles.
- `utilisateur`: Voici ma question: blablabla

En réponse à cette requête, je récupère la réponse que je peux évaluer.

## Limites de ma méthode et tests supplémentaires

En regardant de près les réponses fournies de cette manière, je me suis rendu compte que mes questions manquaient de précision. Pour être plus précis, même un humain n'aurait pas nécessairement fourni les réponses que j'attendais ou pas totalement. Pour être cohérent avec mes précédents tests, j'ai noté la nouvelle API selon les mêmes critères que ceux utilisés précédemment, mais c'est un peu dur. Par exemple, une question demandait comment doit agir un cycliste arrivant à une intersection avec des panneaux d'arrêt dans les quatre directions. La première réponse du modèle était qu'il en faut céder le passage aux véhicules et piétons qui ont la priorité. Sauf que pour mettre une note parfaite, je voulais qu'il m'explique comment est géré la priorité entre véhicules: premier arrivé, premier servi. À noter qu'en parlant des piétons, il introduisait une bonne réponse que je n'attendais pas.

Pour remédier à cette limite, la formule conversationnelle complète, que je n'avais pas implémentée dans mon script, semblait la meilleure approche puisque permettant de demander une précision sur une réponse du modèle. Quelques lignes de code plus tard, je pouvais donc demander au modèle de m'expliquer plus en détail l'ordre de priorité. La réponse devient alors un sans faute: premier arrivé, premier servi et (non attendu de ma part), en cas simultanéité, c'est le véhicule à droite qui a priorité... tout en me rappelant que les piétons ont priorité. L'échange au complet est disponible en annexe ci-bas.

J'avais créé mon ensemble de tests avec des articles du code en tête que je voulais voir sortir: je regardais un article du code et je me demandais quelle question je pouvais formuler pour qu'un modèle génératif me cite cet article. Avec l'API de ChatGPT, le modèle m'a régulièrement surpris (positivement) en combinant plusieurs articles de manière à mieux répondre à ma question que je l'envisageais moi-même.

## Système vs utilisateur

Par la suite, je me suis demandé si j'étais mieux de fournir mes articles du Code selon le persona `utilisateur` ou `système`. Là encore rien de mieux que de tester. Tous les modèles se sont plantés sur une question particulière: le port du casque est-il obligatoire à vélo au Québec ? Le piège: un article (492.2) stipule que le port du casque est obligatoire pour les « bicyclettes assistées » (sous-entendu électriques). Et lorsque j'ai posé la question via la nouvelle API, en fournissant les articles comme un message venant de `utilisateur`, le modèle a sauté à pieds joints dans le piège: le casque est obligatoire. En utilisant la fonction de discussion, je lui ai pointé le terme "assisté", et après une série d'échanges, le modèle a fini par "déduire" que le port du casque n'est pas obligatoire (voir l'échange complet ci-dessous), mais sa réponse manquait prêtait à confusion.

Dans un test suivant, j'ai fourni les articles de contexte comme venant de `système`, et **boum!**: réponse parfaite du premier coup. J'ai fait quelques essais sur des questions difficiles et le comportement s'est reproduit plusieurs fois: la voix du système porte plus. Difficile de donner une explication hors de tout doute, mais il semble qu'il y a un mécanisme, peut-être une forme de pondération, qui fait que les messages du système sont interprétés de manière plus stricte, avec plus d'attention, que les messages de l'utilisateur.

## Ce n'est pas parfait, mais tout de même...

Comme je le mentionnais au début, il reste les limites de l'embedding lui-même. Sur deux questions l'embedding n'a pas fourni un article de loi pertinent, donc le modèle n'avait pas l'information. Dans un cas particulier, ça semble d'ailleurs une erreur de ma part: l'article nécessaire n'était juste pas présent dans ma version segmentée du code de sécurité routière...

Il y a aussi un art de segmenter l'information correctement pour en faire des embeddings qui marchent bien. Avec quelques heures de plus à raffiner mon approche, j'aurais surement encore amélioré le résultat. Je pense même qu'en combinant toutes mes trouvailles subséquentes (meilleurs embeddings, fournir les articles pertinents par le persona `système`, accepter d'intégrer les sous-questions dans le résultat), je pense que j'aurais pu atteindre un score parfait, au moins pour les questions simples.

Il reste toutefois quelques limites. La principale est la limite de longueur: les requêtes à l'API demeurent limitées à 4000 tokens (~3000 mots), *incluant l'ensemble de l'historique*. Donc pour une discussion plus complexe, on atteint rapidement une limite de l'historique qu'il est possible de trainer avec soi —c'est une limite que n'a pas ChatGPT quand on l'utilise via le web. 

Lorsque j'ai interrogé ChatGPT sur sa mémoire, il m'a précisé avoir une "mémoire de dialogue" lui donnant accès à une version sommaire des échanges et qu'il a la capacité de "relire" certains messages passés si besoin. On ne peut pas croire ChatGPT sur parole, mais c’est cohérent avec son comportement. Donc si c’est vrai, j'en déduis que OpenAI a possiblement implémenté une forme de tour de passe-passe... par exemple, demander au modèle de faire une synthèse des échanges au fur et à mesure, synthèse qui est renvoyée dans chaque requête en guise d’historique/contexte (plutôt que d'envoyer l'historique au complet), et à cela pourrait s'ajouter un mécanisme permettant de rappeler un ou des messages spécifiques au besoin, une forme d'embedding.

Quoiqu'il en soit, l'API rendue disponible offre des capacités d'intégration assez impressionnantes. On peut imaginer de l'embedding de qualité sur une grande quantité d'information. Mais on peut aussi intégrer l'API dans des scénarios différents. Par exemple, avec quelques changements, j'ai pu transformer mon script en simulateur d'entrevue pour des embauches (là aussi, voir un exemple plus bas).

Le tout se fait avec une simplicité déconcertante. Par le passé, j'ai déjà suivi de cours/MOOC et joué avec des modèles de *machine learning* (pas seulement des générateurs de texte) et c'était passablement difficile d'obtenir des résultats cohérents sans réellement comprendre le fonctionnement du modèle. Ici, les outils fournis par OpenAI rendent tout cela très accessible à quiconque sachant aligner quelques lignes de code (et là encore, ChatGPT peut le faire pour vous!).

Déjà plusieurs entreprises avaient intégré GPT-3 dans des approches de chatbot ou d'assistant, le nombre d'exemples risque de grimper en flèche avec la nouvelle API. Pour commencer, Snapchat a déjà lancé un "ami virtuel", [MyAI](https://help.snapchat.com/hc/en-us/articles/13266788358932-What-is-My-AI-on-Snapchat-and-how-do-I-use-it-), basé sur cette API. 

## En annexe: quelques exemples mentionnés dans le texte

### Obligation du casque à vélo, version `utilisateur`

**Requête API initiale:** (la liste des articles est générée par la méthode d'embedding)
- `Système`: Tu es un assistant qui répond clairement et de manière aussi fiable que possible à des questions sur le code de sécurité routière du Québec en te basant principalement sur des extraits du Code de sécurité routière du Québec qui te seront fournis. Il est important de fournir le ou les numéros d'articles appuyant la réponse.
- `Utilisateur`: Voici quelques articles de loi tirés du Code de sécurité routière du Québec à utiliser pour la question à venir:
  - 212  Les vélos et les véhicules routiers doivent être équipés de tous les accessoires et équipements requis par la loi ou le règlement en vigueur au Québec.
  - 250.1.  Il est interdit de vendre, offrir en vente, louer ou offrir en location un casque protecteur pour les cyclistes et leurs passagers, à moins qu'il ne soit conforme aux normes établies par règlement.
  - 275.1.  Les propriétaires et les cyclistes dont les vélos ne sont pas conformes aux exigences des articles 212, 232, 233, du deuxième alinéa de l'article 235 ou des articles 237 ou 247 sont passibles d'une amende de 80 $ à 100 $. Les cyclistes qui ne portent pas une bande réfléchissante autour de chaque cheville ou des chaussures pourvues de bandes réfléchissantes sont également passibles d'une amende de 80 $ à 100 $.
  - 492.2.  Pour circuler avec une bicyclette assistée sur un chemin public, il faut être âgé d'au moins 18 ans ou titulaire d'un permis autorisant la conduite d'un cyclomoteur, porter un casque protecteur conforme aux normes établies par règlement, que la bicyclette porte l'étiquette du fabricant exigée par les règlements pris en application de la Loi sur la sécurité automobile et que la bicyclette soit conforme aux normes applicables à la bicyclette assistée prévues par le présent code et par les règlements pris en application de la Loi sur la sécurité automobile.
  - 504  La pratique du vélo est régie par des articles spécifiques et toute infraction à ces articles est passible d'une amende de 80 à 100$.
- `Assistant`: Je vais faire mon possible pour répondre à votre question avec les articles fournis
- `Utilisateur`: Au Québec, est-ce que le port du casque est obligatoire en vélo? Selon quel article de loi?

**Échanges subséquents** (l'ensemble de l'historique est renvoyé à chaque message de l'utilisateur):
- `Assistant`: Au Québec, le port du casque est obligatoire pour les cyclistes âgés de moins de 18 ans. L'article de loi qui régit cette obligation est le 492.1 du Code de sécurité routière du Québec. Toutefois, il est fortement recommandé pour tous les cyclistes de porter un casque pour leur propre sécurité.
- `Utilisateur`: Est-ce que tu es capable de me citer l'article en question?
- `Assistant`: Pardon, je me suis trompé dans la réponse précédente. L'article qui régit l'obligation de porter un casque protecteur pour les cyclistes et leurs passagers est le 250.1 du Code de sécurité routière du Québec. Cet article énonce que "Il est interdit de vendre, offrir en vente, louer ou offrir en location un casque protecteur pour les cyclistes et leurs passagers, à moins qu'il ne soit conforme aux normes établies par règlement." Toutefois, il n'y a pas d'obligation générale pour les cyclistes de porter un casque protecteur, sauf pour les cyclistes âgés de moins de 18 ans.
- `Utilisateur`: D'accord, mais est-ce que cela implique que le port du casque est obligatoire?
- `Assistant`: Comme je l'ai mentionné dans ma réponse précédente, il n'y a pas d'obligation générale pour les cyclistes de porter un casque protecteur. Toutefois, pour les cyclistes âgés de moins de 18 ans, il est obligatoire de porter un casque protecteur conformément à l'article 492.1 du Code de sécurité routière du Québec. Tous les autres cyclistes ne sont pas tenus de porter un casque par loi, mais cela est fortement recommandé pour leur propre sécurité.
- `Utilisateur`: Est-ce que l'article 492.1 dit vraiment que tous les cyclistes âgés de moins de 18 ans doivent porter un casque?
- `Assistant`: Je m'excuse pour la confusion dans ma dernière réponse. L'article 492.1 du Code de la sécurité routière du Québec oblige les cyclistes âgés de moins de 18 ans à porter un casque protecteur lorsqu'ils circulent sur un chemin public. L'article stipule que: "Le conducteur d’une bicyclette sur un chemin public et tout passager dont l’âge est inférieur à 18 ans doivent porter un casque protecteur dont le port est approuvé par règlement." En revanche, les cyclistes âgés de 18 ans et plus ne sont pas tenus de porter un casque. Cependant, le port du casque pour tous les cyclistes est fortement recommandé pour leur propre sécurité.
- `Utilisateur`: Je pense que tu as oublié un mot important: cette règle s'applique seulement aux vélos à assistance électrique
- `Assistant`: Je m'excuse encore une fois pour la confusion et pour les informations erronées que j'ai fournies précédemment. Vous avez raison, l'article 492.1 du Code de la sécurité routière du Québec stipule que le port du casque protecteur est obligatoire pour toute personne âgée de moins de 18 ans qui conduit ou qui est passager sur une bicyclette assistée électrique sur un chemin public. Le texte complet de l'article est le suivant: "Le conducteur d’une bicyclette assistée sur un chemin public et tout passager dont l’âge est inférieur à 18 ans doivent porter un casque protecteur dont le port est approuvé par règlement." Encore mes excuses pour cette confusion et j’espère que cela répond à votre question.
- `Utilisateur`: Donc, est-ce que le port du casque est obligatoire quand on est à vélo au Québec ?
- `Assistant`: Au Québec, le port du casque protecteur n'est pas obligatoire pour les cyclistes âgés de 18 ans et plus, excepté pour les conducteurs et passagers de bicyclettes assistées électriques. Toutefois, il est fortement recommandé de porter un casque protecteur pour tous les cyclistes, quel que soit leur âge, afin d'assurer leur propre sécurité.

En plus d'avoir du mal à interpréter et citer les articles, le modèle se trompe chaque fois dans le numéro de l'article (492.1 au lieu de 492.2).

### Obligation du casque à vélo, version `système`

Le message initial est le même, sauf que la liste des articles est envoyée en tant que `système` plutôt que `utilisateur`.

**Échanges subséquents:**
- `Assistant`: Au Québec, le port du casque est obligatoire pour les cyclistes âgés de 18 ans et plus qui utilisent une bicyclette assistée sur un chemin public, selon l'article 492.2 du Code de sécurité routière. Pour les cyclistes non-assistés, le port du casque n'est pas obligatoire, mais il est fortement recommandé par les autorités de sécurité routière. Cependant, selon l'article 250.1, le casque protecteur doit répondre aux normes établies par règlement, pour être vendu ou loué.
- `Utilisateur`: Est-ce qu'il est explicitement dit dans un article du code de sécurité routière que le port du casque n'est pas obligatoire ou c'est toi qui le déduis?
- `Assistant`: Je m'excuse si ma réponse précédente n'était pas claire. En effet, il n'est pas explicitement mentionné dans le Code de sécurité routière du Québec que le port du casque n'est pas obligatoire pour les cyclistes non-assistés. Cependant, l'article 492.2 du Code de sécurité routière stipule que le port du casque est obligatoire pour les cyclistes âgés de 18 ans et plus qui utilisent une bicyclette assistée sur un chemin public.
En revanche, malgré l'absence d'un article spécifique stipulant que le port du casque est obligatoire pour les autres cyclistes, les autorités de sécurité routière recommandent fortement aux cyclistes de porter un casque, afin de réduire les risques de blessures graves en cas d'accident. De plus, le port du casque protecteur pour les cyclistes est une mesure de sécurité de base qui est fortement recommandée et encouragée dans les campagnes de sensibilisation aux règles de sécurité routière.

Ici le modèle fournit directement les bonnes références tout en reconnaissant, de manière subséquente, que c'est une inférence en l'absence d'article obligeant le port du casque. On notera toutefois le biais "pro-casque" dans la réponse. En l'absence des références venant du code de sécurité routière, tous les modèles GPT d'OpenAI répondent que le port du casque est obligatoire.

### Arrêt quatre directions

Je n'ai pas conservé les articles de loi envoyés en embedding, donc voici directement les échanges:

- `Utilisateur`: Au Québec, comment doit agir un cycliste lorsqu'il arrive à une intersection avec un arrêt pour toutes les directions? Selon quel article de loi?
- `Assistant`: Au Québec, un cycliste doit s'arrêter à une intersection réglementée par des panneaux d'arrêt et céder le passage aux véhicules et aux piétons qui traversent ou longent la chaussée, comme il est mentionné à l'article 370 du Code de sécurité routière du Québec. Cela signifie que le cycliste doit complètement s'arrêter et attendre son tour pour passer, en cédant le passage aux véhicules et piétons qui ont la priorité. Si le cycliste arrive en même temps qu'un autre véhicule, le Code de sécurité routière stipule qu'il doit céder le passage au véhicule se trouvant à sa droite, en conformité avec l'article 402.
- `Utilisateur`: Tu écris "en cédant le passage aux véhicules et piétons qui ont la priorité". Comment définit-on la priorité dans cette situation?
- `Assistant`: En général, la priorité aux intersections réglementées par des panneaux d'arrêt est donnée au premier véhicule qui arrive à l'intersection (et qui a complètement fait un arrêt) en premier. Si plusieurs véhicules arrivent simultanément ou presque simultanément, le véhicule situé à droite a généralement la priorité, cela est mentionné dans l'article 402 du Code de sécurité routière du Québec. Il est important que les usagers de la route fassent preuve de bonne foi et de prudence afin d'éviter des accidents et de faciliter la fluidité de la circulation. Les piétons ont toujours priorité sur les véhicules et les cyclistes lorsqu'ils traversent une intersection ou longent une chaussée, comme le stipule l'article 369 du Code de sécurité routière du Québec.

Ici, la question avait été écrite pour obtenir une citation de l'article 370 précisant l'ordre de passage des véhicules arrivant à un arrêt quatre directions. Le modèle a toutefois perçu la pertinence de l'article 369 et surtout du 402 qui permet de résoudre certains cas d'arrivée simultanée. 

### Simulation d'un entretien d'embauche

**Requête API initiale:**
- `Système`: Tu t'appelles SelectAI, tu es un assistant automatisé simulant des entrevues d'embauche pour aider les chercheurs d'emploi à se préparer à des entrevues d'embauche. C'est toi qui pilotes la rencontre et qui poses des questions, tu simules l'intervieweur. Aujourd'hui, nous voulons simuler une entrevue pour un poste de développeur Python intermédiaire dans une startup.
- `Assistant`: Bonjour, merci d'avoir répondu à notre offre d'emploi pour un développeur Python de niveau intermédiaire. Comment allez-vous aujourd'hui?
 - `Utilisateur`: Je vais bien merci. C'est vraiment un plaisir d'avoir l'opportunité de pouvoir rejoindre votre organisation.

**Échanges subséquents:**
- `Assistant`: (Pour rappel, je suis un assistant automatisé et je simule l'entrevue. Je ne suis pas capable de ressentir des émotions ni de percevoir l'état de la personne à l'autre bout de l'écran.)
Pour commencer, pouvez-vous me parler de votre expérience en programmation Python? Quels sont les projets sur lesquels vous avez travaillé?
 - `Utilisateur`: Ok, je comprends. Avant de répondre à la question, comment dois-je vous appeler si je dois m'adresser à vous?
- `Assistant`: Vous pouvez m'appeler SelectAI. Je suis un assistant automatisé chargé de simuler votre entretien d'embauche pour le poste de développeur Python intermédiaire. Maintenant que nous avons fait les présentations, reprenons : pouvez-vous me parler de votre expérience en programmation Python? Quels sont les projets sur lesquels vous avez travaillé?
 - `Utilisateur`: J'ai 5 ans d'expérience en Python, plus 5 autres années comme Full stack dev incluant qui impliquait également de développer en Python environ la moitié du temps.
- `Assistant`: Excellente expérience! Pourriez-vous me parler de quelques projets sur lesquels vous avez travaillé et des tâches que vous avez effectuées en programmation Python?
- ...

Plusieurs choses que je trouve intéressantes ici: Premièrement, je donne un nom à l'assistant via la commande du système et le modèle est capable de réutiliser ce nom. Ensuite, le fonctionnement de l'API fait qu'il est possible d'amener le modèle à être le premier à parler (plutôt que d'attendre d'être questionné). Enfin, il est intéressant de noter que l'assistant annonce au début de l'interaction qui il est.

Les personnes habituées à ChatGPT ont déjà vu ou testé des cas visant à donner un rôle au modèle. Toutefois, il est intéressant de noter qu'avec l'API, il est possible de donner ce rôle sans que l'utilisateur doive le faire explicitement.