import gradio as gr
import os
import shutil
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from neoforge.crew import EngineeringTeam

OUTPUT_DIR = "output"

def run_engineering_process(requirements: str):
    """Run engineering crew with user requirements and prepare downloadable output."""
    # Initialize crew
    team = EngineeringTeam()

    # Run process with user input
    result = team.run_with_requirements(requirements)

    # Create session-specific output copy
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_output_dir = os.path.join(OUTPUT_DIR, f"session_{timestamp}")
    os.makedirs(session_output_dir, exist_ok=True)

    # Copy current output files into session directory
    for filename in os.listdir(OUTPUT_DIR):
        src = os.path.join(OUTPUT_DIR, filename)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(session_output_dir, filename))

    # Create downloadable zip
    zip_path = f"{session_output_dir}.zip"
    shutil.make_archive(session_output_dir, 'zip', session_output_dir)

    return result, zip_path

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## NeoForge \nEnter your requirements and let the NeoForge work.")

    with gr.Row():
        input_box = gr.Textbox(
            label="User Requirements",
            placeholder="e.g., Build a REST API with authentication and data validation...",
            lines=4
        )

    result_box = gr.Textbox(label="Result Summary", lines=10)
    download_link = gr.File(label="Download Output ZIP")

    run_button = gr.Button("Run NeoForge")

    run_button.click(
        fn=run_engineering_process,
        inputs=input_box,
        outputs=[result_box, download_link]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
