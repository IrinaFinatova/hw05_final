from django.contrib.auth import get_user_model
from .mytestcase import MyTestCase, TEMP_MEDIA_ROOT
User = get_user_model()
from django.test import override_settings


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PostModelTest(MyTestCase):
    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_verboses = {
            'author': 'Автор поста',
            'text': 'Текст поста',
            'group': 'Название группы',
            'pub_date': 'Дата публикации поста',
            'image': 'Картинка'
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).verbose_name, expected_value)

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_help_texts = {
            'text': 'Введите текст поста',
            'group': 'Группа, к которой будет относиться пост'}
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).help_text, expected_value)

    def test_models_have_correct_object_names(self):
        """Проверяем корректную работу __str__."""
        post = PostModelTest.post
        group = PostModelTest.group
        str_object_dict = {post.text[:15]: str(post),
                           group.title: str(group)}
        for expected_object_name, str_function in str_object_dict.items():
            with self.subTest(expected_object_name=expected_object_name):
                self.assertEqual(expected_object_name, str_function)
