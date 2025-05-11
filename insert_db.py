import sqlite3
from datetime import datetime

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

familias = [
    {
        "status_atendimento": "Aguardando Vaga",
        "nome": "Amanda Ferreira Lima",
        "rg": "27.345.891-5",
        "cpf": "105.674.389-40",
        "data_nascimento": "1992-03-12",
        "endereco": "Rua das Rosas, 123",
        "bairro": "Jardim das Flores",
        "cidade": "São Paulo",
        "cep": "03129-070",
        "telefone": "(11) 99823-4567",
        "qtd_membros": "4"
    },
    {
        "status_atendimento": "Ativa",
        "nome": "Bruno Henrique da Costa",
        "rg": "18.209.456-0",
        "cpf": "387.102.568-72",
        "data_nascimento": "1985-07-04",
        "endereco": "Av. Brasil, 3021",
        "bairro": "Centro",
        "cidade": "Campinas",
        "cep": "13010-200",
        "telefone": "(19) 99112-7890",
        "qtd_membros": "3"
    },
    {
        "status_atendimento": "Suspensa",
        "nome": "Carla Beatriz Souza",
        "rg": "42.108.799-3",
        "cpf": "293.615.840-91",
        "data_nascimento": "1997-10-28",
        "endereco": "Rua São João, 45",
        "bairro": "Liberdade",
        "cidade": "Salvador",
        "cep": "40045-170",
        "telefone": "(71) 98745-3211",
        "qtd_membros": "4"
    },
    {
        "status_atendimento": "Suspensa",
        "nome": "Diego Martins Rocha",
        "rg": "12.888.224-9",
        "cpf": "142.370.951-50",
        "data_nascimento": "1990-01-15",
        "endereco": "Travessa Boa Vista, 77",
        "bairro": "Boa Vista",
        "cidade": "Recife",
        "cep": "50060-100",
        "telefone": "(81) 99423-7754",
        "qtd_membros": "7"
    },
    {
        "status_atendimento": "Ativa",
        "nome": "Eliane Campos Tavares",
        "rg": "30.004.112-1",
        "cpf": "064.512.307-23",
        "data_nascimento": "1983-11-09",
        "endereco": "Rua Guaporé, 890",
        "bairro": "Zona Sul",
        "cidade": "Porto Alegre",
        "cep": "91740-580",
        "telefone": "(51) 99321-1144",
        "qtd_membros": "4"
    },
    {
        "status_atendimento": "Ativa",
        "nome": "Felipe Oliveira Braga",
        "rg": "22.765.331-2",
        "cpf": "315.904.872-66",
        "data_nascimento": "1994-06-23",
        "endereco": "Rua das Palmeiras, 300",
        "bairro": "Tijuca",
        "cidade": "Rio de Janeiro",
        "cep": "20510-050",
        "telefone": "(21) 99980-5643",
        "qtd_membros": "2"
    },
    {
        "status_atendimento": "Suspensa",
        "nome": "Gabriela Moura Pinto",
        "rg": "40.112.987-7",
        "cpf": "206.879.350-04",
        "data_nascimento": "2000-09-30",
        "endereco": "Rua Diamante, 12",
        "bairro": "Eldorado",
        "cidade": "Contagem",
        "cep": "32315-110",
        "telefone": "(31) 98432-7700",
        "qtd_membros": "10"
    },
    {
        "status_atendimento": "Aguardando Vaga",
        "nome": "Henrique Alves Nascimento",
        "rg": "11.509.333-8",
        "cpf": "120.764.990-82",
        "data_nascimento": "1988-05-18",
        "endereco": "Av. Independência, 65",
        "bairro": "Estação",
        "cidade": "João Pessoa",
        "cep": "58030-230",
        "telefone": "(83) 99701-1188",
        "qtd_membros": "6"
    }
]

for f in familias:
    cursor.execute("""
        INSERT INTO website_familia (status_atendimento, nome, rg, cpf, data_nascimento, endereco, bairro, cidade, cep, qtd_membros)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        f["status_atendimento"],
        f["nome"],
        f["rg"],
        f["cpf"],
        f["data_nascimento"],
        f["endereco"],
        f["bairro"],
        f["cidade"],
        f["cep"],
        f["qtd_membros"],
    ))
    
    familia_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO website_telefone (telefone, familia_id)
        VALUES (?, ?)
    """, (f["telefone"], familia_id))

conn.commit()
conn.close()

print("Dados inseridos com sucesso.")
