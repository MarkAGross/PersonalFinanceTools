# PersonalFinanceTools
Services, tools, and scripts to keep track of personal finances.

## Recommendations
| **Requirement** | **Value**               | **Link** |
|-----------------|-------------------------|----------|
| Python Version  | 3.11.3                  |          |
| DocString Type  | reStructuredText (reST) |          |

## Project Structure
| **Item**               | **Type**     | **Description**                           |
|------------------------|--------------|-------------------------------------------|
| docs                   | Directory    | Generated code documentation              |
| personal_finance_shell | Package      | Command line interface for provided tools |
| personal_finance_tools | Package      | Tools for managing personal finances      |
| tests                  | Package      | Unit test cases                           |
| definitions.py         | Python File  | Global variables for project              |
| main.py                | Python File  | Main function to start project            |
| test.py                | Python File  | Main function to start unit tests         |
| LICENSE                | License      | Terms of Use                              |
| requirements.txt       | Requirements | Requirements of project Python Packages   |

## How to Use
1) In the command line, navigate to this application's root directory ("PersonalFinanceTools")
2) Start the application with the command:
```
python main.py
```

## How to Test
1) In the command line, navigate to this application's root directory ("PersonalFinanceTools")
2) Start all unit tests with the command:
```
python test.py
```