# API Taskmanager - Meu Primeiro Projeto DRF! 🚀

Olá! Este projeto é o resultado da minha jornada de estudos com o **Django REST Framework**. Depois de muita teoria, erros, acertos e conversas com meu "Mestre" (uma IA do Google!), decidi criar esta API do zero para praticar e solidificar tudo que aprendi.

O objetivo foi ir além do "caminho feliz" dos tutoriais e construir uma **API de Lista de Tarefas (To-Do List)** que fosse segura, multi-usuário e que seguisse as melhores práticas do mercado que venho estudando.

---

## O que eu aprendi e apliquei aqui:

Este projeto não é só sobre o resultado final, mas sobre o processo. Aqui estão os conceitos-chave que eu pratiquei e implementei:

* **✅ Estrutura Profissional:** Organizei o projeto de forma lógica, separando as responsabilidades em diferentes apps (`core`, `accounts` e `tarefas`), um padrão que vejo ser muito valorizado no mercado.

* **🔐 Segurança e Autenticação:** Implementei um sistema de autenticação via Token (`rest_framework.authtoken`). Endpoints que modificam dados (`POST`, `PUT`, `DELETE`) são protegidos e só podem ser acessados por usuários com um "crachá" (token) válido.

* **🔒 Privacidade de Dados (Multi-Tenant):** Esta foi a parte mais legal! Garanti que um usuário não pode, de forma alguma, ver as tarefas de outro. A API filtra os dados automaticamente com base no usuário que faz a requisição (sobrescrevendo o método `get_queryset` no `ViewSet`).

* **⚙️ CRUD Completo e Lógica de Negócio:** A API permite o ciclo completo de operações (Criar, Ler, Atualizar e Deletar) para as tarefas. Além disso, a criação de tarefas é inteligente, vinculando-as automaticamente ao usuário logado (usando `perform_create`).

* **🔑 Gerenciamento de Segredos:** Aprendi a nunca mais subir segredos para o GitHub! Todas as chaves (`SECRET_KEY`) и senhas de banco de dados estão seguras em um arquivo `.env`, que é ignorado pelo Git (`.gitignore`).

---

## 🛠️ Minha Caixa de Ferramentas (Tecnologias)

<table>
  <tr>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40" alt="Python" title="Python"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" width="40" alt="Django" title="Django"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-original.svg" width="40" alt="DRF" title="Django REST Framework"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original-wordmark.svg" width="40" alt="MySQL" title="MySQL"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="40" alt="Git" title="Git"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" width="40" alt="GitHub" title="GitHub"/></td>
  </tr>
</table>

---

## 🚀 Como Rodar o Projeto

Quer testar a agenda? É só seguir os passos:

**1. Clone o repositório:**
```bash
git clone [https://github.com/MarinaldoSilva/taskmanager.git](https://github.com/MarinaldoSilva/taskmanager.git)
cd taskmanager
