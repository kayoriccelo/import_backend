from django.db import models
from django.utils.translation import ugettext_lazy as _


class LogValidator(models.Model):
    date = models.DateField(_('Data da validação'))
    field = models.CharField(_(u'Campo'), max_length=140)
    value = models.TextField(_(u'Valor'))
    message = models.TextField(_(u'Mensagem'))
    
    class Meta:
        verbose_name = _('Histórico de validação')
        verbose_name_plural = _('Históricos de validação')
        db_table = 'log_validador'
