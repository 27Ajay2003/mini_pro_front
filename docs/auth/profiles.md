# Profiles

Admin View access to profiles of Users.

**URL** : `/api/auth/profiles/`

**Method** : `GET`

**Auth required** : ADMIN

## Success Response

**Code** : `200 OK`

**Content example**

```json
[
    {
        "username": "user1",
        "email": "user1@email.com",
        "languages": "c++, python, javascript",
        "frameworks": "angular",
        "databases": "sqlite",
        "skills": "redis",
        "results": []
    },
    {
        "username": "user2",
        "email": "user2@email.com",
        "languages": "python",
        "frameworks": "angular",
        "databases": "sqlite",
        "skills": "redis",
        "results": []
    }
]
```
<br>
<br>

Admin view access to profile of a particular User with pk.

**URL** : `/api/auth/profiles/:pk/`

**URL Parameters** : `pk=[username]`

**Method** : `GET`

**Auth required** : ADMIN

## Success Response

**Code** : `200 OK`

**Content example**

```json
/api/auth/profiles/user2/

{
    "username": "user2",
    "email": "user2@email.com",
    "languages": "python",
    "frameworks": "angular",
    "databases": "sqlite",
    "skills": "redis",
    "results": []
}
```
<br>
<br>

Delete Profile of a User by the Admin. 

**Method** : `DELETE`

**Auth required** : ADMIN

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