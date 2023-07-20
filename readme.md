# Bug List

 1. Review Model db.relationships are incorrect *back_populates="reviews"*
 2. Review Model Foreign Key for user_id is incorrect *db.ForeignKey("users.id")*
 3. New_business.html is missing its methods to send information.
 4. Seed Data is too large for Chuck E Cheese Description
 5. Submit incorrect data to test form validation and show how to debug with forms

```
{% if form.errors['name'] %}
        {{ form.errors['name'][0]}}
    {% endif %}

    {% if form.errors['category'] %}
        {{ form.errors['category'][0]}}
    {% endif %}

    {% if form.errors['desc'] %}
        {{ form.errors['desc'][0]}}
    {% endif %}
```
