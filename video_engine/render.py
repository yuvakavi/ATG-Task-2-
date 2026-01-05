import os

def render_video():
    os.system("manim -pql video_engine/manim_scenes.py ExplainerScene")

if __name__ == "__main__":
    render_video()
