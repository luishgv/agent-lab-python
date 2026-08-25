<!-- l10n-sync: source-file="workshop/01-setup.md" -->
# Parte 1: Configuración y Context Engineering

[📚 Guía del Laboratorio](https://copilot-dev-days.github.io/agent-lab-python/docs/) • [← Visión General](00-overview.md)

---

> ⏱️ **Tiempo:** ~15 minutos

En esta sección, configurarás tu entorno de desarrollo y enseñarás a GitHub Copilot sobre tu código base.

---

## 🔧 Configuración Inicial

### Paso 1: Crea Tu Propio Repositorio (requerido)

1. Abre [github.com/copilot-dev-days/agent-lab-python](https://github.com/copilot-dev-days/agent-lab-python)
2. Haz clic en **Use this template** → **Create a new repository**
   - Nombre: `my-soc-ops-python`
   - Visibilidad: **Public**
3. ✅ ¡Tu propio repositorio de Soc Ops está listo!

### Paso 2: Elige Cómo Abrir Tu Repositorio

Este repositorio incluye un devcontainer listo para usar (`.devcontainer/devcontainer.json`), así que puedes trabajar localmente o en Codespaces.

#### Opción A: Clonar y Abrir en VS Code Local

1. Abre VS Code
2. Ejecuta el comando: `Git: Clone` → `Clone from GitHub`
3. Selecciona tu nuevo repositorio
4. Cuando se te solicite, instala las **extensiones recomendadas**

#### Opción B: Abre Tu Nuevo Repositorio en GitHub Codespaces

1. Abre tu repositorio recién creado en GitHub
2. Haz clic en **Code** → **Codespaces** → **Create codespace on main**
3. Espera a que la configuración termine (el devcontainer ejecuta `uv sync` automáticamente)
4. ✅ Puedes comenzar el laboratorio directamente en la experiencia de VS Code en el navegador

### Paso 3: Ejecuta el Agente de Configuración (ambas opciones)

En el panel de Chat:

```
/setup
```

El agente:
- Detectará tu entorno
- Instalará las dependencias faltantes
- Iniciará el servidor de desarrollo

> ⚠️ **Codespace en el navegador:** Si estás ejecutando la aplicación dentro de un GitHub Codespace a través del navegador (no VS Code Desktop), los estilos e interacciones (por ejemplo, el botón Start Game) podrían no funcionar correctamente debido a la autenticación de puertos privados. Para solucionarlo:
> 1. En el panel **Ports** (barra inferior), haz clic derecho en el puerto `8000` → **Port Visibility** → **Public**
> 2. O abre el Codespace en **VS Code Desktop** (haz clic en el menú hamburguesa `☰` → **Open in VS Code Desktop**)

✅ **Éxito:** ¡La aplicación está ejecutándose en tu navegador!

---

## 📚 Entendiendo Context Engineering

Context engineering es cómo le enseñas a la IA sobre tu código base específico. Esto hace que las sugerencias de Copilot sean más precisas y relevantes.

### Tarea 1: Generar Instrucciones del Workspace

Las instrucciones guían todas las interacciones agénticas, haciéndolas eficientes y confiables.

**Pasos:**

1. Abre la Paleta de Comandos (`Ctrl+Shift+P` / `Cmd+Shift+P`) y ejecuta: `Chat: Generate Agent Instructions`
2. Espera a que el agente analice tu código base
3. Revisa las instrucciones generadas (¡probablemente demasiado detalladas!)
4. Continúa con:
   ```
   Compress down by half and add a mandatory development checklist 
   (lint, build, test) to the top
   ```
5. **Haz commit** del archivo de instrucciones

✅ **Resultado:** Todas las solicitudes futuras tienen un mapa básico de tu workspace.

---

### Tarea 2: Copilot CLI y Cloud Agents para Trabajo en Paralelo

Las sesiones de Copilot CLI se ejecutan en git worktrees aislados, lo cual es perfecto para tareas que no necesitan supervisión constante.

> 💡 **Tres controles de interfaz que debes conocer:**
> - **Nueva sesión (`+`)** (parte superior del panel de Chat) — crea un **New Chat**, **New Chat Editor**, **New Chat Window** o **New Copilot CLI Session**
> - **Menú desplegable de modo de chat** (parte inferior izquierda de la entrada del chat, muestra **Agent** por defecto) — elige un modo (**Agent**, **Ask**, **Plan**) o un agente personalizado
> - **Menú desplegable de tipo de sesión** (parte inferior izquierda de la entrada del chat, muestra **Local** por defecto) — delega o ejecuta en un entorno diferente: **Local**, **Copilot CLI** o **Cloud**

**Inicia una sesión de Copilot CLI:**

1. En el **menú desplegable de tipo de sesión** (parte inferior izquierda, muestra **Local**), selecciona **Copilot CLI**
2. Ingresa:
   ```
   Add linting rules with ruff for unused vars and type hints; fix any errors
   ```
3. Deja que se ejecute, luego **Revisa** y **Aplica** los cambios
4. Haz clic derecho en la sesión para eliminarla cuando termines

**Inicia un Cloud Agent o sesión de Copilot CLI:**

> **Si tienes Copilot Pro, Business o Enterprise:**
>
> 1. En el **menú desplegable de tipo de sesión** (parte inferior izquierda), selecciona **Cloud**
> 2. Ingresa:
>    ```
>    Make the README more engaging as a landing page to the project
>    ```

> **Si estás en el plan gratuito (sin acceso a Cloud):**
>
> 1. En el **menú desplegable de tipo de sesión** (parte inferior izquierda), selecciona **Copilot CLI**
> 2. Ingresa:
>    ```
>    Make the README more engaging as a landing page to the project
>    ```

✅ **Resultado:** Reglas de linting agregadas, errores corregidos, README mejorado -- ¡todo sin interrumpir tu workspace principal!

---

### Tarea 3: Explorar Instrucciones Existentes

Tu repositorio viene con instrucciones preconfiguradas que ayudan a la IA a entender el proyecto.

#### Instrucciones de Utilidades CSS

📄 Consulta `.github/instructions/css-utilities.instructions.md`

Estas documentan las clases de utilidades CSS personalizadas disponibles en este proyecto Python/Jinja2.

> 💡 **Opcional:** Elimina el texto principal y vuelve a ejecutar el prompt para ver cómo se genera

#### Instrucciones de Diseño Frontend

📄 Consulta `.github/instructions/frontend-design.instructions.md`

Las instrucciones de "sin gradientes morados" desafían al agente a pensar como diseñador.

> 💡 **Piensa en:** ¿Qué otros sesgos de la IA podrías desafiar y ajustar?

---

## ✅ ¡Parte 1 Completada!

Has aprendido cómo:
- Configurar tu entorno de desarrollo
- Generar y refinar instrucciones del workspace
- Usar agentes en segundo plano y en la nube para trabajo en paralelo
- Entender archivos de instrucciones existentes
