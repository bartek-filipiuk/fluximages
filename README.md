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