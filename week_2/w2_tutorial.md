# Week 2 Tutorial - Movie Theater Admission

## Activity

### 1. Identify the elements

#### 1.1 What are the inputs?
- Age of the person (13 years old or older)
- Whether the person is accompanied by an adult
- Whether the person has a valid ticket

#### 1.2 What is the process?
- Verify if the person is 13 years old or older
- Verify if the person is accompanied by an adult
- Verify if the person has a valid ticket
- Apply the mechanism:
  - IF (age >= 13) or (accompanied by adult AND has valid ticket)
  - THEN allow entry
  - ELSE deny entry
  #### 1.3 What is the output?
- If conditions does match: "Person is allowed to enter"
- If conditions does not: "Person is not allowed to enter"
#### 2.1 Diagram (Flowchart)

![alt text](<Screenshot 2026-06-10 091651.png>)

##### 2.2 Truth Table

| A (Age>=13) | B (With Adult) | C (Valid Ticket) | B AND C | A OR (B AND C) |
|-------------|----------------|------------------|---------|----------------|
| TRUE  | TRUE  | TRUE  | TRUE  | TRUE  |
| TRUE  | TRUE  | FALSE | FALSE | TRUE  |
| TRUE  | FALSE | TRUE  | FALSE | TRUE  |
| TRUE  | FALSE | FALSE | FALSE | TRUE  |
| FALSE | TRUE  | TRUE  | TRUE  | TRUE  |
| FALSE | TRUE  | FALSE | FALSE | FALSE |
| FALSE | FALSE | TRUE  | FALSE | FALSE |
| FALSE | FALSE | FALSE | FALSE | FALSE |
#### 2.3 Step-by-Step Algorithm
1. START
2. Get person's age, adult accompaniment, ticket status
3. IF age >= 13 THEN allow entry
4. ELSE IF accompanied by adult AND has valid ticket THEN allow entry
5. ELSE deny entry
6. END
#### 2.4 Pseudocode
1. START
2. Get person's age, adult accompaniment, ticket status
3. IF age >= 13 THEN allow entry
4. ELSE IF accompanied by adult AND has valid ticket THEN allow entry
5. ELSE deny entry
6. END
