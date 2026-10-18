# Milestones, Savepoints und Backups

Ziel: sichere Zwischenstände regelmäßig speichern, um Datenverlust zu vermeiden.

Milestone-Plan (empfohlen):
- Milestone 0: Konzept & Episoden-Skripte (COMPLETED)
- Milestone 1: Storyboards & Animatics (DELIVERABLE)
- Milestone 2: Charakter-Model-Sheets & Low-Poly-Blockout
- Milestone 3: Final-Models & Rigging
- Milestone 4: Keyframe-Animationen (1 Episode fertig)
- Milestone 5: Final-Renders & Compositing (1 Episode)
- Milestone 6: Audio-Mix & Mastering (1 Episode)
- Milestone 7: Final Delivery (5 Episoden Master)

Speicher-Policy
- Bei jedem Milestone: erstelle einen "savepoint"-Commit mit Tag: savepoint-<milestone>-YYYYMMDD
- Speichere große Binärdateien (Blend Caches, EXR) in externem Cloud-Speicher (Google Drive/Dropbox/AWS S3), im Repo nur Referenz-Links
- Jede Szene-Ordner enthält "SCENE_README.md" mit Blend-Version, benötigten Add-ons und kurzer Renderbeschreibung

Automatisierung
- Nutze nightly backups: script backup_to_s3.sh (nicht in Repo, konfiguriert lokal)
- Führe vor großen Änderungen: export of current scene as .blend (incremental name)

Wiederherstellungs-Prozedur
1. Prüfe neueste savepoint-Tag
2. Lade Referenzen/Assets aus Cloud (falls notwendig)
3. Lade Blendfile vXX und öffne in Blender
4. Erstelle lokalen Branch: work/<scene>-<date>

