# Projet Légifrance - Monitorage d'Application et maintien en condition opérationnelle

Ce projet a pour objectif de mettre en place un système de monitorage complet pour l'application web Django. Il vise à assurer le maintien en condition opérationnelle de l'application en fournissant une visibilité en temps réel sur ses performances, sa santé et ses logs. Ce travail s'inscrit dans le cadre de la compétence E5 du référentiel.

Le système permet de détecter, diagnostiquer et résoudre les incidents rapidement, garantissant ainsi une meilleure disponibilité et une meilleure expérience utilisateur.

Le système de monitorage est construit autour de plusieurs services :

- Prometheus : Un système de surveillance et d'alerte basé sur une base de données de séries temporelles. Il collecte les métriques exposées par l'application Django.

- Grafana : Une plateforme d'analyse et de visualisation de données. Elle permet de créer des tableaux de bord interactifs et de configurer des règles d'alerte.

- Loki : Un système d'agrégation de logs, optimisé pour le stockage et l'interrogation de grands volumes de données textuelles, conçu pour s'intégrer parfaitement avec Grafana.

- Promtail : L'agent de collecte de logs pour Loki. Il est déployé aux côtés de l'application Django pour collecter ses logs et les envoyer à Loki.

- Django-Prometheus : Une bibliothèque Python qui expose automatiquement les métriques de l'application Django au format Prometheus.


## Table des matières

- [Lancement du projet](docs/setup.md)
- [Orchestration](docs/orchestration.md)
- [Alertes](docs/alertes.md)
- [Dashboard](docs/dashboard.md)




