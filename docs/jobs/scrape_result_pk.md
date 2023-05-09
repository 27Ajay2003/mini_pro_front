# Scrape-Result-pk

Retrieves the scrape result for a specific job.

**URL** : `api/jobs/scrape-result/:pk`

**Method** : `GET`

**Auth required** : ADMIN

<br>

**Code** : `200 OK`

**Content example**

```json
api/jobs/scrape-result/Software Engineer/

{
    
    "id": "178",
    "json_resp": {
        "Software Engineer": [
            {
            "location":"",
            "job_title":"",
            "company_link":"",
            "company_name":"",
            "company_rating":"",
            "company_skills":{
                "skills":[
                    "",
                    "",
                    ..
                ],
                "databases":[],
                "languages":[],
                "frameworks":[]
            },
            "job_description":"",
            "avg_base_pay_est":"",
            "time_since_posted":""
        },
        ...
        ...
        ]
    },
    "date created": "2023-04-30T10:23:48.179304Z",
    "job_name":"Software Engineer"

}
```