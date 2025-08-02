"""
Tool for creating images using OpenAI's image generation API with asset incorporation.
"""

import base64
import os
from typing import Dict, Optional

import google.genai.types as types
from google.adk.tools.tool_context import ToolContext
from openai import OpenAI
from ....constants import (
    GENERATED_THUMBNAILS_DIR,
    IMAGE_ROOT_DIR,
    THUMBNAIL_IMAGE_SIZE
)


def create_image(
    tool_context: ToolContext
) -> Dict:
    """
    Create an image using OpenAI's image generation API with gpt-image-1 model,


    Args:
        tool_context (ToolContext, optional): The tool context

    Returns:
        dict: Result containing status and message
    """
    print("before try")
    try:
        # Get API key from environment
        api_key = os.environ.get("OPENAI_API_KEY")
        org_id = os.environ.get("OPENAI_ORG_ID")
        if not api_key:
            return {
                "status": "error",
                "message": "OPENAI_API_KEY not found in environment variables",
            }

        client = OpenAI(api_key=api_key, organization=org_id)
        print("Image prompt not generated")
        prompt = tool_context.state.get("image_prompt_generated")
        print(f"Image prompt generated {prompt}")
        # Clean up prompt if needed
        clean_prompt = prompt.strip()

        # Initialize response variable
        response = None

        # Ensure root images directory exists
        os.makedirs(IMAGE_ROOT_DIR, exist_ok=True)

        # No assets and no previous thumbnail - use the generate endpoint
        response = client.images.generate(
            model="gpt-image-1",
            prompt=clean_prompt,
            n=1,
            size=THUMBNAIL_IMAGE_SIZE,
        )

        # Get the base64 image data
        if response and response.data and len(response.data) > 0:
            print("Image Response is there......")
            image_base64 = response.data[0].b64_json
            if image_base64:
                image_bytes = base64.b64decode(image_base64)
            else:
                return {
                    "status": "error",
                    "message": "No image data returned from the API",
                }
        else:
            return {
                "status": "error",
                "message": "No data returned from the API",
            }

        # Use simple filename as requested
        filename = "youtube_thumbnail.png"

        # Save as an artifact if tool_context is provided
        artifact_version = None
        if tool_context:
            print("Image Artifact is created......")
            # Create a Part object for the artifact
            image_artifact = types.Part(
                inline_data=types.Blob(data=image_bytes, mime_type="image/png")
            )

            try:
                # Save the artifact
                artifact_version = tool_context.save_artifact(
                    filename=filename, artifact=image_artifact
                )
                print(f"Artifact created {artifact_version}")
                tool_context.state["image_filename"] = filename
                tool_context.state["image_version"] = artifact_version

            except ValueError as e:
                # Handle the case where artifact_service is not configured
                return {
                    "status": "warning",
                    "message": f"Image generated but could not be saved as an artifact: {str(e)}. Is ArtifactService configured?",
                }
            except Exception as e:
                # Handle other potential artifact storage errors
                return {
                    "status": "warning",
                    "message": f"Image generated but encountered an error saving as artifact: {str(e)}",
                }

        # Create directory for local file saving
        os.makedirs(GENERATED_THUMBNAILS_DIR, exist_ok=True)

        # Save the image locally as well
        filepath = os.path.join(GENERATED_THUMBNAILS_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(image_bytes)

        # Update state with thumbnail path
        if tool_context:
            tool_context.state["thumbnail_path"] = filepath
            tool_context.state["thumbnail_generated"] = True

        # Return success with artifact details if available
        if artifact_version is not None:
            return {
                "status": "success",
                "message": f"Image created successfully and saved as artifact '{filename}' (version {artifact_version}) and local file '{filepath}'",
                "filepath": filepath,
                "artifact_filename": filename,
                "artifact_version": artifact_version,
                "thumbnail_generated": True
            }
        else:
            return {
                "status": "success",
                "message": f"Image created successfully and saved as local file '{filepath}'",
                "filepath": filepath,
                "thumbnail_generated": True,
            }

    except Exception as e:
        return {"status": "error", "message": f"Error creating image: {str(e)}"}
