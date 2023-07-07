from yaml.parser import ParserError
from yaml import safe_load as load

'''
Given a path to a yaml file, the function validates if the file readable as a YAML file
'''
def validate_yaml(file):
    with open(file, 'r') as subject:
        try:
            result = load(subject)
        except ParserError:
            return False
    return True

def main():
    path = "root.yaml"
    with open(path, 'r') as file:
        #Validating the root yaml file
        exams = load(file)

    print("***** Initiating validation of {} exam(s) *****".format(len(exams)))
    for exam in exams:
        print("Exam name: {}".format(exam.get('Exam')))
        print("Year: {}".format(exam.get('Year')))
        print("Type: {}".format(exam.get('Type')))
        subjects = exam.get('Subjects')
        print("********** Validating files **********")
        for subject in subjects:
            for key in subject:
                subject_path = subject.get(key)
                res = validate_yaml(subject_path)
                subject_path = subject_path.split('/')[1]
                print('{} ********** {}'.format(subject_path, 'Ok' if res else 'Failed'))
        print("\n")

if __name__ == "__main__":
    main()