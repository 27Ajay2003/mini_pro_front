# Provide Questions

Provides question details for a given list of question ids.

**URL** : `/api/technical/question/provide/`

**Method** : `POST`

**Auth required** : ADMIN

**Data constraints**

```json
{
    "ids": "[comma separated list of ids]"
}
```

**Data example**

```json
{
    "ids":[1, 56, 231]
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "questions": [
        {
            "question_id": 1,
            "topic": "Device Drivers and System Calls",
            "question": "What is a device driver stack?",
            "options": [
                "A hierarchy of device drivers that are used to control a device",
                "A hierarchy of system calls that are used to interact with a device",
                "A hierarchy of operating systems that are used to control a device",
                "A hierarchy of programs that are used to interact with a device"
            ],
            "correct_answer": "a",
            "difficulty": "hard",
            "cognitive_level": "analyzing",
            "subject": "OS"
        },
        {
            "question_id": 56,
            "topic": "File Systems and Management",
            "question": "Which of the following is not a common file system used in modern operating systems?",
            "options": [
                "NTFS",
                "Ext4",
                "FAT32",
                "MS-DOS"
            ],
            "correct_answer": "d",
            "difficulty": "medium",
            "cognitive_level": "applying",
            "subject": "OS"
        },
        {
            "question_id": 231,
            "topic": "Data Manipulation Language (DML) and Query Optimization",
            "question": "Which of the following is not a type of SQL statement?",
            "options": [
                "Data Definition Language (DDL)",
                "Data Manipulation Language (DML)",
                "Data Query Language (DQL)",
                "Data Control Language (DCL)"
            ],
            "correct_answer": "c",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "DBMS"
        }
    ]
}
```