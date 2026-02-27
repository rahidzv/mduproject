# MDU Global Fair 2026

**Django (Backend) + React (Frontend)** əsaslı layihənin **Docker** platforması üzərində qurulması və istismara verilməsi.

---

## 1. Sistem Tələbləri

Layihənin problemsiz çalışması üçün serverdə və ya lokal kompüterinizdə aşağıdakı proqram təminatları quraşdırılmış olmalıdır:

- **Docker** (20+ versiya tövsiyə olunur)
- **Docker Compose** (`docker compose` əmrinin mövcud olması)
- **Git** (repozitoriyanı kopyalamaq üçün)

---

## 2. Layihənin Yüklənməsi

Repozitoriyanı Git vasitəsilə kopyalayın və layihənin kök qovluğuna daxil olun:

```bash
git clone https://github.com/rahidzv/mduproject.git
cd UnipProject
```

### Qovluq Strukturu

| Qovluq / Fayl | Təsvir |
|---|---|
| `config/` | Django layihəsinin əsas konfiqurasiya faylları |
| `api/` | API tətbiqi (abunəlik və əlaqə endpointləri) |
| `mdu-global-horizon/` | React frontend (Vite + Tailwind) |
| `Dockerfile` | Konteynerin qurulma (build) təlimatları |
| `docker-compose.yml` | Bütün sistemi idarə edən orkestrasiya faylı |
| `requirements.txt` | Python paketlərinin siyahısı |

---

## 3. İmajın Qurulması (Build)

Sistemi ilk dəfə işə saldıqda və ya kodda əsaslı dəyişikliklər etdikdə Docker imajını yenidən qurmaq lazımdır. `UnipProject` qovluğunda aşağıdakı əmri icra edin:

```bash
docker compose build
```

Bu mərhələdə avtomatik olaraq:

1. **Frontend build** — Node.js mühitində `npm install` və `npm run build` icra olunur, `dist/` qovluğu formalaşır.
2. **Backend hazırlıq** — Python mühiti yaradılır, `requirements.txt` kitabxanaları quraşdırılır.
3. **İnteqrasiya** — React-in statik faylları Django layihəsinin müvafiq qovluğuna köçürülür.

---

## 4. Konteynerlərin İşə Salınması

Build prosesi tamamlandıqdan sonra sistemi arxa planda işə salmaq üçün:

```bash
docker compose up -d
```

Konteyner daxilində avtomatik olaraq:

- Verilənlər bazasının miqrasiyaları (`python manage.py migrate`) yerinə yetirilir
- `gunicorn` serveri vasitəsilə tətbiq `0.0.0.0:8000` ünvanında aktivləşir

### Tətbiqə Giriş

| Mühit | Ünvan |
|---|---|
| Lokal | `http://127.0.0.1:8000` |
| Uzaq server | `http://<server-ip-adresi>:8000` |

---

## 5. Konteynerlərin Dayandırılması

İşləyən xidmətləri dayandırmaq və konteynerləri ləğv etmək üçün:

```bash
docker compose down
```

> **Qeyd:** Bu əmrlə konteynerlər silinir, lakin qurulmuş imajlar yaddaşda qalır. Növbəti dəfə `docker compose up -d` əmri ilə sistem daha tez işə düşəcək.

---

## 6. Jurnal (Log) Fayllarının İzlənməsi

Sistemin daxili gedişatını və mümkün xətaları canlı izləmək üçün:

```bash
docker compose logs -f
```

İzləməni dayandırmaq üçün `Ctrl + C` düymə kombinasiyasından istifadə edin.

---

## 7. Django İdarəetmə Əmrləri

Django-nun idarəetmə əmrlərini konteyner daxilində icra etmək mümkündür.

**Admin (superuser) yaratmaq:**

```bash
docker compose exec web python manage.py createsuperuser
```

**Python shell mühitinə daxil olmaq:**

```bash
docker compose exec web python manage.py shell
```

---

## 8. Frontend Yenilənmələri

React kodunda dəyişiklik etdiyiniz təqdirdə imajı yenidən qurun və konteynerləri yeniləyin:

```bash
docker compose build
docker compose up -d
```

---

## 9. Vacib Təhlükəsizlik Qeydləri (Production)

Layihəni canlı serverə çıxarmazdan əvvəl `config/settings.py` faylında aşağıdakı tənzimləmələri mütləq nəzərdən keçirin:

| Parametr | Dəyər | Açıqlama |
|---|---|---|
| `DEBUG` | `False` | İstehsal mühitində debug rejimi bağlanmalıdır |
| `SECRET_KEY` | Unikal, təsadüfi sətir | Mövcud açarı mürəkkəb bir sətir ilə əvəzləyin |
| `ALLOWED_HOSTS` | `['sizin-domain.az', 'server-ip']` | Serverinizin ünvanlarını əlavə edin |

```python
DEBUG = False
SECRET_KEY = 'yeni-murakkab-tasadufi-acari-bura-yazin'
ALLOWED_HOSTS = ['domain.az', 'server-ip-adresi']
```

---

## API Endpointləri

| Metod | Ünvan | Təsvir |
|---|---|---|
| `POST` | `/api/abune/` | Xəbərlər bülleteninə abunə olmaq |
| `POST` | `/api/elaqe/` | Əlaqə formu vasitəsilə mesaj göndərmək |

### Abunəlik Nümunəsi

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}' \
  http://127.0.0.1:8000/api/abune/
```

### Əlaqə Formu Nümunəsi

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"ad": "Ad Soyad", "email": "test@example.com", "mesaj": "Salam, sualim var."}' \
  http://127.0.0.1:8000/api/elaqe/
```

---

© 2026 MDU Global Fair. Bütün hüquqlar qorunur.
