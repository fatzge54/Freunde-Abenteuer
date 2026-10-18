# Charakter Model Sheets & Specs

Dieses Dokument beschreibt detailliert Design- und Modellanforderungen für die Hauptcharaktere: Lilo, Max, Pippa, Bobo und Wuffi. Verwende diese Spezifikation als Vorlage für Modellierung und Rigging.

Allgemeine Vorgaben
- Stil: rund, kindgerecht, starke Silhouetten, einfache, übertriebene Proportionen (großer Kopf, kurze Gliedmaßen).
- Texturstil: handpainted-stylized PBR (flächig, klare Farbflächen, geringe Texturdetails).
- Topologie: saubere Edge-Loops an Gelenken, quad-basierte Topologie.
- Polycount (Ziel): Hauptcharaktere: 20k–40k Tris (high), 3k–8k Tris (game/preview). Wuffi: 15k–30k (high), 2k–6k (preview).
- UV: Single UDIM optional, bevorzugt 0..1 Layout für einfache Pipeline.
- Materialien: Base color, Roughness, Normal (optional), Mask/ID map.

Lilo
- Größe (in Szene-Einheiten): ~1.0m (Kopf proportional größer)
- Merkmale: Univokales Kleid, kurze Haare mit Pony, freundlicher Gesichtsausdruck
- Farbschema: Pastellgelb (Haupt), Hellblau (Akzent), warmes Beige für Haut
- Blendshapes: Lächeln, Überraschung, Traurigkeit, Augenblinzeln
- Rig: Standard Humanoid (FK/IK für Arme, FK für Beine, Controls für Augen/Brow/Mouth)

Max
- Größe: ~1.05m
- Merkmale: etwas kräftiger, kurze Haare, abenteuerliches Outfit
- Farbschema: Grüntöne, warmes Braun
- Blendshapes: Lachen, Erstaunen, Verlegenheit
- Rig: Humanoid + sekundäre Feather controls für Schulterbewegungen

Pippa
- Größe: ~0.95m
- Merkmale: Brille, ordentliche Frisur, kleines Notizbuch als Prop
- Farbschema: Lavendel/rosa, neutrale Hauttöne
- Blendshapes: Denkerstirn, freundliches Lächeln
- Rig: Humanoid mit Finger-Controls für Halte- und Schreibposes

Bobo
- Größe: ~1.0m
- Merkmale: rundlicher, größere Augen, verrückte Frisur, bunte Kleidung
- Farbschema: Orange/rot/gelb Akzente
- Blendshapes: übertriebene Mimik (großes Lachen, Frust, Staunen)
- Rig: Humanoid mit zusätzlichen Stretch-Controls für komische Posen

Wuffi (Hund)
- Größe: ~0.5m Schulterhöhe
- Merkmale: runde Pfoten, große Augen, wedelnder Schwanz
- Farbschema: Creme/Braun Akzente
- Rig: Quadruped-Rig (FK/IK Beine, Tail-Spline, Face Controls für Ohren/Mund)
- Blendshapes: Schnauzenbewegung, Augen, Ohren-Positions

Export & Interchange
- Austauschformat: FBX export profile (animations baked optional), glTF für Web-Preview
- Namenskonvention: char_<name>_v01.fbx
- Versionierung: semantic (v01, v02) und Commit-Nachricht mit "MODEL: <char> v01".

Qualitäts-Checklist (pre-commit)
- [ ] Saubere Topologie an Gelenken
- [ ] Keine n-Verts/N-gons
- [ ] UVs ohne Überlappungen (außer symmetrische Shells)
- [ ] Materialslots korrekt benannt
- [ ] Rig controls klar benannt und dokumentiert
- [ ] Testpose in T-Pose und 3 Test-Posen (stehen, sitzen, laufen)

