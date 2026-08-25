<!-- l10n-sync: source-file="workshop/03-quiz-master.md" -->
# Parte 3: Quiz Master Personalizado

[📚 Guia do Lab](GUIDE.md) • [← Parte 2](02-design.md)

---

> ⏱️ **Tempo:** ~10 minutos

Crie seus próprios temas de quiz especializados usando agentes personalizados — fluxos de trabalho que vão além de prompts genéricos de programação.

---

## 🎲 Entendendo Agentes Personalizados

Agentes personalizados são definidos em `.github/agents/` e fornecem:
- **Conhecimento especializado** para tarefas específicas
- **Fluxos de trabalho consistentes** para processos repetíveis
- **Contexto focado** que melhora a qualidade da saída

📄 Confira: `.github/agents/quiz-master.agent.md`

---

## 🎯 Tarefa: Seu Próprio Quiz Master

### Passos

1. No **menu suspenso de modo de chat** (canto inferior esquerdo da entrada de chat), você verá os modos integrados (**Agent**, **Ask**, **Plan**) e os agentes personalizados listados abaixo deles. Selecione **Quiz Master**
2. Certifique-se de que o **menu suspenso de tipo de sessão** mostre **Local**
3. Digite seu tema:
   ```
   Update questions to [YOUR THEME]
   ```
   Ou simplesmente:
   ```
   Update quiz
   ```

5. Revise as perguntas geradas
6. Continue pedindo mais criatividade:
   ```
   Make them more chaotic and unexpected!
   ```
7. Quando estiver satisfeito com o resultado, faça **commit** das perguntas atualizadas

### 🎭 Ideias de Temas

| Categoria | Temas |
|-----------|-------|
| **Profissional** | Skill Bingo, Team Bingo, Work Culture Bingo |
| **Pessoal** | Personality Bingo, Lifestyle Bingo, Travel Bingo |
| **Tech** | Tech Life Bingo, Fandom Bingo, Dev Memes Bingo |
| **Interativo** | Secret Challenge Bingo, Micro-Challenge Bingo, Mystery Bingo |
| **Diversão** | Office Humor Bingo, Chaos Bingo, Opposites Bingo |
| **Profundo** | Deep Chat Bingo, Creative Bingo, Reflective Bingo |

### Descrições dos Temas

- **Skill Bingo** — Habilidades profissionais ou técnicas em vez de fatos pessoais
- **Personality Bingo** — Preferências, manias e características divertidas
- **Secret Challenge Bingo** — Micro-tarefas rápidas com as pessoas que você conhece
- **Team Bingo** — Categorias por departamento ou equipe
- **Tech Life Bingo** — Linguagens de programação, atalhos, frameworks, memes de dev
- **Chaos Bingo** — Prompts surpreendentes, absurdos e imprevisíveis
- **Opposites Bingo** — Encontre alguém que é o seu oposto em eixos específicos

---

## ☁️ Tarefa: Geração de Quiz na Nuvem

Execute o quiz master como um cloud agent para geração assíncrona.

### Passos

> **Se você tem Copilot Pro, Business ou Enterprise:**
>
> 1. No **menu suspenso de modo de chat** (canto inferior esquerdo da entrada de chat), selecione **Quiz Master**
> 2. No **menu suspenso de tipo de sessão** (canto inferior esquerdo), selecione **Cloud**
> 3. Digite um tema diferente:
>    ```
>    Create a Tech Life Bingo with questions about 
>    coding habits, IDE preferences, and developer culture
>    ```
> 4. Deixe rodar em segundo plano
> 5. Revise o PR quando estiver pronto

> **Se você está no plano gratuito (sem acesso ao Cloud):**
>
> 1. No **menu suspenso de modo de chat** (canto inferior esquerdo da entrada de chat), selecione **Quiz Master**
> 2. Mantenha o **menu suspenso de tipo de sessão** configurado como **Local**
> 3. Digite um tema diferente:
>    ```
>    Create a Tech Life Bingo with questions about 
>    coding habits, IDE preferences, and developer culture
>    ```

✅ **Resultado:** O agente personalizado gera perguntas criativas e temáticas enquanto você continua trabalhando.

---

## 📝 Exemplo de Saída: Tech Life Bingo

Veja o que um tema Tech Life pode gerar:

```
┌────────────────────────────────────────────────┐
│  Uses dark mode     │  Has 50+ browser tabs   │
│  for everything     │  open right now         │
├────────────────────────────────────────────────┤
│  Knows vim          │  Has a mechanical       │
│  keybindings        │  keyboard               │
├────────────────────────────────────────────────┤
│  Prefers tabs       │  Has strong opinions    │
│  over spaces        │  about semicolons       │
├────────────────────────────────────────────────┤
│  Uses AI to write   │  Has a dotfiles         │
│  commit messages    │  repository             │
└────────────────────────────────────────────────┘
```

---

## 💡 Dicas

1. **Seja específico** — "Faça perguntas sobre cultura de startups" funciona melhor do que "deixe engraçado"
2. **Itere** — Continue refinando o tom e a criatividade
3. **Misture temas** — "Combine Tech Life com Chaos Bingo" para resultados inesperados
4. **Teste localmente** — Execute o app para ver como as perguntas ficam no grid do bingo

---

## ✅ Parte 3 Completa!

Você aprendeu como:
- Usar agentes personalizados para fluxos de trabalho especializados
- Gerar perguntas de quiz temáticas
- Executar agentes personalizados na nuvem
- Iterar na saída do agente para melhores resultados
