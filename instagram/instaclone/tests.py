from django.test import TestCase
from .models import Image,User,Comments,Profile

# Create your tests here.
class ImageTestClass(TestCase):
    '''
    Test case for the Image class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Image class
        '''
        # Create a image instance
        self.new_image = Image(image = 'flower.png',image_name = 'flower',image_caption='beautiful')

    def test_instance(self):
        '''
        Test case to check if self.new_image in an instance of image class
        '''
        self.assertTrue(isinstance(self.new_image, Image))

    def test_display_image(self):
        '''
        Test case to check if all images are retreived from the database
        '''
        found_photos = Image.get_photos()
        photos = Image.objects.all()

        self.assertTrue(len(found_photos) == len(photos))


    def test_save_image(self):
        '''
        Test case to save images uploaded
        '''
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def update_caption(self):
        '''
        Test case to update a  new image caption
        '''
        self.new_caption.save_caption()
        caption_id = self.new_caption.id
        Image.update_caption(id,"book.jpg","book")
        self.assertEqual(self.caption.caption,"book.jpg","book")

    def test_get_image_by_id(self):
        '''
        Test case to get a single image by its id
        '''
        search_image = self.image.get_image_by_id(self.image.id)
        searched_image = Image.objects.get(id=self.image.id)
        self.assertTrue(searched_image,search_image)

    
    def test_delete_image(self):
        '''
        Test case to delete uploaded images
        '''
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

   
class ProfileTestCase(TestCase):
    '''
    Test case for the Profile class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create instance of Profile class
        self.new_profile = Profile(name = 'murimi',email = 'muriuki.ms.com',bio="I am Groot",avatar = 'flower.jpg')

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of Profile class
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_get_profile(self):
        '''
        Test case to check if all profiles are retreived from the database
        '''
        profiles = Profile.get_profiles()
        profile = Profile.objects.all()

        self.assertTrue(len(profiles) == len(profile))

    def test_save_profile(self):
        '''
        Test case to save profile
        '''
        self.test_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(profile)

    def test_update_profile(self):
        '''
        Test case to update profile detailsof a user
        '''
        self.new_caption.save_caption()
        caption_id = self.new_caption.id
        Image.update_caption(id, "book.jpg", "book")
        self.assertEqual(self.caption.caption, "book.jpg", "book")

    def test_get_profile(self):
        '''
        Test case to test getting a single image
        '''
        search_image = self.image.get_image_by_id(self.image.id)
        searched_image = Image.objects.get(id=self.image.id)
        self.assertTrue(searched_image, search_image)

    def test_delete_profile(self):
        ''''
        Test to delete a user profile
        '''
        self.image.save_profile()
        self.image.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

    def test_search_by_name(self):
        '''
        Test case to get a single image by its id
        '''
        search_name = self.profile.search_by_name(self.searched_name)
        searched_name = Profile.objects.get(name = searched_name)
        self.assertTrue(searched_name, search_name)

class CommentsTestCase(TestCase):
    '''
    Test case for the Comment class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.new_comment = Comments(comment='very nice')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_save_comment(self):
        '''
        Test case to save comment
        '''
        self.test_comment.save_comment()
        comment = Comments.objects.all()
        self.assertTrue(comment)

    def test_update_comment(self):
        '''
        Test case to update comments of an image
        '''
        self.new_comment.save_comment()
        comment_id = self.new_comment.id
        Image.update_comment(id, "very nice")
        self.assertEqual(self.comment.comment, "very nice")


    def test_delete_comment(self):
        ''''
        Test to delete a comment in an image
        '''
        self.image.save_comment()
        self.image.delete_comment()
        comment = Comments.objects.all()
        self.assertTrue(len(comment) == 0)
