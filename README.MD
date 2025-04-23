
# ✅ Checkpoint QA - Projeto Completo

Este repositório reúne os testes automatizados funcionais e não-funcionais desenvolvidos para o **Checkpoint 4 da disciplina de Quality Assurance** do curso de Análise e Desenvolvimento de Sistemas da FIAP.

---

## 👥 Integrantes

- **Murillo Ferreira Ramos** – RM553315
- **Pedro Luiz Prado Saraiva Pereira** – RM553874

---

## 🧩 Aplicação Base

- Projeto: [Restful Booker Platform](https://github.com/prof-desiglo/restful-booker-platform/tree/trunk)
- Web App: `http://localhost:3003`
- API REST: `http://localhost:3001/api/room`
- Login: `admin / password`

---

## 🗂 Estrutura do Repositório

```
📁 postman/
│   ├── api-tests-final-entregavel.json
│   └── README_API_TESTS.md

📁 selenium/
│   ├── test_login.py
│   ├── test_room_list.py
│   ├── requirements.txt
│   ├── chromedriver.exe
│   ├── evidencias/
│   └── README_SELENIUM.md

📁 performance/
│   ├── k6_20vus.js
│   ├── RELATORIO_PERFORMANCE_K6.md
│   ├── RELATORIO_COMPARATIVO.md
│   └── README_PERFORMANCE.md

📄 README.md (este arquivo)
```

---

## ✅ Entregas

### 📦 Testes de API com Postman – (Murillo)
- Collection com métodos `GET`, `POST`, `PUT`, `DELETE`
- Testes positivos e negativos
- Cobertura completa com validações e fallback
- Algumas falhas foram mantidas para demonstrar **bugs da API**

### 🖱 Testes WEB com Selenium – (Pedro)
- Testes com Selenium + Pytest
- Simulação de login válido e inválido
- Verificação da listagem de quartos
- Prints de tela automáticos como evidência

### 📈 Testes de Performance com K6 – (Murillo)
- Simulação com 20, 50 e 100 usuários
- Coleta de métricas como tempo médio, p95 e throughput
- Análise de desempenho da API com relatório comparativo

---

## 📥 Como Executar

### ✅ Inicie a aplicação:
- Via Docker ou com os scripts `build_locally.cmd` e `run_locally.cmd` (disponíveis no projeto do professor)

### 🧪 Postman:
```bash
Importar a collection `api-tests-final-entregavel.json` no Postman
Executar os testes
```

### 🤖 Selenium:
```bash
pip install -r requirements.txt
pytest test_login.py
pytest test_room_list.py
```

### 📈 Performance:
```bash
k6 run k6_20vus.js
```

---

## 📹 Apresentação em Vídeo

> 🔗 [[Link do Vídeo no Youtube](https://www.youtube.com/watch?v=8oOtYEgFMpI)]

---

## 📌 Observações Finais

- Os testes foram organizados em pastas independentes, cada uma com seu próprio `README.md`
- Algumas falhas propositalmente mantidas nos testes destacam comportamentos inesperados da API (como ausência de validação ou exigência de autenticação no DELETE)
- O projeto foi desenvolvido em dupla, com cada integrante responsável por partes distintas e complementares

---

📅 Abril/2025 – FIAP 2TDSPC
