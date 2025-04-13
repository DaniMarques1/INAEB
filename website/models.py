from django.db import models

class Familia(models.Model):
    # Django cria automaticamente o id como pk: id = models.AutoField(primary_key=True)

    data_entrevista = models.DateField()
    # Dados do Responsável
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=12)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    receita_apro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    despesa_apro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Endereço
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    ponto_referencia = models.CharField(max_length=50, null=True, blank=True)
    complemento = models.CharField(max_length=50, null=True, blank=True)

    # Status de atendimento da família
    status_atendimento = models.CharField(max_length=20)
    inicio_atendimento = models.DateField(null=True, blank=True)
    termino_atendimento = models.DateField(null=True, blank=True)

    # Lixo e Limpeza da Casa
    lixo = models.CharField(max_length=50, null=True, blank=True)
    limpeza_casa = models.CharField(max_length=50, null=True, blank=True)
    obs_limpeza = models.CharField(max_length=2000, null=True, blank=True)

    # Saneamento
    agua = models.CharField(max_length=50, null=True, blank=True)
    esgoto = models.CharField(max_length=50, null=True, blank=True)
    obs_esgoto = models.CharField(max_length=2000, null=True, blank=True)

    # Moradia
    tipo_moradia= models.CharField(max_length=20, null=True, blank=True)
    num_comodo = models.IntegerField(null=True, blank=True)
    num_moradores = models.IntegerField(null=True, blank=True)
    banheiro = models.CharField(max_length=10, null=True, blank=True)
    construcao = models.CharField(max_length=50, null=True, blank=True)
    
    # Itens diversos (checkboxes)
    televisor = models.BooleanField(null=True, blank=True)
    geladeira = models.BooleanField(null=True, blank=True)
    celular_smartphone_tablet = models.BooleanField(null=True, blank=True)
    aparelho_som = models.BooleanField(null=True, blank=True)
    maquina_lavar = models.BooleanField(null=True, blank=True)
    carro_moto = models.BooleanField(null=True, blank=True)
    dvd = models.BooleanField(null=True, blank=True)
    computador_notebook = models.BooleanField(null=True, blank=True)
    telefone_internet = models.BooleanField(null=True, blank=True)

    # Observações Gerais
    obs_gerais = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome or f"Família {self.pk}"

class Telefone(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return f"Tel: {self.telefone} - Cel: {self.celular}"

class Parente(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

    nome = models.CharField(max_length=50, null=True, blank=True)
    parentesco = models.CharField(max_length=50, null=True, blank=True)
    instrucao = models.CharField(max_length=50, null=True, blank=True)
    profissao = models.CharField(max_length=20, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    ocupacao = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome or f"Parente {self.pk}"

class Produto(models.Model):
    produto = models.CharField(max_length=50)
    qtd_estoque = models.IntegerField()
    
    def __str__(self):
        return self.produto

class Doacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.IntegerField()
    data_entrada = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Doações'

    def __str__(self):
        return f"Estoque {self.pk}"

class Entrega(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

    data_doacao = models.DateTimeField()
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Entrega {self.pk}"

class ItemCesta(models.Model):
    produto = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    quantidade = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Itens da Cesta'

    def __str__(self):
        return f"{self.produto} (Qtd: {self.quantidade})"