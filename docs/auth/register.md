# Register

Used to register a new User without admin status.

**URL** : `/api/auth/register/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[valid username]",
    "password": "[password in plain text]",
    "email": "[valid email address]",
    "languages": "[comma separated list]",
    "frameworks": "[comma separated list]",
    "databases": "[comma separated list]",
    "skills": "[comma separated list]"
}
```

**Data example**

```json
{
    "username": "user1",
    "password": "user1",
    "email": "user1@email.com",
    "languages": "c++, python, javascript",
    "frameworks": "angular",
    "databases": "sqlite",
    "skills": "redis"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "user1",
    "email": "user1@email.com",
    "languages": "c++, python, javascript",
    "frameworks": "angular",
    "databases": "sqlite",
    "skills": "redis",
    "results": []
}
```