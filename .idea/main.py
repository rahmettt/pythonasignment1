import os
import csv
import json


# ─────────────────────────────────────────────
#  Task 1 — Class FileManager
# ─────────────────────────────────────────────
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


# ─────────────────────────────────────────────
#  Task 2 — Class DataLoader
# ─────────────────────────────────────────────
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        except Exception as e:
            print(f"Error: {e}")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)


# ─────────────────────────────────────────────
#  Task 3 — Class DataAnalyser (Variant A — GPA Statistics)
# ─────────────────────────────────────────────
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_performers = 0

        for s in self.students:
            try:
                gpa = float(s['GPA'])
                gpas.append(gpa)
                if gpa > 3.5:
                    high_performers += 1
            except ValueError:
                print(f"Warning: could not convert value for student {s['student_id']} — skipping row.")
                continue

        avg_gpa = round(sum(gpas) / len(gpas), 2)
        max_gpa = max(gpas)
        min_gpa = min(gpas)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_performers
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f"Total students : {self.result['total_students']}")
        print(f"Average GPA    : {self.result['average_gpa']}")
        print(f"Highest GPA    : {self.result['max_gpa']}")
        print(f"Lowest GPA     : {self.result['min_gpa']}")
        print(f"Students GPA>3.5 : {self.result['high_performers']}")
        print("-" * 30)


# ─────────────────────────────────────────────
#  Task 4 — Class ResultSaver
# ─────────────────────────────────────────────
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


# ─────────────────────────────────────────────
#  Task 5 — Main
# ─────────────────────────────────────────────
def main():
    # --- FileManager ---
    fm = FileManager('students.csv')
    if not fm.check_file():
        print('Stopping program.')
        exit()
    fm.create_output_folder()

    # --- DataLoader ---
    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    # --- DataAnalyser ---
    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    # --- Lambda / Map / Filter (Practice 5, Task A3) ---
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

    # --- Exception handling demo (Practice 5, Task A4) ---
    dl2 = DataLoader('wrong_file.csv')
    dl2.load()

    # --- ResultSaver ---
    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()


if __name__ == '__main__':
    main()