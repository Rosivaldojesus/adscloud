from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class tbAdministradora(models.Model):
    administradora = models.CharField(max_length=50, blank=50, null=True)
    class Meta:
        db_table = 'tbAdministradora'
        verbose_name_plural = 'Administradora'
    def __str__(self):
        return self.administradora


class tbSistemaCftv(models.Model):
    sistemaCftv = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaCftv'
        verbose_name_plural = 'Sistema de CFTV'
    def __str__(self):
        return self.sistemaCftv


class tbSistemaSai(models.Model):
    sistemaSai = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSai'
        verbose_name_plural = 'Sistema de SAI'
    def __str__(self):
        return self.sistemaSai


class tbSistemaSca(models.Model):
    sistemaSca = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSca'
        verbose_name_plural = 'Sistema de SCA'
    def __str__(self):
        return self.sistemaSca


class tbSistemaSap(models.Model):
    sistemaSap= models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSap'
        verbose_name_plural = 'Sistema de SAP'
    def __str__(self):
        return self.sistemaSap


class tbSistemaSdai(models.Model):
    sistemaSdai = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSdai'
        verbose_name_plural = 'Sistema de SDAI'
    def __str__(self):
        return self.sistemaSdai

class tbFabricante(models.Model):
    sistemaFabricante = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbFabricante'
        verbose_name_plural = 'Sistema Fabricante'
    def __str__(self):
        return self.sistemaFabricante





class tbCidade(models.Model):
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cidadeEstado = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbCidade'
        verbose_name_plural = 'Cidade'
    def __str__(self):
        return self.cidade


class tbSistemas(models.Model):
    sistemasTipo = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemas'
        verbose_name_plural = 'Sistemas'
    def __str__(self):
        return "{}".format(self.sistemasTipo)

    # return "{} - {}".format(self.id, self.clienteNome)


class tbArtigos(models.Model):
    artigoTitulo = models.CharField(max_length=255, blank=True, null=True)
    artigoSubtitulo = models.CharField(max_length=255, blank=True, null=True)
    artigoTexto = RichTextField(blank=True, null=True)
    class Meta:
        db_table = 'tbArtigos'
        verbose_name_plural = 'Artigos'
    def __str__(self):
        return self.artigoTitulo


class tbCliente(models.Model):
    clienteNome = models.CharField(max_length=50, blank=True, null=True)
    clienteAdministrador = models.CharField(max_length=20, blank=True, null=True)
    clienteAdministradora = models.ForeignKey(tbAdministradora, on_delete=models.CASCADE)
    clienteCftv = models.ForeignKey(tbSistemaCftv, on_delete=models.CASCADE)
    clienteSai = models.ForeignKey(tbSistemaSai, on_delete=models.CASCADE)
    clienteSca = models.ForeignKey(tbSistemaSca, on_delete=models.CASCADE)
    clienteSap = models.ForeignKey(tbSistemaSap, on_delete=models.CASCADE)
    clienteSdai = models.ForeignKey(tbSistemaSdai, on_delete=models.CASCADE)
    clienteCidade = models.ForeignKey(tbCidade, on_delete=models.CASCADE)
    clienteObservacao = RichTextField(blank=True, null=True)
    class Meta:
        db_table = 'tbCliente'
        verbose_name_plural = 'Clientes'
    def __str__(self):
        return "{}".format(self.clienteNome)


class tbEquipamento(models.Model):
    equipamento = models.CharField(max_length=50, blank=True, null=True)
    equipamentoLogin = models.CharField(max_length=50, blank=True, null=True)
    equipamentoPassword = models.CharField(max_length=50, blank=True, null=True)
    equipamentoQrCode = models.CharField(max_length=50, blank=True, null=True)
    equipamentoObservacao = RichTextField(blank=True, null=True)
    equipamentoCliente = models.ForeignKey(tbCliente, on_delete=models.CASCADE)
    equipamentoSistema = models.ForeignKey(tbSistemas, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbEquipamento'
        verbose_name_plural = 'Equipamentos'
    def __str__(self):
        return self.equipamento


class tbManuais(models.Model):
    manualNome = models.CharField(max_length=100, blank=True, null=True)
    manualLink = models.CharField(max_length=255, blank=True, null=True)
    manualDescricao = models.CharField(max_length=255, blank=True, null=True)
    manualFabricante = models.ForeignKey(tbFabricante, on_delete=models.CASCADE)
    manualSistema = models.ForeignKey(tbSistemas, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbManuais'
        verbose_name_plural = 'Manuais'
    def __str__(self):
        return self.manualNome


class tbPreventivas(models.Model):
    preventivaEquipamento = models.CharField(max_length=100, blank=True, null=True)
    preventivaProcedimento = RichTextField(blank=True, null=True)
    preventivaTempo = models.IntegerField(blank=True, null=True)
    preventivaObservacao = RichTextField(blank=True, null=True)
    manualSistema = models.ForeignKey(tbSistemas, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbPreventivas'
        verbose_name_plural = 'Preventivas'
    def __str__(self):
        return self.preventivaEquipamento

class tbSenhasPadroes(models.Model):
    senhaEquipamento = models.CharField(max_length=255, blank=True, null=True)
    senhaLogin = models.CharField(max_length=50, blank=True, null=True)
    senhaPassword = models.CharField(max_length=50, blank=True, null=True)
    senhaFabricante = models.ForeignKey(tbFabricante, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbSenhasPadroes'
        verbose_name_plural = 'Senhas Padrões'
    def __str__(self):
        return self.senhaLogin


class tbWework(models.Model):
    wework = models.CharField(max_length=50, blank=True, null=True)
    weworkQuantAndares = models.IntegerField(blank=True, null=True)
    weworkAndares = models.CharField(max_length=50, blank=True, null=True)
    weworkCondominio = models.CharField(max_length=100, blank=True, null=True)
    weworkSdai = models.ForeignKey(tbSistemaSdai, on_delete=models.CASCADE)
    clienteCidade = models.ForeignKey(tbCidade, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbWework'
        verbose_name_plural = 'Weworks'
    def __str__(self):
        return self.wework
# ------------------------------------------------------
# --------------- Iguatemi Ribeirão Preto --------------
# ------------------------------------------------------

class tbSapScirp(models.Model):
    quadroSap = models.CharField(max_length=50, blank=True, null=True, verbose_name="Quadro: ")
    GERENCIADORA = (
        ("BCX_SUP_01", "BCX_SUP_01"),
        ("BCX_SUP_02", "BCX_SUP_02"),
        ("BCX_2SS_01", "BCX_2SS_01"),
        ("NET_SUP_01", "NET_SUP_01"),
        ("NET_2SS_01", "NET_2SS_01"),
    )
    gerenciadora = models.CharField(max_length=255, choices=GERENCIADORA, verbose_name="Gerenciadora: ")
    STATUS =(
        ("Online","Online"),
        ("Offline","Offline"),
    )
    statusSap = models.CharField(max_length=50, choices=STATUS, verbose_name="Status ON/OFF: ")
    quantidadeControladoras = models.IntegerField(blank=True, null=True, verbose_name="Quant. Controladoras: ")
    quadroIluminacao = models.CharField(max_length=50, blank=True, null=True, verbose_name="Quadro de Iluminação: ")
    atualizacao = models.DateField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Atualização: ")
    observacoesSap = RichTextField(blank=True, null=True, verbose_name="Observação: ")
    class Meta:
        db_table = 'tbSapScirp'
        verbose_name_plural = 'Quadros SCIRP'
    def __str__(self):
        return self.quadroSap




# class tbCameraIp(models.Model):
#     nomeCamera = models.CharField(max_length=255, blank=True, null=True)
#     numeroCamera = models.IntegerField(blank=True, null=True)
#     numeroIp = models.IntegerField(blank=True, null=True)
#     cliente = models.ForeignKey(tbCliente, on_delete=models.CASCADE)
#     class Meta:
#         db_table = 'tbCameraIp'
#         verbose_name_plural = 'Câmeras IP'
#
#     def __str__(self):

class tbCameraIp(models.Model):
    nomeCamera = models.CharField(max_length=255, blank=True, null=True)
    numeroCamera = models.IntegerField(blank=True, null=True)
    numeroIp = models.CharField(max_length=20,blank=True, null=True)
    FABRICANTE_CAMERA = (
        ("Axis", "Axis"),
        ("Interlbras", "Intelbras"),
    )
    fabricanteCamera = models.CharField(max_length=255, choices=FABRICANTE_CAMERA)
    loginCamera = models.CharField(max_length=20, blank=True, null=True)
    senhaCamera = models.CharField(max_length=20, blank=True, null=True)
    EQUIPAMENTO_GRAVACAO = (
        ("DVR 1", "DVR 1"),
        ("DVR 2", "DVR 2"),
        ("DVR 3", "DVR 3"),

        ("NVR 1", "NVR 1"),
        ("NVR 2", "NVR 2"),
        ("NVR 3", "NVR 3"),

        ("VAU 1", "VAU 1"),
        ("VAU 2", "VAU 2"),
        ("VAU 3", "VAU 3"),
    )
    equipamentoGravacao = models.CharField(max_length=50, choices=EQUIPAMENTO_GRAVACAO)
    cliente = models.ForeignKey(tbCliente, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbCameraIp'
        verbose_name_plural = 'Câmeras IP'

    def __str__(self):
        return self.nomeCamera
