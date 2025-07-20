import os
from datetime import datetime
from pymongo import MongoClient, errors
from gridfs import GridFS
import uuid

def context_collector(
    product_name,
    description,
    images=None,
    hosting_platform=None,
    target_audience=None,
    additional_info=None,
    user_id=None,
    created_at=None,
    updated_at=None,
    mongodb_uri=None
):
    """
    Collects product marketing info, uploads images to MongoDB GridFS, and stores metadata in MongoDB.
    
    Required parameters:
    - product_name: Name of the product
    - description: Description of the product
    
    Optional parameters:
    - images: List of file paths to upload as images
    - hosting_platform: Where the product will be hosted
    - target_audience: Target audience for the product
    - additional_info: Dictionary of additional information
    - user_id: User identifier
    - created_at: Creation timestamp (defaults to current time)
    - updated_at: Update timestamp (defaults to current time)
    - mongodb_uri: MongoDB connection URI (defaults to MONGODB_URI env var)
    
    Returns:
    - Dictionary with inserted_id and image_links (MongoDB document IDs)
    """
    
    # Validate required fields
    if not product_name or not description:
        raise ValueError("product_name and description are required")
    
    # Set default timestamps
    now = datetime.utcnow()
    if created_at is None:
        created_at = now
    if updated_at is None:
        updated_at = now
    
    # Get MongoDB URI from environment if not provided
    if mongodb_uri is None:
        mongodb_uri = os.environ.get("MONGODB_URI")
    
    if not mongodb_uri:
        raise RuntimeError("MONGODB_URI environment variable not set")
    
    # Connect to MongoDB
    try:
        client = MongoClient(mongodb_uri)
        db = client["marketing_db"]
        collection = db["product_marketing"]
        
        # Initialize GridFS for image storage
        fs = GridFS(db, collection="product_images")
        
    except errors.PyMongoError as e:
        raise RuntimeError(f"Failed to connect to MongoDB: {e}")
    
    # Upload images to MongoDB GridFS
    image_links = []
    if images:
        for img_path in images:
            try:
                with open(img_path, "rb") as f:
                    image_bytes = f.read()
                
                # Generate unique filename
                filename = f"{product_name}_{uuid.uuid4().hex}_{os.path.basename(img_path)}"
                
                # Store image in GridFS
                file_id = fs.put(
                    image_bytes,
                    filename=filename,
                    product_name=product_name,
                    content_type="image/png"  # Adjust based on file type
                )
                
                # Create a link/ID that can be used to retrieve the image
                image_link = str(file_id)
                image_links.append(image_link)
                
            except Exception as e:
                raise RuntimeError(f"Failed to upload image {img_path}: {e}")
    
    # Prepare document for MongoDB
    document = {
        "product_name": product_name,
        "description": description,
        "created_at": created_at,
        "updated_at": updated_at
    }
    
    # Add optional fields if provided
    if image_links:
        document["images"] = image_links
    if hosting_platform:
        document["hosting_platform"] = hosting_platform
    if target_audience:
        document["target_audience"] = target_audience
    if additional_info:
        document["additional_info"] = additional_info
    if user_id:
        document["user_id"] = user_id
    
    # Insert into MongoDB
    try:
        result = collection.insert_one(document)
        inserted_id = result.inserted_id
    except errors.PyMongoError as e:
        raise RuntimeError(f"Failed to insert document into MongoDB: {e}")
    finally:
        client.close()
    
    return {
        "inserted_id": str(inserted_id),
        "image_links": image_links
    }

# Helper function to retrieve images from MongoDB GridFS
def get_image_from_mongodb(image_id, mongodb_uri=None):
    """
    Retrieve an image from MongoDB GridFS using the image ID.
    
    Args:
        image_id: The MongoDB ObjectId of the image
        mongodb_uri: MongoDB connection URI (defaults to MONGODB_URI env var)
    
    Returns:
        Image bytes or None if not found
    """
    if mongodb_uri is None:
        mongodb_uri = os.environ.get("MONGODB_URI")
    
    if not mongodb_uri:
        raise RuntimeError("MONGODB_URI environment variable not set")
    
    try:
        client = MongoClient(mongodb_uri)
        db = client["marketing_db"]
        fs = GridFS(db, collection="product_images")
        
        # Retrieve the file from GridFS
        grid_out = fs.get(image_id)
        image_bytes = grid_out.read()
        
        return image_bytes
        
    except errors.PyMongoError as e:
        raise RuntimeError(f"Failed to retrieve image from MongoDB: {e}")
    finally:
        client.close()

result = context_collector(
    product_name="My Product",
    description="A great product description",
    images=["./image.png"],
    hosting_platform="Shopify",
    target_audience="Developers"
)