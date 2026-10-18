# Voice Casting, TTS-Konfiguration und Skripte

Vorbereitung
- Jede Episode: VO-Skript-Datei in /audio/voice-scripts/ep01_vo_de.md
- Stimme pro Figur zuordnen: Lilo (hell, weiblich-kindlich), Max (nicht zu laut, mutig), Pippa (ruhig und freundlich), Bobo (überdreht, fröhlich), Wuffi (effektbasiert, Barks/Whines)

TTS-Empfehlungen (Prototyp)
- Coqui TTS: deutsch, voice model: "linda" oder "anna" (prüfe auf natürl.)
- Google Cloud TTS: "de-DE-Wavenet-A" (mild), "de-DE-Wavenet-B" (kinderlich)
- ElevenLabs: sehr natürlich, aber kommerziell lizenziert

Parameter für TTS
- Sprache: de-DE
- Speaking rate: 0.95–1.05 (variiere per Figur)
- Pitch: +2–6% für kindliche Stimme
- SSML: kurze Pausen (<break time="200ms"/>) zwischen Sätzen

Dateiformat
- WAV, 48kHz, 24bit
- Benennung: ep##_charname_line##_v01.wav

Beispiel-Skript (Episode 1, Szene 1)
- LILO: "Oh! Seht mal! Diese Blume ist gelb wie die Sonne!"
- MAX: "Und das hier ist grün! So grün wie die Blätter auf den Bäumen!"

Casting-Notes (Final-VO)
- Bitte Aufnahmen trocken (ohne Raumhall) liefern
- 3 takes pro Satz: neutral, fröhlich, nachdenklich
- Dateinennung + Voice-Release-Form unterschreiben
