import datetime
import scheduler.models as models

class WeekSchedule:

    def __init__(self, categories):
        self._categories = categories

    def getSchedule(self):
        return {d:self._getDayItems(d) for d in self._getWeekDays()}

    def _getWeekDays(self):
        today = datetime.date.today()
        week = 1 if today.weekday() > 4 else 0
        monday = today + datetime.timedelta(days = -today.weekday(), weeks = week)
        return [monday + datetime.timedelta(days = x) for x in range(5)]

    def _getDayItems(self, day):
        return {c:self._getItems(day, c) for c in self._categories}

    def _getItems(self, day, category):
        return models.Item.objects.filter(category = category, day = day)
