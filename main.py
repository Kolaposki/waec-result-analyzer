import pdfplumber
import os

print("BATCH WORK STARTED...")

path = "WAEC RESULT"  # specify the folder where the results are located
os.chdir(path)
SCORE_LIST = []
GRADES = ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9', 'OUTSTANDING']  # for reference
SUBJECT_LIST = [

    'MATHEMATICS', 'FURTHER MATHEMATICS', 'ENGLISH LANGUAGE', 'LITERATURE IN ENGLISH',
    'PHYSICS', 'BIOLOGY', 'CHEMISTRY', 'ECONOMICS', 'CIVIC EDUCATION', 'COMPUTER STUDIES', 'PHYSICAL EDUCATION',
    'GEOGRAPHY', 'FINANCIAL ACCOUNTING', 'GOVERNMENT', 'DATA PROCESSING', 'CHRISTIAN RELIGIOUS STUDIES',
    'OFFICE PRACTICE', 'TECHNICAL DRAWING', 'VISUAL ART', 'FRENCH', 'GARMENT MAKING', 'ISLAMIC RELIGIOUS STUDIES',
    'HISTORY', 'COMMERCE', 'BASIC ELECTRONICS', 'ELECTRICAL INSTALLATION AND MAINTENANCE WORKS', 'AUTO MECHANICS',
    'MARKETING', 'FOODS & NUTRITION'
]  # for reference


def read_results(pdf_path):
    """
    Extracts the subjects and grades from a pdf file
    :param pdf_path:
    :return: None
    """
    with pdfplumber.open(pdf_path) as pdf:  # open the pdf and extract the contents as tables
        extract_tables = pdf.pages[0].extract_tables()
        SCORES_DICT = {}

        try:
            score_list = extract_tables[3]  # the third table is where the grades are located
            for score in score_list:
                subject = score[0]
                grade = score[1]
                SCORES_DICT.update({subject: grade})

        except IndexError:  # some pdfs are not grouped by tables and hence can't be accessed by indexing
            # fetch using another approach
            text = extract_tables[0][0]
            spliter = text[0].split('\n')[8:-4]

            for sp in spliter:
                if len(sp) > 7:  # Subject should be more than 7 characters
                    grade = str(sp[-3:]).rstrip().lstrip()  # last 3 characters are the grade
                    if len(grade) == 2:  # confirm if its the grade
                        subject = str(sp[0:len(sp) - 3]).rstrip().lstrip()  # 0 to -3 chars is the subject
                        if subject == 'CHRISTIAN RELIGIOUS':  # CRS isn't always complete
                            subject = 'CHRISTIAN RELIGIOUS STUDIES'

                        SCORES_DICT.update({subject: grade})  # populate the scores as dict

        SCORE_LIST.append(SCORES_DICT)


def batch_work():
    """
    Loops through the pdf files in the work directory and sends them to read_results for processing
    :return: None
    """
    for file in os.listdir():
        if file.endswith(".pdf"):
            read_results(file)


# Begin the work
batch_work()

print("SCORE_LIST", SCORE_LIST)

ECONOMICS_LIST, MATHEMATICS_LIST, FURTHER_MATHEMATICS_LIST, ENGLISH_LIST, LIT_IN_ENG_LIST = [], [], [], [], []
PHYSICS_LIST, BIOLOGY_LIST, CHEMISTRY_LIST, CIVIC_LIST, COMPUTER_LIST = [], [], [], [], []
PHYSICAL_EDU_LIST, GEOGRAPHY_LIST, ACCOUNTING_LIST, GOVERNMENT_LIST = [], [], [], []
DP_LIST, CRS_LIST, OFFICE_PRACTICE_LIST, TD_LIST, VISUAL_ART_LIST = [], [], [], [], []
FRENCH_LIST, GARMENT_MAKING_LIST, IRS_LIST, HISTORY_LIST, COMMERCE_LIST = [], [], [], [], []
BASIC_ELECT_LIST, ELECT_INSTALLATION_LIST, AUTO_MECHANICS_LIST, MARKETING_LIST = [], [], [], []
FOOD_NUT_LIST = []

ECONOMICS_CHECK, MATHEMATICS_CHECK, FURTHER_MATHEMATICS_CHECK, ENGLISH_CHECK, = 0, 0, 0, 0
LIT_IN_ENG_CHECK, PHYSICS_CHECK, BIOLOGY_CHECK, CHEMISTRY_CHECK, CIVIC_CHECK, COMPUTER_CHECK = 0, 0, 0, 0, 0, 0
PHYSICAL_EDU_CHECK, GEOGRAPHY_CHECK, ACCOUNTING_CHECK, GOVERNMENT_CHECK, DP_CHECK, CRS_CHECK = 0, 0, 0, 0, 0, 0
OFFICE_PRACTICE_CHECK, TD_CHECK, VISUAL_ART_CHECK, FRENCH_CHECK, GARMENT_MAKING_CHECK, IRS_CHECK = 0, 0, 0, 0, 0, 0
HISTORY_CHECK, COMMERCE_CHECK, BASIC_ELECT_CHECK, ELECT_INSTALLATION_CHECK, AUTO_MECHANICS_CHECK = 0, 0, 0, 0, 0
MARKETING_CHECK, FOOD_NUT_CHECK = 0, 0

for score in SCORE_LIST:
    # Check if a student has a subject in the result then add it to the required list, then count.
    if score.get('MATHEMATICS'):
        MATHEMATICS_CHECK += 1
        MATHEMATICS_LIST.append(score.get('MATHEMATICS'))

    if score.get('FURTHER MATHEMATICS'):
        FURTHER_MATHEMATICS_CHECK += 1
        FURTHER_MATHEMATICS_LIST.append(score.get('FURTHER MATHEMATICS'))

    if score.get('ENGLISH LANGUAGE'):
        ENGLISH_CHECK += 1
        ENGLISH_LIST.append(score.get('ENGLISH LANGUAGE'))

    if score.get('LITERATURE IN ENGLISH'):
        LIT_IN_ENG_CHECK += 1
        LIT_IN_ENG_LIST.append(score.get('LITERATURE IN ENGLISH'))

    if score.get('PHYSICS'):
        PHYSICS_CHECK += 1
        PHYSICS_LIST.append(score.get('PHYSICS'))

    if score.get('BIOLOGY'):
        BIOLOGY_CHECK += 1
        BIOLOGY_LIST.append(score.get('BIOLOGY'))

    if score.get('CHEMISTRY'):
        CHEMISTRY_CHECK += 1
        CHEMISTRY_LIST.append(score.get('CHEMISTRY'))

    if score.get('ECONOMICS'):
        ECONOMICS_CHECK += 1
        ECONOMICS_LIST.append(score.get('ECONOMICS'))

    if score.get('CIVIC EDUCATION'):
        CIVIC_CHECK += 1
        CIVIC_LIST.append(score.get('CIVIC EDUCATION'))

    if score.get('COMPUTER STUDIES'):
        COMPUTER_CHECK += 1
        COMPUTER_LIST.append(score.get('COMPUTER STUDIES'))

    if score.get('PHYSICAL EDUCATION'):
        PHYSICAL_EDU_CHECK += 1
        PHYSICAL_EDU_LIST.append(score.get('PHYSICAL EDUCATION'))

    if score.get('GEOGRAPHY'):
        GEOGRAPHY_CHECK += 1
        GEOGRAPHY_LIST.append(score.get('GEOGRAPHY'))

    if score.get('FINANCIAL ACCOUNTING'):
        ACCOUNTING_CHECK += 1
        ACCOUNTING_LIST.append(score.get('FINANCIAL ACCOUNTING'))

    if score.get('GOVERNMENT'):
        GOVERNMENT_CHECK += 1
        GOVERNMENT_LIST.append(score.get('GOVERNMENT'))

    if score.get('DATA PROCESSING'):
        DP_CHECK += 1
        DP_LIST.append(score.get('DATA PROCESSING'))

    if score.get('CHRISTIAN RELIGIOUS STUDIES'):
        CRS_CHECK += 1
        CRS_LIST.append(score.get('CHRISTIAN RELIGIOUS STUDIES'))

    if score.get('OFFICE PRACTICE'):
        OFFICE_PRACTICE_CHECK += 1
        OFFICE_PRACTICE_LIST.append(score.get('OFFICE PRACTICE'))

    if score.get('TECHNICAL DRAWING'):
        TD_CHECK += 1
        TD_LIST.append(score.get('TECHNICAL DRAWING'))

    if score.get('VISUAL ART'):
        VISUAL_ART_CHECK += 1
        VISUAL_ART_LIST.append(score.get('VISUAL ART'))

    if score.get('FRENCH'):
        FRENCH_CHECK += 1
        FRENCH_LIST.append(score.get('FRENCH'))

    if score.get('GARMENT MAKING'):
        GARMENT_MAKING_CHECK += 1
        GARMENT_MAKING_LIST.append(score.get('GARMENT MAKING'))

    if score.get('ISLAMIC STUDIES'):
        IRS_CHECK += 1
        IRS_LIST.append(score.get('ISLAMIC STUDIES'))

    if score.get('HISTORY'):
        HISTORY_CHECK += 1
        HISTORY_LIST.append(score.get('HISTORY'))

    if score.get('COMMERCE'):
        COMMERCE_CHECK += 1
        COMMERCE_LIST.append(score.get('COMMERCE'))

    if score.get('BASIC ELECTRONICS'):
        BASIC_ELECT_CHECK += 1
        BASIC_ELECT_LIST.append(score.get('BASIC ELECTRONICS'))

    if score.get('ELECTR INSTAL & MAINTEN WORKS'):
        ELECT_INSTALLATION_CHECK += 1
        ELECT_INSTALLATION_LIST.append(score.get('ELECTR INSTAL & MAINTEN WORKS'))

    if score.get('AUTO MECHANICS'):
        AUTO_MECHANICS_CHECK += 1
        AUTO_MECHANICS_LIST.append(score.get('AUTO MECHANICS'))

    if score.get('MARKETING'):
        MARKETING_CHECK += 1
        MARKETING_LIST.append(score.get('MARKETING'))

    if score.get('FOODS & NUTRITION'):
        FOOD_NUT_CHECK += 1
        FOOD_NUT_LIST.append(score.get('FOODS & NUTRITION'))

# group similar grades together and keep count
MATHEMATICS_SCORES = dict([[x, MATHEMATICS_LIST.count(x)] for x in set(MATHEMATICS_LIST)])
FURTHER_MATHEMATICS_SCORES = dict([[x, FURTHER_MATHEMATICS_LIST.count(x)] for x in set(FURTHER_MATHEMATICS_LIST)])
ENGLISH_SCORES = dict([[x, ENGLISH_LIST.count(x)] for x in set(ENGLISH_LIST)])
LIT_IN_ENG_SCORES = dict([[x, LIT_IN_ENG_LIST.count(x)] for x in set(LIT_IN_ENG_LIST)])
PHYSICS_SCORES = dict([[x, PHYSICS_LIST.count(x)] for x in set(PHYSICS_LIST)])
BIOLOGY_SCORES = dict([[x, BIOLOGY_LIST.count(x)] for x in set(BIOLOGY_LIST)])
CHEMISTRY_SCORES = dict([[x, CHEMISTRY_LIST.count(x)] for x in set(CHEMISTRY_LIST)])
ECONOMICS_SCORES = dict([[x, ECONOMICS_LIST.count(x)] for x in set(ECONOMICS_LIST)])
CIVIC_SCORES = dict([[x, CIVIC_LIST.count(x)] for x in set(CIVIC_LIST)])
COMPUTER_SCORES = dict([[x, COMPUTER_LIST.count(x)] for x in set(COMPUTER_LIST)])
PHYSICAL_EDU_SCORES = dict([[x, PHYSICAL_EDU_LIST.count(x)] for x in set(PHYSICAL_EDU_LIST)])
GEOGRAPHY_SCORES = dict([[x, GEOGRAPHY_LIST.count(x)] for x in set(GEOGRAPHY_LIST)])
ACCOUNTING_SCORES = dict([[x, ACCOUNTING_LIST.count(x)] for x in set(ACCOUNTING_LIST)])
GOVERNMENT_SCORES = dict([[x, GOVERNMENT_LIST.count(x)] for x in set(GOVERNMENT_LIST)])
DP_SCORES = dict([[x, DP_LIST.count(x)] for x in set(DP_LIST)])
CRS_SCORES = dict([[x, CRS_LIST.count(x)] for x in set(CRS_LIST)])
OFFICE_PRACTICE_SCORES = dict([[x, OFFICE_PRACTICE_LIST.count(x)] for x in set(OFFICE_PRACTICE_LIST)])
TD_SCORES = dict([[x, TD_LIST.count(x)] for x in set(TD_LIST)])
VISUAL_ART_SCORES = dict([[x, VISUAL_ART_LIST.count(x)] for x in set(VISUAL_ART_LIST)])
FRENCH_SCORES = dict([[x, FRENCH_LIST.count(x)] for x in set(FRENCH_LIST)])
GARMENT_MAKING_SCORES = dict([[x, GARMENT_MAKING_LIST.count(x)] for x in set(GARMENT_MAKING_LIST)])
IRS_SCORES = dict([[x, IRS_LIST.count(x)] for x in set(IRS_LIST)])
HISTORY_SCORES = dict([[x, HISTORY_LIST.count(x)] for x in set(HISTORY_LIST)])
COMMERCE_SCORES = dict([[x, COMMERCE_LIST.count(x)] for x in set(COMMERCE_LIST)])
BASIC_ELECT_SCORES = dict([[x, BASIC_ELECT_LIST.count(x)] for x in set(BASIC_ELECT_LIST)])
ELECT_INSTALLATION_SCORES = dict([[x, ELECT_INSTALLATION_LIST.count(x)] for x in set(ELECT_INSTALLATION_LIST)])
AUTO_MECHANICS_SCORES = dict([[x, AUTO_MECHANICS_LIST.count(x)] for x in set(AUTO_MECHANICS_LIST)])
MARKETING_SCORES = dict([[x, MARKETING_LIST.count(x)] for x in set(MARKETING_LIST)])
FOOD_NUT_SCORES = dict([[x, FOOD_NUT_LIST.count(x)] for x in set(FOOD_NUT_LIST)])

print("MATHEMATICS_SCORES: ", MATHEMATICS_SCORES, " ~ TOTAL: ", MATHEMATICS_CHECK)
print("FURTHER_MATHEMATICS_SCORES: ", FURTHER_MATHEMATICS_SCORES, " ~ TOTAL: ", FURTHER_MATHEMATICS_CHECK)
print("ENGLISH_SCORES: ", ENGLISH_SCORES, " ~ TOTAL: ", ENGLISH_CHECK)
print("LIT_IN_ENG_SCORES: ", LIT_IN_ENG_SCORES, " ~ TOTAL: ", LIT_IN_ENG_CHECK)
print("PHYSICS_SCORES: ", PHYSICS_SCORES, " ~ TOTAL: ", PHYSICS_CHECK)
print("BIOLOGY_SCORES: ", BIOLOGY_SCORES, " ~ TOTAL: ", BIOLOGY_CHECK)
print("CHEMISTRY_SCORES: ", CHEMISTRY_SCORES, " ~ TOTAL: ", CHEMISTRY_CHECK)
print("ECONOMICS_SCORES: ", ECONOMICS_SCORES, " ~ TOTAL: ", ECONOMICS_CHECK)
print("CIVIC_SCORES: ", CIVIC_SCORES, " ~ TOTAL: ", CIVIC_CHECK)
print("COMPUTER_SCORES: ", COMPUTER_SCORES, " ~ TOTAL: ", COMPUTER_CHECK)

print("PHYSICAL_EDU_SCORES: ", PHYSICAL_EDU_SCORES, " ~ TOTAL: ", PHYSICAL_EDU_CHECK)
print("GEOGRAPHY_SCORES: ", GEOGRAPHY_SCORES, " ~ TOTAL: ", GEOGRAPHY_CHECK)
print("ACCOUNTING_SCORES: ", ACCOUNTING_SCORES, " ~ TOTAL: ", ACCOUNTING_CHECK)
print("GOVERNMENT_SCORES: ", GOVERNMENT_SCORES, " ~ TOTAL: ", GOVERNMENT_CHECK)
print("DP_SCORES: ", DP_SCORES, " ~ TOTAL: ", DP_CHECK)
print("CRS_SCORES: ", CRS_SCORES, " ~ TOTAL: ", CRS_CHECK)
print("OFFICE_PRACTICE_SCORES: ", OFFICE_PRACTICE_SCORES, " ~ TOTAL: ", OFFICE_PRACTICE_CHECK)
print("TD_SCORES: ", TD_SCORES, " ~ TOTAL: ", TD_CHECK)
print("VISUAL_ART_SCORES: ", VISUAL_ART_SCORES, " ~ TOTAL: ", VISUAL_ART_CHECK)
print("FRENCH_SCORES: ", FRENCH_SCORES, " ~ TOTAL: ", FRENCH_CHECK)
print("GARMENT_MAKING_SCORES: ", GARMENT_MAKING_SCORES, " ~ TOTAL: ", GARMENT_MAKING_CHECK)
print("IRS_SCORES: ", IRS_SCORES, " ~ TOTAL: ", IRS_CHECK)

print("HISTORY_SCORES: ", HISTORY_SCORES, " ~ TOTAL: ", HISTORY_CHECK)
print("COMMERCE_SCORES: ", COMMERCE_SCORES, " ~ TOTAL: ", COMMERCE_CHECK)
print("BASIC_ELECT_SCORES: ", BASIC_ELECT_SCORES, " ~ TOTAL: ", BASIC_ELECT_CHECK)
print("ELECT_INSTALLATION_SCORES: ", ELECT_INSTALLATION_SCORES, " ~ TOTAL: ", ELECT_INSTALLATION_CHECK)
print("AUTO_MECHANICS_SCORES: ", AUTO_MECHANICS_SCORES, " ~ TOTAL: ", AUTO_MECHANICS_CHECK)
print("MARKETING_SCORES: ", MARKETING_SCORES, " ~ TOTAL: ", MARKETING_CHECK)
print("FOOD_NUT_SCORES: ", FOOD_NUT_SCORES, " ~ TOTAL: ", FOOD_NUT_CHECK)
