# Configuration du Système de Monitorage

Ce document décrit la configuration détaillée des composants Prometheus, Grafana, Loki et Promtail, ainsi que leur orchestration via Docker Compose.

## Structure des Fichiers

```bash
├── docker-compose.yml
├── prometheus_config/
│   └── prometheus.yml
├── loki_config/
│   └── loki-config.yml
└── promtail_config/
    └── promtail-config.yml
```




## Fichier docker-compose.yml
Ce fichier est le cœur projet, il définit et orchestre tous les services de monitoring (Prometheus, Grafana, Loki, Promtail) en tant que conteneurs Docker. Il gère également la persistance des données de ces services grâce à des volumes nommés, ce qui garantit que les métriques et logs ne sont pas perdus lorsque les conteneurs sont arrêtés ou recréés. De plus, il connecte ces services à un réseau Docker externe (backend_net) pour qu'ils puissent communiquer avec l'application Django, qui est déployée dans un autre docker-compose. Chaque service est configuré avec son image Docker, les ports exposés, et les volumes pour monter les fichiers de configuration et stocker les données.

## Fichier prometheus.yml
Ce fichier est le fichier de configuration de Prometheus. Il indique à Prometheus quelles cibles il doit surveiller et à quelle fréquence. Dans ce cadre, il est configuré pour collecter les métriques de l'application Django. La section scrape_configs définit un "job" nommé 'django' qui cible le service Django sur le port 8000. C'est ainsi que Prometheus sait où aller chercher les données de performance de l'application. L'intervalle de collecte est également défini ici, indiquant à quelle fréquence Prometheus va interroger l'application pour de nouvelles métriques.

## Fichier loki-config.yml
Ce fichier configure le serveur Loki, le système d'agrégation de logs. Il définit comment Loki doit fonctionner, notamment le port sur lequel il écoute pour recevoir les logs de Promtail. La configuration spécifie également le chemin où Loki va stocker ses données de logs de manière persistante sur le volume Docker dédié. Des paramètres de schéma de stockage sont également définis pour optimiser la manière dont les logs sont indexés et récupérés, tout en assurant la compatibilité avec la version de Loki utilisée.

## Fichier promtail-config.yml
Ce fichier configure Promtail, l'agent de collecte de logs. Son rôle est de lire les logs générés par les conteneurs Docker et de les envoyer à Loki. Promtail peut filtrer les logs pour ne collecter que ceux du conteneur Django (django_app) et leur attribuer des labels spécifiques (service: django_app), rendant ainsi les logs facilement interrogeables dans Grafana. C'est ce fichier qui fait le lien entre les logs bruts de l'application et le système de gestion de logs Loki.

Tu peux maintenant consulter la liste des alertes configurée dans le fichier suivant : [Voir la documentation des alertes](alertes.md)
