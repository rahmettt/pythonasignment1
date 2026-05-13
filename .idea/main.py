
from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser



def main():


    fm = FileManager('students.csv')
    if not fm.check_file():

        print('Stopping program.')
        exit()
    fm.create_output_folder()


    dl = DataLoader('students.csv')
    dl.load()     # загружает все 10000 строк в dl.students
    dl.preview()  # печатает первые 5


    students = dl.students

    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)



    high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, students))
    print(f"GPA > 3.8 : {len(high_gpa)}")

    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"GPA values (first 5) : {gpa_values[:5]}")


    hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, students))
    print(f"study_hours_per_day > 4 : {len(hard_workers)}")
    print("-" * 30)


    dl_bad = DataLoader('wrong_file.csv')
    dl_bad.load()

    analysers = [
        GpaAnalyser(dl.students),       # наш основной вариант A
        CountryAnalyser(dl.students),   # второй класс для демонстрации
    ]

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)

    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()

    saver = ResultSaver(analysers[0].result, 'output/result.json')
    report = Report(analysers[0], saver)
    report.generate()


if __name__ == '__main__':
    main()