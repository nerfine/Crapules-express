# 🚚 Crapules Express - Discord Bot ![Version](https://img.shields.io/badge/version-1.4.7-blue.svg)

Bienvenue dans le dépôt officiel du bot Discord de **Crapules Express**, une VTC virtuelle sur le jeu *Euro Truck Simulator 2* (ETS2).

Ce bot a été développé spécifiquement pour gérer les **recrutements**, les **tickets personnalisés**, les **convois**, les **logs RH**, et la **modération interne** de la VTC.

> 🔧 **Développé par** : [nerfine](https://github.com/nerfine)

---

**⚠️ MAINTENANCE INDÉTERMINÉE ⚠️**

Un problème technique majeur est survenu avec le PC utilisé pour le développement et l’hébergement du bot.

---

## ℹ️ État actuel du bot

* Le bot est **partiellement hors ligne**.  
* **Aucune fonctionnalité principale** (tickets, recrutements, logs, modération) n’est actuellement disponible.  
* **Aucune donnée compromise**. Pour des raisons de sécurité, toutes les données ont été supprimées : tout est sécurisé.

---

## 🔄 Changements récents

* Le bot a été **réécrit en Python** (fin du développement en Discord.js).  
* La commande `/bot` a été entièrement **refaite**.  
* Le système d’**invite tracker** et le **welcomer** ont été refaits et fonctionnent actuellement.

---

## 📌 Fonctionnalités principales (hors ligne actuellement)

- 🎟️ Système complet de **tickets Discord** :  
  - Recrutement (formulaire + suivi)  
  - Questions à la direction (message RH + bouton dirigeant)  
  - Réservations et invitations de convois  
- 📋 **Formulaire de recrutement interactif** (boutons, embeds dynamiques)  
- ✅ Validation RH avec boutons **Accepter / Refuser / Blacklist**  
- 🔁 **Attribution automatique de casier** RH lors du recrutement  
- 📁 **Archivage automatique** du casier si le chauffeur quitte Discord  
- 🔒 **Limitation à 3 tentatives** de candidature (blocage automatique)  
- 🛑 Suppression automatique des tickets de recrutement **inactifs après 24h**  
- 🧠 Système de **logs internes** (recrutement, blacklist, whitelist, départs)  
- 🔔 Notifications RH / Direction / Communication (selon type de ticket)  
- 🧾 Panel d’administration pour activer/désactiver les recrutements  
- ⚙️ Commandes avancées : `/blacklist`, `/whitelist`, `/modifier-db`, `/info`  
- 🌐 **Traduction de message via réactions** (:globe_with_meridians:, :flag_gb:, :flag_us:) *(hors embeds)*  
- 🕒 Commande `/bot` pour consulter version, ping, uptime  

---

## 💬 Commandes disponibles

| Commande | Description |
|---------|-------------|
| `/bot`  | Affiche les **informations du bot** : version, ping, uptime |

---

## 🔐 Politique de confidentialité

Crapules Express s'engage à respecter la vie privée des utilisateurs.

- ✅ [Lire la politique de confidentialité complète](https://github.com/Nerfine/crapules-express/blob/main/privacy.md)  
- 📁 Données stockées localement (VPS personnel) sans partage tiers  
- 🗑️ Suppression des salons de recrutement inactifs après 24h  
- 🔐 Accès restreint au staff RH, DRH et Direction uniquement  

---

## 🧱 Technologies utilisées

- Anciennement Discord.js (Interactions via boutons, menus, embeds dynamiques)  
- Maintenant : **Python** (réécriture en cours)  
- Base de données locale (fichiers JSON ou stockage persistant VPS)  
- Webhooks pour logs internes  
- Système de permissions basé sur rôles Discord  
- Hébergement local via **VPS sur machine personnelle**  

---

## 🧑‍💼 Destiné à :

Ce bot est **strictement réservé** à un usage interne au sein de la VTC **Crapules Express**.

> ❌ Toute reproduction, distribution ou adaptation sans accord est interdite.

---

## 📄 Licence

Ce projet est sous **licence privée**.  
Tous droits réservés © **Crapules Express** – [nerfine](https://github.com/nerfine)

---

## 🤝 Contact

Pour toute question, demande de modification ou signalement de bug :

- 💬 Discord : **@nerfine**  
- 📬 GitHub : [Créer une issue](https://github.com/Nerfine/crapules-express/issues)  

---

Merci pour votre compréhension et votre patience pendant cette période difficile.
