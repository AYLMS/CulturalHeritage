# Cultural Heritage Flask Application

by Arkhangelsk Team

## First run

```bash
git clone https://github.com/AYLMS/CulturalHeritage 
cd CulturalHeritage
pip install -r requirements.txt
python -m app create-db   # run once
python -m app populate-db  # run once (optional)
python -m app add-user -u admin -p 1234  # ads a user
python -m app run
```

Go to:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/