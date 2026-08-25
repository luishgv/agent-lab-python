<!-- l10n-sync: source-file="workshop/03-quiz-master.md" -->
# Parte 3: Quiz Master Personalizado

[📚 Guía del Laboratorio](GUIDE.md) • [← Parte 2](02-design.md)

---

> ⏱️ **Tiempo:** ~10 minutos

Crea tus propios temas de quiz especializados usando agentes personalizados — flujos de trabajo que van más allá de los prompts de codificación genéricos.

---

## 🎲 Entendiendo los Agentes Personalizados

Los agentes personalizados se definen en `.github/agents/` y proporcionan:
- **Conocimiento especializado** para tareas específicas
- **Flujos de trabajo consistentes** para procesos repetibles
- **Contexto enfocado** que mejora la calidad del resultado

📄 Revisa: `.github/agents/quiz-master.agent.md`

---

## 🎯 Tarea: Tu Propio Quiz Master

### Pasos

1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), verás los modos integrados (**Agent**, **Ask**, **Plan**) y los agentes personalizados listados debajo. Selecciona **Quiz Master**
2. Asegúrate de que el **menú desplegable de tipo de sesión** muestre **Local**
3. Ingresa tu tema:
   ```
   Update questions to [YOUR THEME]
   ```
   O simplemente:
   ```
   Update quiz
   ```

5. Revisa las preguntas generadas
6. Continúa pidiendo más creatividad:
   ```
   Make them more chaotic and unexpected!
   ```
7. Cuando estés satisfecho con el resultado, **haz commit** de las preguntas actualizadas

### 🎭 Ideas de Temas

| Categoría | Temas |
|-----------|-------|
| **Professional** | Skill Bingo, Team Bingo, Work Culture Bingo |
| **Personal** | Personality Bingo, Lifestyle Bingo, Travel Bingo |
| **Tech** | Tech Life Bingo, Fandom Bingo, Dev Memes Bingo |
| **Interactive** | Secret Challenge Bingo, Micro-Challenge Bingo, Mystery Bingo |
| **Fun** | Office Humor Bingo, Chaos Bingo, Opposites Bingo |
| **Deep** | Deep Chat Bingo, Creative Bingo, Reflective Bingo |

### Descripciones de Temas

- **Skill Bingo** — Habilidades laborales o técnicas en lugar de datos personales
- **Personality Bingo** — Preferencias, peculiaridades y rasgos divertidos
- **Secret Challenge Bingo** — Micro-tareas rápidas con personas que conoces
- **Team Bingo** — Categorías por departamento o equipo
- **Tech Life Bingo** — Lenguajes de programación, atajos, frameworks, memes de desarrolladores
- **Chaos Bingo** — Prompts sorprendentes, absurdos e impredecibles
- **Opposites Bingo** — Encuentra a alguien que sea tu opuesto en ejes específicos

---

## ☁️ Tarea: Generación de Quiz en la Nube

Ejecuta el quiz master como un cloud agent para generación asíncrona.

### Pasos

> **Si tienes Copilot Pro, Business o Enterprise:**
>
> 1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **Quiz Master**
> 2. En el **menú desplegable de tipo de sesión** (parte inferior izquierda), selecciona **Cloud**
> 3. Ingresa un tema diferente:
>    ```
>    Create a Tech Life Bingo with questions about 
>    coding habits, IDE preferences, and developer culture
>    ```
> 4. Deja que se ejecute en segundo plano
> 5. Revisa el PR cuando esté listo

> **Si estás en el plan gratuito (sin acceso a Cloud):**
>
> 1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **Quiz Master**
> 2. Mantén el **menú desplegable de tipo de sesión** configurado en **Local**
> 3. Ingresa un tema diferente:
>    ```
>    Create a Tech Life Bingo with questions about 
>    coding habits, IDE preferences, and developer culture
>    ```

✅ **Resultado:** El agente personalizado genera preguntas creativas y temáticas mientras tú sigues trabajando.

---

## 📝 Ejemplo de Resultado: Tech Life Bingo

Esto es lo que un tema de Tech Life podría generar:

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

## 💡 Consejos Pro

1. **Sé específico** — "Haz preguntas sobre la cultura startup" funciona mejor que "hazlo gracioso"
2. **Itera** — Continúa pidiendo para refinar el tono y la creatividad
3. **Mezcla temas** — "Combina Tech Life con Chaos Bingo" para resultados inesperados
4. **Prueba localmente** — Ejecuta la aplicación para ver cómo se ven las preguntas en la cuadrícula del bingo

---

## ✅ ¡Parte 3 Completada!

Has aprendido cómo:
- Usar agentes personalizados para flujos de trabajo especializados
- Generar preguntas de quiz temáticas
- Ejecutar agentes personalizados en la nube
- Iterar en el resultado del agente para obtener mejores resultados
