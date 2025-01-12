# Pokemon Image Generator

A simple web application that generates Pokemon coloring book style images using the Together AI FLUX model.

## Features
- Generate black and white Pokemon illustrations perfect for coloring
- Simple and intuitive web interface
- Real-time image generation
- Error handling with automatic retries

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

## Important Notes
- Make sure you have Python 3.x installed
- Keep your API key private and never share it publicly
- The application requires an internet connection to generate images
- If you encounter any issues, verify that all packages are installed correctly

## Dependencies
- Flask
- OpenAI
- python-dotenv
- Other dependencies listed in `requirements.txt`

## License
This project is open source and available under the MIT License.

## Contributing
Feel free to submit issues and pull requests to improve the application. 