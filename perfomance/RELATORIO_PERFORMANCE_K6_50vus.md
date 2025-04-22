
# 📈 Relatório de Teste de Performance - API `/room` - 50 VUs

Este relatório apresenta os resultados do teste com **50 usuários virtuais durante 15 segundos**, utilizando o K6.

---

## 📊 Resumo do teste

- **Total de requisições**: 1500
- **Requisições bem-sucedidas**: ✅ 100% (1500/1500)
- **Tempo médio de resposta**: ⚡ 4.43 ms
- **Mediana (med)**: 1.88 ms
- **Percentil 90 (p90)**: 11.71 ms
- **Percentil 95 (p95)**: 20.4 ms
- **Tempo máximo**: 45.14 ms
- **Falhas**: ❌ 0%
- **Iterações completas**: 🔁 750
- **VUs simultâneos**: 👥 50
- **Dados recebidos**: 📥 425 KB
- **Dados enviados**: 📤 159 KB

---

## 🖼 Captura de tela da execução 

![Teste de Perfomance com 50 usuários](assets/k6-test-50vus.png)


---

## 📌 Interpretação

| Métrica                   | Valor       | Interpretação                               |
|--------------------------|-------------|---------------------------------------------|
| Sucesso nas requisições  | ✅ 100%      | Todas as requisições foram aceitas          |
| Tempo médio               | ⚡ 4.43ms    | Extremamente rápido                         |
| Percentil 95              | 🟢 20.4ms    | Bem dentro da margem de tolerância          |
| Estabilidade              | 🟢 Alta      | Nenhuma falha ou queda registrada           |
| Escalabilidade            | 🔼 Excelente| API lida bem com aumento de carga           |

---

## 📜 Script utilizado

[`k6_50vus.js`](./k6_50vus.js)

---

### 👨‍💻 Desenvolvido por

**Murillo Ferreira Ramos - RM553315** \
**Pedro Luiz Prado Saraiva Pereira - RM553874**

**2TDSPC – FIAP – Abril/2025**
