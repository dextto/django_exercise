import mock
from django.test import TestCase

import exercise
from exercise import books
from exercise.books import search_form


class Object(object):
    pass


def google_query():
    return exercise.books.search_form.SearchForm().search()


class Sandbox(TestCase):
    # def test_sandbox(self):
    #     author = AuthorFactory()
    #     self.assertEqual("joe.blow@example.com", author.email)

    def _mock_response(self, value):
        mock_resp = mock.Mock()
        mock_resp.value = value
        return mock_resp

    @mock.patch('exercise.books.search_form.SearchForm.search', return_value=10)
    # @mock.patch('books.tests.google_query', return_value=10)
    def test_mock1(self, mock_get):
        result = google_query()
        self.assertEqual(10, result)

    @mock.patch('exercise.books.search_form.SearchForm.search', return_value=10)
    # @mock.patch('books.tests.google_query')
    def test_mock2(self, mock_get):
        mock_resp = self._mock_response(10)
        mock_get.return_value = mock_resp.value

        result = google_query()
        self.assertEqual(10, result)
