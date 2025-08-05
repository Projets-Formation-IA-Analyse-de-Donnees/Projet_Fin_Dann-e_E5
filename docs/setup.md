# Lancement du projet

Voici les étapes nécessaires pour configurer et lancer l’ensemble du projet 



## Prérequis

- Python 3.10 ou supérieur
- Docker



## Étapes d'installation


### 1. Cloner le dépôt dans votre répertoire de travail
```bash
git clone <lien-du-repos>
cd Projet_Fin_Dannee_E5
```

### 2. Lancer les services Docker
```bash
docker-compose up -d --build
```

### 3. Accéder aux interfaces

* Grafana : `http://localhost:3001` (identifiants par défaut : admin/admin si non modifiés).

* Prometheus : `http://localhost:9090`



## Configuration des services


Pour la configuration et des explications sur chaque composant, consultez le fichier suivant : [Voir la documentation d'orchestration](orchestration.md)
