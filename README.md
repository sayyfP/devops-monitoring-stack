#  DevOps Monitoring Stack

Architecture multi-conteneurs orchestrée avec **Docker Compose** combinant un serveur web **Nginx**, un cache **Redis** et une sonde de disponibilité développée en **Python**.

## 🛠️ Technologies utilisées
- **Docker & Docker Compose** (Build d'image personnalisée, réseaux internes, volumes)
- **Nginx & Redis** (Images officielles Alpine)
- **Python 3** (Script de healthcheck automatisé avec journalisation)

## ▶️ Démarrage rapide
```bash
docker compose up -d --build
```
Accès au tableau de bord : `http://localhost:8085`
