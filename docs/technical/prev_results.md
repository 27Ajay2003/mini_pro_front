# Prev-Results

View Previous Test Results for all Users. 

**URL** : `/api/technical/prev-results/`

**Method** : `GET`

**Auth required** : ADMIN

## Success Response

**Code** : `200 OK`

**Content example**

```json
[
   {
      "id":1,
      "test_date":"2023-04-29T19:35:09.502223Z",
      "results":{
         "user_responses":[
            {
               "question_id":2,
               "answer":"b"
            },
            {
               "question_id":3,
               "answer":"v"
            }
         ],
         "scores":{
            "cn_score":1,
            "dbms_score":1,
            "oops_score":0,
            "os_score":0,
            "total_score":2
         },
         "visualization":{
            "CO1_correct":1,
            "CO2_correct":1,
            "CO3_correct":1,
            "CO4_correct":1,
            "CO1_total":1,
            "CO2_total":1,
            "CO3_total":1,
            "CO4_total":1,
            "easy_correct":1,
            "medium_correct":1,
            "hard_correct":1,
            "easy_total":1,
            "medium_total":1,
            "hard_total":1,
            "sub1_correct":1,
            "sub2_correct":1,
            "sub3_correct":1,
            "sub4_correct":1
         }
      },
      "user":"user1"
   },
   ...
   ...
]
```
<br>
<br>

Create a Test Result entry for a user into the ResultTest table. [by Admin]

**Method** : `POST`

**Auth required** : ADMIN

**Data constraints**

```json
{
    "username": "",
    "email": "[valid email address]",
    "languages": "[comma separated list]",
    "frameworks": "[comma separated list]",
    "databases": "[comma separated list]",
    "skills": "[comma separated list]",
    "results": "[list of json]"
}
{
   "user":"[valid username]",
   "results":{
      "user_responses":[
         {
            "question_id":["pk"],
            "answer":["valid option"]
         },
         {
            "question_id":["pk"],
            "answer":["valid option"]
         },
         ...
         ...
      ],
      "scores":{
         "cn_score":["valid score"],
         "dbms_score":["valid score"],
         "oops_score":["valid score"],
         "os_score":["valid score"],
         "total_score":["valid score"]
      },
      "visualization":{
         "CO1_correct":["valid score"],
         "CO2_correct":["valid score"],
         "CO3_correct":["valid score"],
         "CO4_correct":["valid score"],
         "CO1_total":["valid score"],
         "CO2_total":["valid score"],
         "CO3_total":["valid score"],
         "CO4_total":["valid score"],
         "easy_correct":["valid score"],
         "medium_correct":["valid score"],
         "hard_correct":["valid score"],
         "easy_total":["valid score"],
         "medium_total":["valid score"],
         "hard_total":["valid score"],
         "sub1_correct":["valid score"],
         "sub2_correct":["valid score"],
         "sub3_correct":["valid score"],
         "sub4_correct":["valid score"]
      }
   }
}
```

**Data example**

```json
{
   "user":"user1",
   "results":{
      "user_responses":[
         {
            "question_id":2,
            "answer":"b"
         },
         {
            "question_id":3,
            "answer":"v"
         }
      ],
      "scores":{
         "cn_score":1,
         "dbms_score":1,
         "oops_score":0,
         "os_score":0,
         "total_score":2
      },
      "visualization":{
         "CO1_correct":1,
         "CO2_correct":1,
         "CO3_correct":1,
         "CO4_correct":1,
         "CO1_total":1,
         "CO2_total":1,
         "CO3_total":1,
         "CO4_total":1,
         "easy_correct":1,
         "medium_correct":1,
         "hard_correct":1,
         "easy_total":1,
         "medium_total":1,
         "hard_total":1,
         "sub1_correct":1,
         "sub2_correct":1,
         "sub3_correct":1,
         "sub4_correct":1
      }
   }
}
```

## Success Response

**Code** : `201 CREATED`

**Content example**

```json
{
   "id":1,
   "test_date":"2023-04-29T19:35:09.502223Z",
   "results":{
      "user_responses":[
         {
            "question_id":2,
            "answer":"b"
         },
         {
            "question_id":3,
            "answer":"v"
         }
      ],
      "scores":{
         "cn_score":1,
         "dbms_score":1,
         "oops_score":0,
         "os_score":0,
         "total_score":2
      },
      "visualization":{
         "CO1_correct":1,
         "CO2_correct":1,
         "CO3_correct":1,
         "CO4_correct":1,
         "CO1_total":1,
         "CO2_total":1,
         "CO3_total":1,
         "CO4_total":1,
         "easy_correct":1,
         "medium_correct":1,
         "hard_correct":1,
         "easy_total":1,
         "medium_total":1,
         "hard_total":1,
         "sub1_correct":1,
         "sub2_correct":1,
         "sub3_correct":1,
         "sub4_correct":1
      }
   },
   "user":"user1"
}
```
