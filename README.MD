# About waec-result-analyzer


A python script that fetches the grades of a student from a [WAEC](https://www.waecdirect.org/) result in pdf format.
Built for federal government college, Warri, Delta State. 

A typical WAEC (West African Examination Council) result contains the Candidate Information and Subject Grades. This script is focused on the Subject Grades section.

## Expected Data
This following data are what the school expects from a WAEC result.

POSSIBLE GRADES

    'A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9', 'OUTSTANDING', 'HELD', 'ABSENT'

SUBJECTS OFFERED BY ALL STUDENTS

    'MATHEMATICS', 'FURTHER MATHEMATICS', 'ENGLISH LANGUAGE', 'LITERATURE IN ENGLISH',
    'PHYSICS', 'BIOLOGY', 'CHEMISTRY', 'ECONOMICS', 'CIVIC EDUCATION', 'COMPUTER STUDIES', 'PHYSICAL EDUCATION',
    'GEOGRAPHY', 'FINANCIAL ACCOUNTING', 'GOVERNMENT', 'DATA PROCESSING', 'CHRISTIAN RELIGIOUS STUDIES',
    'OFFICE PRACTICE', 'TECHNICAL DRAWING', 'VISUAL ART', 'FRENCH', 'GARMENT MAKING', 'ISLAMIC RELIGIOUS STUDIES',
    'HISTORY', 'COMMERCE', 'BASIC ELECTRONICS', 'ELECTRICAL INSTALLATION AND MAINTENANCE WORKS', 'AUTO MECHANICS',
    'MARKETING', 'FOODS & NUTRITION'


## Libraries

The library used in reading the PDF is [pdfplumber](https://github.com/jsvine/pdfplumber)

```bash
pip install pdfplumber
```
## Necessity
The reason for building this project is that the method in which the result analysis is being carried out is of manual paper work. All the results (400+) are printed and checked manually by workers which is really tedious and tiring. 

So this project aims to reduce if not eliminate manual labour and save time. The analysis is done so to know the number of students with an exact grade for all subjects.


For instance, below shows the analysis of mathematics. You can imagine processing all the grades for all subjects.
```
MATHEMATICS
A1 - 20, B2 - 34, B3 - 16, C4 - 7, C5 - 4, C6 - 8, D7 - 10, E8 - 1, F9 - 2, HELD - 3, ABSENT - 0

TOTAL PASSED - 89/105 * 100 = 85%
TOTAL FAILED - 16/105 * 100 = 15%
```


## Contributing
Pull requests are very much welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
