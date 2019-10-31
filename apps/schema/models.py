from django.db import models
from django.utils.translation import ugettext_lazy as _


class SchemaValidator(models.Model):
    field_name = models.CharField(_(u'Nome do campo'), max_length=140)
    validator = models.TextField(_(u'Validador'))
    message =  models.TextField(_(u'Mensagem'))

    class Meta:
        verbose_name = _('Esquema de validação')
        verbose_name_plural = _('Esquemas de validação')
        db_table = 'schema_validador'
