from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import yaml
import os
import re

@CrewBase
class EngineeringTeam():
    """EngineeringTeam crew"""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    agents_config_path = os.path.join(BASE_DIR, 'config', 'agents.yaml')
    tasks_config_path = os.path.join(BASE_DIR, 'config', 'tasks.yaml')

    def __init__(self):
        with open(self.agents_config_path, 'r') as af:
            self.agents_config = yaml.safe_load(af)

        with open(self.tasks_config_path, 'r') as tf:
            self.tasks_config = yaml.safe_load(tf)


    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['engineering_lead'],
            verbose=True,
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=500,
            max_retry_limit=3
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            verbose=True,
        )

    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=500,
            max_retry_limit=3
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task']
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task']
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task']
        )

    @task
    def test_task(self) -> Task:
        return Task(
            config=self.tasks_config['test_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
    

    @staticmethod
    def extract_module_name(requirements: str) -> str:
        
        match = re.search(r"(?:called|named)\s+['\"]?(\w+)['\"]?", requirements, re.IGNORECASE)
        if match:
            return match.group(1)

        
        match = re.search(r"(?:module|class)\s+([A-Za-z_]\w*)", requirements, re.IGNORECASE)
        if match:
            return match.group(1).lower()

        
        return "module"


    def run_with_requirements(self, requirements: str):
        module_name = self.extract_module_name(requirements)
        class_name = module_name.capitalize()

        inputs = {
            "requirements": requirements,
            "module_name": module_name,
            "class_name": class_name
        }

        crew_instance = self.crew()
        result = crew_instance.kickoff(inputs=inputs)

        result_text = str(result)
        os.makedirs("output", exist_ok=True)
        with open("output/result.txt", "w", encoding="utf-8") as f:
            f.write(result_text)

        return result_text