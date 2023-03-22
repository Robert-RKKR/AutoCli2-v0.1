# Django - URL revers import
from django.urls import reverse

# AutoCli2 - base API test import:
from autocli2.base.tests.base_api_test import BaseApiTest


# Test classes:
class ExecutorApiTest(BaseApiTest):

    def setUp(self) -> None:
        # Collect test URLs:
        self.celery_registered_tasks = reverse('api-task:celery_registered_tasks-list')
        self.celery_scheduled = reverse('api-task:celery_scheduled-list')
        self.celery_reserved = reverse('api-task:celery_reserved-list')
        self.celery_revoked = reverse('api-task:celery_revoked-list')
        self.celery_report = reverse('api-task:celery_report-list')
        self.celery_stats = reverse('api-task:celery_stats-list')
        # self.task_status = reverse('api-task:task_status-list')
        # Inherit from base method:
        return super().setUp()
    
    def tearDown(self) -> None:
        # Inherit from base method:
        return super().tearDown()


class TestExecutorApi(ExecutorApiTest):

    def test_api_update(self):
        # Collect responses:
        responses = []
        # Run API tests:
        responses.append(self.api_simple_test_list(
            self.celery_registered_tasks, False))
        responses.append(self.api_simple_test_list(
            self.celery_scheduled, False))
        responses.append(self.api_simple_test_list(
            self.celery_reserved, False))
        responses.append(self.api_simple_test_list(
            self.celery_revoked, False))
        responses.append(self.api_simple_test_list(
            self.celery_report, False))
        responses.append(self.api_simple_test_list(
            self.celery_stats, False))
        # Check responses status
        self.assertEqual(True,
            self.check_status_code_list(True, responses))
