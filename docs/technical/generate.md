# Generate Questions

Randomly provides 40 questions [10 for each of the 4 subjects].

**URL** : `/api/technical/question/generate/`

**Method** : `GET`

**Auth required** : ADMIN
<br>
<br>

## Success Response

**Code** : `200 OK`

**Content example**

```json
[
    {
        "question_id": 23,
        "topic": "Operating System Architecture and Components",
        "question": "Which of the following components is responsible for translating high-level programming languages into machine code that can be executed by the computer?",
        "option_a": "Compiler",
        "option_b": "Interpreter",
        "option_c": "Assembler",
        "option_d": "Linker",
        "correct_answer": "a",
        "difficulty": "medium",
        "cognitive_level": "applying",
        "subject": "OS"
    },
    {
        "question_id": 68,
        "topic": "Input/Output (I/O) Management",
        "question": "What is the role of a buffer in I/O operations?",
        "option_a": "To hold data temporarily while it is being transferred between devices",
        "option_b": "To allocate memory to processes",
        "option_c": "To schedule processes for execution",
        "option_d": "To provide an interface between the CPU and the memory",
        "correct_answer": "a",
        "difficulty": "easy",
        "cognitive_level": "understanding",
        "subject": "OS"
    },
    ...
    ...
    ...
]
```