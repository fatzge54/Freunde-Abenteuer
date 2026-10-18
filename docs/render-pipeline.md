# Render- und Produktions-Pipeline

Ziel: effizienter, reproduzierbarer Workflow für 5×5 Minuten 3D-Episoden.

1) Software-Stack
- Blender (Modeling, Rigging, Animation, Shading, Compositing)
- GIMP/Krita (Texturen, Storyboard-Illustrationen)
- Audacity/Reaper (Audio-Editing)
- DaVinci Resolve (Final Cut, Color Grading)
- Optional: Render-Farm (SheepIt, Blendergrid, oder kommerzielle Anbieter)

2) Arbeitsdateien & Ordnerstruktur (im Repo)
- /scenes/episode-01/ -- .blend-Dateien (keine großen baked caches committed)
- /assets/models/
- /assets/textures/
- /audio/voiceover/
- /audio/music/
- /boards/
- /exports/renders/ (PNG/EXR sequences)

3) Render-Einstellungen (Empfehlung)
- Auflösung: 1920x1080 (Full HD) für finale Exporte
- Renderer: Cycles (GPU) für hochwertige Bilder; Eevee für schnelle Vorschauen
- Samples (final): 512–2048 abhängig von GPU; Denoise aktiv
- Dateiformat: EXR (multilayer) für Renderpass-Workflows; PNG für Proxies
- Color Management: Filmic (Blender), ACES optional

4) Animation & Proxy-Workflow
- Animations: Arbeite mit Low-Res Proxy-Geometrie für schnellere Playback
- Baking: Nur lokal für Physics; vermeide große Caches in Repo
- Versioning: speichere iterative Dateien mit semantischen Tags (v01, v02)

5) Compositing & Finalisierung
- Nutze Render Passes (diffuse, specular, emission, shadow) für Kontrolle
- Color Grade in DaVinci/Blender Compositor
- Export: H.264 MP4 (for web) + ProRes or DNxHD for archival masters

6) Audio-Sync
- VO: 48 kHz, 24-bit WAV
- Musik: separate tracks für Anpassung während Schnitt
- Master: Final mix in DaVinci with 3-band EQ and light compression

7) Templating & Automation
- Blender startup .blend mit standardized scene scale, camera rigs, light rigs
- Python-Scripts für batch render (CLI), naming conventions, and EXR packing

8) Hardware & Zeitplanung
- Einzelperson, Desktop GPU (RTX 3060+): Rechenzeit für 5min Episoden kann Tage dauern
- Für Final-Quality: erwäge Cloud-Render oder Queueing über mehrere Maschinen

9) Dokumentation
- Jede Szene-Ordner hat eine README.md mit: Blend-Version, verwendete Addons, render-aufgabe, zuständig
