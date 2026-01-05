"""
Visual Learning Pattern Analysis Module
Analyzes text content to identify optimal visual representations
"""

import re
from typing import Dict, List, Tuple

class VisualPatternAnalyzer:
    """Analyzes content to determine best visual learning patterns"""
    
    def __init__(self):
        self.visual_patterns = {
            'comparison': ['vs', 'versus', 'compared to', 'difference between', 'contrast'],
            'process': ['step', 'process', 'flow', 'sequence', 'procedure', 'how to'],
            'hierarchy': ['structure', 'organization', 'levels', 'hierarchy', 'layers'],
            'relationship': ['relationship', 'connection', 'linked', 'related', 'association'],
            'timeline': ['timeline', 'history', 'evolution', 'chronology', 'over time'],
            'statistics': ['data', 'statistics', 'percentage', 'number', 'chart', 'graph'],
            'concept': ['concept', 'idea', 'principle', 'theory', 'fundamental']
        }
        
    def analyze_content(self, text: str) -> Dict[str, any]:
        """Analyze text to identify visual learning patterns"""
        text_lower = text.lower()
        
        # Detect visual patterns
        detected_patterns = {}
        for pattern_type, keywords in self.visual_patterns.items():
            count = sum(1 for keyword in keywords if keyword in text_lower)
            if count > 0:
                detected_patterns[pattern_type] = count
        
        # Sort patterns by frequency
        sorted_patterns = sorted(detected_patterns.items(), key=lambda x: x[1], reverse=True)
        
        # Extract key concepts
        key_concepts = self._extract_key_concepts(text)
        
        # Determine optimal visualization
        primary_pattern = sorted_patterns[0][0] if sorted_patterns else 'concept'
        
        return {
            'primary_visual_pattern': primary_pattern,
            'all_patterns': dict(sorted_patterns),
            'key_concepts': key_concepts,
            'word_count': len(text.split()),
            'sentence_count': len(re.split(r'[.!?]+', text)),
            'recommended_scenes': self._recommend_scenes(primary_pattern, len(key_concepts))
        }
    
    def _extract_key_concepts(self, text: str) -> List[str]:
        """Extract key concepts from text"""
        # Simple extraction based on capitalized words and important terms
        sentences = re.split(r'[.!?]+', text)
        concepts = []
        
        for sentence in sentences[:5]:  # Focus on first 5 sentences
            words = sentence.split()
            for i, word in enumerate(words):
                if word and (word[0].isupper() or word.lower() in ['important', 'key', 'main', 'primary']):
                    if len(word) > 3 and word not in ['The', 'This', 'That', 'With']:
                        concepts.append(word.strip('.,!?'))
        
        return list(set(concepts))[:8]  # Return top 8 unique concepts
    
    def _recommend_scenes(self, pattern_type: str, concept_count: int) -> List[Dict]:
        """Recommend scene structure based on pattern type"""
        scene_templates = {
            'comparison': [
                {'type': 'intro', 'duration': 3, 'visual': 'split_screen'},
                {'type': 'comparison', 'duration': 5, 'visual': 'side_by_side'},
                {'type': 'conclusion', 'duration': 2, 'visual': 'merge'}
            ],
            'process': [
                {'type': 'intro', 'duration': 3, 'visual': 'title'},
                {'type': 'steps', 'duration': 2, 'visual': 'flowchart', 'repeat': concept_count},
                {'type': 'summary', 'duration': 3, 'visual': 'overview'}
            ],
            'hierarchy': [
                {'type': 'intro', 'duration': 3, 'visual': 'title'},
                {'type': 'structure', 'duration': 6, 'visual': 'tree_diagram'},
                {'type': 'details', 'duration': 4, 'visual': 'zoom_in'}
            ],
            'timeline': [
                {'type': 'intro', 'duration': 3, 'visual': 'title'},
                {'type': 'timeline', 'duration': 7, 'visual': 'horizontal_timeline'},
                {'type': 'conclusion', 'duration': 2, 'visual': 'summary'}
            ],
            'concept': [
                {'type': 'intro', 'duration': 3, 'visual': 'fade_in'},
                {'type': 'explanation', 'duration': 5, 'visual': 'bullet_points'},
                {'type': 'conclusion', 'duration': 2, 'visual': 'fade_out'}
            ]
        }
        
        return scene_templates.get(pattern_type, scene_templates['concept'])
    
    def generate_visual_blueprint(self, text: str) -> str:
        """Generate detailed visual blueprint from analyzed content"""
        analysis = self.analyze_content(text)
        
        blueprint = f"""
=== VISUAL LEARNING PATTERN ANALYSIS ===

Primary Pattern: {analysis['primary_visual_pattern'].upper()}
Key Concepts: {', '.join(analysis['key_concepts'])}
Content Stats: {analysis['word_count']} words, {analysis['sentence_count']} sentences

=== RECOMMENDED SCENE STRUCTURE ===
"""
        
        scenes = analysis['recommended_scenes']
        total_duration = 0
        
        for i, scene in enumerate(scenes, 1):
            repeat = scene.get('repeat', 1)
            duration = scene['duration'] * repeat
            total_duration += duration
            
            blueprint += f"""
Scene {i}: {scene['type'].upper()}
Duration: {duration}s
Visual Style: {scene['visual']}
Animation: {"Repeated " + str(repeat) + " times" if repeat > 1 else "Single scene"}
"""
        
        blueprint += f"""
=== TOTAL VIDEO LENGTH: {total_duration} seconds ===

=== VISUAL ELEMENTS ===
- Primary Color Scheme: Blue gradient (professional)
- Secondary Colors: White text, accent colors for highlights
- Font: Sans-serif, modern and clean
- Transitions: Smooth fades and slides
- Background: Gradient or solid with subtle animations
"""
        
        return blueprint


if __name__ == "__main__":
    # Test the analyzer
    analyzer = VisualPatternAnalyzer()
    
    sample_text = "This video explains the step-by-step process of how WebSockets work. First, the client initiates a connection. Then, the server accepts the handshake. Finally, bidirectional communication begins."
    
    analysis = analyzer.analyze_content(sample_text)
    print("Analysis:", analysis)
    
    blueprint = analyzer.generate_visual_blueprint(sample_text)
    print("\nBlueprint:", blueprint)
