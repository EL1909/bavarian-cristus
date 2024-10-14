from django.test import TestCase
from .forms import ImagePostForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ImagePostForm({'name' : ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_location_field_is_not_required(self):
        form = ImagePostForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['title', 'image', 'location', 'text', 'status'])

