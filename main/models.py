from django.db import models
from django.utils import timezone


class Main(models.Model):
    titulo_grupo = models.CharField(max_length=255)
    descricao_grupo = models.TextField()
    imagem_grupo = models.ImageField(
        upload_to='../main/static/imgs/grupo_imagens/')  # Defina o diretório onde as imagens serão armazenadas
    qtd_membros_total = models.IntegerField(default=100)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo_grupo


class Mensagem(models.Model):
    conteudo = models.TextField()
    grupo = models.ForeignKey(Main, on_delete=models.CASCADE)
    remetente = models.CharField(max_length=100, default="Sistema")
    data_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Mensagem de {self.remetente} em {self.grupo.titulo_grupo} em {self.data_envio}'
