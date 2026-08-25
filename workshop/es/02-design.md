<!-- l10n-sync: source-file="workshop/02-design.md" -->
# Parte 2: Desarrollo Frontend Orientado al Diseño

[📚 Guía del Laboratorio](https://copilot-dev-days.github.io/agent-lab-python/docs/) • [← Parte 1](01-setup.md)

---

> ⏱️ **Tiempo:** ~15 minutos

Ahora que el contexto de tu repositorio está diseñado, ¡seamos creativos! Rediseñarás toda la interfaz usando desarrollo asistido por IA.

---

## 🎨 Tarea 1: Hazlo Tuyo

Usa el agente **Plan** para iniciar cualquier elemento de trabajo más grande. ¡Itera en el plan (2+ veces!) con ajustes y aclaraciones.

### Pasos

1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **Plan**
2. Asegúrate de que el **menú desplegable de tipo de sesión** muestre **Local** (si tu sesión anterior fue Cloud, cámbialo de vuelta)
3. Ingresa tu visión:
   ```
   Let's do a full redesign. Make it [YOUR THEME]
   ```
4. Revisa el plan generado
5. Pide ajustes hasta que estés satisfecho
6. Haz clic en **Start Implementation** para ejecutar

### 🎭 Ideas de Temas

Elige uno que te inspire:

| Categoría | Temas |
|-----------|-------|
| **Minimal** | Minimalist Mono, Scandinavian Calm, Desert Sand Minimal |
| **Retro** | Retro Terminal Green, Pixel Arcade Style, Vaporwave Sunset |
| **Dark** | Cyberpunk Neon, Dark Mode Noir, Space Galaxy Glow |
| **Playful** | Playful Candy Pop, Toybox Primary Colors, Anime Bubble |
| **Professional** | Corporate Clean Blue, Gradient Glass UI, Metallic Chrome |
| **Creative** | Brutalist Blocks, Geometric Memphis, Bold Constructivist |
| **Cozy** | Cozy Coffee Shop, Soft Pastel Clouds, Notebook Doodle |
| **Unique** | Skeuomorphic Stickers, Paper Card Cutouts, Chalkboard |

✅ **Resultado:** Las instrucciones de frontend y utilidades CSS se combinan para construir un diseño hermoso.

---

## 📝 Tarea 2: Mantén las Instrucciones Actualizadas

Cuando hagas cambios importantes en la arquitectura, diseño o dependencias, ¡actualiza tus instrucciones!

### Pasos

1. Después de tu rediseño, continúa con:
   ```
   Add a design guide section to copilot-instructions.md
   ```
2. Revisa los cambios
3. **Haz commit y push**

---

## 🚀 Tarea 3: Escala la Exploración con Cloud Agents

Genera múltiples variaciones de diseño en paralelo usando cloud agents.

> **Si tienes Copilot Pro, Business o Enterprise:**
>
> 1. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **Plan**
> 2. Ingresa:
>    ```
>    Redesign the start screen as a more engaging landing page
>    ```
> 3. Observa las variaciones sugeridas en el plan
> 4. Ejecuta el prompt de exploración:
>    ```
>    /cloud-explore design variations
>    ```
>    📄 Consulta `.github/prompts/cloud-explore.prompt.md`
>
> 5. Revisa **Agent Sessions** para seguir los 3 nuevos cloud agents
> 6. Haz clic en cualquier sesión para seguir el progreso o abrir en la web

> **Si estás en el plan gratuito (sin acceso a Cloud):**
>
> 1. Usa el modo **Autopilot** o una sesión local de **Plan** para explorar una variación de diseño a la vez
> 2. En el **menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat), selecciona **Plan**
> 3. Ingresa:
>    ```
>    Redesign the start screen as a more engaging landing page
>    ```
> 4. Revisa e implementa el plan, luego repite con una dirección diferente

### Lo Que Está Sucediendo

El prompt inicia **3 cloud agents en paralelo**, cada uno explorando una dirección de diseño diferente. Ellos:
- Crearán ramas
- Implementarán variaciones
- Tomarán capturas de pantalla
- Abrirán PRs para tu revisión

✅ **Resultado:** ¡3 variaciones de diseño para comparar, todas ejecutándose en paralelo!

> ⏰ Esto toma unos minutos. Continúa con la Parte 3 mientras se ejecutan.

---

## ✅ ¡Parte 2 Completada!

Has aprendido cómo:
- Usar el agente Plan para tareas de diseño complejas
- Iterar en planes antes de implementar
- Mantener las instrucciones actualizadas con los cambios
- Escalar la exploración con cloud agents en paralelo
