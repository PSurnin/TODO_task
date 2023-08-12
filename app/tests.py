from rest_framework import status
from rest_framework.test import APITestCase
from app.models import TaskItem

import logging
logger = logging.getLogger(__name__)


class TaskTests(APITestCase):
    def add_test_task(self):
        """
        Adds a test person into the database
        """
        logger.debug('Adding a new task into database')
        t = TaskItem(title="UnitTask1", description='Testing')
        t.save()
        logger.debug('Successfully added')

    def test_list_persons(self):
        """
        Test to list all the persons in the list
        """
        logger.debug('Testing list')

        self.add_test_task()

        url = 'http://127.0.0.1:8000/tasks-list/'
        response = self.client.get(url, format='json')
        json = response.json()

        logger.debug(f'Testing status code response: {json} code:{response.status_code}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing result count')
        self.assertEqual(len(json), 1)