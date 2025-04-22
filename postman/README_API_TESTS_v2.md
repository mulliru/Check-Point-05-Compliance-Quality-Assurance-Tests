
# ✅ API Tests - Restful Booker Platform

Este projeto contém uma coleção de testes da API `/room` do sistema **Restful Booker Platform**, utilizando o **Postman** para validação funcional.

---

## 📌 Endpoints testados

| Método | Endpoint          | Descrição                          | Status Esperado |
|--------|-------------------|------------------------------------|-----------------|
| GET    | `/room`           | Lista todos os quartos             | 200 OK          |
| POST   | `/room`           | Cria um novo quarto                | 201 Created     |
| POST   | `/room` (inválido)| Teste de erro com campos faltando | 400 Bad Request |
| PUT    | `/room/1`         | Atualiza o quarto 1                | 200 OK          |
| DELETE | `/room/1`         | Deleta o quarto 1 e valida remoção| 200 OK + 404    |

---

## 🚀 Como rodar os testes

1. Inicie sua API localmente (certifique-se de que o módulo `room` está rodando)
2. Acesse o Postman
3. Clique em **Import**
4. Selecione o arquivo `api-tests-v3-delete-check.postman_collection.json`
5. Execute cada requisição e observe os testes

---

## ⚙️ Observações técnicas

- A API está configurada para rodar em `http://localhost:3001/room`
- Caso sua aplicação esteja em outra porta (ex: `3003` via Docker), altere a URL no Postman
- O `DELETE /room/1` inclui um **teste de verificação**, garantindo que o quarto foi realmente removido com um `GET` subsequente

---

## 📄 Estrutura dos testes

### ✅ GET `/room`
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

### ✅ POST `/room` (válido)
```javascript
pm.test("Room created successfully", function () {
    pm.response.to.have.status(201);
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("roomid");
    pm.expect(jsonData.roomName).to.eql("203");
});
```

### ❌ POST `/room` (inválido)
```javascript
pm.test("Invalid data returns error", function () {
    pm.response.to.have.status(400);
});
```

### 🔄 PUT `/room/1`
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Body should reflect updated data", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.roomName).to.eql("101 Atualizado");
    pm.expect(jsonData.type).to.eql("suite");
});
```

### 🗑 DELETE `/room/1`
```javascript
pm.test("Room deleted", function () {
    pm.response.to.have.status(200);
});

pm.sendRequest("http://localhost:3001/room/1", function (err, res) {
    pm.test("Room should not exist anymore", function () {
        pm.expect(res.code).to.eql(404);
    });
});
```

---

## 📷 Exemplo da coleção no Postman

![Exemplo da coleção](./assets/postman-collection-preview.png)

---

## 👨‍💻 Desenvolvido por

Murillo Ferreira Ramos – RM553315  
FIAP 2TDSPC – Checkpoint QA – Abril 2025
