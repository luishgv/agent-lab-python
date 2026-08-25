<!-- l10n-sync: source-file="workshop/01-setup.md" -->
# Parte 1: Configuração & Engenharia de Contexto

[📚 Guia do Lab](https://copilot-dev-days.github.io/agent-lab-python/docs/) • [← Visão Geral](00-overview.md)

---

> ⏱️ **Tempo:** ~15 minutos

Nesta seção, você vai configurar seu ambiente de desenvolvimento e ensinar o GitHub Copilot sobre sua base de código.

---

## 🔧 Configuração Inicial

### Passo 1: Crie Seu Próprio Repositório (obrigatório)

1. Abra [github.com/copilot-dev-days/agent-lab-python](https://github.com/copilot-dev-days/agent-lab-python)
2. Clique em **Use this template** → **Create a new repository**
   - Nome: `my-soc-ops-python`
   - Visibilidade: **Public**
3. ✅ Seu próprio repositório Soc Ops está pronto!

### Passo 2: Escolha Como Abrir Seu Repositório

Este repositório inclui um devcontainer pronto para uso (`.devcontainer/devcontainer.json`), então você pode trabalhar localmente ou no Codespaces.

#### Opção A: Clone & Abra no VS Code Local

1. Abra o VS Code
2. Execute o comando: `Git: Clone` → `Clone from GitHub`
3. Selecione seu novo repositório
4. Quando solicitado, instale as **extensões recomendadas**

#### Opção B: Abra Seu Novo Repositório no GitHub Codespaces

1. Abra seu repositório recém-criado no GitHub
2. Clique em **Code** → **Codespaces** → **Create codespace on main**
3. Aguarde a configuração terminar (o devcontainer executa `uv sync` automaticamente)
4. ✅ Você pode iniciar o lab diretamente na experiência VS Code baseada no navegador

### Passo 3: Execute o Agente de Setup (ambas as opções)

No painel de Chat:

```
/setup
```

O agente vai:
- Detectar seu ambiente
- Instalar dependências faltantes
- Iniciar o servidor de desenvolvimento

> ⚠️ **Codespace no navegador:** Se você estiver executando o aplicativo dentro de um GitHub Codespace pelo navegador (não VS Code Desktop), os estilos e interações (ex.: o botão Start Game) podem não funcionar corretamente devido à autenticação de porta privada. Para corrigir, faça uma das opções:
> 1. No painel **Ports** (barra inferior), clique com o botão direito na porta `8000` → **Port Visibility** → **Public**
> 2. Ou abra o Codespace no **VS Code Desktop** (clique no menu hambúrguer `☰` → **Open in VS Code Desktop**)

✅ **Sucesso:** O aplicativo está rodando no seu navegador!

---

## 📚 Entendendo a Engenharia de Contexto

Engenharia de contexto é como você ensina a IA sobre sua base de código específica. Isso torna as sugestões do Copilot mais precisas e relevantes.

### Tarefa 1: Gerar Instruções de Workspace

Instruções guiam todas as interações agênticas, tornando-as eficientes e confiáveis.

**Passos:**

1. Abra a Paleta de Comandos (`Ctrl+Shift+P` / `Cmd+Shift+P`) e execute: `Chat: Generate Agent Instructions`
2. Aguarde o agente analisar sua base de código
3. Revise as instruções geradas (provavelmente detalhadas demais!)
4. Continue com:
   ```
   Compress down by half and add a mandatory development checklist 
   (lint, build, test) to the top
   ```
5. **Faça commit** do arquivo de instruções

✅ **Resultado:** Todas as futuras solicitações terão um mapa básico do seu workspace.

---

### Tarefa 2: Copilot CLI e Cloud Agents para Trabalho Paralelo

Sessões do Copilot CLI rodam em worktrees git isoladas, o que é perfeito para tarefas que não precisam de acompanhamento.

> 💡 **Três controles de interface para conhecer:**
> - **Nova sessão (`+`)** (topo do painel de Chat) — crie um **New Chat**, **New Chat Editor**, **New Chat Window** ou **New Copilot CLI Session**
> - **Dropdown de modo de chat** (canto inferior esquerdo da entrada do chat, mostra **Agent** por padrão) — escolha um modo (**Agent**, **Ask**, **Plan**) ou um agente customizado
> - **Dropdown de tipo de sessão** (canto inferior esquerdo da entrada do chat, mostra **Local** por padrão) — transfira ou execute em um ambiente diferente: **Local**, **Copilot CLI** ou **Cloud**

**Inicie uma sessão Copilot CLI:**

1. No **dropdown de tipo de sessão** (canto inferior esquerdo, mostra **Local**), selecione **Copilot CLI**
2. Digite:
   ```
   Add linting rules with ruff for unused vars and type hints; fix any errors
   ```
3. Deixe rodar, depois **Revise** e **Aplique** as mudanças
4. Clique com o botão direito na sessão para deletá-la quando terminar

**Inicie um Cloud Agent ou sessão Copilot CLI:**

> **Se você tem Copilot Pro, Business ou Enterprise:**
>
> 1. No **dropdown de tipo de sessão** (canto inferior esquerdo), selecione **Cloud**
> 2. Digite:
>    ```
>    Make the README more engaging as a landing page to the project
>    ```

> **Se você está no plano gratuito (sem acesso ao Cloud):**
>
> 1. No **dropdown de tipo de sessão** (canto inferior esquerdo), selecione **Copilot CLI**
> 2. Digite:
>    ```
>    Make the README more engaging as a landing page to the project
>    ```

✅ **Resultado:** Regras de linting adicionadas, erros corrigidos, README melhorado — tudo sem interromper seu workspace principal!

---

### Tarefa 3: Explore Instruções Existentes

Seu repositório já vem com instruções pré-configuradas que ajudam a IA a entender o projeto.

#### Instruções de Utilitários CSS

📄 Veja `.github/instructions/css-utilities.instructions.md`

Estas documentam as classes utilitárias CSS customizadas disponíveis neste projeto Python/Jinja2.

> 💡 **Opcional:** Delete o texto principal e re-execute o prompt para ver como ele gera

#### Instruções de Design Frontend

📄 Veja `.github/instructions/frontend-design.instructions.md`

As instruções "sem gradientes roxos" desafiam o agente a pensar como um designer.

> 💡 **Pense sobre:** Quais outros vieses da IA você poderia desafiar e direcionar?

---

## ✅ Parte 1 Completa!

Você aprendeu como:
- Configurar seu ambiente de desenvolvimento
- Gerar e refinar instruções de workspace
- Usar background e cloud agents para trabalho paralelo
- Entender arquivos de instruções existentes
