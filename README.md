# Django Property Listings Caching Project

A Django application demonstrating advanced caching strategies using Redis for a property listings system.

## 🚀 Features

- **Property Management**: CRUD operations for property listings
- **Multi-level Caching**: Page-level and low-level API caching
- **Cache Invalidation**: Automatic cache invalidation using Django signals
- **Cache Metrics**: Real-time Redis cache performance monitoring
- **Dockerized Infrastructure**: PostgreSQL and Redis services

## 🏗️ Architecture

### Cache Strategy
1. **Page-level caching** (15 minutes) using `@cache_page` decorator
2. **Low-level caching** (1 hour) for database queryset caching
3. **Signal-based invalidation** for automatic cache management
4. **Metrics tracking** for cache performance analysis

### Tech Stack
- **Backend**: Django 5.2.4
- **Database**: PostgreSQL (Dockerized)
- **Cache**: Redis (Dockerized)
- **Python**: 3.11+

## 📦 Installation

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Git

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd alx-backend-caching_property_listings
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install django django-redis psycopg2-binary
```

4. **Start services**
```bash
docker-compose up -d
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Start development server**
```bash
python manage.py runserver
```

## 🛠️ API Endpoints

### Properties
- `GET /properties/` - List all properties (cached for 15 minutes)
- `GET /properties/metrics/` - View cache performance metrics

### Admin
- `GET /admin/` - Django admin interface

## 📊 Cache Metrics

The application provides detailed cache performance metrics:

- **Keyspace Hits**: Successful cache retrievals
- **Keyspace Misses**: Cache misses requiring database queries
- **Hit Ratio**: Percentage of successful cache hits
- **Total Requests**: Combined hits and misses

Access metrics at: `http://localhost:8000/properties/metrics/`

## 🔧 Cache Configuration

### Redis Settings
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Cache Timeouts
- **Page cache**: 15 minutes (`@cache_page(60 * 15)`)
- **Queryset cache**: 1 hour (`cache.set('all_properties', queryset, 3600)`)

## 🔄 Cache Invalidation

Automatic cache invalidation triggers:
- Property creation (`post_save` signal)
- Property updates (`post_save` signal)  
- Property deletion (`post_delete` signal)

## 🐳 Docker Services

```yaml
services:
  postgres:
    image: postgres:latest
    ports: ["5432:5432"]
    environment:
      POSTGRES_DB: property_listings
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres

  redis:
    image: redis:latest
    ports: ["6379:6379"]
```

## 📈 Performance Benefits

- **Reduced Database Load**: Queryset caching minimizes database queries
- **Faster Response Times**: Page-level caching serves cached responses
- **Smart Invalidation**: Automatic cache updates ensure data consistency
- **Monitoring**: Real-time cache performance tracking

## 🧪 Testing Cache Behavior

1. **Initial Request**: Database query + cache storage
2. **Subsequent Requests**: Served from cache (fast response)
3. **Data Modification**: Automatic cache invalidation
4. **Cache Metrics**: Monitor hit/miss ratios

## 📝 Project Structure

```
alx-backend-caching_property_listings/
├── alx_backend_caching_property_listings/
│   ├── settings.py      # Django configuration
│   └── urls.py          # Main URL routing
├── properties/
│   ├── models.py        # Property model
│   ├── views.py         # Cached views
│   ├── utils.py         # Cache utilities & metrics
│   ├── signals.py       # Cache invalidation signals
│   └── urls.py          # App URL routing
├── docker-compose.yml   # Service orchestration
└── README.md           # Project documentation
```

## 🏆 Tasks Completed

- ✅ **Task 0**: Django project setup with PostgreSQL & Redis
- ✅ **Task 1**: Page-level caching with `@cache_page` decorator
- ✅ **Task 2**: Low-level queryset caching with Django cache API
- ✅ **Task 3**: Signal-based cache invalidation system
- ✅ **Task 4**: Redis cache metrics analysis and monitoring

---

*Built with ❤️ using Django & Redis caching strategies*
