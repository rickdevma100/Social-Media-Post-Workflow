"""
Configuration module for the YouTube Thumbnail Generator.

This module provides a centralized configuration system using a Config class
that manages all settings including API models, image sizes, and directory paths.
"""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Config:
    """Configuration settings for the YouTube Thumbnail Generator."""

    # Model settings
    GEMINI_MODEL: str = "gemini-2.5-flash-preview-04-17"

    # Image generation settings
    THUMBNAIL_IMAGE_SIZE: str = "1536x1024"  # Landscape format for YouTube thumbnails

    # Directory structure
    IMAGE_ROOT_DIR: Path = Path("images")
    REFERENCE_IMAGES_DIR: Path = IMAGE_ROOT_DIR / "reference_images"
    THUMBNAIL_ASSETS_DIR: Path = IMAGE_ROOT_DIR / "assets"
    GENERATED_THUMBNAILS_DIR: Path = IMAGE_ROOT_DIR / "generated"

    # API Keys
    OPENAI_API_KEY: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    YOUTUBE_API_KEY: Optional[str] = None

    def __post_init__(self):
        """Initialize configuration after dataclass initialization."""
        # Load API keys from environment
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

        # Create necessary directories
        self._create_directories()

    def _create_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        for directory in [
            self.IMAGE_ROOT_DIR,
            self.REFERENCE_IMAGES_DIR,
            self.THUMBNAIL_ASSETS_DIR,
            self.GENERATED_THUMBNAILS_DIR,
        ]:
            directory.mkdir(parents=True, exist_ok=True)

    def validate(self) -> None:
        """Validate the configuration settings.

        Raises:
            ValueError: If any required configuration is missing or invalid.
        """
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        if not self.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        if not self.YOUTUBE_API_KEY:
            raise ValueError("YOUTUBE_API_KEY not found in environment variables")


# Create a global config instance
config = Config()