from django.db import models

class Material_pass(models.Model):
    serial_number = models.IntegerField(max_length=10, blank=False,
                                        verbose_name='Номер материального номера',
                                        unique=True)
    name_property = models.CharField(max_length=255, blank=False, verbose_name='Наименование имущества')
    reason = models.CharField(max_length=255, verbose_name='Основание')
    time_registration = models.DateTimeField(max_length=255, verbose_name='Время оформления пропуска')
    type_transport = models.CharField(max_length=255, verbose_name='Вид транспорта, гос номер')
    where_from = models.CharField(max_length=255, verbose_name='Откуда')
    where = models.CharField(max_length=255, verbose_name='Куда')
    issued_pass = models.CharField(max_length=255, verbose_name='Пропуск выдал')
    today_data = models.DateTimeField(max_length=255, verbose_name='Дата')
    approved = models.CharField(max_length=255, verbose_name='Вывоз разрешаю')

    def __str__(self):
        return self.name_property
