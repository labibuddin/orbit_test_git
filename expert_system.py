# make diabetes diagnoses using expert system
def main():
    # create knowledge base
    knowledge_base = {
        'diabetes': {
            'systolic': {
                'normal': {
                    'diabetes': 'no'
                },
                'high': {
                    'diabetes': 'yes'
                }
            },
            'age': {
                'normal': {
                    'diabetes': 'no'
                },
                'old': {
                    'diabetes': 'yes'
                }
            }
        }
    }

    # create knowledge base
    knowledge_base = {
        'diabetes': {
            'systolic': {
                'normal': {
                    'diabetes': 'no'
                },
                'high': {
                    'diabetes': 'yes'
                }
            },
            'age': {
                'normal': {
                    'diabetes': 'no'
                },
                'old': {
                    'diabetes': 'yes'
                }
            }
        }
    }

    # ask questions
    print('Are you taking your blood pressure?')
    systolic = input('Systolic: ')
    print('Are you at least 40 years old?')
    age = input('Age: ')

    # look up answers
    if systolic in knowledge_base['diabetes']['systolic']:
        if age in knowledge_base['diabetes']['age']:
            if knowledge_base['diabetes']['systolic'][systolic][age] == 'diabetes':
                print('Yes, you have diabetes.')
            else:
                print('No, you do not have diabetes.')
        else:
            print('No, you do not have diabetes.')
    else:
        print('No, you do not have diabetes.')

if __name__ == '__main__':
    main()