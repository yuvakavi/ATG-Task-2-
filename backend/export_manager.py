"""
Export and Download Module
Handles exporting videos, reports, and data
"""

import json
import zipfile
from pathlib import Path
from datetime import datetime
import base64

class ExportManager:
    """Manages export and download functionality"""
    
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.exports_dir = self.output_dir / "exports"
        self.exports_dir.mkdir(exist_ok=True)
    
    def export_project(self, topic, script, blueprint, analysis, quality_assessment):
        """
        Export complete project as a zip file
        
        Args:
            topic: Video topic
            script: Generated script
            blueprint: Animation blueprint
            analysis: Visual pattern analysis
            quality_assessment: Quality assessment results
        
        Returns:
            Path to the exported zip file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        project_name = f"{topic.replace(' ', '_')}_{timestamp}"
        project_dir = self.exports_dir / project_name
        project_dir.mkdir(exist_ok=True)
        
        # Save script
        with open(project_dir / "script.txt", 'w', encoding='utf-8') as f:
            f.write(script)
        
        # Save blueprint
        with open(project_dir / "blueprint.txt", 'w', encoding='utf-8') as f:
            f.write(blueprint)
        
        # Save analysis as JSON
        with open(project_dir / "analysis.json", 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2)
        
        # Save quality assessment
        with open(project_dir / "quality_report.json", 'w', encoding='utf-8') as f:
            json.dump(quality_assessment, f, indent=2)
        
        # Create README
        readme_content = f"""# {topic}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Project Contents

- `script.txt`: The generated video script
- `blueprint.txt`: Animation blueprint with scene descriptions
- `analysis.json`: Visual learning pattern analysis
- `quality_report.json`: Video quality assessment report

## Visual Pattern

Primary Pattern: {analysis.get('primary_visual_pattern', 'N/A')}

## Quality Score

Overall Score: {quality_assessment.get('overall_score', 0):.1%}
Rating: {quality_assessment.get('rating', 'N/A')}

## Key Concepts

{', '.join(analysis.get('key_concepts', []))}
"""
        
        with open(project_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        # Create zip file
        zip_path = self.exports_dir / f"{project_name}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in project_dir.rglob('*'):
                if file.is_file():
                    zipf.write(file, file.relative_to(project_dir))
        
        return zip_path
    
    def get_download_link(self, file_path, link_text="Download"):
        """
        Generate a download link for Streamlit
        
        Args:
            file_path: Path to the file
            link_text: Text for the download link
        
        Returns:
            Tuple of (bytes_data, filename)
        """
        with open(file_path, 'rb') as f:
            bytes_data = f.read()
        
        filename = Path(file_path).name
        return bytes_data, filename
    
    def export_analytics(self, video_history):
        """
        Export analytics data as JSON
        
        Args:
            video_history: List of generated video records
        
        Returns:
            Path to exported analytics file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        analytics_file = self.exports_dir / f"analytics_{timestamp}.json"
        
        analytics_data = {
            'export_date': datetime.now().isoformat(),
            'total_videos': len(video_history),
            'videos': video_history
        }
        
        with open(analytics_file, 'w', encoding='utf-8') as f:
            json.dump(analytics_data, f, indent=2)
        
        return analytics_file
    
    def cleanup_old_exports(self, days=7):
        """
        Clean up exports older than specified days
        
        Args:
            days: Number of days to keep exports
        """
        cutoff = datetime.now().timestamp() - (days * 24 * 60 * 60)
        
        for file in self.exports_dir.rglob('*'):
            if file.is_file() and file.stat().st_mtime < cutoff:
                file.unlink()
        
        # Remove empty directories
        for dir in self.exports_dir.rglob('*'):
            if dir.is_dir() and not list(dir.iterdir()):
                dir.rmdir()


if __name__ == "__main__":
    # Test export functionality
    export_manager = ExportManager()
    
    test_data = {
        'topic': 'Test Video',
        'script': 'This is a test script',
        'blueprint': 'This is a test blueprint',
        'analysis': {'primary_visual_pattern': 'concept', 'key_concepts': ['test']},
        'quality_assessment': {'overall_score': 0.85, 'rating': 'Good'}
    }
    
    zip_file = export_manager.export_project(**test_data)
    print(f"Exported to: {zip_file}")
