# 🎬 AI Video Generator Pro

**Visual Learning Pattern Analysis + AI Video Synthesis System**

An advanced AI-powered video generation system that automatically analyzes content, detects optimal visual learning patterns, and creates educational videos with quality assessment.

## 🌟 Features

### Core Capabilities
- ✨ **AI Script Generation** - Generates detailed video scripts from topics using Hugging Face models
- 🎨 **Visual Pattern Analysis** - Automatically detects optimal visual learning patterns (comparison, process, hierarchy, timeline, etc.)
- 📐 **Smart Blueprint Generation** - Creates optimized animation blueprints based on detected patterns
- 🎥 **Video Synthesis** - Renders professional videos using Manim animation engine
- 📊 **Quality Assessment** - Comprehensive quality metrics and recommendations
- 📥 **Export & Download** - Complete project export with all assets

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
- FFmpeg (for video rendering)
- Hugging Face account (free)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
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

4. **Set up API keys**
   - Get free Hugging Face token: https://huggingface.co/settings/tokens
   - Copy `.env` file and add your token:
     ```
     HUGGINGFACE_API_KEY=your_token_here
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 💡 Usage

### Demo Mode (Recommended for Testing)
1. Open the app and **enable Demo Mode** in the sidebar
2. Enter any topic (e.g., "How WebSockets work")
3. Click "Generate Video"
4. Explore the analysis, blueprint, and quality assessment
5. Download your project files

### API Mode (Production)
1. Disable Demo Mode in the sidebar
2. Ensure your Hugging Face API key is configured
3. Enter a topic and generate
4. Wait for AI processing (first call may take 20-30 seconds)
5. Review and download the complete video project

## 📊 Dashboard Features

### Generation Tab
- Script generation with AI
- Real-time visual pattern analysis
- Scene structure recommendations
- Quality assessment with metrics
- Export and download options

### Analytics Tab
- Generation history tracking
- Quality score statistics
- Pattern usage analytics
- Recent generations overview

### Help Tab
- Comprehensive documentation
- Visual pattern explanations
- Quality metrics guide
- Troubleshooting tips

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
# Hugging Face API (Free)
HUGGINGFACE_API_KEY=your_token_here

# Optional: OpenAI API (Paid, better quality)
OPENAI_API_KEY=your_key_here
```

### Customization
- Modify visual patterns in `backend/visual_pattern_analyzer.py`
- Adjust quality thresholds in `backend/quality_assessor.py`
- Customize Manim scenes in `video_engine/manim_scenes.py`
- Edit AI prompts in `prompts/` directory

## 📦 Export Options

- **📦 Complete Project ZIP** - Includes script, blueprint, analysis, and quality report
- **📝 Script TXT** - Generated video script
- **📐 Blueprint TXT** - Animation blueprint
- **📊 Quality Report** - Detailed assessment

## 🐛 Troubleshooting

### API Errors
- **401 Unauthorized**: Check your API key in `.env`
- **410 Gone / 404**: Model unavailable, use Demo Mode
- **429 Rate Limit**: Wait a few moments or use Demo Mode
- **503 Loading**: Model is loading, wait 20-30 seconds

### Video Rendering Issues
- Ensure FFmpeg is installed and in PATH
- Check Manim installation: `manim --version`
- Verify `output/` directory exists and is writable

### Performance
- First API call may take 20-30 seconds (model loading)
- Subsequent calls are faster (model cached)
- Demo Mode is instant (no API calls)

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional visual pattern types
- More Manim scene templates
- Enhanced quality metrics
- UI/UX improvements
- Documentation and examples

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- **Hugging Face** - Free AI model inference
- **Manim** - Mathematical animation engine
- **Streamlit** - Web app framework
- **OpenAI** - GPT models (optional)

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the Help tab in the app
- Enable Demo Mode for testing without API

---

**Built with ❤️ for educators and content creators**

*Transform any topic into engaging educational videos with AI-powered visual learning analysis*
