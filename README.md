
# Django Profile API with Cat Facts
A simple RESTful API endpoint that returns my profile information along with a dynamic cat fact fetched from an external API. This task validates your ability to consume third-party APIs, format JSON responses, and return dynamic data.

### Endpoint
`GET /me`

### Exampe response
```
{
  "status": "success",
  "user": {
    "email": "evil.morty@example.com",
    "name": "Lucky Morty",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-17T11:53:02.428Z",
  "fact": "Cats have 9 lives."
}
```

### Setup Instructions
```
git clone https://github.com/lumpy72006/profileAPI
cd profile-api
pip install -r requirements.txt
python manage.py runserver
```
