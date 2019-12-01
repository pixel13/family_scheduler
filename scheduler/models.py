from django.db import models

CATEGORY_EVENTS = 'events'
CATEGORY_ICONSET = 'iconset'
CATEGORY_TEXT = 'text'
CATEGORY_CHECKBOX = 'checkbox'
CATEGORY_SELECT = 'select'
CATEGORY_OPENSELECT = 'open_select'

# Data types for categories
CATEGORY_TYPES = [
    (CATEGORY_EVENTS, 'events - A list of events'),
    (CATEGORY_TEXT, 'text - Free text'),
    (CATEGORY_CHECKBOX, 'checkbox - A boolean information (true or false)'),
    (CATEGORY_ICONSET, 'iconset - A choice among a list of icons'),
    (CATEGORY_SELECT, 'select - A select box'),
    (CATEGORY_OPENSELECT, 'open_select - A select box that accepts (and store) new values')
]

# Categories we want to show in our schedule
class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    data_type = models.CharField(max_length = 30, choices = CATEGORY_TYPES)
    data_args = models.TextField(blank = True, null = True, help_text = 'Arguments (depending on data_type)')

    def __str__(self):
        return self.name + ' (' + self.data_type + ')'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'


# Schedule categories
class Schedule(models.Model):
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return str(self.order) + '. ' + self.category.name

    class Meta:
        ordering = ['order']


# Items
class Item(models.Model):
    day = models.DateField()
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    description = models.CharField(max_length = 200)
    start = models.TimeField(null = True, blank = True)
    end = models.TimeField(null = True, blank = True)
    order = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return str(self.day) + ' - ' + self.description

    class Meta:
        ordering = ['day', 'order', 'start']
