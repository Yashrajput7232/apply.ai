from setuptools import setup, find_packages

setup(
    name="applyai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "reportlab",
        "python-dotenv",
        "google-genai",
        "dotenv",
        "reportlab"
        # Add other dependencies
    ],
)