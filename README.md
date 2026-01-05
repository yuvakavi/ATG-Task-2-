# 🎬 AI Video Generator

**AI-Powered Video Generation with Groq**

An AI-powered video generation system that automatically creates educational videos using Groq's lightning-fast AI models.

## 🌟 Features

### Core Capabilities
- ✨ **AI Script Generation** - Generates detailed video scripts using Groq Llama 3.3 70B
- 🎨 **Visual Pattern Analysis** - Automatically detects optimal visual learning patterns
- 📐 **Smart Blueprint Generation** - Creates optimized animation blueprints
- 🎥 **Video Generation** - Creates MP4 videos with MoviePy
- 📊 **Quality Assessment** - Comprehensive quality metrics
- 📥 **Export & Download** - Download script, blueprint, and video

### Visual Learning Patterns
The system intelligently detects and optimizes for:
- **Comparison** - Side-by-side comparisons, A vs B scenarios
- **Process** - Step-by-step procedures and workflows
- **Hierarchy** - Organizational structures and levels
- **Timeline** - Historical progressions and chronological events
- **Concept** - Abstract ideas and principles
- **Statistics** - Data-driven content with charts and graphs
- **Relationship** - Connections and associations

### Quality Metrics
Videos are assessed on multiple dimensions:
- **Duration** - Optimal length for learning (30-120 seconds)
- **Scene Structure** - Appropriate number of scenes (3-8)
- **Pacing** - Time per scene (3-8 seconds)
- **Content Clarity** - Concept density and information flow

## 📁 Project Structure

```
AI-Video-Generator/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (API keys)
├── .gitignore                     # Git ignore rules
│
├── backend/                       # Backend modules
│   ├── __init__.py
│   ├── script_generator.py       # AI script generation
│   ├── blueprint_generator.py    # Blueprint creation
│   ├── visual_pattern_analyzer.py # Pattern detection & analysis
│   ├── quality_assessor.py       # Video quality assessment
│   └── export_manager.py         # Export and download management
│
├── video_engine/                  # Video synthesis
│   ├── manim_scenes.py           # Manim scene definitions
│   ├── render.py                 # Video rendering
│   └── enhanced_synthesis.py     # Enhanced video synthesis
│
├── prompts/                       # AI prompts
│   ├── script_prompt.txt
│   └── blueprint_prompt.txt
│
└── output/                        # Generated outputs
    ├── final_video.mp4
    └── exports/                   # Exported projects
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Groq API key (100% FREE - no credit card required)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yuvakavi/ATG-Task-2-.git
   cd AI-Video-Generator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Groq API key**
   - Get FREE Groq API key: https://console.groq.com
   - Sign up (no credit card needed)
   - Create an API key
   - Add to `.env` file:
     ```
     GROQ_API_KEY=your_key_here
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 💡 Usage

1. Open the app at http://localhost:8501
2. Enter any topic (e.g., "How Machine Learning Works")
3. Click "🎬 Generate Video"
4. Wait for AI to generate script and create video
5. Watch the video and download files

## 📊 Features

- **Script Generation** - AI writes detailed video scripts
- **Pattern Analysis** - Detects best visual learning approach
- **Video Creation** - Generates MP4 videos automatically
- **Quality Assessment** - Rates video quality
- **Downloads** - Get script, blueprint, and video files

## 🎯 Visual Pattern Detection

The system analyzes your content and automatically determines the best visualization approach:

```python
# Example patterns detected:
"Step 1, Step 2, Step 3" → Process Flow
"A vs B" → Comparison View
"Timeline from 2010 to 2020" → Timeline Animation
"Organizational hierarchy" → Tree Diagram
```

## 📈 Quality Assessment

Each video receives a comprehensive quality report:

```
Overall Rating: Excellent
Overall Score: 87%

Metrics:
✓ Duration: Optimal (45s)
✓ Scene Structure: 5 scenes
⚠ Pacing: Slightly fast (5s per scene)
✓ Content Clarity: Well balanced

Recommendations:
1. Slow down transitions for better comprehension
2. Consider adding a summary scene
```

## 🔧 Configuration

### Environment Variables (.env)
```bash
# Groq API (100% FREE)
GROQ_API_KEY=your_key_here
```

### Why Groq?
- ✅ **100% FREE** - No credit card required
- ⚡ **World's Fastest** - Fastest LLM inference
- 🎯 **Latest Models** - Llama 3.3 70B
- 🔒 **Reliable** - Enterprise-grade infrastructure

## 📦 Export Options

- **📝 Script** - Generated video script
- **📐 Blueprint** - Animation blueprint  
- **🎥 Video** - MP4 video file

## 🐛 Troubleshooting

### API Errors
- **API Key Error**: Check your Groq API key in `.env` file
- **Rate Limit**: Groq has generous free tier limits
- **Connection Error**: Check your internet connection

### Video Generation
- Videos are generated as MP4 files in the `output/` folder
- First generation may take a few seconds
- Videos show topic title with clean design

## 🙏 Acknowledgments

- **Groq** - Lightning-fast AI inference (FREE)
- **MoviePy** - Video generation library
- **Streamlit** - Web app framework

## 📞 Support

For issues or questions:
- Open an issue on GitHub: https://github.com/yuvakavi/ATG-Task-2-
- Get Groq API key: https://console.groq.com

---

**Built with ❤️ using Groq AI**

*Transform any topic into educational videos with lightning-fast AI*
