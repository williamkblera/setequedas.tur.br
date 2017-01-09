from django.db import models
from django.utils import timezone
import hashlib

class News(models.Model):
    name = models.CharField('nome', max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(
        'Data de Cadastro',
        default=timezone.now()
    )
    email = models.EmailField('E-mail')
    confirm = models.BooleanField('Cadastro confirmado', default=False)
    confirm_date = models.DateTimeField(
        'Data de confirmacao',
        blank=True,
        null=True
    )

    hash = models.CharField('hash', max_length=200, blank=True, null=True)
    date_hash = models.DateTimeField('data hash', blank=True, null=True)

    def cria_hash(self):
        #### Cria um hash com a timezone.now do pedido e o email. ###
        h = hashlib.md5()
        self.date_hash = timezone.now()
        chave = str(self.date_hash) + str(self.email)
        h.update(chave.encode('utf-8'))
        self.hash = str(h.hexdigest())

    def valida_hash(self):
        ### Ao chamar verifica se a hash ainda e valida ###
        ### Mais de 7 dias não e valida ###
        if (self.date_hash):
            dias = timezone.now() - self.date_hash
            if dias.days <= 7:
                ### Se a hash foi criada a mais de 7 dias já esta invalida ###
                return True

        return False


    def confirm_email(self):
        self.confirm = True
        self.confirm_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email
