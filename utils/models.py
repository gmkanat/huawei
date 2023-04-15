from django.db import models

from django.utils.translation import gettext as _

from mixins.models import TimeStampMixin, IsActiveMixin


class Address(TimeStampMixin, IsActiveMixin):
    oblast = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Oblast'),
    )
    city = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('City'),
    )
    street = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Street'),
    )
    house_number = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Apartment number'),
    )
    apartment = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Apartment'),
    )
    entrance = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Entrance'),
    )
    floor = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Floor'),
    )
    housing = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Housing'),
    )
    residential_complex = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Residential complex'),
    )
    additional_info = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Additional info'),
    )

