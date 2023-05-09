# Login

Used to retrieve access and refresh token for a registered User. [Including Admin]

**URL** : `/api/auth/login/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[valid email address]",
    "password": "[password in plain text]"
}
```

**Data example**

```json
{
    "username":"user1",
    "password":"user1"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjYxODExMSwiaWF0IjoxNjgyNTMxNzExLCJqdGkiOiJlZTAwNjFiMTJiMjQ0Yzg0OWMwOTZjMjEzMmY5M2FhMSIsInVzZXJfaWQiOiJ1c2VyMSJ9.qCQ8f3weA-BcooRbkjIFDia8Pykk24C2Rif-jIICBxs",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyNjE4MTExLCJpYXQiOjE2ODI1MzE3MTEsImp0aSI6ImU1NmRlZTg4YzFiNjRlYWViYTBjMDE0ZmQ5NGQyNjA5IiwidXNlcl9pZCI6InVzZXIxIn0.Uj1QsXLU6FSdq25nXUl_glYEhLKAgxanm5coVaivY0o"
}
```