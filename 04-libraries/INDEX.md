# Python Libraries & Frameworks Course - Index

## Course Overview
This course explores the most powerful and widely-used Python libraries across various domains. Each lesson provides hands-on experience with a specific library or framework, including installation, core concepts, practical examples, and real-world applications. All lessons are provided as Jupyter notebooks (.ipynb) for interactive learning.

## Prerequisites
- Solid understanding of Python fundamentals (variables, data types, control flow)
- Experience with functions, classes, and OOP concepts
- Familiarity with file handling and error management
- Python 3.8+ installed
- Basic command line/terminal usage

## Course Structure

### Module 1: Data Science & Analysis (Lessons 01-05)
- **01_numpy_fundamentals.ipynb** - Arrays, operations, broadcasting, mathematical functions
- **02_pandas_data_manipulation.ipynb** - DataFrames, Series, data cleaning, filtering
- **03_pandas_advanced.ipynb** - Merging, grouping, pivot tables, time series
- **04_matplotlib_visualization.ipynb** - Plots, charts, customization, subplots
- **05_seaborn_advanced_viz.ipynb** - Statistical visualizations, themes, complex plots

### Module 2: Machine Learning Basics (Lessons 06-10)
- **06_scikit_learn_intro.ipynb** - ML basics, supervised/unsupervised learning
- **07_scikit_learn_classification.ipynb** - Classification algorithms, model evaluation
- **08_scikit_learn_regression.ipynb** - Regression models, feature engineering
- **09_scikit_learn_clustering.ipynb** - K-means, hierarchical clustering, DBSCAN
- **10_model_evaluation_tuning.ipynb** - Cross-validation, grid search, metrics

### Module 3: Deep Learning Frameworks (Lessons 11-15)
- **11_tensorflow_basics.ipynb** - Tensors, operations, computational graphs
- **12_keras_neural_networks.ipynb** - Sequential models, layers, training
- **13_pytorch_fundamentals.ipynb** - Tensors, autograd, building models
- **14_cnn_image_classification.ipynb** - Convolutional networks for images
- **15_transfer_learning.ipynb** - Pre-trained models, fine-tuning

### Module 4: Natural Language Processing (Lessons 16-18)
- **16_nltk_text_processing.ipynb** - Tokenization, stemming, lemmatization, POS tagging
- **17_spacy_nlp.ipynb** - Named entity recognition, dependency parsing, pipelines
- **18_text_classification_sentiment.ipynb** - Sentiment analysis, text classification

### Module 5: Web Development (Lessons 19-23)
- **19_flask_basics.ipynb** - Routes, templates, request handling
- **20_flask_rest_api.ipynb** - Building RESTful APIs, JSON responses
- **21_django_introduction.ipynb** - MVC/MTV architecture, models, views, templates
- **22_fastapi_modern_apis.ipynb** - Async APIs, automatic documentation, Pydantic
- **23_streamlit_data_apps.ipynb** - Interactive dashboards, widgets, data visualization

### Module 6: Web Scraping & Automation (Lessons 24-27)
- **24_requests_http.ipynb** - HTTP requests, APIs, authentication
- **25_beautifulsoup_scraping.ipynb** - Parsing HTML, extracting data, navigation
- **26_selenium_automation.ipynb** - Browser automation, form filling, dynamic content
- **27_pyautogui_gui_automation.ipynb** - Mouse/keyboard control, screenshots

### Module 7: Image Processing & Computer Vision (Lessons 28-31)
- **28_pillow_image_basics.ipynb** - Opening, editing, filters, transformations
- **29_opencv_fundamentals.ipynb** - Reading videos, image operations, drawing
- **30_opencv_computer_vision.ipynb** - Edge detection, contours, feature matching
- **31_face_detection_recognition.ipynb** - Haar cascades, face recognition algorithms

### Module 8: Scientific Computing (Lessons 32-34)
- **32_scipy_scientific_tools.ipynb** - Optimization, integration, interpolation
- **33_sympy_symbolic_math.ipynb** - Symbolic mathematics, equations, calculus
- **34_statistics_data_analysis.ipynb** - Statistical tests, distributions, hypothesis testing

### Module 9: Desktop & GUI Development (Lessons 35-37)
- **35_tkinter_gui_basics.ipynb** - Widgets, layout managers, event handling
- **36_pyqt_desktop_apps.ipynb** - Qt framework, signals/slots, modern UIs
- **37_kivy_cross_platform.ipynb** - Mobile and desktop apps, touch interfaces

### Module 10: Database & Data Storage (Lessons 38-40)
- **38_sqlite_database.ipynb** - SQL basics, CRUD operations, Python integration
- **39_sqlalchemy_orm.ipynb** - Object-relational mapping, models, queries
- **40_redis_caching.ipynb** - Key-value store, caching, pub/sub

### Module 11: Testing & Quality (Lessons 41-43)
- **41_pytest_testing.ipynb** - Unit tests, fixtures, parametrization
- **42_unittest_mocking.ipynb** - Test suites, mocking, assertions
- **43_code_quality_tools.ipynb** - Linting (pylint, flake8), formatting (black), type checking (mypy)

### Module 12: Data Formats & Serialization (Lessons 44-46)
- **44_json_xml_parsing.ipynb** - Working with JSON and XML data
- **45_yaml_config_files.ipynb** - Configuration management, YAML parsing
- **46_protobuf_serialization.ipynb** - Protocol buffers, efficient data exchange

### Module 13: Async & Concurrency (Lessons 47-49)
- **47_asyncio_basics.ipynb** - Async/await, coroutines, event loops
- **48_aiohttp_async_requests.ipynb** - Async HTTP client/server
- **49_celery_task_queues.ipynb** - Distributed task processing, scheduling

### Module 14: DevOps & Deployment (Lessons 50-52)
- **50_docker_python_apps.ipynb** - Containerization, Dockerfile, docker-compose
- **51_logging_monitoring.ipynb** - Logging module, structured logging, monitoring
- **52_deployment_best_practices.ipynb** - Production deployment, environment management

### Module 15: Specialized Libraries (Lessons 53-55)
- **53_plotly_interactive_viz.ipynb** - Interactive charts, dashboards, Plotly Express
- **54_geopy_location_data.ipynb** - Geocoding, distance calculation, maps
- **55_schedule_task_automation.ipynb** - Job scheduling, periodic tasks

## Learning Objectives
By the end of this course, students will be able to:
- Work confidently with major Python libraries across different domains
- Choose the appropriate library for specific tasks and projects
- Build data analysis pipelines with NumPy, Pandas, and visualization libraries
- Create machine learning models using scikit-learn
- Develop deep learning applications with TensorFlow/PyTorch
- Build web applications and APIs using Flask, Django, or FastAPI
- Automate web scraping and browser interactions
- Process images and implement computer vision solutions
- Develop desktop GUI applications
- Integrate databases and handle various data formats
- Write comprehensive tests and maintain code quality
- Deploy Python applications in production environments

## How to Use These Materials
1. **Install required libraries** - Each notebook includes installation instructions
2. **Open notebooks sequentially** - Follow the module order for best learning
3. **Run code cells** - Execute examples and observe outputs
4. **Modify and experiment** - Change parameters and explore library features
5. **Complete exercises** - Practice problems at the end of each lesson
6. **Build mini-projects** - Apply learned concepts to small projects
7. **Reference documentation** - Links to official docs provided in each notebook

## Installation Notes
Each library can be installed using pip:
```bash
pip install library-name
```

For specific lessons, installation requirements are listed at the beginning of each notebook.

We recommend using a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Estimated Time
- Total: 110-140 hours
- Per lesson: 2-2.5 hours
- Recommended pace: 4-5 lessons per week
- Duration: 11-14 weeks

## Projects Integration
Each module culminates in a practical mini-project that combines learned libraries:
- **Data Science:** Complete data analysis pipeline (cleaning → analysis → visualization)
- **Machine Learning:** End-to-end ML project (preprocessing → training → evaluation → deployment)
- **Web Development:** Full-stack web application with database and API
- **Automation:** Web scraper with data storage and scheduling
- **Computer Vision:** Image processing application with GUI
- **NLP:** Text analysis tool with sentiment analysis and entity recognition

## Additional Resources
- Official documentation links in each notebook
- Recommended tutorials and courses
- Community resources and forums
- GitHub repositories with examples
- Kaggle datasets for practice

## Notes for Web Platform Conversion
- All notebooks are structured for easy markdown conversion
- Code examples are self-contained and executable
- Visual outputs (plots, images) are embedded in notebooks
- Interactive elements can be preserved in web format
- Each lesson includes downloadable datasets where applicable
