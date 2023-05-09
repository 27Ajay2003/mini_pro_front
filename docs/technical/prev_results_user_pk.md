# Prev-Results-User-pk

View a specific Previous Test Result for a logged in User. 

**URL** : `/api/technical/prev-results/user/:pk`

**Method** : `GET`

**Auth required** : YES

## Success Response

**Code** : `200 OK`

**Content example**

```json
/api/technical/prev-results/user/1

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