

## 1) Introduction


Lors de ce stage mon but est de compenser les variations globales de champ magnétique. Pour cela, je dispose d'un capteur tri-dimensionel relié à un arduino, qui sera chargé de détecter une perturbation du champ magnétique pour ensuite commander les sources de courant des nappes qui entourent la manip et corriger le zéro de champ magnétique.


### 2) Librairie LSM303 

Ce capteur fonctionne avec le protocole I²C. Le signal renvoyé sur les pins du capteurs n'est donc pas directement la valeur du champ magnétique. J'ai donc utilisé une librairie arduino pour obtenir alors cette valeur.

Librairie arduino utilisée : LSM303 par Polulu 

Lien github : https://github.com/pololu/lsm303-arduino

Pour avoir 220 Hz de fréquence d'échantillonage du capteur (fréquence maximale) il faut modifier la valeur du DO (data output) dans le fichier cpp 0x0c ==> 0x1c. .

Possibilité de modifier l'amplitude de mesure en modifiant le GN dans le fichier cpp. Actuellement reglé à $\pm$ 1.3 g

Attention, une mise à jour de la librairie resetera probablement ces paramètres.

Une fois que le capteur renvoie une valeur, on peut vérifier qu'il n'y a pas d'offset. Pour cela on peut print les valeurs renvoyées par le capteur dans le serial monitor, noter la valeur des trois axes puis tourner le capteur de 180 degrés pour chaque axe. On est censé retrouver la même valeur, à un signe moins près. Si ce n'est pas le cas c'est qu'il y a un offset.

$$ B_{\textrm{à l'endroit}} = B + \textrm{offset}  $$

$$ B_{\textrm{à l'envers}} = - B + \textrm{offset}  $$

$$ \implies \textrm{offset} = \frac{B_{\textrm{à l'endroit}} + B_{\textrm{à l'envers}} }{2}$$

On soustrait ensuite la valeur de cet offset pour avoir des valeurs sans offset. On peut vérifier notre calibration en calculant la norme du champ magnétique et en vérifiant qu'elle reste constante pendant qu'on tourne le capteur.

Le capteur nous renvoie maintenant un float, auquel il faut maintenant appliquer la calibration ("Magnetic gain setting") donnée dans le manuel d'utilisation du LSM303 page 9 : https://cdn-shop.adafruit.com/datasheets/LSM303DLHC.PDF 

Pour le GN à '001', il est indiqué 1100 LSB/gauss (Least Significant Bit / gauss) pour x et y et 980 LSB/gauss pour z.

On obtient finalement une mesure du champ magnétique.

Plus d'infos sur DO et GN dans la docu du LSM303


### 3) Lecture


Pour récupérer les données du capteur dans python, on importe la bibliothèque serial, qui permet d'accéder à l'arduino. On crée deux fonctions pour initialiser et fermer la connection avec l'arduino depuis python.

On peut alors lire ce qu'il y a dans le serial monitor puis on le décode dans un array numpy avec le temps de la mesure, Bx, By et Bz. On save ensuite cette mesure dans un fichier npy. c'est la fonction querry.

On peut aussi avoir envie de mesurer plus qu'une mesure à la fois, d'où la fonction lecture, qui mesure le champ autant de fois qu'on lui demande et stocke le log dans un fichier npy.

### 4) Visualisation

Pour visualiser nos mesures on peut les plots dans ce notebook en chargeant le fichier log et en le plottant avec matplotlib, et on peut aussi essayer d'en analyser le spectre avec un transformée de Fourier, pour voir si des phénomènes périodiques se cachent dans le bruit, comme le signal à 50 Hz du courant alternatif. Cependant, même en enlevant la moyenne, la composante constante du signal crée un pic en 0 Hz qui nous empêche d'observer le spectre. C'est pourquoi on plot qu'une partie de ce dernier.

### 5) Commandes en SCPI

Les sources de courant qui alimentent les nappes ont un port GPIB ce qui nous permet de les piloter via un ordinateur avec des commandes SCPI. Voila les fonctions de bases qui permettent d'établir et fermer la connection avec les sources, leur envoyer une commande et recevoir une réponse.

### 6) Modélisation des nappes

Pour connaître la réponse en courant des bobines, on peut tenter de mesurer cela expérimentalement, ou alors on peut faire une modélisation de ces dernières, puis de calculer le champ qu'elles émettent en fonction du courant qu'on leur envoie. C'est ce qui est fait ici à l'aide de la librairie magpylib. Elle a pour convention de mettre les courants en ampère, les champs en mT et les distances en mm. 

Les axes x, y et z utilisés ici correspondent à ceux utilisés dans la salle de manip pour l'orientation des bobines

Le ratio entre le courant envoyé dans les bobines Bz 1 et 2 permet d'avoir un champ plutôt homogène au niveau de la manip. C'est pourquoi on utilise que 3 courants et qu'on en déduit le 4ème avec ce ratio.


En inversant le coefficient de proportionalité entre B et I on peut connaître la correction à appliquer sur le courant pour compenser une variation de champ magnétique. C'est ce qu'on cherche à faire ici.

### 7) Calibration

Après avoir calculé ces coefficients numériquement, on peut aussi essayer une approche expérimentale en faisant les mesures en vrai. Cependant le centre de la manip n'est pas accesible, il faut donc réaliser les mesures au plus près et soit approximer que le champ est parfaitement uniforme proche du centre, soit réaliser plusieurs mesures autour du centre et interpoler les résultats. Pour faire cette manip, voici le protocole :

On place notre capteur à une position fixe au plus près de la manip en minimisant tout autre source de champ magnétique. 

A l'aide du code ci-dessous on commande les sources pour faire varier le courant dans les bobines indépendamment et mesurer la réponse en champ magnétique dans les trois directions. On obtient alors une matrice 3x3 qu'on doit inverser pour obtenir la conversion entre champ et courant. D'après la modélisation, cette matrice est diagonale sur l'axe, donc en étant un peu excentré, elle ne le sera pas mais les termes non diagonaux devraient être plus petits que les termes diagonaux.

### 8) Conversion

Le passage du champ magnétique mesuré au courant se fait donc par simple multiplication matricielle.

### 9) Compensation

### 10) Temps de réponse

Pour mesurer un temps de réponse du système, j'ai triggé sur l'oscilloscope un GBF qui commandait un switch laissant passer ou non du courant dans un bobine. En parallèle, le capteur était branché aux sources et pouvait les piloter. Une des 4 sorties de la source de courant était branchée sur une résitance dont la tension était envoyée sur une autre voie de l'oscilloscope. J'ai pu donc observer que lorsque le courant passe dans la bobine, le capteur mesure une modification du champ magnétique puis envoie une commande aux sources qui changent alors la valeur du courant en sortie. On mesure alors le temps de réponse du capteur, puis du code, puis de la commande GPIB, auquel s'ajoute le temps que met la source à changer le nouveau courant. D'après la documentation de la source, il serait inférieur à 10 ms. A cela il faudra ajouter le temps de réponse des bobines.

