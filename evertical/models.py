from django.db import models

# Create your models here.
class tbAdministradora(models.Model):
    administradoraNome = models.CharField(max_length=50, blank=50, null=True)
    class Meta:
        db_table = 'tbAdministradora'
        verbose_name_plural = 'Administradora'
    def __str__(self):
        return self.administradoraNome


class tbSistemaCftv(models.Model):
    sistemaCftvNome = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaCftv'
        verbose_name_plural = 'Sistema de CFTV'
    def __str__(self):
        return self.sistemaCftvNome


class tbSistemaSai(models.Model):
    sistemaSaiNome = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSai'
        verbose_name_plural = 'Sistema de SAI'
    def __str__(self):
        return self.sistemaSaiNome


class tbSistemaSca(models.Model):
    sistemaScaNome = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSca'
        verbose_name_plural = 'Sistema de SCA'
    def __str__(self):
        return self.sistemaScaNome


class tbSistemaSap(models.Model):
    sistemaSapNome = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSap'
        verbose_name_plural = 'Sistema de SAP'
    def __str__(self):
        return self.sistemaSapNome


class tbSistemaSdai(models.Model):
    sistemaSdaiNome = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbSistemaSdai'
        verbose_name_plural = 'Sistema de SDAI'
    def __str__(self):
        return self.sistemaSdaiNome


class tbCidade(models.Model):
    cidadeNome = models.CharField(max_length=50, blank=True, null=True)
    cidadeEstado = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tbCidade'
        verbose_name_plural = 'Cidade'
    def __str__(self):
        return self.cidadeNome



class tbCliente(models.Model):
    clienteNome = models.CharField(max_length=50, blank=True, null=True)
    clienteAdministrador = models.CharField(max_length=20, blank=True, null=True)
    clienteAdministradora = models.CharField(max_length=20, blank=True, null=True)
    clienteCftv = models.ForeignKey(tbSistemaCftv, on_delete=models.CASCADE)
    clienteSai = models.ForeignKey(tbSistemaSai, on_delete=models.CASCADE)
    clienteSca = models.ForeignKey(tbSistemaSca, on_delete=models.CASCADE)
    clienteSap = models.ForeignKey(tbSistemaSap, on_delete=models.CASCADE)
    clienteSdai = models.ForeignKey(tbSistemaSdai, on_delete=models.CASCADE)
    clienteCidade = models.ForeignKey(tbCidade, on_delete=models.CASCADE)



    class Meta:
        db_table = 'tbCliente'
        verbose_name_plural = 'Clientes'
    def __str__(self):
        return self.clienteNome





class tbSistemas(models.Model):
    sistemasTipo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'tbSistemas'
        verbose_name_plural = 'Sistemas'

    def __str__(self):
        return self.sistemasTipo










class tbEquipamento(models.Model):
    equipamentoNome = models.CharField(max_length=50, blank=True, null=True)
    equipamentoLogin = models.CharField(max_length=50, blank=True, null=True)
    equipamentoPassword = models.CharField(max_length=50, blank=True, null=True)
    equipamentoQrCode = models.CharField(max_length=50, blank=True, null=True)
    equipamentoObservacao = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'tbEquipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return self.equipamentoNome

class tbPreventivas(models.Model):
    preventivaEquipamento = models.CharField(max_length=100, blank=True, null=True)
    preventivaProcedimento = models.CharField(max_length=255, blank=True, null=True)
    preventivaTempo = models.IntegerField(blank=True, null=True)


    class Meta:
        db_table = 'tbPreventivas'
        verbose_name_plural = 'Preventivas'

    def __str__(self):
        return self.preventivaEquipamento

class tbSenhasPadroes(models.Model):
    senhaLogin = models.CharField(max_length=50, blank=True, null=True)
    senhaPassword = models.CharField(max_length=50, blank=True, null=True)
    senhaObservacao = models.CharField(max_length=255, blank=True, null=True)



    class Meta:
        db_table = 'tbSenhasPadores'
        verbose_name_plural = 'Senhas Padrões'

    def __str__(self):
        return self.senhaLogin


class tbWework(models.Model):
    weworkNome = models.CharField(max_length=50, blank=True, null=True)
    weworkQuantAndares = models.IntegerField(blank=True, null=True)
    weworkAndares = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        db_table = 'tbWework'
        verbose_name_plural = 'Weworks'

    def __str__(self):
        return self.weworkNome


