## workflow
1. **Start**
   - Input: User provides criteria, topic, tone, and platform.
   
2. **Resource Generation Task**
   - **Agent**: `Resource_Generator`
   - **Action**: Generates a detailed list of resources required for the specified project or scenario.
   - Output: Comprehensive resource list.

3. **Post Creation Task**
   - **Agent**: `Post_Creator`
   - **Action**: Uses the generated resources to craft a well-structured post based on the provided topic and tone.
   - Output: A three-paragraph post tailored to the specified tone.

4. **Platform Adaptation Task**
   - **Agent**: `Platform_Adapter`
   - **Action**: Adapts the created post to the best practices and format of the specified platform (e.g., LinkedIn, Twitter).
   - Output: A formatted post ready for publishing on the chosen platform.

5. **End**
   - Final Output: Optimized post for the specified platform.

## Usage

To use the Social Media Post Generator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/owl-Dr/crewai.git
   cd crewai
   ```

2. **Create a Virtual Environment** using [Poetry](https://python-poetry.org/) with the `pyproject.toml` file:
   ```bash
   poetry install
   ```

   This command will create a virtual environment and install all the dependencies specified in the `pyproject.toml` file.

3. **Activate the Virtual Environment**:
   ```bash
   poetry shell
   ```

4. **Configure the Gemini API Key**:
   - Create a `.env` file in the project's root directory.
   - Add your Gemini API key to the `.env` file as follows:
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

5. **Run the Social Media Post Generator**:
   ```bash
   python main.py
   ```

   Follow the prompts to generate social media posts using the Gemini API.

--- 
