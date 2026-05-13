

import unittest
from analytics.analyser import GpaAnalyser  # импортируем класс который тестируем


class TestAnalyser(unittest.TestCase):

    def setUp(self):

        self.sample = [
            {"GPA": "3.8", "sleep_hours": "7", "country": "USA",
             "final_exam_score": "95", "study_hours_per_day": "4"},
            {"GPA": "2.5", "sleep_hours": "5", "country": "India",
             "final_exam_score": "72", "study_hours_per_day": "2"},
            {"GPA": "3.9", "sleep_hours": "8", "country": "USA",
             "final_exam_score": "98", "study_hours_per_day": "5"},
            {"GPA": "1.8", "sleep_hours": "4", "country": "Canada",
             "final_exam_score": "55", "study_hours_per_day": "1"},
            {"GPA": "3.5", "sleep_hours": "6", "country": "India",
             "final_exam_score": "88", "study_hours_per_day": "3"},
        ]

    def test_result_is_not_empty(self):
        # Тест 1: после вызова analyse() результат не должен быть пустым словарём
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})
        # assertNotEqual(a, b) — тест проходит если a != b

    def test_total_students(self):
        # Тест 2: в результате должно быть правильное количество студентов (5)
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)
        # assertEqual(a, b) — тест проходит если a == b

    def test_result_has_required_keys(self):
        # Тест 3: словарь result должен содержать все обязательные ключи для варианта A
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("average_gpa", analyser.result)
        self.assertIn("max_gpa", analyser.result)
        self.assertIn("min_gpa", analyser.result)
        self.assertIn("high_performers", analyser.result)
        # assertIn(key, dict) — тест проходит если ключ есть в словаре

    def test_analyse_twice(self):
        # Тест 4: вызов analyse() дважды должен давать одинаковый результат
        # Проверяет что метод не накапливает данные при повторном вызове
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()  # сохраняем копию первого результата
        analyser.analyse()                # запускаем снова
        self.assertEqual(analyser.result, result1)
        # assertEqual — проверяем что результаты идентичны


if __name__ == '__main__':
    unittest.main()