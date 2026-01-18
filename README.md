# django-pgjson

PostgreSQL json support for Django.

**Version:** 0.4.0  
**Django:** 5.2+  
**Python:** 3.10+  
**PostgreSQL:** 9.2+ (JSON), 9.4+ (JSONB)

## Requirements

- Django >= 5.2, < 5.3
- Python >= 3.10
- psycopg2-binary >= 2.9.0
- PostgreSQL >= 9.2 (for JSON fields), >= 9.4 (for JSONB fields)

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

## Quick Start

```python
from django_pgjson.fields import JsonField, JsonBField

class MyModel(models.Model):
    data = JsonField()
    metadata = JsonBField()
```

## Documentation

Full documentation: http://djangonauts.github.io/django-pgjson/

## Upgrade from Previous Versions

This is a major version upgrade (0.4.0) that requires:
- Python 3.10 or higher
- Django 5.2 or higher

See [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md) for detailed upgrade instructions.
