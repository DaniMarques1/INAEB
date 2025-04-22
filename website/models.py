from django.db import models

class Familia(models.Model):
    # Django cria automaticamente o id como pk: id = models.AutoField(primary_key=True)
    
    # Status de atendimento da família
    STATUS_ATENDIMENTO_CHOICES = [
        ("Ativa", "Ativa"),
        ("Suspensa", "Suspensa"),
        ("Aguardando Vaga", "Aguardando Vaga"),
    ]
    status_atendimento = models.CharField(max_length=20, choices=STATUS_ATENDIMENTO_CHOICES, default="Aguardando Vaga")
    inicio_atendimento = models.DateField(null=True, blank=True)
    termino_atendimento = models.DateField(null=True, blank=True)

    # Dados do Responsável
    data_entrevista = models.DateField(null=True, blank=True)
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=12)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    receita_apro = models.CharField(max_length=50, null=True, blank=True)
    despesa_apro = models.CharField(max_length=50, null=True, blank=True)
    obs_responsavel = models.CharField(max_length=50, null=True, blank=True)

    # Endereço
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    ponto_referencia = models.CharField(max_length=50, null=True, blank=True)
    complemento = models.CharField(max_length=50, null=True, blank=True)

    # -------- QUESTIONÁRIO SÓCIO ECONÔMICO -------- #
    data_visita = models.DateField(null=True, blank=True)

    # Higiene do Ambiente
    LIXO_CHOICES = [
        ("Queima", "Queima"),
        ("Enterra", "Enterra"),
        ("Coleta", "Coleta"),
    ]
    lixo = models.CharField(max_length=50, choices=LIXO_CHOICES, null=True, blank=True)

    LIMPEZA_CASA_CHOICES = [
        ("Varre", "Varre"),
        ("Lava", "Lava"),
        ("Ambos", "Ambos"),
    ]
    limpeza_casa = models.CharField(max_length=50, choices=LIMPEZA_CASA_CHOICES, null=True, blank=True)
    obs_limpeza = models.CharField(max_length=2000, null=True, blank=True)

    # Saneamento Básico
    AGUA_CHOICES = [
        ("Encanada", "Encanada"),
        ("Poço", "Poço"),
        ("Cisterna", "Cisterna"),
    ]
    agua = models.CharField(max_length=50, null=True, blank=True, choices=AGUA_CHOICES)
    ESGOTO_CHOICES = [
        ("Rede", "Rede"),
        ("Fossa", "Fossa"),
        ("Céu Aberto", "Céu Aberto"),
    ]
    esgoto = models.CharField(max_length=50, null=True, blank=True, choices=ESGOTO_CHOICES)
    obs_saneamento = models.CharField(max_length=2000, null=True, blank=True)

    # Moradia
    TIPO_MORADIA_CHOICES = [
        ("Própria", "Própria"),
        ("Alugada", "Alugada"),
        ("Cedida", "Cedida"),
    ]
    tipo_moradia= models.CharField(max_length=20, null=True, blank=True, choices=TIPO_MORADIA_CHOICES)
    num_comodo = models.IntegerField(null=True, blank=True)
    num_moradores = models.IntegerField(null=True, blank=True)
    BANHEIRO_CHOICES = [
        ("Banheiro Externo", "Banheiro Externo"),
        ("Banheiro Interno", "Banheiro Interno"),
    ]
    banheiro = models.CharField(max_length=20, null=True, blank=True, choices=BANHEIRO_CHOICES)
    CONSTRUCAO_CHOICES = [
        ("Alvenaria", "Alvenaria"),
        ("Taipa", "Taipa"),
        ("Madeira", "Madeira"),
    ]
    construcao = models.CharField(max_length=50, null=True, blank=True, choices=CONSTRUCAO_CHOICES)
    
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
    obs_gerais = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.nome or f"Família {self.pk}"

class Telefone(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return f"Tel: {self.telefone}"

class Parente(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

    nome = models.CharField(max_length=50, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
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