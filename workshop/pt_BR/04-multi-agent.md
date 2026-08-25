<!-- l10n-sync: source-file="workshop/04-multi-agent.md" -->
# Parte 4: Desenvolvimento Multi-Agente

[📚 Guia do Lab](GUIDE.md) • [← Parte 3](03-quiz-master.md)

---

> ⏱️ **Tempo:** ~20 minutos

Construa novas funcionalidades usando agentes especializados: agentes TDD para código confiável e agentes de design para uma UI bonita.

---

## 🧪 Tarefa 1: Modo Caça ao Tesouro (TDD)

Agentes personalizados com handoffs dividem fluxos de trabalho complexos em etapas menores, mantendo você no controle para decisões críticas.

### Como Funciona o TDD Red → Green → Refactor

Desenvolvimento Orientado a Testes significa escrever testes **antes** de escrever código. Você descreve o que o código *deveria* fazer, observa os testes falharem (porque o código ainda não existe) e então escreve apenas o código suficiente para fazê-los passar. Isso lhe dá confiança de que cada linha de código existe por uma razão.

Cada fase tem seu próprio agente:

| Fase | Agente | O que faz |
|------|--------|-----------|
| **Red** | TDD Red | Escreve testes para a funcionalidade planejada — eles **falham** porque nada foi implementado ainda |
| **Green** | TDD Green | Escreve o **código mínimo** para fazer os testes que estão falhando passarem — sem extras |
| **Refactor** | TDD Refactor | Limpa o código (legibilidade, estrutura) mantendo todos os testes **passando** |

> **Importante para este workshop:** Na Fase 1 abaixo, você vai planejar a funcionalidade mas **não implementá-la**. Dessa forma, quando o TDD Red escrever os testes, eles vão genuinamente falhar — que é exatamente o objetivo.

### O que Vamos Construir

Um novo modo **Scavenger Hunt**:
- Mesmas perguntas do bingo
- Exibidas como uma lista simples com checkboxes
- Medidor de progresso no topo
- Clique para marcar itens como completos

### Passos

#### Fase 1: Planejar

1. No **menu suspenso de modo de chat** (canto inferior esquerdo da entrada de chat), selecione **Plan**
2. Digite:
   ```
   Add a new Scavenger Hunt mode: same questions, but shown as a 
   simple list with checkboxes and a progress meter
   ```
3. **Itere no plano** — verifique se ele:
   - ✅ Adiciona o modo à tela inicial
   - ✅ Cria um novo componente para a visualização em lista
   - ✅ Inclui um indicador de progresso
   - ❌ Não exagera nas funcionalidades
4. Quando estiver satisfeito com o plano, **NÃO clique em Start Implementation** — queremos que os agentes TDD conduzam a implementação

#### Fase 2: TDD Red (Escrever Testes que Falham)

1. Na mesma sessão, abra o **menu suspenso de modo de chat** (canto inferior esquerdo da entrada de chat) e selecione o agente **TDD Red** — isso faz o handoff do contexto da conversa (incluindo seu plano) para o novo agente
2. Digite:
   ```
   Write failing tests for the scavenger hunt feature from the plan above
   ```
3. O agente vai escrever testes para:
   - Renderização de componentes
   - Interações com checkboxes
   - Cálculo de progresso
   - Gerenciamento de estado
4. Os testes devem **todos falhar** já que nenhuma implementação existe ainda — verifique o **Test Explorer** do VS Code para confirmar

#### Fase 3: TDD Green (Fazer os Testes Passarem)

1. Mude para o agente **TDD Green** usando o **menu suspenso de modo de chat**
2. Digite:
   ```
   Make the failing tests pass with minimal implementation
   ```
3. Observe enquanto ele:
   - Implementa o código mínimo para passar nos testes
   - Executa testes após cada mudança
   - Itera até todos os testes passarem

#### Fase 4: Refactor (Limpar o Código)

1. Mude para o agente **TDD Refactor** usando o **menu suspenso de modo de chat**
2. Deixe ele limpar o código mantendo os testes verdes

### Recuperação com Checkpoints

Se algo der errado:
1. Use os **Checkpoints** do Chat para reverter
2. Volte para antes do "TDD Red" começar
3. Tente novamente com prompts ajustados

> 💡 **Bônus:** Experimente o **TDD Supervisor** para um fluxo TDD totalmente automatizado

✅ **Resultado:** Uma funcionalidade de Scavenger Hunt totalmente testada, construída com TDD disciplinado!

---

## 🎴 Tarefa 2: Modo Baralho de Cartas (Design)

Use o agente **Pixel Jam** para focar na iteração de UI enquanto constrói novas funcionalidades.

### O que Vamos Construir

Um novo modo **Card Deck Shuffle**:
- O jogador abre o jogo
- Toca para receber uma carta aleatória
- A carta vira com animação
- Mostra uma pergunta para discussão

### Passos

1. No **menu suspenso de modo de chat** (canto inferior esquerdo da entrada de chat), selecione **Pixel Jam**
2. Digite:
   ```
   New mode: Card Deck Shuffle. Every player opens the game, 
   taps, and gets a random card with a question
   ```
4. Observe enquanto ele itera na UI
5. Continue refinando:
   ```
   Add a cool 3D flip animation when revealing the card
   ```
   ```
   Make the card styling match the cyberpunk theme
   ```
6. **Faça commit** quando estiver satisfeito

### O que o Pixel Jam Faz de Diferente

- Foca no **design visual** primeiro
- Itera na **UI/UX** antes da lógica
- Usa as instruções de design frontend
- Cria interfaces polidas e animadas

---

## 🔍 Tarefa 3: Agente de UI Review

Combine ferramentas MCP, fluxos personalizados e isolamento de subagentes para capacidades poderosas de revisão.

### Passos

1. No **menu suspenso de modo de chat** (canto inferior esquerdo da entrada de chat), selecione **UI Review**
2. Digite:
   ```
   start
   ```
3. Quando solicitado, clique em **Allow for this Workspace** para acesso à ferramenta Playwright
4. Observe enquanto ele:
   - Tira capturas de tela de cada página
   - Analisa problemas de usabilidade
   - Verifica acessibilidade
   - Revisa consistência visual

### O que é Revisado

| Categoria | Verificações |
|-----------|-------------|
| **Usabilidade** | Fluxo de navegação, clareza dos botões, feedback |
| **Acessibilidade** | Contraste de cores, navegação por teclado, leitores de tela |
| **Visual** | Consistência, espaçamento, alinhamento |
| **Interação** | Alvos de toque, estados de hover, animações |

### Ações de Acompanhamento

Após a revisão:
```
File the critical findings as GitHub issues
```
```
Fix the accessibility issues you found
```
```
Assign the navigation bug to a Copilot CLI session
```

✅ **Resultado:** Uma revisão de UX completa com descobertas acionáveis!

---

## 🎯 Desafios Bônus

Se você tiver tempo, tente estes:

| Desafio | Abordagem |
|---------|-----------|
| Corrigir problemas de UX | Delegue para background agent ou cloud agent |
| Múltiplos temas | Adicione seletor de temas à tela inicial |
| Compartilhamento social | Adicione botão de compartilhar ao estado de vitória |
| Placar | Acompanhe e exiba pontuações mais altas |
| Efeitos sonoros | Adicione feedback de áudio para interações |

---

## ✅ Parte 4 Completa!

Você aprendeu como:
- Usar agentes TDD para desenvolvimento orientado a testes
- Construir funcionalidades com o ciclo Red-Green-Refactor
- Usar agentes focados em design como Pixel Jam
- Executar revisões de UX abrangentes
- Combinar múltiplos agentes para fluxos de trabalho complexos

---

## 🎉 Workshop Completo!

Parabéns! Você completou o VS Code GitHub Copilot Agent Lab.

### O que Você Construiu

- ✅ Um app de Social Bingo totalmente redesenhado
- ✅ Temas de quiz personalizados
- ✅ Modo Scavenger Hunt (construído com TDD)
- ✅ Modo Card Deck Shuffle (guiado por design)

### O que Você Aprendeu

1. **Engenharia de Contexto** — Ensinar a IA sobre sua base de código
2. **Primitivas Agênticas** — Background agents, cloud agents e agentes personalizados
3. **Desenvolvimento Design-First** — Iteração de UI com assistência de IA
4. **Desenvolvimento Orientado a Testes** — Código confiável com agentes TDD

### Continue Aprendendo

- 📺 [VS Code no YouTube](https://www.youtube.com/code)
- 📖 [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot/overview)
- 🌟 [Awesome Copilot](https://github.com/github/awesome-copilot)
