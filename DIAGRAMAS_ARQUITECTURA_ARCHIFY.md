# 📐 Diagramas de Arquitectura y Flujo (Skill Archify)
## Libro: *"Usa la IA y Trabaja Menos"*
*Colección completa de esquemas visuales para documentación, diapositivas y material gráfico del e-Book.*

---

### 1. Figura 0.1: Transformación del Empresario (De Esclavo Operativo a Director de Sistemas)

```mermaid
flowchart LR
    subgraph Pasado ["❌ Modelo Tradicional (Operador Saturado)"]
        A1["👤 Dueño / Emprendedor"] -->|14 horas/día| A2["🔥 Apaga fuegos"]
        A2 --> A3["📝 Tareas manuales repetitivas"]
        A3 --> A4["⏳ Cuello de botella del negocio"]
    end

    subgraph Futuro ["✅ Modelo Apalancado (Director de Sistemas)"]
        B1["👑 Director de Sistemas"] -->|Supervisión & Estrategia| B2["🧠 Copilotos de IA (Costo marginal $0)"]
        B2 --> B3["⚙️ Flujos 24/7 & Agentes"]
        B3 --> B4["📈 Escala sin aumentar costos fijos"]
    end

    Pasado -.->|Adopción de IA| Futuro

    classDef redStyle fill:#450a0a,stroke:#ef4444,stroke-width:2px,color:#fecaca;
    classDef greenStyle fill:#022c22,stroke:#10b981,stroke-width:2px,color:#a7f3d0;

    class A1,A2,A3,A4 redStyle;
    class B1,B2,B3,B4 greenStyle;
```

---

### 2. Figura 1.1: La Pirámide del Apalancamiento Cognitivo en la PYME

```mermaid
flowchart TD
    N3["🥇 NIVEL 3: Agentes y Sistemas Autónomos<br/>• Flujos multi-paso 24/7 (Make, n8n, Webhooks)<br/>• Cotizaciones automáticas, agendamiento y cobros<br/>• <i>Impacto: Crecimiento exponencial sin aumentar nómina</i>"]
    
    N2["🥈 NIVEL 2: Asistentes Documentales & Segundo Cerebro<br/>• Bases privadas RAG (NotebookLM)<br/>• Consultas inmediatas sobre manuales, contratos y tarifas<br/>• <i>Impacto: Reducción del 90% en interrupciones internas</i>"]
    
    N1["🥉 NIVEL 1: Tareas y Redacción Básica<br/>• LLMs para redacción de correos, copies y resúmenes<br/>• Transcripción de minutas de juntas a texto<br/>• <i>Impacto: Ahorro de 5 a 7 horas semanales por colaborador</i>"]

    N1 --> N2 --> N3

    classDef l1 fill:#1e293b,stroke:#94a3b8,stroke-width:2px,color:#fff;
    classDef l2 fill:#0f3959,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef l3 fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#fff;

    class N1 l1;
    class N2 l2;
    class N3 l3;
```

---

### 3. Figura 2.1: Anatomía del Prompt Perfecto (Framework R.C.E.F.)

```mermaid
flowchart TD
    subgraph RCEF ["🎯 Estructura Maestra del Prompt R.C.E.F."]
        R["👤 1. ROL (Identidad Experta)<br/>'Actúa como un Director de Cobranza Senior...'"]
        C["🏢 2. CONTEXTO (Datos y Situación)<br/>'Cliente con 15 días de atraso en factura de $2,500 USD...'"]
        E["⚡ 3. EJECUCIÓN (Instrucción Precisa)<br/>'Redacta un correo de recordatorio cordial pero firme...'"]
        F["📄 4. FORMATO (Estructura de Salida)<br/>'Asunto claro + 3 párrafos cortos + CTA de pago...'"]
        L["🛡️ 5. LÍMITES & RESTRICCIONES<br/>'Sin amenazas legales, tono profesional y empático...'"]
    end

    R --> C --> E --> F --> L

    classDef rcefStyle fill:#0f172a,stroke:#6366f1,stroke-width:2px,color:#fff;
    class R,C,E,F,L rcefStyle;
```

---

### 4. Figura 3.1: Arquitectura del Segundo Cerebro Empresarial (NotebookLM / RAG)

```mermaid
flowchart LR
    subgraph Sources ["📂 Fuentes Oficiales de la PYME"]
        Doc1["📄 Manuales de Procesos"]
        Doc2["📑 Tarifarios & Políticas"]
        Doc3["📝 Contratos & Garantías"]
        Doc4["🎙️ Transcripciones de Juntas"]
    end

    subgraph RAG_Engine ["🧠 Motor RAG Privado (NotebookLM)"]
        Index["🔒 Indexación Semántica Privada<br/>(Cero entrenamiento en modelos públicos)"]
        Cite["📌 Anclaje Estricto a Fuentes<br/>(Citas a párrafos exactos)"]
    end

    subgraph Users ["👥 Equipo de Trabajo"]
        Staff["💼 Asesores de Ventas / Soporte"]
        Resp["⚡ Respuesta en 5 seg<br/>(100% libre de alucinaciones)"]
    end

    Sources --> Index
    Index --> Cite
    Staff -->|Pregunta en lenguaje natural| Cite
    Cite -->|Respuesta verificada| Resp

    classDef srcStyle fill:#1e293b,stroke:#94a3b8,stroke-width:1px,color:#fff;
    classDef ragStyle fill:#0c4a6e,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef userStyle fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#fff;

    class Doc1,Doc2,Doc3,Doc4 srcStyle;
    class Index,Cite ragStyle;
    class Staff,Resp userStyle;
```

---

### 5. Figura 4.1: Flujo de Ventas Automatizado en WhatsApp (Caso Inmobiliario / Comercial)

```mermaid
sequenceDiagram
    autonumber
    actor Cliente as 📱 Cliente / Lead
    participant WA as 💬 WhatsApp / ManyChat
    participant Bot as 🤖 Agente IA (n8n + LLM)
    participant Cal as 📅 Google Calendar
    participant CRM as 📊 CRM / Asesor Humano

    Cliente->>WA: "Hola, me interesa información de un departamento"
    WA->>Bot: Dispara webhook de nuevo mensaje
    Bot->>Bot: Evalúa presupuesto, zona y fecha de mudanza
    alt Lead Calificado
        Bot->>Cal: Consulta disponibilidad de citas en tiempo real
        Bot->>Cliente: "Tenemos espacio el jueves a las 4 PM o viernes a las 11 AM. ¿Cuál te queda mejor?"
        Cliente->>Bot: "Viernes a las 11 AM"
        Bot->>Cal: Agenda cita y bloquea horario
        Bot->>CRM: Crea ficha de prospecto con resumen de necesidades
        Bot->>Cliente: "¡Listo! Cita confirmada. Tu asesor Juan te esperará en la sala de ventas."
    else Lead No Calificado / Fuera de Rango
        Bot->>Cliente: Envía catálogo digital y opciones de financiamiento
    end
```

---

### 6. Figura 5.1: Flujo de Cotización Autónomo en 3 Minutos

```mermaid
flowchart TD
    In["📝 Cliente llena formulario web"] --> Trigger["⚡ Webhook (Make / n8n)"]
    Trigger --> Calc["🤖 Agente IA calcula costos según tarifas vigentes"]
    Calc --> PDF["📄 Genera PDF formal de cotización con marca"]
    PDF --> Mail["📧 Envía email automático con enlace de pago / aceptación"]
    Mail --> Check{"¿Acepta cotización?"}
    Check -- Sí --> Stripe["💳 Genera orden de cobro en Stripe / Terminal"]
    Check -- Sin respuesta 48h --> FollowUp["📲 Agente envía mensaje de seguimiento suave"]

    classDef autoStyle fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef decisionStyle fill:#312e81,stroke:#a855f7,stroke-width:2px,color:#fff;
    class In,Trigger,Calc,PDF,Mail,Stripe,FollowUp autoStyle;
    class Check decisionStyle;
```

---

### 7. Figura 6.1: El Semáforo de Privacidad & Protocolo Human-in-the-Loop

```mermaid
flowchart TD
    subgraph Semaforo ["🚦 Semáforo de Clasificación de Datos"]
        Verde["🟢 VERDE (Seguro para IA Pública)<br/>• Textos comerciales, artículos de blog, correos genéricos<br/>• Dudas conceptuales y lluvia de ideas"]
        Amarillo["🟡 AMARILLO (Requiere Anonimización)<br/>• Cotizaciones (remueve nombre del cliente y montos exactos)<br/>• Transcripciones de minutas (reemplaza datos personales)"]
        Rojo["🔴 ROJO (PROHIBIDO en Modelos Públicos)<br/>• Contraseñas, claves bancarias y tokens de API<br/>• Expedientes médicos y secretos industriales<br/><i>(Usar solo en entornos locales o RAG privado auditado)</i>"]
    end

    subgraph HITL ["🛡️ Protocolo Human-in-the-Loop"]
        Draft["🤖 IA genera borrador inicial (80% del trabajo pesado)"] --> Audit["👁️ Humano audita datos clave y tono de marca (20%)"] --> Send["🚀 Aprobación y envío final"]
    end

    classDef gStyle fill:#064e3b,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef yStyle fill:#713f12,stroke:#eab308,stroke-width:2px,color:#fff;
    classDef rStyle fill:#450a0a,stroke:#ef4444,stroke-width:2px,color:#fff;
    classDef hitlStyle fill:#1e1b4b,stroke:#818cf8,stroke-width:2px,color:#fff;

    class Verde gStyle;
    class Amarillo yStyle;
    class Rojo rStyle;
    class Draft,Audit,Send hitlStyle;
```

---

### 8. Figura 7.1: Hoja de Ruta de Transformación en 14 Días

```mermaid
gantt
    title Cronograma de Implementación Táctico en 14 Días
    dateFormat  D
    axisFormat  Día %d

    section Fase 1: Cimientos
    Día 1: Auditoría de Tiempo y Retorno Cognitivo :a1, 1, 1d
    Día 2: Selección de los 3 Dolores Operativos    :a2, after a1, 1d
    Día 3: Configurar Semáforo de Seguridad         :a3, after a2, 1d
    Día 4: Biblioteca de Prompts R.C.E.F.           :a4, after a3, 1d

    section Fase 2: Segundo Cerebro
    Día 5: Recopilar Manuales y Políticas           :b1, after a4, 1d
    Día 6: Cargar Base RAG en NotebookLM            :b2, after b1, 1d
    Día 7: Pruebas de Estrés y Validación           :b3, after b2, 1d

    section Fase 3: Agentes & ROI
    Días 8-10: Construcción de Flujo No-Code + HITL :c1, after b3, 3d
    Días 11-14: Lanzamiento Piloto y Medición de ROI:c2, after c1, 4d
```
