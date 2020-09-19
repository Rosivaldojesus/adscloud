from django.contrib import admin
from .models import tbCliente, tbCidade, tbAdministradora, tbSistemaCftv, tbSistemaSai, tbSistemaSca, \
    tbSistemaSap, tbSistemaSdai, tbPreventivas, tbSenhasPadroes, tbEquipamento, tbWework, tbSistemas, \
    tbFabricante, tbManuais, tbArtigos

# Register your models here.
class tbClienteAdmin(admin.ModelAdmin):
    list_display = ('id')

admin.site.register(tbCliente)



admin.site.register(tbCidade)
admin.site.register(tbFabricante)
admin.site.register(tbAdministradora)
admin.site.register(tbSistemaCftv)
admin.site.register(tbSistemaSca)
admin.site.register(tbSistemaSai)
admin.site.register(tbSistemaSap)
admin.site.register(tbSistemaSdai)
admin.site.register(tbPreventivas)
admin.site.register(tbSenhasPadroes)
admin.site.register(tbEquipamento)
admin.site.register(tbWework)
admin.site.register(tbSistemas)
admin.site.register(tbManuais)
admin.site.register(tbArtigos)