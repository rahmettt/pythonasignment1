
class DataAnalyser:

    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):

        print("Not implemented — use a child class")

    def print_results(self):

        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):

        return f"DataAnalyser: base class, {len(self.students)} students"


# =============================================================
#  ДОЧЕРНИЙ КЛАСС — GpaAnalyser (Task 2, Practice 7) — ВАРИАНТ A
#  Наследует от DataAnalyser, переопределяет analyse() и print_results()
# =============================================================
class GpaAnalyser(DataAnalyser):

    def __init__(self, students):

        super().__init__(students)
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
                print(f"Warning: could not convert GPA for student {s.get('student_id', '?')} — skipping.")
                continue

        avg_gpa = round(sum(gpas) / len(gpas), 2)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": avg_gpa,
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high_performers
        }
        return self.result

    def print_results(self):

        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):

    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        country_counts = {}

        for s in self.students:
            country = s['country']
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        self.result = {
            "analysis": "Country Analysis",
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": top_3,
            "all_countries": country_counts
        }
        return self.result

    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)

        print(f"total_students: {self.result['total_students']}")
        print(f"total_countries: {self.result['total_countries']}")
        print(f"top_3: {self.result['top_3']}")
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"