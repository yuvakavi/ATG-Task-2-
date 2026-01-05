import streamlit as st
from backend.script_generator import generate_script
from backend.blueprint_generator import generate_blueprint
from backend.visual_pattern_analyzer import VisualPatternAnalyzer
from backend.quality_assessor import VideoQualityAssessor
from backend.export_manager import ExportManager
from video_engine.enhanced_synthesis import VideoSynthesizer
from video_engine.simple_video_generator import SimpleVideoGenerator
import os
import traceback
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Initialize analyzers
pattern_analyzer = VisualPatternAnalyzer()
quality_assessor = VideoQualityAssessor()
video_synthesizer = VideoSynthesizer()
simple_video_gen = SimpleVideoGenerator()
export_manager = ExportManager()

st.set_page_config(
    page_title="AI Video Generator Pro",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Video Generator")
st.caption("Create educational videos with AI")

# Check if API key is loaded
if not os.getenv("GROQ_API_KEY") or os.getenv("GROQ_API_KEY") == "YOUR_GROQ_API_KEY_HERE":
    st.error("⚠️ Groq API key not found!")
    st.markdown("""
    **Get your FREE Groq API key (No credit card required):**
    1. Go to [Groq Console](https://console.groq.com)
    2. Sign up (free)
    3. Create an API key
    4. Copy and paste it in the `.env` file as `GROQ_API_KEY=your_key`
    
    **Why Groq?**
    - ✅ **100% FREE** - No credit card needed
    - ⚡ **Super Fast** - Fastest inference in the world
    - 🎯 **Reliable** - Enterprise-grade models
    - 🔥 **Latest Models** - Llama 3.3 70B
    """)
    st.stop()

topic = st.text_input("Enter a topic", placeholder="e.g., How Machine Learning Works", key="topic_input")

generate_btn = st.button("🎬 Generate Video", type="primary", use_container_width=True)

if generate_btn:
        if not topic:
            st.warning("⚠️ Please enter a topic first!")
            st.stop()
        
        try:
            # Step 1: Generate script
            with st.spinner("🎬 Generating script with Groq AI..."):
                script = generate_script(topic)
            
            st.success("✅ Script generated!")
            
            # Display script in expandable section
            with st.expander("📝 View Generated Script", expanded=False):
                st.text_area("Script", script, height=200, key="script_display", label_visibility="collapsed")
            
            # Step 2: Analyze visual patterns
            with st.spinner("🔍 Analyzing visual learning patterns..."):
                pattern_analysis = pattern_analyzer.analyze_content(script)
            
            st.success(f"✅ Detected pattern: **{pattern_analysis['primary_visual_pattern'].upper()}**")
            
            # Step 3: Generate blueprint
            with st.spinner("📐 Generating enhanced animation blueprint..."):
                visual_blueprint = generate_blueprint(script)
            
            st.success("✅ Blueprint generated!")
            
            with st.expander("📐 View Animation Blueprint", expanded=False):
                st.text_area("Blueprint", visual_blueprint, height=300, key="blueprint_display", label_visibility="collapsed")
            
            # Step 4: Synthesize video
            with st.spinner("🎥 Generating MP4 video..."):
                # Use simple video generator to create actual MP4
                video_result = simple_video_gen.generate_from_analysis(topic, script, pattern_analysis)
                
                synthesis_result = {
                    'video_path': video_result['video_path'],
                    'estimated_duration': video_result['duration']
                }
            
            st.success(f"✅ Video generated successfully! ({video_result['duration']:.1f}s)")
            
            # Step 5: Quality Assessment
            with st.spinner("📊 Assessing video quality..."):
                video_metadata = {
                    'duration': synthesis_result.get('estimated_duration', 30),
                    'scene_count': len(pattern_analysis['recommended_scenes']),
                    'concept_count': len(pattern_analysis['key_concepts'])
                }
                
                quality_assessment = quality_assessor.assess_video(
                    synthesis_result['video_path'],
                    video_metadata
                )
            
            rating = quality_assessment.get('rating', 'Good')
            st.success(f"✅ Quality Assessment: **{rating}**")
            
            # Display video if exists
            if os.path.exists(synthesis_result['video_path']):
                st.success("🎉 Video Generated Successfully!")
                st.video(synthesis_result['video_path'])
            else:
                st.error("❌ Video file not found. Please try again.")
            
            # Export and Download Section
            st.divider()
            
            col_e1, col_e2, col_e3 = st.columns(3)
            
            with col_e1:
                # Download script
                st.download_button(
                    label="📝 Script",
                    data=script,
                    file_name=f"{topic.replace(' ', '_')}_script.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with col_e2:
                # Download blueprint
                st.download_button(
                    label="📐 Blueprint",
                    data=visual_blueprint,
                    file_name=f"{topic.replace(' ', '_')}_blueprint.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with col_e3:
                # Download video if exists
                if os.path.exists(synthesis_result['video_path']):
                    with open(synthesis_result['video_path'], 'rb') as video_file:
                        st.download_button(
                            label="🎥 Video",
                            data=video_file.read(),
                            file_name=os.path.basename(synthesis_result['video_path']),
                            mime="video/mp4",
                            use_container_width=True
                        )
            
            # Save session data
            if 'generated_videos' not in st.session_state:
                st.session_state.generated_videos = []
            
            st.session_state.generated_videos.append({
                'topic': topic,
                'pattern': pattern_analysis.get('primary_visual_pattern', 'concept'),
                'quality_score': quality_assessment.get('overall_score', 0.8),
                'rating': quality_assessment.get('rating', 'Good')
            })
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            if "groq" in str(e).lower() or "api" in str(e).lower():
                st.info("💡 Check your Groq API key in the `.env` file")
