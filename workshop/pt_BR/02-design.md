<!-- l10n-sync: source-file="workshop/02-design.md" -->
# Parte 2: Frontend Design-First

[📚 Guia do Lab](https://copilot-dev-days.github.io/agent-lab-python/docs/) • [← Parte 1](01-setup.md)

---

> ⏱️ **Tempo:** ~15 minutos

Agora que o contexto do seu repositório está engenheirado, vamos ser criativos! Você vai redesenhar toda a UI usando desenvolvimento assistido por IA.

---

## 🎨 Tarefa 1: Deixe do Seu Jeito

Use o agente **Plan** para começar qualquer item de trabalho maior. Itere no plano (2+ vezes!) com ajustes e esclarecimentos.

### Passos

1. No **dropdown de modo de chat** (canto inferior esquerdo da entrada do chat), selecione **Plan**
2. Certifique-se de que o **dropdown de tipo de sessão** mostra **Local** (se sua sessão anterior foi Cloud, mude de volta)
3. Digite sua visão:
   ```
   Let's do a full redesign. Make it [YOUR THEME]
   ```
4. Revise o plano gerado
5. Peça ajustes até ficar satisfeito
6. Clique em **Start Implementation** para executar

### 🎭 Ideias de Temas

Escolha um que combine com você:

| Categoria | Temas |
|-----------|-------|
| **Minimal** | Minimalist Mono, Scandinavian Calm, Desert Sand Minimal |
| **Retro** | Retro Terminal Green, Pixel Arcade Style, Vaporwave Sunset |
| **Dark** | Cyberpunk Neon, Dark Mode Noir, Space Galaxy Glow |
| **Playful** | Playful Candy Pop, Toybox Primary Colors, Anime Bubble |
| **Professional** | Corporate Clean Blue, Gradient Glass UI, Metallic Chrome |
| **Creative** | Brutalist Blocks, Geometric Memphis, Bold Constructivist |
| **Cozy** | Cozy Coffee Shop, Soft Pastel Clouds, Notebook Doodle |
| **Unique** | Skeuomorphic Stickers, Paper Card Cutouts, Chalkboard |

✅ **Resultado:** Instruções de frontend e utilitários CSS se combinam para construir um design bonito.

---

## 📝 Tarefa 2: Mantenha as Instruções Atualizadas

Quando você fizer mudanças grandes de arquitetura, design ou dependências, atualize suas instruções!

### Passos

1. Após o redesign, continue com:
   ```
   Add a design guide section to copilot-instructions.md
   ```
2. Revise as mudanças
3. **Faça commit e push**

---

## 🚀 Tarefa 3: Escale a Exploração com Cloud Agents

Gere múltiplas variações de design em paralelo usando cloud agents.

> **Se você tem Copilot Pro, Business ou Enterprise:**
>
> 1. No **dropdown de modo de chat** (canto inferior esquerdo da entrada do chat), selecione **Plan**
> 2. Digite:
>    ```
>    Redesign the start screen as a more engaging landing page
>    ```
> 3. Note as variações sugeridas no plano
> 4. Execute o prompt de exploração:
>    ```
>    /cloud-explore design variations
>    ```
>    📄 Veja `.github/prompts/cloud-explore.prompt.md`
>
> 5. Verifique as **Agent Sessions** para acompanhar os 3 novos cloud agents
> 6. Clique em qualquer sessão para acompanhar o progresso ou abrir na web

> **Se você está no plano gratuito (sem acesso ao Cloud):**
>
> 1. Use o modo **Autopilot** ou uma sessão **Plan** local para explorar uma variação de design por vez
> 2. No **dropdown de modo de chat** (canto inferior esquerdo da entrada do chat), selecione **Plan**
> 3. Digite:
>    ```
>    Redesign the start screen as a more engaging landing page
>    ```
> 4. Revise e implemente o plano, depois repita com uma direção diferente

### O que Está Acontecendo

O prompt inicia **3 cloud agents em paralelo**, cada um explorando uma direção de design diferente. Eles vão:
- Criar branches
- Implementar variações
- Tirar capturas de tela
- Abrir PRs para sua revisão

✅ **Resultado:** 3 variações de design para comparar, todas rodando em paralelo!

> ⏰ Isso leva alguns minutos. Continue para a Parte 3 enquanto eles rodam.

---

## ✅ Parte 2 Completa!

Você aprendeu como:
- Usar o agente Plan para tarefas complexas de design
- Iterar em planos antes de implementar
- Manter instruções atualizadas com as mudanças
- Escalar a exploração com cloud agents em paralelo
