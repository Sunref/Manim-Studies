# Manim Python Studies

This repository contains my studies of the Manim library in Python. Manim is a powerful library for creating mathematical animations programmatically.

## Installation

### Prerequisites (Debian/Ubuntu OS)

Install the necessary packages (including LaTeX, which is optional but recommended for rendering equations):

```bash
sudo apt install python3-pip ffmpeg libcairo2-dev \
     texlive-latex-base texlive-latex-extra texlive-fonts-recommended \
     texlive-fonts-extra texlive-latex-recommended \
     pkg-config python3-dev libpango1.0-dev
```

### Python Environment Setup

1. Create a virtual environment (optional, but recommended):
```bash
python3 -m venv manim-venv
source manim-venv/bin/activate
```

2. Install Manim:
```bash
pip install --upgrade pip
pip install manim
```

## Running Animations

1. Create a Python file with your scene:
```python
# example.py
from manim import *

class MyAnimation(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(circle))
```

2. Run the command:
```bash
manim -pql your_project.py SceneName
```

Where:
- `-p`: Plays the animation after rendering
- `-q`: Quality (l=low, m=medium, h=high, k=4K)
- `-l`: Low quality (854x480 pixels resolution, 15fps)
- `your_project.py`: The Python file containing the scene
- `SceneName`: The name of the class that defines the scene to be rendered

## Repository Structure

- `/scenes`: Python files with scene definitions
- `/media`: Rendered animations and images

## Useful Resources

- [Official Manim Documentation](https://docs.manim.community/)
- [Beginner Tutorial](https://docs.manim.community/en/stable/tutorials/quickstart.html)
- [Manim Community Examples](https://docs.manim.community/en/stable/examples.html)

## License

[MIT](LICENSE)
