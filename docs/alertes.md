# Règles d'Alertes Grafana
Ce document détaille les règles d'alertes configurées dans Grafana pour le monitorage de l'application Django. Ces alertes sont essentielles pour la détection proactive des incidents et sont acheminées vers un canal Discord.

![Graphique](img\alertes_all.png)

## Alerte : Erreurs serveur (5xx)
- Objectif : Notifier immédiatement toute erreur interne du serveur.

- Source de données : Prometheus

- Requête PromQL :
```bash
sum(rate(django_http_responses_total_by_status_total{status=~" 50. ",job="django"}[1m])) > 0
```


-  Condition : est supérieure à 0 pendant 1 minute.

-  Justification : Un taux d'erreurs 5xx supérieur à zéro indique un dysfonctionnement critique de l'application.

## Alerte : Erreurs client (4xx)
-  Objectif : Signaler un nombre anormalement élevé de requêtes client invalides ou de ressources non trouvées.

-  Source de données : Prometheus

-  Requête PromQL :
```bash
sum(rate(django_http_responses_total_by_status_total{status=~" 40. "}[1m])) > 0
```


-  Condition : est supérieure à 0 pendant 1 minutes.

-  Justification : Un taux d'erreurs 4xx supérieur à zéro peut indiquer des liens brisés, des tentatives d'accès non autorisées ou des problèmes de configuration côté client.

## Alerte : Latence élevée
-  Objectif : Prévenir si le temps de réponse de l'application dépasse un seuil acceptable.

-  Source de données : Prometheus

-  Requête PromQL :
```bash
histogram_quantile(0.95, rate(django_http_requests_latency_including_middlewares_seconds_bucket{job="django"}[1m])) > 2
```


-  Condition : est supérieure à 2 pendant 1 minutes.

-  Justification : Un 95e centile de latence supérieur à 2 secondes dégrade significativement l'expérience utilisateur.



## Alerte : Aucune donnée Prometheus (Panne de service)
-  Objectif : Alerter si Prometheus ne parvient plus à collecter les métriques de l'application Django, indiquant une potentielle panne du service.

-  Source de données : Prometheus

-  Requête PromQL :
```bash
up{job="django"} == 0 
```

-  Condition : est égale à 0.

-  Justification : La métrique up à 0 signifie que le service est inaccessible, signalant une panne critique.

## Configuration de la gestion du "No Data"
Pour éviter les faux positifs dus à des absences temporaires de données, toutes les alertes sont configurées avec l'option "No Data". Cela garantit que l'alerte ne se déclanche que lorsque des données apparaissent.

## Configuration des notifications
Pour recevoir les notifications d'alerte, Grafana utilise des points de contact qui définissent où et comment les alertes doivent être envoyées. Pour ce projet, plusieurs webhook Discord ont été configurés comme point de contact. Cela permet de centraliser les alertes directement dans un serveur Discord dédié (répartissant les mesages dans plusieurs canaux spécialisés), offrant une visibilité immédiate du problème. La création d'un webhook Discord est une étape simple dans les paramètres du serveur Discord, fournissant une URL unique que Grafana utilise pour envoyer les messages d'une alerte.



Tu peux maintenant consulter le dashboard configurée avec Graphana dans le fichier suivant : [Voir la documentation du Dashboard](dashboard.md)