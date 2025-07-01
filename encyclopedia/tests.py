from django.test import TestCase
from django.urls import reverse
from . import util

class EncyclopediaTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/index.html')

    def test_entry_view_existing_entry(self):
        response = self.client.get(reverse('entry', args=['Python']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/entry.html')

    def test_entry_view_non_existing_entry(self):
        response = self.client.get(reverse('entry', args=['NonExistingEntry']))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'encyclopedia/error.html')

    def test_list_entries(self):
        entries = util.list_entries()
        self.assertIn('Python', entries)
        self.assertIn('HTML', entries)

    def test_create_entry(self):
        response = self.client.post(reverse('create'), {
            'title': 'Test Entry',
            'content': '# Test Entry Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertIn('Test Entry', util.list_entries())

    def test_edit_entry(self):
        # First create an entry to edit
        util.save_entry('Test Entry', '# Test Entry Content')
        response = self.client.post(reverse('edit', args=['Test Entry']), {
            'title': 'Test Entry',
            'content': '# Updated Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful edit
        content = util.get_entry('Test Entry')
        self.assertIn('Updated Content', content)