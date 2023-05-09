# User

View Profile for a logged in User. 

**URL** : `/api/auth/user/`

**Method** : `GET`

**Auth required** : YES

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
<br>
<br>

Update Profile for a logged in User. 

**Method** : `PUT`

**Auth required** : YES

**Data constraints**

```json
{
    "username": "[valid username]",
    "email": "[valid email address]",
    "languages": "[comma separated list]",
    "frameworks": "[comma separated list]",
    "databases": "[comma separated list]",
    "skills": "[comma separated list]",
    "results": "[list of json]"
}
```

**Data example**

```json
{
    "username": "user1",
    "email": "user1@email.com",
    "languages": "python, javascript",
    "frameworks": "angular",
    "databases": "sqlite",
    "skills": "redis",
    "results": []
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "user1",
    "email": "user1@email.com",
    "languages": "python, javascript",
    "frameworks": "angular",
    "databases": "sqlite",
    "skills": "redis",
    "results": []
}
```
<br>
<br>

Delete Profile for a logged in User. 

**Method** : `DELETE`

**Auth required** : YES

**Data example**

```json
Empty Body
```

## Success Response

**Code** : `204 NO CONTENT`

**Content example**

```json
Empty Response
```