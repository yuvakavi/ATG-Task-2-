"""Simple video generator using MoviePy to create actual MP4 videos"""
import os
from moviepy import ImageClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class SimpleVideoGenerator:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def create_text_clip(self, text, duration=3, size=(1920, 1080), bg_color=(30, 30, 50), 
                        text_color=(255, 255, 255), font_size=60, is_title=False):
        """Create a text clip with given parameters"""
        # Create image with text
        img = Image.new('RGB', size, color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a nice font, fall back to default
        try:
            if is_title:
                font = ImageFont.truetype("arialbd.ttf", font_size)  # Bold for titles
            else:
                font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        # Word wrap text - split into lines
        words = text.split()
        lines = []
        current_line = []
        max_chars = 35 if is_title else 45  # Shorter lines for titles
        
        for word in words:
            current_line.append(word)
            test_line = ' '.join(current_line)
            if len(test_line) > max_chars:
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(test_line)
                    current_line = []
        
        if current_line:
            lines.append(' '.join(current_line))
        
        # Calculate positioning
        line_height = font_size + 25
        total_height = len(lines) * line_height
        start_y = (size[1] - total_height) // 2
        
        # Draw each line centered
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            
            # Center text horizontally
            x = (size[0] - text_width) // 2
            y = start_y + i * line_height
            
            draw.text((x, y), line, fill=text_color, font=font)
        
        # Convert PIL image to numpy array
        img_array = np.array(img)
        
        # Create video clip from image (no fade effects)
        return ImageClip(img_array, duration=duration)
    
    def generate_video(self, topic, script, scenes, output_filename=None):
        """Generate a simple video with text scenes"""
        if output_filename is None:
            output_filename = f"{topic.replace(' ', '_')}_video.mp4"
        
        output_path = os.path.join(self.output_dir, output_filename)
        
        # Create clips for each scene
        clips = []
        
        # ONLY show the topic - no bullet points, no content scenes
        title_clip = self.create_text_clip(
            topic,
            duration=5,  # Show topic for 5 seconds
            bg_color=(20, 30, 60),
            font_size=90,
            is_title=True
        )
        clips.append(title_clip)
        
        # That's it! Just the topic, nothing else
        final_video = clips[0]  # Only one clip - the topic
        
        # Write video file
        final_video.write_videofile(
            output_path,
            fps=24,
            codec='libx264',
            audio=False,
            preset='ultrafast'
        )
        
        # Clean up
        final_video.close()
        
        return {
            'video_path': output_path,
            'duration': final_video.duration,
            'scene_count': 1  # Only the topic
        }
    
    def generate_from_analysis(self, topic, script, pattern_analysis):
        """Generate video from pattern analysis"""
        scenes = pattern_analysis.get('recommended_scenes', [])
        
        if not scenes:
            # Create default scenes from script
            sentences = script.split('. ')
            scenes = [
                {
                    'type': 'content',
                    'visual': sent.strip(),
                    'duration': 4
                }
                for sent in sentences[:5]  # First 5 sentences
                if sent.strip()
            ]
        
        return self.generate_video(topic, script, scenes)
