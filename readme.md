

Bu faylda layihenin (Django + React) Docker ile nec qurulub ishfe salinmasi addim-addim izah olunur.

## 1. Telebler

Serverde / komputerinizde asagidakilar quraşdirilmiş olmalidir:

- Docker (20+ versiyasi)
- Docker Compose (docker compose emri ishlemelidir)
- Git (reponu cekmek ucun)

## 2. Layiheni yuklemek

```bash
git clone <sizin-repo-url>
cd UnipProject
```

Bu qovluqda asagidakilar olacaq:

- `config/` — Django layihe fayllari
- `api/` — API app (abune + elaqe endpointleri)
- `mdu-global-horizon/` — React frontend (Vite + Tailwind)
- `Dockerfile` — konteyner ucun resept
- `docker-compose.yml` — butov sistemi bir emrle qaldirmaq ucun
- `requirements.txt` — Python paket siyahisi

## 3. İlk defe image build etmek

Birinci defe ishledende image build olunmalidir. Bunun ucun root qovluqda (`UnipProject`) asagidaki emri icra et:

```bash
docker compose build
```

Bu addimda:

1. Node image-inden istifade olunaraq `mdu-global-horizon` daxilinde:
   - `npm install`
   - `npm run build`
   icra olunur ve `dist/` qovlugu yaranir.
2. Python image-i yaradilir, `requirements.txt` faylindan butun Django/DRF paketleri qurasdirilir.
3. React-in build neticesi (dist/) Django layihezine kocurulur.

## 4. Konteyneri ise salmaq

Build bitenden sonra proqrami ishfe salmaq ucun:

```bash
docker compose up -d
```

Bu emr:

- `web` adli servisi ayaqa qaldirir,
- konteyner daxilinde avtomatik olaraq:
  - `python manage.py migrate`
  - `gunicorn config.wsgi:application --bind 0.0.0.0:8000`
  icra edir.

### Saytin acilmasi

Brauzerde asagidaki unvana get:

```text
http://127.0.0.1:8000
```

Server uzaq masindadirsa, `127.0.0.1` yerine serverin IP-sini ve ya domainini istifade et (meselen `http://sizin-domain.az:8000`).

## 5. Konteyneri dayandirmaq

Isleyen konteynerleri dayandirmag ucun:

```bash
docker compose down
```

Bu emr konteynerleri dayandirir ve silir, amma image-lar saxlanilir. Növbəti defe `docker compose up -d` dedikde tez qaldirilacaq.

## 6. Loglara baxmaq

Backend-den gelen loglari gormek ucun:

```bash
docker compose logs -f
```

`Ctrl + C` ile log izlemeni dayandira bilersen.

## 7. Django idarfe emrlerini konteyner icinde ishletmek

Meselen, admin ucun superuser yaratmaq isteyirsen:

```bash
docker compose exec web python manage.py createsuperuser
```

Bashqa `manage.py` emrleri de eyni qaydada ishleyir:

```bash
docker compose exec web python manage.py shell
```

## 8. Frontend-i yenileyende ne etmek lazimdir?

React (mdu-global-horizon) kodunda deyisiklik edende bu deyisikliklerin konteynerde gormek ucun:

1. Kodu deyis (komputerinde)
2. Yeniden build et ve konteyneri yenile:

```bash
docker compose build
docker compose up -d
```

Bu zaman:
- yeni React build yaradilir,
- yeni image qurlur,
- konteyner yenilenmis kodla yeniden ishfe dushur.

## 9. Qeydler

- `config/settings.py` icinde hal-hazirda `DEBUG = True` olaraq qalib. Real server ucun bunu `False` ele:
  ```python
  DEBUG = False
  ```
- `SECRET_KEY` deyishkenini qapali, tesadufi ve uzun bir setr ile deyishmek meslehetdir.
- `ALLOWED_HOSTS` massivine oz domainini / IP-ni elave et:
  ```python
  ALLOWED_HOSTS = ['sizin-domain.az', 'server-ip-adresi']
  ```

Bu fayldaki addimlari izlfmekle layiheyi Docker ile tek emrle (`docker compose up -d`) qaldira ve rahat sekilde idare ede bilersen.
