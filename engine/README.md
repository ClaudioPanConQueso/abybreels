# Motor de reels AByB Host (estilo educativo, 7 láminas)
Requisitos: python3, Pillow, numpy, ffmpeg.
1) pip install kokoro-onnx soundfile --break-system-packages
2) curl -L -o k.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
   curl -L -o v.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
3) Copiar host.py, build.py y build2.py a una carpeta con k.onnx y v.bin
4) python3 build2.py  -> genera w_<video>.py (un script por video, definido en el dict V2 de build2.py)
5) python3 w_<video>.py salida.mp4   (tarda ~2-3 min; correr de a 2 en paralelo con timeout 280)
Para un video nuevo: agregar una entrada a V2 en build2.py (S = locución [(texto en pantalla, texto hablado)], tags, SC = escenas usando helpers: title, features, stat, cmp, grid, chat, panel, stopw, chip, rack, monitor, avatar, gamer, cta2).
Voz: em_alex (Kokoro). Pronunciación: Abyb, Guasap, Ce Pe U, Terodáctil, Ese Ce Pe.
