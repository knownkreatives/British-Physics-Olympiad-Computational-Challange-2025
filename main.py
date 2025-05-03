import sys
import os
# Add the /src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


if __name__ == "__main__":
    # Import the config module from the src directory
    import src.config

    # Print the configuration settings
    src.config.print_config()