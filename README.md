# alkalomadtanDjango
[![wakatime](https://wakatime.com/badge/user/0ec14411-be49-464a-9639-0907ad5f39a6/project/61257642-a2e0-450e-9857-f2db7d6278f9.svg)](https://wakatime.com/badge/user/0ec14411-be49-464a-9639-0907ad5f39a6/project/61257642-a2e0-450e-9857-f2db7d6278f9)

[![wakatime](https://wakatime.com/badge/user/0ec14411-be49-464a-9639-0907ad5f39a6/project/128ab571-63bb-4654-aebb-60967f1583b4.svg)](https://wakatime.com/badge/user/0ec14411-be49-464a-9639-0907ad5f39a6/project/128ab571-63bb-4654-aebb-60967f1583b4)

## Szoftveres követelmény
### Windwos
- Python 3.10 vagy újabb
- Django 4.1 vagy újabb
- Windows 10 / 11

## Szerver és projekt futtatásához
Ahhoz hogy a szerver megfelelően fusson fontos egy pár lépést megtenni a futtatáshoz!

### Windows
1. Klónozza le a projekt-et
2. A klónozott mappába ahova hozzon létre egy python virtuális környezetet!
``` python
py -m venv vnev 
```
Javasoljuk ahogy apéldában is látszódik a "venv" nevet meghagyni.
3. Virtuális környezet indítása
Ez után índítsa el az adott virtuális környezetet *cmd*-ben majd navigáljon el a `\alkalomadtanProjekt` mappába és kedje el írni az alábbi parancssort:
``` cmd
venv\Scripts\activate.bat
```
Természetesen a "venv" rész változhat amennyiben Ön máshogy hozta létre a virtuális környezetet!
4. Telepítse a Django keretrendszert míg a fut a virtuáliskörnyezet!
Ügyeljen arra hogy a telepítéshez kell a `pip` python kiegészítő!
```
py -m pip install Django
```
5. Lépjen bele az "alkalomadtan" nevű mappába
6. futtasa le az indító kódot!
``` cmd
py manage.py runserver
```

Ha mindent jól csinálta akkor ennek kell majd megjelennie:
![image](https://user-images.githubusercontent.com/93611221/235539936-56992f33-8d9f-4172-b53e-17c8950ec091.png)

## Oldal fájlai
Az projekt fájlai az "alkalomadtan" mappában vannak. Kérem ne abba a mappába hozza létre virtuális környezetet!

## Dokumentáció
A dokumentáció és egyéb kiegészítő fájlok a "Dokumentációk" mappában találhatók
