
# ✅ Checkpoint QA - Testes Automatizados

## 👥 Integrantes
- Murillo Ferreira Ramos
- Pedro Luiz Prado Saraiva Pereira

---

## 🔗 Projeto utilizado
Aplicação: [Restful Booker Platform](https://github.com/prof-desiglo/restful-booker-platform/tree/trunk)  
- Web: http://localhost:3003  
- API: http://localhost:3003/api/room  
- Login: `admin` / `password`

---

## 📁 Estrutura do Repositório

```
📁 /postman
  └── api-tests.postman_collection.json

📁 /selenium
  └── login_test.py
  └── outros_testes.py

📁 /performance
  ├── script_k6.js  OU  script_jmeter.jmx
  └── relatório_performance.md

📄 README.md
```

---

## ✍️ Testes de API - Postman (Murillo)
- Testes dos métodos: `GET`, `POST`, `PUT`, `DELETE`
- Casos positivos e negativos (status 200 e 400)
- Validação de status code e corpo da resposta
- Exportado como coleção `.json` e armazenado na pasta `/postman`

---

## 🖱 Testes Web - Selenium (Pedro)
- 4 cenários testados:
  - Login com sucesso
  - Login com erro (negativo)
  - Criação de entidade
  - Edição ou exclusão
- Scripts executáveis com instruções no próprio diretório `/selenium`

---

## 📈 Testes de Performance - K6 ou JMeter (Murillo)
- Simulação de:
  - 20 usuários
  - 50 usuários
  - 100 usuários
- Métricas avaliadas:
  - Tempo de resposta
  - Throughput
  - Erros
- Relatório com comparação de cenários na pasta `/performance`

---

## 📹 Apresentação em Vídeo
- Link do vídeo: [Inserir link do YouTube aqui]

---

## 🚀 Como Executar

### API - Postman
1. Abrir o Postman
2. Importar `/postman/api-tests.postman_collection.json`
3. Executar a collection

### Web - Selenium
```bash
cd selenium
python login_test.py
```

### Performance - K6
```bash
cd performance
k6 run script_k6.js
```

---

## ✅ Observações
- Todas as pastas contém os arquivos executáveis e documentações complementares.
- Scripts testados e funcionais com o ambiente local rodando.

---
