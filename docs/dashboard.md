# Tableaux de Bord Grafana
Ce document décrit les tableaux de bord Grafana mis en place pour visualiser les métriques et les logs de l'application Django. Ces visualisations permettent un aperçu rapide de la santé et des performances de l'application.


# Vue d'ensemble du Tableau de Bord
Le tableau de bord est structuré pour fournir une vue complète, combinant des métriques de performance, des taux d'erreurs et des logs bruts pour faciliter le diagnostic.

# # # Capture d'écran du tableau de bord complet 

Panneaux de Métriques (Source : Prometheus)
Ces panneaux utilisent les métriques collectées par Prometheus via django-prometheus.

1. Latence par Vue (95e centile)
Description : Affiche le 95e centile du temps de réponse des requêtes, segmenté par chaque vue de l'application. C'est un indicateur clé de l'expérience utilisateur.

Type de panneau : Graph

Requête PromQL :

histogram_quantile(0.95, rate(django_http_requests_latency_seconds_by_view_method_bucket{job="django"}[5m]))

Capture d'écran du panneau :

2. Taux de Requêtes par Vue
Description : Montre le nombre de requêtes par seconde pour chaque vue de l'application, permettant d'identifier les points d'entrée les plus sollicités.

Type de panneau : Graph

Requête PromQL :

sum by (view) (rate(django_http_requests_total_by_view_transport_method_total{job="django"}[5m]))

Capture d'écran du panneau :

3. Taux d'Erreurs HTTP (4xx et 5xx)
Description : Visualise le taux d'erreurs client (4xx) et serveur (5xx) sur l'application. Crucial pour la détection des dysfonctionnements.

Type de panneau : Graph

Requêtes PromQL :

Erreurs 5xx : sum(rate(django_http_responses_total_by_status_total{status=~"5..",job="django"}[5m]))

Erreurs 4xx : sum(rate(django_http_responses_total_by_status_total{status=~"4..",job="django"}[5m]))

Capture d'écran du panneau :

4. Utilisation des Ressources (CPU et Mémoire)
Description : Surveille la consommation des ressources système par le processus Django.

Type de panneau : Graph

Requêtes PromQL :

CPU : rate(process_cpu_seconds_total{job="django"}[5m])

Mémoire : process_resident_memory_bytes{job="django"}

Capture d'écran du panneau :

Panneaux de Logs (Source : Loki)
Ces panneaux affichent les logs collectés par Promtail et stockés dans Loki.

1. Logs de l'Application Django
Description : Affiche les logs bruts de l'application Django en temps réel, essentiels pour le diagnostic détaillé des incidents.

Type de panneau : Logs

Requête LogQL :

{service="django_app"}

Capture d'écran du panneau :

2. Logs d'Erreurs (filtrés)
Description : Affiche uniquement les lignes de logs contenant le mot "error", facilitant l'identification rapide des problèmes.

Type de panneau : Logs

Requête LogQL :

{service="django_app"} |= "error"

Capture d'écran du panneau :