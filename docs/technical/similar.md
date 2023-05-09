# Similar Questions

Provides 40 similar questions for a given list of question ids.

**URL** : `/api/technical/question/similar/`

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
    "ids":[1, 56, 231, 388]
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "questions": [
        {
            "question_id": 3,
            "topic": "Device Drivers and System Calls",
            "question": "Which type of system call is used to create a new process?",
            "option_a": "Process management system call",
            "option_b": "Memory management system call",
            "option_c": "File system system call",
            "option_d": "Device driver system call",
            "correct_answer": "a",
            "difficulty": "hard",
            "cognitive_level": "applying",
            "subject": "OS"
        },
        {
            "question_id": 4,
            "topic": "Device Drivers and System Calls",
            "question": "Which of the following is a system call used to interact with hardware devices?",
            "option_a": "ioctl()",
            "option_b": "open()",
            "option_c": "close()",
            "option_d": "read()",
            "correct_answer": "a",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "OS"
        },
        ...
        ...
        ...
    ]
}
```