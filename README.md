# Image Generator

A simple web application that generates images using the Together AI FLUX model.

## Features
- Generate black and white Pokemon illustrations perfect for coloring
- Simple and intuitive web interface
- Real-time image generation
- Error handling with automatic retries
- Configurable image generation parameters

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/bartek-filipiuk/fluximages.git
   cd fluximages
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # for Linux/Mac
   # or
   venv\Scripts\activate  # for Windows
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**
   - Create a `.env` file in the project root directory
   - Add your Together API key in the following format:
     ```
     TOGETHER_API_KEY=your_api_key_here
     ```
   - You can obtain an API key from [Together.ai](https://together.ai)

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Use the application**
   - Open your web browser
   - Go to: `http://127.0.0.1:5000`
   - Enter a description of the Pokemon you want to generate
   - Click the "Generate Image" button

## Model Configuration

You can customize the image generation by modifying the following parameters in `app.py`:

```python
response = openai.Image.create(
    model="black-forest-labs/FLUX.1-schnell-Free",  # Model name
    prompt=prompt,                                  # Your text prompt
    n=1,                                           # Number of images to generate
    size="1024x1024"                               # Image resolution
)
```

Available parameters:
- `model`: Choose between different FLUX models
  - `black-forest-labs/FLUX.1-schnell-Free` (Free version)
  - `black-forest-labs/FLUX.1.1-pro` (Pro version)
- `size`: Image resolution options, depends on the model
  - `"1440x1440"`
  - `"1024x1024"`
  - `"512x512"`
  - `"256x256"`
  - "`and combinations of these`"
- `n`: Number of images to generate (1-4)
- `steps`: Number of steps for image generation (1-4)

## Example Prompts

Here are some example prompts showcasing different artistic styles you can generate:

1. **Abstract Geometric Art**
   ```
   Create an abstract composition with floating geometric shapes in vibrant neon colors against a deep black background. Include circles, triangles, and hexagons interconnected with thin glowing lines, creating a sense of depth and movement. Style inspired by Kandinsky with a modern cyberpunk twist.
   ```

2. **Hyper-Realistic Nature**
   ```
   A close-up macro photograph of a morning dew drop on a spider web, capturing the refraction of sunrise through the water droplet. Ultra-detailed with visible light spectrum rainbow effects, photorealistic texture of the silk thread, and perfect clarity in 8K resolution.
   ```

3. **Surreal Dreamscape**
   ```
   A surreal scene where a giant antique pocket watch floats in a cloudy sky, its gears and mechanisms spilling out and transforming into butterflies. The background transitions from sunset orange at the top to deep purple at the bottom, with floating islands covered in bioluminescent flowers.
   ```

4. **Digital Oil Painting**
   ```
   A moody cityscape at twilight in the style of classical oil painting, showing narrow cobblestone streets of an old European city during light rain. Warm glowing windows reflect in wet pavements, with detailed architectural elements and atmospheric perspective creating depth. Style similar to Eduard Gorter's urban scenes.
   ```

5. **Sci-Fi Concept Art**
   ```
   A highly detailed futuristic spaceport carved into the side of a crystalline mountain, with sleek chrome ships docking at multiple levels. Crystal formations emit a soft blue glow, while holographic advertisements float in the air. The scene is lit by three setting suns of different colors, creating complex shadows and reflections on the metallic surfaces.
   ```

6. **Realistic Portrait**
   ```
   Professional studio portrait of a middle-aged Asian woman with elegant features, wearing a crisp white silk blouse. Natural makeup, subtle smile, and confident pose. Short black hair styled in a modern bob cut. Soft studio lighting from the left creating gentle shadows. Shot with a Canon EOS R5, 85mm f/1.2 lens, shallow depth of field with background slightly blurred. Photorealistic quality with detailed skin texture, catch lights in eyes, and natural color grading.
   ```

7. **Ultra-Detailed Abstract Mechanism**
   ```
   Intricate mechanical abstract artwork in the style of a deconstructed watch movement. Hundreds of precisely detailed brass and silver gears, ranging from microscopic to large, interconnected with delicate chains and springs. Each gear tooth perfectly defined, with visible metallic wear patterns and subtle patina. Floating crystalline structures weave between the mechanisms, refracting light into prismatic patterns. Deep focus showing multiple layers of depth, with elements ranging from 0.1mm to 10cm in size. Extreme macro photography quality, shot at f/32 for maximum detail, with ray-traced reflections on polished surfaces. Background transitions from deep cobalt blue to burgundy, with floating particles of gold dust catching the light.
   ```

8. **Hyper-Detailed Realistic Nature Scene**
   ```
   Ultra-high resolution capture of a moss-covered ancient tree trunk in a rainforest after rainfall, shot with a 100MP medium format camera. Every water droplet contains perfect reflections of the canopy above. Individual moss filaments visible in microscopic detail, showing cellular structures and reproductive spores. Tiny insects navigate through the moss forest - a 2mm iridescent beetle with visible leg joints and antenna segments, translucent mites smaller than a water droplet. Multiple layers of lichen in varying colors from sage green to burnt orange, each showing intricate fractal patterns. Web-like fungal hyphae spread across the bark in gossamer-thin white strands. Bark texture shows years of growth with deep fissures and complex patterns. Natural afternoon sunlight filtering through the canopy creates scattered light rays and rainbow refractions in the water droplets. 8K resolution with focus stacking for perfect sharpness from 1mm to 1m depth.
   ```

9. **Black and White Elephant Coloring Book**
   ```
   Create a simple black and white line art illustration of a friendly elephant, perfect for a coloring book. Clean, bold outlines with no shading or colors. The elephant should be in a standing pose, slightly turned to the side, with its trunk gently raised. Include basic details like wrinkles on the skin, simple ear texture, and toenails, but keep the lines clear and well-spaced for easy coloring. White background with black lines only. Style should be similar to professional coloring books with lines of consistent thickness. Avoid any gray tones or gradients - pure black and white only. Make sure there are enough empty spaces between lines for comfortable coloring with markers or colored pencils.
   ```

## Important Notes
- Make sure you have Python 3.x installed
- Keep your API key private and never share it publicly
- The application requires an internet connection to generate images
- If you encounter any issues, verify that all packages are installed correctly
- Different models may have different capabilities and generation speeds

## Dependencies
- Flask
- OpenAI
- python-dotenv
- Other dependencies listed in `requirements.txt`

## License
This project is open source and available under the MIT License.

## Contributing
Feel free to submit issues and pull requests to improve the application. 