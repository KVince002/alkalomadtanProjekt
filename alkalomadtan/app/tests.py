from django.test import TestCase, Client, tag
from django.urls import reverse
# Create your tests here.
# megjelenik e rendesen e a főoldal?
# chatGPT tanácsolása
class HomepageViewTestCase(TestCase):
    @tag("core")
    def test_homepage_view(self):
        # Make a GET request to the homepage URL
        response = self.client.get(reverse("Kezdolap"))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the expected text
        self.assertContains(response, "Kezdőlap")

        # Check that the response uses the correct template
        self.assertTemplateUsed(response, "app/index.html")

