# API Taskmanager

Projeto feito com base em estudos realizados com o Copilot e Gemini.

Um simples lista de tarefas que se alimenta via API, podem ignoar as más praticas, estou começando ainda, se está assim foi a forma que consegui solidificar o conhecimento, um passo por vez!

Este projeto não é só sobre o resultado final, mas sobre o process, aprender conceitos novos e por em prática é sempre um desafio a ser superado.

Usei o authtoken nativo do DRF para ter uma camada de segurança, os meus endpoints que modificam dados (`POST`, `PUT`, `DELETE`) só podem ser acessados por usuários válidos.

Somente o proprio usuário pode ver as suas tarefas, isso nós garante a privacidade.

Nessa aplicação o CRUD foi completo, e os arquivos como SECRET_KEY estão salvos em um .env, e não so esses, diversos outros arquivos estão assim, somente o necessário foi upado.

## Tecnologias utilizadas

<table>
  <tr>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40" alt="Python" title="Python"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-original.svg" width="40" alt="DRF" title="Django REST Framework"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original-wordmark.svg" width="40" alt="MySQL" title="MySQL"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="40" alt="Git" title="Git"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" width="40" alt="GitHub" title="GitHub"/></td>
  </tr>
</table>

---


** Para testar o projeto, clone meu repositório, gere uma nova chave e configure o banco para receber o migrate:**
```bash
git clone [https://github.com/MarinaldoSilva/taskmanager.git](https://github.com/MarinaldoSilva/taskmanager.git)
