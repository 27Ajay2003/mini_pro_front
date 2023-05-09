# Search-Routes

Database operations on the QuizQuestions Model. 

**URL** : `/api/jobs/search/< >/?q=< >`

**URL Parameters** : `q=[query_param]`

**Method** : `GET`

**Auth required** : ADMIN

<br>

## Possible Usecases

**Endpoints**

```json
GET /api/jobs/search/languages/
GET /api/jobs/search/frameworks/
GET /api/jobs/search/databases/
GET /api/jobs/search/skills
GET /api/jobs/search/scrape-jobs

where q = [query_param]
```

**Example** : `/api/jobs/search/skills/?q=cloud`

**Sample Response** :
```json
[
    "aws cloudformation",
    "aws cloudwatch",
    "cloudflare"
]
```

Note:
<br>
For getting all items without filter either give 
<br>
`/api/jobs/search/skills/?q=`
<br>
or
<br>
`/api/jobs/search/skills/`
