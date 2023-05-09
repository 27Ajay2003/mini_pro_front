# Token-Refresh

Used to generate an access token with a valid refresh token.

**URL** : `/api/auth/refresh/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "refresh":"[valid refresh token]"
}
```

**Data example**

```json
{
    "refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjYxODExMSwiaWF0IjoxNjgyNTMxNzExLCJqdGkiOiJlZTAwNjFiMTJiMjQ0Yzg0OWMwOTZjMjEzMmY5M2FhMSIsInVzZXJfaWQiOiJ1c2VyMSJ9.qCQ8f3weA-BcooRbkjIFDia8Pykk24C2Rif-jIICBxs"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
   "access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyNjE4NTQzLCJpYXQiOjE2ODI1MzE3MTEsImp0aSI6ImU2MzNiN2U0ZWQzMjQxMTQ4OTdlYmU3NWQyNTFmMGI4IiwidXNlcl9pZCI6InVzZXIxIn0.hgX90dDvlrFDpHiDPEJkUmLXVAYbP5osIhfdbOtWQgo"
}
```