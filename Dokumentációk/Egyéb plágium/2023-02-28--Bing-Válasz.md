If I understand correctly, you want to create a button that can navigate you to a site based on
model id. There are different ways to achieve this, but one possible way is to use the 'urł•
emplate tag with a named URL pattern that accepts an id as an argumentl.
For example, if you have a model called Book and a view called book_detail that takes an id
s an argument and displays the details of a book, you can create a URL pattern like this:
```python
from django.urls import path
from .views import book_detail
urlpatterns = [
    path('book/<int:id>/',book_detail, name='book_detail')
]
```
Then, in your template, you can create a button that links to this URL using the 'url' tag and passing the id of the book as an argument (1):

```html
<button
<a href="{% url 'book_detai' book.id}">View Book</a>
```
This Will create a button that navigates you to the site where is
the id of the book.
I hope this helps. Do you have any other questions about Django?
Forrás: Beszélgetés a Binggel, 2023.02. 28.(1) python - Django: button link - Stack
Overflow. https://stackoverflow.com/questions/21916835/diango-button-link
Hozzáférés 2023.02. 28..
(2) The "sites" framework I Django documentation I Django.
https://docs.diangoproiect.com/en/4.1/ref/contrib/sites/Hozzáférés 2023.02. 28..
(3) Django Tutorial Part 4: Django admin site - Learn web development - Mozilla.
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Diango/Admin site
Hozzáférés 2023.02. 28..

kép:
[Kép](2023-02-28--Bing-Válasz---kép.png)
