In Django, you can change the `login_redirect_url` by adding `LOGIN_REDIRECT_URL = 'path/to/url'` to your project settings ¹. You can then import this `LOGIN_REDIRECT_URL` in your views and add `@login_required(login_url=LOGIN_REDIRECT_URL)` to the top of your views that you want to restrict ¹.

Is there anything else you would like to know?

Forrás: Beszélgetés a Binggel, 2023. 03. 04.(1) How to specify the login_required redirect url in django?. https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django Hozzáférés 2023. 03. 04..
(2) Django authentication - wrong redirect url to login page. https://stackoverflow.com/questions/3367757/django-authentication-wrong-redirect-url-to-login-page Hozzáférés 2023. 03. 04..
(3) Using the Django authentication system. https://docs.djangoproject.com/en/4.1/topics/auth/default/ Hozzáférés 2023. 03. 04..
