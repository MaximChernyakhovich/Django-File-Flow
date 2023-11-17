from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.utils import timezone
from api.views import FileList, FileUploadView
from api.models import File

class TestUrls(SimpleTestCase):
    def test_file_upload_url_resolves(self):
        url = reverse('file-upload')
        self.assertEquals(resolve(url).func.view_class, FileUploadView)

    def test_file_list_url_resolves(self):
        url = reverse('file-list')
        self.assertEquals(resolve(url).func.view_class, FileList)

class FileModelTest(TestCase):
    def setUp(self):
        self.test_file = File.objects.create(
            file='test_file.txt',
            uploaded_at=timezone.now(),
            processed=True
        )

    def test_file_model(self):
        file_from_db = File.objects.get(id=self.test_file.id)

        now_with_timezone = timezone.now()

        self.assertEqual(file_from_db.file, 'test_file.txt')
        self.assertTrue(file_from_db.uploaded_at <= now_with_timezone)
        self.assertTrue(file_from_db.processed)

    def test_file_model_default_values(self):

        default_file = File.objects.create(file='default_file.txt')
        default_file_from_db = File.objects.get(id=default_file.id)
        self.assertFalse(default_file_from_db.processed)

