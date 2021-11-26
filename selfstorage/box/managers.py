from django.db import models


class DisplayCostQuerySet(models.QuerySet):
    def get_seasonal_keeping_costs(self, thing_name, costs=None):
        '''Вычисляет стоимостИ бокса в зависимости от вида вещи и периода хранения'''

        costs = costs or []
        DAYS_IN_WEEK = 7
        DAYS_IN_MONTH = 30

        thing = self.get(name=thing_name)

        min_storage_time = thing.min_storage_time
        max_storage_time = thing.max_storage_time

        storage_cost_for_min_period = thing.storage_cost
        storage_cost_per_day = storage_cost_for_min_period / DAYS_IN_WEEK
        storage_cost_for_max_period = storage_cost_per_day * DAYS_IN_MONTH
        costs.append(storage_cost_for_min_period)
        costs.append(storage_cost_for_max_period)

        return costs
