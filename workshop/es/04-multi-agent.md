<!-- l10n-sync: source-file="workshop/04-multi-agent.md" -->
# Parte 4: Desarrollo Multi-Agente

[📚 Guía del Laboratorio](GUIDE.md) • [← Parte 3](03-quiz-master.md)

---

> ⏱️ **Tiempo:** ~20 minutos

Construye nuevas funcionalidades usando agentes especializados: agentes TDD para código confiable y agentes de diseño para interfaces hermosas.

---

## 🧪 Tarea 1: Modo Búsqueda del Tesoro (Dirigido por TDD)

Los agentes personalizados con handoffs dividen flujos de trabajo complejos en pasos más pequeños, manteniéndote en control para decisiones críticas.

### Cómo Funciona TDD Red → Green → Refactor

Test-Driven Development significa escribir tests **antes** de escribir código. Describes lo que el código *debería* hacer, observas cómo los tests fallan (porque el código aún no existe), y luego escribes solo el código necesario para que pasen. Esto te da la confianza de que cada línea de código existe por una razón.

Cada fase tiene su propio agente:

| Fase | Agente | Qué hace |
|------|--------|----------|
| **Red** | TDD Red | Escribe tests para la funcionalidad planificada — **fallan** porque nada está implementado aún |
| **Green** | TDD Green | Escribe el **código mínimo** para que los tests que fallan pasen — sin extras |
| **Refactor** | TDD Refactor | Limpia el código (legibilidad, estructura) manteniendo todos los tests **pasando** |

> **Importante para este taller:** En la Fase 1 a continuación, planificarás la funcionalidad pero **no la implementarás**. De esta forma, cuando TDD Red escriba los tests, fallarán genuinamente — que es todo el punto.

### Lo Que Vamos a Construir

Un nuevo modo de **Búsqueda del Tesoro**:
- Las mismas preguntas que el bingo
- Mostradas como una lista simple con casillas de verificación
- Medidor de progreso en la parte superior
- Haz clic para marcar elementos como completados

### Pasos

#### Fase 1: Plan

1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **Plan**
2. Ingresa:
   ```
   Add a new Scavenger Hunt mode: same questions, but shown as a 
   simple list with checkboxes and a progress meter
   ```
3. **Itera en el plan** — verifica que:
   - ✅ Agrega el modo a la pantalla de inicio
   - ✅ Crea un nuevo componente para la vista de lista
   - ✅ Incluye un indicador de progreso
   - ❌ No se excede con funcionalidades
4. Una vez que estés satisfecho con el plan, **NO hagas clic en Start Implementation** — queremos que los agentes TDD dirijan la implementación

#### Fase 2: TDD Red (Escribir Tests que Fallen)

1. En la misma sesión, abre el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat) y selecciona el agente **TDD Red** — esto transfiere el contexto de la conversación (incluyendo tu plan) al nuevo agente
2. Ingresa:
   ```
   Write failing tests for the scavenger hunt feature from the plan above
   ```
3. El agente escribirá tests para:
   - Renderizado de componentes
   - Interacciones con casillas de verificación
   - Cálculo de progreso
   - Gestión de estado
4. Los tests deberían **fallar todos** ya que no existe implementación aún — verifica en el **Test Explorer** de VS Code para confirmar

#### Fase 3: TDD Green (Hacer que los Tests Pasen)

1. Cambia al agente **TDD Green** usando el **menú desplegable de modo de chat**
2. Ingresa:
   ```
   Make the failing tests pass with minimal implementation
   ```
3. Observa cómo:
   - Implementa el código mínimo para pasar los tests
   - Ejecuta los tests después de cada cambio
   - Itera hasta que todos los tests pasen

#### Fase 4: Refactor (Limpiar)

1. Cambia al agente **TDD Refactor** usando el **menú desplegable de modo de chat**
2. Deja que limpie el código mientras mantiene los tests en verde

### Recuperación con Checkpoints

Si algo sale mal:
1. Usa los **Checkpoints** del Chat para revertir
2. Reinicia al punto antes de que "TDD Red" comenzara
3. Intenta de nuevo con prompts ajustados

> 💡 **Bonus:** Prueba **TDD Supervisor** para un flujo TDD completamente automatizado

✅ **Resultado:** ¡Una funcionalidad de Búsqueda del Tesoro completamente testeada construida con TDD disciplinado!

---

## 🎴 Tarea 2: Modo Baraja de Cartas (Dirigido por Diseño)

Usa el agente **Pixel Jam** para enfocarte en la iteración de la interfaz mientras construyes nuevas funcionalidades.

### Lo Que Vamos a Construir

Un nuevo modo de **Baraja de Cartas**:
- El jugador abre el juego
- Toca para obtener una carta aleatoria
- La carta se voltea con animación
- Muestra una pregunta para discutir

### Pasos

1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **Pixel Jam**
2. Ingresa:
   ```
   New mode: Card Deck Shuffle. Every player opens the game, 
   taps, and gets a random card with a question
   ```
4. Observa cómo itera en la interfaz
5. Continúa refinando:
   ```
   Add a cool 3D flip animation when revealing the card
   ```
   ```
   Make the card styling match the cyberpunk theme
   ```
6. **Haz commit** cuando estés satisfecho

### Lo Que Pixel Jam Hace Diferente

- Se enfoca en el **diseño visual** primero
- Itera en **UI/UX** antes que en la lógica
- Usa las instrucciones de diseño frontend
- Crea interfaces pulidas y animadas

---

## 🔍 Tarea 3: Agente de Revisión de UX

Combina herramientas MCP, flujos de trabajo personalizados y aislamiento de subagentes para capacidades de revisión potentes.

### Pasos

1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **UI Review**
2. Ingresa:
   ```
   start
   ```
3. Cuando se te solicite, haz clic en **Allow for this Workspace** para acceder a la herramienta Playwright
4. Observa cómo:
   - Toma capturas de pantalla de cada página
   - Analiza problemas de usabilidad
   - Verifica accesibilidad
   - Revisa consistencia visual

### Lo Que Se Revisa

| Categoría | Verificaciones |
|-----------|----------------|
| **Usabilidad** | Flujo de navegación, claridad de botones, retroalimentación |
| **Accesibilidad** | Contraste de colores, navegación por teclado, lectores de pantalla |
| **Visual** | Consistencia, espaciado, alineación |
| **Interacción** | Objetivos táctiles, estados hover, animaciones |

### Acciones de Seguimiento

Después de la revisión:
```
File the critical findings as GitHub issues
```
```
Fix the accessibility issues you found
```
```
Assign the navigation bug to a Copilot CLI session
```

✅ **Resultado:** ¡Una revisión integral de UX con hallazgos accionables!

---

## 🎯 Desafíos Bonus

Si tienes tiempo, prueba estos:

| Desafío | Enfoque |
|---------|---------|
| Corregir problemas de UX | Delegar a un agente en segundo plano o en la nube |
| Múltiples temas | Agregar selector de temas a la pantalla de inicio |
| Compartir en redes | Agregar botón de compartir al estado de victoria |
| Tabla de clasificación | Rastrear y mostrar puntuaciones altas |
| Efectos de sonido | Agregar retroalimentación de audio para interacciones |

---

## ✅ ¡Parte 4 Completada!

Has aprendido cómo:
- Usar agentes TDD para desarrollo guiado por tests
- Construir funcionalidades con el ciclo Red-Green-Refactor
- Usar agentes enfocados en diseño como Pixel Jam
- Ejecutar revisiones integrales de UX
- Combinar múltiples agentes para flujos de trabajo complejos

---

## 🎉 ¡Taller Completado!

¡Felicidades! Has completado el Laboratorio de Agentes de GitHub Copilot en VS Code.

### Lo Que Construiste

- ✅ Una aplicación de Bingo Social completamente rediseñada
- ✅ Temas de quiz personalizados
- ✅ Modo Búsqueda del Tesoro (construido con TDD)
- ✅ Modo Baraja de Cartas (dirigido por diseño)

### Lo Que Aprendiste

1. **Context Engineering** — Enseñar a la IA sobre tu código base
2. **Primitivas Agénticas** — Agentes en segundo plano, en la nube y personalizados
3. **Desarrollo Orientado al Diseño** — Iteración de interfaz con asistencia de IA
4. **Desarrollo Guiado por Tests** — Código confiable con agentes TDD

### Sigue Adelante

- 📺 [VS Code on YouTube](https://www.youtube.com/code)
- 📖 [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot/overview)
- 🌟 [Awesome Copilot](https://github.com/github/awesome-copilot)
