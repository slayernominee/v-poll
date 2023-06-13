# Nutzung

## front end konfigurieren
- in v-poll die rsc/main.js datei anpassen ($api anpassen)

## mongo db aufsetzen 
_kann auch einfach irgendwo gehostet sein man braucht halt einfach nur zugriff_
_hier ein beispiel:_
- `docker run -d -p 9001:27017 -v /Users/zero/Development/Projekte/v-poll/api/mongodb:/data/db --name v-poll-mongo mongo:latest`

## mongo db einrichten
zB mongo compass nutzen
- tabelle polls anlegen mit collection polls anlegen

nach diesem format dann dort drinnen die fragen anlegen:
_id ist schon vorgegeben, nicht ändern
{
  "_id": {
    "$oid": "647aeefce83e3176282be776"
  },
  "title": "Test Poll",
  "description": "an example poll",
  "public": True,
  "votes": 0,
  "protection": True, "_protection": "allow only a vote for this poll from one ip",
  "questions": [
    {
      "title": "Ort",
      "text": "Select a city you like .... | .       na elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.",
      "answers": [
        {
          "component": "v-select",
          "options": [
            "Heidelberg",
            "Berlin",
            "Florida",
            "Georgia",
            "Texas",
            "Wyoming"
          ],
          "label": "Citys",
          "multiple": true,
          "chips": true,
          "hint": ""
        }
      ]
    },
    {
      "title": "Slider 0,1",
      "text": "Question 2 ist sehr kurz ..",
      "answers": [
        {
          "component": "v-slider",
          "range": [
            1,
            10
          ],
          "steps": 0.1
        }
      ]
    },
    {
      "title": "IQ",
      "text": "Wie hoch ist dein IQ?  velit id anim esse. Cteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.",
      "answers": [
        {
          "component": "v-slider",
          "range": [
            60,
            200
          ],
          "steps": 1
        }
      ]
    },
    {
      "title": "Wort",
      "text": "Dein Lieblingswort? . a et commodo velit id anim esse. Consectetur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.",
      "answers": [
        {
          "component": "v-text",
          "label": "Dein Lieblingswort"
        }
      ]
    }
  ]
}

- collection questions hinzufügen
bsp:
{
  "_id": {
    "$oid": "6481882375333fd87812ed0b"
  },
  "title": "Von wo anders geladen",
  "text": "Dein LDiese Frage wurde von questions geladen ... ur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.",
  "answers": [
    {
      "component": "v-text",
      "label": "Dein Lieblingswort"
    }
  ]
}
/** 
* Paste one or more documents here
*/

**Sicherheit: Mongo DB Port von außen blockieren so das nur das Backend was auf dem selben Server läuft zugreifen kann**
_oder halt absichern ..._

## backnd konfigurieren & deployment
- main.py Konstanten am anfang anpassen
- main.py deployment (wie halt die main.js eingegeben muss die api auch erreichbar sein ...)


## Weitere Schritte
- Certbot für API / Frontend für https
