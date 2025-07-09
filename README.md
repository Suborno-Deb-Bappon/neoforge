# Neora

**Neora** is an **Autonomous Multi-Agent System** that transforms software requirements into **production-ready backend modules, frontend UIs, and unit tests**. It leverages **CrewAI** for multi-agent orchestration and **Gradio** for UI generation, empowering developers to rapidly prototype and automate the creation of entire software stacks.

---

## ✨ Features

- 🤖 Multi-agent collaboration using [CrewAI](https://docs.crewai.com/)
- 🧠 Task orchestration from human-readable YAML definitions
- 🎨 Automatic frontend UI generation with [Gradio](https://www.gradio.app/)
- 🏗️ Backend module scaffolding (Flask/Django-compatible structure)
- ✅ Built-in unit test generation
- ⚙️ Custom tools integration (e.g., for API calls, code templates)
- 🔄 Fully extensible for custom workflows

---

## 🗂️ Project Structure

## 🗂️ Project Structure

![Neora Project Structure](pstructure.png)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/neora.git
cd neora
```

### 2. Create a Virtual Environment
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Application
```
python src/neora/main.py
```

## 🧩 Configuration
Neora is configured using two YAML files:

    - config/agents.yaml: Defines the autonomous agents (roles, tools, goals).

    - config/tasks.yaml: Defines task flow and orchestration logic.

Update these files to reflect your software requirements and custom logic.

## 🧪 Running Tests
```bash
pytest tests/
```

## 🐳 Docker Usage
Build and run Neora inside a container:
```
docker build -t neora .
docker run -it neora
```
## 📦 Packaging
Neora follows standard Python packaging structure using pyproject.toml.

## 🙋‍♂️ Contributing
PRs are welcome! Please open an issue first to discuss your feature idea or bug fix.