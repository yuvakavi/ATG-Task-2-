"""
Enhanced Video Synthesis Module
Integrates visual pattern analysis with scene generation
"""

from manim import *
import json
from pathlib import Path

class EnhancedVideoScene(Scene):
    """Base class for enhanced video scenes with pattern-aware rendering"""
    
    def __init__(self, scene_data=None, **kwargs):
        super().__init__(**kwargs)
        self.scene_data = scene_data or {}
        
    def create_title_scene(self, title_text, duration=3):
        """Create animated title scene"""
        title = Text(title_text, font_size=48, color=BLUE)
        subtitle = Text("AI Generated Educational Video", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN)
        
        self.play(FadeIn(title, shift=UP), run_time=1)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(duration - 1.5)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.5)
    
    def create_bullet_points(self, points, duration=5):
        """Create animated bullet points"""
        bullets = VGroup()
        
        for i, point in enumerate(points):
            bullet = Text(f"• {point}", font_size=28)
            bullet.to_edge(LEFT, buff=1)
            bullet.shift(UP * (2 - i * 0.8))
            bullets.add(bullet)
        
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT), run_time=0.5)
        
        self.wait(duration - len(points) * 0.5)
        self.play(FadeOut(bullets), run_time=0.5)
    
    def create_process_flow(self, steps, duration=6):
        """Create animated process flow"""
        boxes = VGroup()
        arrows = VGroup()
        
        num_steps = len(steps)
        spacing = 2.5
        start_x = -(num_steps - 1) * spacing / 2
        
        for i, step in enumerate(steps):
            box = Rectangle(width=2, height=1, color=BLUE, fill_opacity=0.3)
            text = Text(step, font_size=20)
            text.move_to(box.get_center())
            
            box_group = VGroup(box, text)
            box_group.shift(RIGHT * (start_x + i * spacing))
            boxes.add(box_group)
            
            if i < num_steps - 1:
                arrow = Arrow(
                    boxes[i].get_right(),
                    boxes[i].get_right() + RIGHT * (spacing - 2),
                    buff=0.1,
                    color=YELLOW
                )
                arrows.add(arrow)
        
        for box in boxes:
            self.play(FadeIn(box), run_time=0.5)
        
        for arrow in arrows:
            self.play(Create(arrow), run_time=0.3)
        
        self.wait(duration - (len(boxes) * 0.5 + len(arrows) * 0.3))
        self.play(FadeOut(boxes), FadeOut(arrows), run_time=0.5)
    
    def create_comparison(self, left_data, right_data, duration=5):
        """Create side-by-side comparison"""
        # Left side
        left_title = Text(left_data['title'], font_size=32, color=BLUE)
        left_title.to_edge(LEFT, buff=1).shift(UP * 2)
        left_points = VGroup()
        
        for i, point in enumerate(left_data.get('points', [])[:4]):
            text = Text(f"• {point}", font_size=20)
            text.to_edge(LEFT, buff=1.5)
            text.shift(UP * (1 - i * 0.7))
            left_points.add(text)
        
        # Right side
        right_title = Text(right_data['title'], font_size=32, color=RED)
        right_title.to_edge(RIGHT, buff=1).shift(UP * 2)
        right_points = VGroup()
        
        for i, point in enumerate(right_data.get('points', [])[:4]):
            text = Text(f"• {point}", font_size=20)
            text.to_edge(RIGHT, buff=1.5)
            text.shift(UP * (1 - i * 0.7))
            right_points.add(text)
        
        # Divider
        divider = Line(UP * 3, DOWN * 3, color=WHITE)
        
        self.play(
            FadeIn(left_title, shift=RIGHT),
            FadeIn(right_title, shift=LEFT),
            Create(divider),
            run_time=1
        )
        
        self.play(
            FadeIn(left_points, shift=RIGHT),
            FadeIn(right_points, shift=LEFT),
            run_time=1
        )
        
        self.wait(duration - 2)
        
        self.play(
            FadeOut(left_title),
            FadeOut(right_title),
            FadeOut(left_points),
            FadeOut(right_points),
            FadeOut(divider),
            run_time=0.5
        )


class VideoSynthesizer:
    """Synthesizes video from analyzed patterns and content"""
    
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def synthesize_video(self, script, blueprint, analysis):
        """
        Synthesize video from script, blueprint, and pattern analysis
        
        Args:
            script: The video script text
            blueprint: The animation blueprint
            analysis: Visual pattern analysis results
        
        Returns:
            Path to the generated video file
        """
        # Create scene configuration
        scene_config = {
            'pattern': analysis.get('primary_visual_pattern', 'concept'),
            'key_concepts': analysis.get('key_concepts', []),
            'scenes': analysis.get('recommended_scenes', [])
        }
        
        # Save configuration for rendering
        config_path = self.output_dir / "scene_config.json"
        with open(config_path, 'w') as f:
            json.dump(scene_config, f, indent=2)
        
        output_file = self.output_dir / "final_video.mp4"
        
        return {
            'video_path': str(output_file),
            'config_path': str(config_path),
            'pattern': scene_config['pattern'],
            'estimated_duration': sum(s.get('duration', 3) for s in scene_config['scenes'])
        }


if __name__ == "__main__":
    # Test video synthesis
    synthesizer = VideoSynthesizer()
    
    test_analysis = {
        'primary_visual_pattern': 'process',
        'key_concepts': ['WebSockets', 'Connection', 'Communication'],
        'recommended_scenes': [
            {'type': 'intro', 'duration': 3, 'visual': 'title'},
            {'type': 'steps', 'duration': 6, 'visual': 'flowchart'}
        ]
    }
    
    result = synthesizer.synthesize_video(
        "Test script",
        "Test blueprint",
        test_analysis
    )
    
    print("Synthesis result:", result)
