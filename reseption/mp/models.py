from django.db import models


class Material_pass(models.Model):
    serial_number = models.IntegerField(
                                        verbose_name='Номер материального номера',
                                        unique=True)
    name_property = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Наименование имущества') # Наименование имуества
    reason = models.CharField(max_length=255, verbose_name='Основание',null=True, blank=True)  # Основание
    owner_reason = models.CharField(max_length=255, verbose_name='Основание',null=True, blank=True)  # ФИО Кто оформляет
    time_registration = models.DateTimeField(max_length=255, verbose_name='Время оформления пропуска',null=True, blank=True) # Время оформления пропуска
    type_transport = models.CharField(max_length=255, verbose_name='Вид транспорта, гос номер',null=True, blank=True)
    where = models.CharField(max_length=255, verbose_name='Куда',null=True, blank=True)
    issued_pass = models.CharField(max_length=255, verbose_name='Пропуск выдал',null=True, blank=True)
    today_data = models.DateTimeField(max_length=255, verbose_name='Дата',null=True, blank=True)
    approved = models.CharField(max_length=255, verbose_name='Вывоз разрешаю',null=True, blank=True)

    def __str__(self):
        return self.name_property
