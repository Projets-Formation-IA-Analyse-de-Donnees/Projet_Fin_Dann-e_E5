# Tableaux de Bord Grafana
Ce document décrit le tableau de bord Grafana mis en place pour visualiser les métriques et les logs de l'application Django. Ces visualisations permettent un aperçu rapide de la santé et des performances de l'application.


## Vue d'ensemble du Tableau de Bord
Le tableau de bord est structuré pour fournir une vue complète, combinant des métriques de performance, des taux d'erreurs et des logs bruts pour faciliter le diagnostic.

![Vue d'ensemble du Tableau de Bord](img\all.png)


## Latence 
Description : Affiche le 95e centile du temps de réponse des requêtes. C'est un indicateur clé de l'expérience utilisateur.




 
```promql
rate(django_http_requests_latency_including_middlewares_seconds_sum[5m]) / rate(django_http_requests_latency_including_middlewares_seconds_count[5m])
```





![Graphique](img\latence.png)

## Taux de Requêtes par Vue
Description : Montre le nombre de requêtes par seconde pour chaque vue de l'application, permettant d'identifier les points d'entrée les plus sollicités.




```promql
rate(django_http_requests_total_by_view_transport_method_total[5m])
```


![Graphique](img\requetes_par_vue.png)

## Taux d'Erreurs HTTP (4xx et 5xx)
Description : Visualise le taux d'erreurs client (4xx) et serveur (5xx) sur l'application. Crucial pour la détection des dysfonctionnements.




* Erreurs 5xx : 
```promql
sum(rate(django_http_responses_total_by_status_total{status=~"5.."}[1m]))
```
![Graphique](img\taux_erreur_5XX.png)

* Erreurs 4xx :
```promql
sum(rate(django_http_responses_total_by_status_total{status=~"4.."}[1m]))
```

![Graphique](img\taux_erreur_4XX.png)


## Utilisation des Ressources (CPU et Mémoire)
Description : Surveille la consommation des ressources système par le processus Django.



* CPU: 
```promql
rate(process_cpu_seconds_total[1m])*100
```
![Graphique](img\CPU.png)

* Mémoire:
```promql
process_resident_memory_bytes{instance="django:8000"}
```

![Graphique](img\memoire.png)



## Logs de l'Application Django
Description : Affiche les logs bruts de l'application Django en temps réel, essentiels pour le diagnostic détaillé des incidents.




 ```logql
{service="django_app"}
```


![Graphique](img\logs.png)

![Graphique](img\nb_logs.png)




